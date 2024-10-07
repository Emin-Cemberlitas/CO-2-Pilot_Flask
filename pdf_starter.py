import pdfkit
from flask import Flask, render_template, make_response
from pdf_sankey import sankey_diagram_svg
from dcf_diagram import cash_flow_chartz
from compression_diagram import compression_technology_chart

app = Flask(__name__)
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

@app.route('/')
def startseite():
    # Daten, die an das Template übergeben werden
    data = {
        'industry': 'Cement',
        'country': 'Norway',
        'currency': 'EUR',
        'lifetime': 30,
        'operationHours': 8500,
        'installyear': 2030,
        'captured_co2': 0.4,
        'co2_content': 15,
        'transport_type': 'Shipping',
        'distance_storage': 800,
        'co2Price': 90,
        'electricityPrice': 70,
        'subsidy_amount': 100,
        'discount_rate': 8,
        'compression_technology': 'Inline',
        'payback_time': '6 - 7',
        'ROI': '14 - 16',
        'LCOC': '70 - 75',
        'effiency_compression': -12.5,
        'compression_cost_benefit': 20.9,
        'RB_framesize': '1 x RG71',
        'RG_framesize': '1 x (RB80 + R35)'
    }


    # Daten für das Diagramm
    cash_flows_lifetime = [-400000000,	-353703703.703704,	-310836762.688615,	-271145150.637606,	-234393657.997783,	-200364498.146096,	-168856016.801941,	-139681497.038834,	-112668052.813735,	-87655604.4571621,	-64495930.0529279,	-43051787.0860444,	-23196099.1537448,	-4811202.92013411,	12211849.1480239,	27973934.3963184,	42568457.7743689,	56081905.3466378,	68594356.8024424,	80179960.0022615,	90907370.3724643,	100840157.752282,	110037183.103965,	118552947.318486,	126437914.183783,	133738809.429429,	140498897.619841,	146758238.53689,	152553924.571194,	157920300.528884,	162889167.156374]  # Beispiel-Daten
    symbol = '€'

    RB_flow = [10000000, 10925925.9259259, 11783264.7462277, 12577096.9872479, 13312126.8400443, 13992710.0370781, 14622879.6639612, 15206370.0592233, 15746638.9437253, 16246887.9108568, 16710081.3989414, 17138964.2582791, 17536078.0169251, 17903775.9415973, 18244236.9829605, 18559478.6879264, 18851369.1554874, 19121638.1069328, 19371887.1360488, 19603599.2000452, 19818147.4074493, 20016803.1550456, 20200743.6620793, 20371058.9463697, 20528758.2836757, 20674776.1885886, 20809977.9523968, 20935164.7707378, 21051078.4914239, 21158406.0105777, 21257783.3431275]
    RG_flow = [14000000, 14462962.962963, 14891632.3731139, 15288548.4936239, 15656063.4200222, 15996355.018539, 16311439.8319806, 16603185.0296117, 16873319.4718626, 17123443.9554284, 17355040.6994707, 17569482.1291396, 17768039.0084625, 17951887.9707987, 18122118.4914802, 18279739.3439632, 18425684.5777437, 18560819.0534664, 18685943.5680244, 18801799.6000226, 18909073.7037246, 19008401.5775228, 19100371.8310396, 19185529.4731849, 19264379.1418378, 19337388.0942943, 19404988.9761984, 19467582.3853689, 19525539.2457119, 19579203.0052888, 19628891.6715637]

    # Generiere das Cash Flow-Diagramm als SVG
    sankey_svg = sankey_diagram_svg(500, 100, 200, 150, 80, 300)

    cash_flow_svg = cash_flow_chartz(cash_flows_lifetime, symbol)

    compression_chart_svg = compression_technology_chart(RB_flow, RG_flow, '€')

    # Render die HTML-Seite
    html = render_template('CCUS_pdf.html', data=data, sankey_svg=sankey_svg,cash_flow_svg=cash_flow_svg,compression_chart_svg=compression_chart_svg)

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
    response.headers['Content-Disposition'] = 'inline; filename=CCUS_report.pdf'

    return response

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify
from flask_cors import CORS
from setter_getter import *
app = Flask(__name__)
CORS(app, supports_credentials=True)
import main
from main import calculate_all
@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

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

    results = main.calculate_all()
    print('Sensitivity Toggle:', sensitivity_toggle)
    print('sensitivity_range:', sensitivity_range)

    print(f"sddss {data}")


    return jsonify(results)




if __name__ == '__main__':
    app.run(debug=True)