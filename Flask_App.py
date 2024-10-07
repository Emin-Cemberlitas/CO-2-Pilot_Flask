from datetime import timedelta
from flask import Flask, request, jsonify,render_template, make_response,session
from flask_cors import CORS
from setter_getter import *
import pdfkit
from pdf_sankey import sankey_diagram_svg
from dcf_diagram import cash_flow_chartz
from compression_diagram import compression_technology_chart
import main
from redis import Redis
import numpy as np
import redis

r = redis.Redis(host='localhost', port=6379)
if r.ping():
    print("Redis server is running")
else:
    print("Redis server is not available")

def convert_np_to_python(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()  # Konvertiere NumPy-Arrays in Python-Listen
    elif isinstance(obj, np.float64):
        return float(obj)  # Konvertiere numpy.float64 in Python float
    elif isinstance(obj, dict):
        return {key: convert_np_to_python(value) for key, value in obj.items()}  # Rekursiv für Dictionaries
    elif isinstance(obj, list):
        return [convert_np_to_python(i) for i in obj]  # Rekursiv für Listen
    return obj  # Andere Typen bleiben unverändert

app = Flask(__name__)
# Session Config
app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='localhost', port=6379)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=1)
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = True

path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
CORS(app, supports_credentials=True)
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    session.permanent = True

    # Beispiel für die Verarbeitung der empfangenen Daten
    industry = data.get('industry', '')
    country = data.get('country', '')
    currency = data.get('currency', '')
    lifetime = data.get('lifetime', 0)
    operation_hours = data.get('operationHours', 0)
    install_year = data.get('installyear', 0)
    captured_co2 = data.get('captured_co2', 0)
    co2_content = data.get('co2_content', 0)
    co2_capture_rate = data.get('co2_capture_rate', 0)
    transport_type = data.get('transport_type', '')
    distance_storage = data.get('distance_storage', 0)
    co2_price = data.get('co2Price', 0)
    electricity_price = data.get('electricityPrice', 0)
    subsidy_amount = data.get('subsidy_amount')
    if subsidy_amount is None:
        subsidy_amount = 0
    discount_rate = data.get('discount_rate', 0)
    sensitivity_parameter = data.get('sensitivity_parameter', '')
    sensitivity_range = data.get('sensitivity_range', '')
    sensitivity_toggle = data.get('sensitivity_toggle', '')
    compression_technology = data.get('compression_technology', '')

    set_industry(industry)
    set_country(country)
    set_currency(currency)
    set_lifetime(lifetime)
    set_operation_hours(operation_hours)
    set_install_year(install_year)
    set_captured_co2(captured_co2)
    set_co2_content(co2_content)
    set_co2_capture_rate(co2_capture_rate)
    set_transport_type(transport_type)
    set_distance_storage(distance_storage)
    set_co2_price(co2_price)
    set_electricity_price(electricity_price)
    set_subsidy_amount(subsidy_amount)
    set_discount_rate(discount_rate)
    set_sensitivity_parameter(sensitivity_parameter)
    set_sensitivity_range(sensitivity_range)
    set_sensitivity_enabled(sensitivity_toggle)
    set_compression_technology(compression_technology)

    # Daten speichern in der Session
    session['data'] = data
    print(f"Session data saved: {session['data']}")

    results = main.calculate_all()
    results = convert_np_to_python(results)

    print('Sensitivity Toggle:', sensitivity_toggle)
    print('sensitivity_range:', sensitivity_range)


    # Ergebnisse speichern
    session['results'] = results
    print(f"Session results saved: {session['results']}")
    print(f"Session keys after saving: {session.keys()}")
    session.modified = True
    return jsonify(results)


@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    session.permanent = True
    print(f"Session keys by pdf: {session.keys()}")
    data = session.get('data')
    results = session.get('results')
    print(f"Session data retrieved: {data}")
    print(f"Session results retrieved: {results}")

    if not data or not results:
        return jsonify({'error': 'No data available for PDF generation'}), 400

    data_result = {
    'lcoc_min': round(results['lcoc_min'],0),
    'lcoc_max': round(results['lcoc_max'],0),
    'payback_display': results['payback_display'],
    'roi_display': results['roi_display'],
    'effiency_compression': results['effiency_compression'],
    'compression_cost_benefit': results['compression_cost_benefit'],
    'RB_framesize': results['RB_framesize'],
    'RG_framesize': results['RG_framesize'],
    'cumulative_OPEX': results['cumulative_OPEX'],
    'cumulative_O_M': results['cumulative_O_M'],
    'cumulative_T_S': results['cumulative_T_S'],
    'capex_without_subsidy': results['capex_without_subsidy'],
    'subsidy': results['subsidy'],
    'cumulative_revenue': results['cumulative_revenue'],
    'cash_flows_lifetime': results['cash_flows_lifetime'],
    'RB_flow': results['RB_flow'],
    'RG_flow': results['RG_flow'],
    'symbol_currency': results['symbol_currency'],
    }


    # Generiere das Cash Flow-Diagramm als SVG
    sankey_svg = sankey_diagram_svg(data_result['cumulative_revenue'], data_result['subsidy'],
                                    data_result['cumulative_OPEX'], data_result['cumulative_O_M'],
                                    data_result['cumulative_T_S'], data_result['capex_without_subsidy'])

    cash_flow_svg = cash_flow_chartz(data_result['cash_flows_lifetime'], data_result['symbol_currency'])

    compression_chart_svg = compression_technology_chart(data_result['RB_flow'], data_result['RG_flow'], data_result['symbol_currency'])

    # Render die HTML-Seite
    html = render_template('CCUS_pdf.html', data=data,data_result =data_result, sankey_svg=sankey_svg,cash_flow_svg=cash_flow_svg,compression_chart_svg=compression_chart_svg)

    # Konvertiere die gerenderte HTML-Seite zu einer PDF mit pdfkit
    options = {
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm',
        'page-size': 'A4'
    }

    pdf = pdfkit.from_string(html, False, options=options, configuration=config)

    # Erstelle eine Antwort mit PDF-Inhalt
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=CO-2-Pilot_Results.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)
