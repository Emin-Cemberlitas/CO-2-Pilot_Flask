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
