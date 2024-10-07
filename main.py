import math
import numpy as np
from Assumptions import *
from setter_getter import *
from Cost_functions import *
rate = None
symbol = "€"
def construction_cost(region):
    region_index = {
        "Afghanistan": 0.429,
        "Albania": 0.403,
        "Algeria": 0.375,
        "Andorra": 0.446,
        "Angola": 0.429,
        "Anguilla": 0.536,
        "Argentina": 0.536,
        "Armenia": 0.429,
        "Aruba": 0.536,
        "Australia": 0.58,
        "Austria": 0.8,
        "Azerbaijan": 0.429,
        "Bahamas": 0.536,
        "Bahrain": 0.429,
        "Bangladesh": 0.429,
        "Barbados": 0.536,
        "Belarus": 0.435,
        "Belgium": 0.693,
        "Belize": 0.643,
        "Benin": 0.322,
        "Bermuda": 0.536,
        "Bhutan": 0.429,
        "Bolivia": 0.536,
        "Bosnia and Herzegovina": 0.403,
        "Botswana": 0.429,
        "Brazil": 0.536,
        "British Virgin Islands": 0.536,
        "Brunei": 0.536,
        "Bulgaria": 0.403,
        "Burkina Faso": 0.322,
        "Burundi": 0.322,
        "Cambodia": 0.536,
        "Cameroon": 0.322,
        "Canada": 0.965,
        "Cape Verde": 0.322,
        "Cayman Islands": 0.536,
        "Central African Republic": 0.322,
        "Chad": 0.322,
        "Chile": 0.536,
        "China": 0.643,
        "Colombia": 0.536,
        "Comoros": 0.429,
        "Congo": 0.322,
        "Cook Islands": 0.429,
        "Costa Rica": 0.643,
        "Cote d`Ivoire": 0.322,
        "Croatia": 0.403,
        "Cuba": 0.536,
        "Cyprus": 0.429,
        "Czech Republic": 0.666,
        "Democratic Republic of the Congo": 0.322,
        "Denmark": 1,
        "Djibouti": 0.322,
        "Dominica": 0.536,
        "Dominican Republic": 0.536,
        "Ecuador": 0.536,
        "Egypt": 0.375,
        "El Salvador": 0.643,
        "Equatorial Guinea": 0.322,
        "Eritrea": 0.322,
        "Estonia": 0.435,
        "Ethiopia": 0.322,
        "Falkland Islands": 0.536,
        "Faroe Islands": 1,
        "Fiji": 0.429,
        "Finland": 1,
        "France": 0.9,
        "Gabon": 0.322,
        "Gambia": 0.322,
        "Georgia": 0.429,
        "Germany": 0.95,
        "Ghana": 0.322,
        "Gibraltar": 0.446,
        "Greece": 0.403,
        "Greenland": 0.965,
        "Grenada": 0.536,
        "Guadeloupe": 0.536,
        "Guam": 0.429,
        "Guatemala": 0.643,
        "Guernsey": 0.693,
        "Guinea": 0.322,
        "Guinea-Bissau": 0.322,
        "Guyana": 0.536,
        "Guyana": 0.536,
        "Haiti": 0.536,
        "Honduras": 0.643,
        "Hungary": 0.666,
        "Iceland": 1,
        "India": 0.429,
        "Indonesia": 0.536,
        "Iran": 0.429,
        "Iraq": 0.429,
        "Ireland": 0.693,
        "Israel": 0.429,
        "Italy": 0.639,
        "Jamaica": 0.536,
        "Japan": 0.643,
        "Jersey": 0.693,
        "Jordan": 0.429,
        "Kazakhstan": 0.429,
        "Kenya": 0.322,
        "Kiribati": 0.429,
        "Kuwait": 0.429,
        "Kyrgyzstan": 0.429,
        "Laos": 0.536,
        "Latvia": 0.435,
        "Lebanon": 0.429,
        "Lesotho": 0.429,
        "Liberia": 0.322,
        "Libya": 0.375,
        "Liechtenstein": 0.666,
        "Lithuania": 0.435,
        "Luxembourg": 0.693,
        "Macedonia": 0.403,
        "Madagascar": 0.429,
        "Malawi": 0.429,
        "Malaysia": 0.536,
        "Maldives": 0.429,
        "Mali": 0.322,
        "Malta": 0.639,
        "Marshall Islands": 0.429,
        "Mauritania": 0.322,
        "Mauritius": 0.429,
        "Mayotte": 0.429,
        "Mexico": 0.643,
        "Micronesia": 0.429,
        "Moldova": 0.435,
        "Monaco": 0.693,
        "Mongolia": 0.643,
        "Morocco": 0.375,
        "Mozambique": 0.429,
        "Myanmar": 0.536,
        "Namibia": 0.429,
        "Nauru": 0.429,
        "Nepal": 0.429,
        "Netherlands": 0.693,
        "New Caledonia": 0.429,
        "New Zealand": 0.58,
        "Nicaragua": 0.643,
        "Niger": 0.322,
        "Nigeria": 0.322,
        "North Korea": 0.643,
        "Norway": 1,
        "Oman": 0.429,
        "Pakistan": 0.429,
        "Palestine": 0.429,
        "Panama": 0.643,
        "Papua New Guinea": 0.429,
        "Paraguay": 0.536,
        "Peru": 0.536,
        "Philippines": 0.536,
        "Poland": 0.435,
        "Portugal": 0.65,
        "Puerto Rico": 0.536,
        "Qatar": 0.429,
        "Romania": 0.403,
        "Russia": 0.643,
        "Rwanda": 0.322,
        "San Marino": 0.639,
        "Sao Tome and Principe": 0.322,
        "Saudi Arabia": 0.429,
        "Senegal": 0.322,
        "Serbia and Montenegro": 0.403,
        "Seychelles": 0.429,
        "Sierra Leone": 0.322,
        "Singapore": 0.536,
        "Slovakia": 0.666,
        "Slovenia": 0.403,
        "Solomon Islands": 0.429,
        "Somalia": 0.322,
        "South Africa": 0.429,
        "South Korea": 0.643,
        "Spain": 0.65,
        "Sri Lanka": 0.429,
        "Sudan": 0.375,
        "Swaziland": 0.429,
        "Sweden": 1,
        "Switzerland": 1,
        "Syria": 0.429,
        "Taiwan": 0.643,
        "Tajikistan": 0.429,
        "Tanzania": 0.322,
        "Thailand": 0.536,
        "Togo": 0.322,
        "Tokelau": 0.429,
        "Tonga": 0.429,
        "Trinidad and Tobago": 0.536,
        "Tunisia": 0.375,
        "Turkey": 0.429,
        "Turkmenistan": 0.429,
        "Tuvalu": 0.429,
        "Uganda": 0.322,
        "Ukraine": 0.435,
        "United Arab Emirates": 0.429,
        "United Kingdom": 0.85,
        "United States": 0.965,
        "Uruguay": 0.536,
        "Uzbekistan": 0.429,
        "Vanuatu": 0.429,
        "Venezuela": 0.536,
        "Vietnam": 0.536,
        "Virgin Islands": 0.536,
        "Western Sahara": 0.375,
        "Western Samoa": 0.429,
        "Yemen": 0.429,
        "Zambia": 0.429,
        "Zimbabwe": 0.429,
    }
    # Return the cost for the given region, or None if the region is not found
    return region_index.get(region.strip())

def get_exchange_rate(to_currency):
    conversion_rates = {
    "EUR": 1,
    "AUD": 1.6792,
    "CAD": 1.4734,
    "CHF": 0.9623,
    "CNY": 7.9178,
    "DKK": 7.4604,
    "GBP": 0.8623,
    "JPY": 157.5246,
    "NZD": 1.8102,
    "SEK": 11.7227,
    "USD": 1.0970,
    }

    return conversion_rates[to_currency]

def update_currency_labels(*args):
    global symbol, rate
    currency_symbols = {
        "AUD": "$", "CAD": "$", "CHF": "CHF", "CNY": "¥", "DKK": "kr.",
        "EUR": "€", "GBP": "£", "JPY": "¥", "NZD": "$", "SEK": "kr", "USD": "$"
    }
    rate = get_exchange_rate(get_selected_currency())
    symbol = currency_symbols[get_currency()]

    return rate,symbol

def get_selected_currency():
    global selected_currency
    selected_currency = get_currency()
    return selected_currency

########################################################################################################################
def calculate_all():

    rate,symbol = update_currency_labels()

    ### Laden der Eingabeparameter
    industry = get_industry()
    country = get_country()
    currency = get_currency()
    lifetime = get_lifetime()
    operation_hours = get_operation_hours()
    install_year = get_install_year()
    captured_co2 = get_captured_co2() * 1_000_000
    co2_content = get_co2_content()
    co2_capture_rate = get_co2_capture_rate()/100
    transport_type = get_transport_type()
    distance_storage = get_distance_storage()
    co2_price = get_co2_price()
    electricity_price = get_electricity_price()
    discount_rate = float(get_discount_rate()/100)
    sensitivity_parameter = get_sensitivity_parameter()
    construction_index = construction_cost(country)
    subsidy = get_subsidy_amount()*1_000_000
    compression_technology = get_compression_technology()
    print(f"compression technology: {compression_technology}")
    if get_sensitivity_range() == '':
        sensitivity_range = 0
    else:
        sensitivity_range = float(get_sensitivity_range()) / 100

    sensitivity_on = get_sensitivity_enabled()



    ########################################################################################################################

    m_dot = captured_co2 / operation_hours  # CO2/h
    captured_co2_change = (captured_co2/operation_hours)*8760

    big_tanker_needed, small_tanker_needed, big_tanker_trips, small_tanker_trips,tanker_total_fuel_cost = calculate_tanker_requirements(
        captured_co2, distance_storage, tanker_speed, tanker_loading,
        tanker_ship_small_capacity, tanker_ship_big_capacity, tanker_ship_small_energy, tanker_ship_big_energy, fuel_cost_tanker,rate
    )
    tanker_ship_total_O_M = (tanker_ship_big_O_M * big_tanker_needed + tanker_ship_small_O_M * small_tanker_needed)*rate

    if transport_type == "Shipping":
        storage_capex = storage_capex_uper * rate

    else:
        storage_capex = storage_capex_lower * rate
        tanker_ship_total_O_M = pipline_O_M*distance_storage*m_dot
        tanker_total_fuel_cost = 0

    capex_capture = (calculate_cap_cost(m_dot,co2_content)*0.5 + calculate_cap_cost(m_dot,co2_content)*0.5*construction_index)  * rate            # €/t CO2/h, Annahme, das 50% der Capture Kosten durch Baustellenkostenindex beeinflusst werden

    O_M_total = (variable_O_M * captured_co2 + fixed_O_M * m_dot)* rate

    if transport_type == "Shipping":
        transport_capex_total = (big_tanker_needed * tanker_capex_big + small_tanker_needed * tanker_capex_small)* rate
    else:
        transport_capex_total = pipeline_capex(m_dot, distance_storage, rate, transport_type)

    RG_powers = compressor_power_consumption(captured_co2_change, transport_type)
    RB_powers = RB_power_consumption(captured_co2_change, transport_type)
    compressor_power_per_ton = RG_powers/m_dot

    effiency_compression = round(((RB_powers-RG_powers)/RB_powers)*100,1)
    print(f"effiency_compression: {effiency_compression}")
    RB_power_per_ton = RB_powers/m_dot
    RG_power_per_ton = RG_powers/m_dot

    RG_CAPEX = compressor_calculation(captured_co2_change, rate, transport_type)
    RB_CAPEX = RB_costs(captured_co2_change,rate,transport_type)

    if compression_technology == "Inline":
        compressor_powers =         RB_powers
        compressor_power_per_ton =  RB_power_per_ton
        compressor_capex =          RB_CAPEX
    else:
        compressor_powers =         RG_powers
        compressor_power_per_ton =  RG_power_per_ton
        compressor_capex =          RG_CAPEX

    capex_capture_compression = compressor_capex * 1_000_000 + capex_capture - subsidy
    capex_without_subsidy = capex_capture_compression + subsidy
    capex_storage_transport = transport_capex_total + storage_capex * captured_co2 * lifetime

    OPEX_Energy = (capture_energy_consumption(co2_content)+compressor_power_per_ton) * electricity_price * captured_co2

    RB_framesize, RG_framesize = calculate_framesize(m_dot)

    def levelized_cost_of_co2(i, n):
        # Arrays für Investitionskosten, Betriebs- und Wartungskosten, Energiekosten und abgeschiedene Menge CO2 pro Jahr
        I =     [capex_capture_compression] + [0] * (n - 1)
        I_TS =  [capex_storage_transport/lifetime]  * n
        O_M =   [O_M_total+tanker_ship_total_O_M] * n
        E =     [OPEX_Energy + tanker_total_fuel_cost] * n
        m_dot = [captured_co2] * n

        # Numerator
        numerator =     sum((I[t] + I_TS[t] + O_M[t] + E[t]) / (1 + i) ** t for t in range(n))
        # Denominator
        denominator =   sum(m_dot[t] / (1 + i) ** t for t in range(n))
        # Levelized cost of CO2
        LC_CO2 = numerator / denominator
        # Separate costs
        I_cost =    sum(I[t] / (1 + i) ** t for t in range(n)) / denominator
        I_TS_cost = sum(I_TS[t] / (1 + i) ** t for t in range(n)) / denominator
        O_M_cost =  sum(O_M[t] / (1 + i) ** t for t in range(n)) / denominator
        E_cost =    sum(E[t] / (1 + i) ** t for t in range(n)) / denominator

        return LC_CO2, I_cost, I_TS_cost, O_M_cost, E_cost



    def calculate_lifetime_costs_and_revenues():
        cumulative_costs =      [capex_capture_compression]
        cumulative_revenues =   [0]


        for t in range(1, lifetime + 1):

            annual_revenue =        captured_co2 * co2_price
            annual_cost =           (OPEX_Energy + tanker_total_fuel_cost) + (O_M_total + tanker_ship_total_O_M) + capex_storage_transport/lifetime
            discounted_cost =       annual_cost / ((1 + discount_rate) ** t)
            discounted_revenue =    annual_revenue / ((1 + discount_rate) ** t)

            cumulative_costs.append(cumulative_costs[-1] + discounted_cost)
            cumulative_revenues.append(cumulative_revenues[-1] + discounted_revenue)
        return cumulative_costs, cumulative_revenues

    cumulative_costs, cumulative_revenues = calculate_lifetime_costs_and_revenues()


    def calculate_payback_period(cash_flows):
        cumulative_cash_flow = cash_flows[0]
        previous_cumulative_cash_flow = cumulative_cash_flow
        annual_revenue = captured_co2 * co2_price
        annual_cost = (OPEX_Energy + tanker_total_fuel_cost) + (
                O_M_total + tanker_ship_total_O_M) + capex_storage_transport / lifetime
        annual_cash_flow = annual_revenue - annual_cost  # Calculate annual cash flow (revenue minus cost)
        # Iterate through the cash flows to calculate payback period
        for t in range(1, len(cash_flows)):
            # Calculate annual revenue and cost dynamically for each year

            # Check if annual cash flow is positive
            if annual_cash_flow > 0:
                cumulative_cash_flow = cash_flows[t]
                if cumulative_cash_flow >= 0:
                    interpolation = -previous_cumulative_cash_flow / (
                                cumulative_cash_flow - previous_cumulative_cash_flow)
                    exact_payback_period = t - 1 + interpolation
                    roi = 100 / exact_payback_period
                    return round(exact_payback_period, 3), round(roi, 2)
            else:
                # If annual cash flow is negative, return 100
                return -100, -100

            previous_cumulative_cash_flow = cumulative_cash_flow

        # If cumulative cash flow never becomes positive, return 100
        return 100, -100

    def calculate_cash_flows_for_payback():
        cumulative_cash_flow = -capex_capture_compression
        cash_flows = [-capex_capture_compression]  # Initial investment is a negative cash flow

        # Initial Berechnung für die gegebene Lebensdauer
        for t in range(1, lifetime + 1):
            annual_revenue = captured_co2 * co2_price
            annual_cost = (OPEX_Energy + tanker_total_fuel_cost) + (
                        O_M_total + tanker_ship_total_O_M) + capex_storage_transport / lifetime
            discounted_cash_flow = (annual_revenue - annual_cost) / ((1 + discount_rate) ** t)
            cumulative_cash_flow += discounted_cash_flow
            cash_flows.append(cumulative_cash_flow)

        # Fortsetzen der Berechnung, falls der kumulative Cashflow nach der Lebensdauer noch negativ ist
        max_years = 100  # Maximal 100 Jahre als Obergrenze
        t = lifetime + 1
        while cumulative_cash_flow < 0 and t <= max_years:
            annual_revenue = captured_co2 * co2_price
            annual_cost = (OPEX_Energy + tanker_total_fuel_cost) + (
                        O_M_total + tanker_ship_total_O_M) + capex_storage_transport / lifetime
            discounted_cash_flow = (annual_revenue - annual_cost) / ((1 + discount_rate) ** t)
            cumulative_cash_flow += discounted_cash_flow
            cash_flows.append(cumulative_cash_flow)
            t += 1

        return cash_flows

    def cash_flow_compression():
        cumulative_cash_flow_RB = RB_CAPEX*1_000_000
        cumulative_cash_flow_RG = RG_CAPEX*1_000_000
        cash_flow_RB = [RB_CAPEX*1_000_000]
        cash_flow_RG = [RG_CAPEX*1_000_000]
        for t in range(1, lifetime + 1):
            RB_opex_pa = RB_power_per_ton*m_dot*operation_hours*electricity_price/((1 + discount_rate) ** t)
            RG_opex_pa = RG_power_per_ton*m_dot*operation_hours*electricity_price/((1 + discount_rate) ** t)
            cumulative_cash_flow_RB += RB_opex_pa
            cumulative_cash_flow_RG += RG_opex_pa

            cash_flow_RB.append(cumulative_cash_flow_RB)
            cash_flow_RG.append(cumulative_cash_flow_RG)

        return cash_flow_RB, cash_flow_RG, cumulative_cash_flow_RB, cumulative_cash_flow_RG

    RB_flow, RG_flow,cumulative_cash_flow_RB, cumulative_cash_flow_RG = cash_flow_compression()

    compression_cost_benefit = round((cumulative_cash_flow_RB - cumulative_cash_flow_RG)/1_000_000,1)
    print(f"compression_cost_benefit {compression_cost_benefit}")

    def calculate_cash_flows_lifetime():
        cumulative_cash_flow = -capex_capture_compression
        cash_flows = [-capex_capture_compression]  # Initial investment is a negative cash flow
        cumulative_OPEX = 0
        cumulative_O_M = 0
        cumulative_T_S = 0
        cumulative_revenue = 0
        for t in range(1, lifetime + 1):
            annual_revenue = captured_co2 * co2_price
            annual_cost = (OPEX_Energy + tanker_total_fuel_cost) + (O_M_total + tanker_ship_total_O_M) + capex_storage_transport/lifetime
            discounted_cash_flow = (annual_revenue - annual_cost) / ((1 + discount_rate) ** t)
            cumulative_cash_flow += discounted_cash_flow

            discounted_OPEX =    OPEX_Energy / ((1 + discount_rate) ** t)
            discounted_O_M =  O_M_total / ((1 + discount_rate) ** t)
            discounted_T_S =    (tanker_total_fuel_cost+tanker_ship_total_O_M+( capex_storage_transport/lifetime)) / ((1 + discount_rate) ** t)
            discounted_revenue =    annual_revenue / ((1 + discount_rate) ** t)

            cumulative_OPEX += discounted_OPEX
            cumulative_O_M += discounted_O_M
            cumulative_T_S += discounted_T_S
            cumulative_revenue += discounted_revenue

            cash_flows.append(cumulative_cash_flow)
        print(f"cash flow total {cumulative_cash_flow}")
        return cash_flows, cumulative_cash_flow, cumulative_OPEX, cumulative_O_M, cumulative_T_S, cumulative_revenue

    cash_flows, cumulative_cash_flow, cumulative_OPEX, cumulative_O_M, cumulative_T_S, cumulative_revenue = calculate_cash_flows_lifetime()

    cash_flows_lifetime = cash_flows
    cash_flows_for_payback = calculate_cash_flows_for_payback()
    LC_CO2, I_cost, I_TS_cost, O_M_cost, E_cost = levelized_cost_of_co2(discount_rate, lifetime)
    print("Kostenanteil LCOC:")
    print(f"LCOC total: {LC_CO2} €/t CO2")
    print(f"CAPEX: {I_cost} €/t CO2")
    print(f"OPEX: {O_M_cost+E_cost} €/t CO2")
    print(f"Transport & Storage: {I_TS_cost} €/t CO2")

    payback_period, roi = calculate_payback_period(cash_flows_for_payback) if calculate_payback_period(cash_flows_for_payback) else (None, None)

    if payback_period is not None and not math.isinf(payback_period):
        payback_period_lower = math.floor(payback_period)
        payback_period_upper = math.ceil(payback_period)
    else:
        payback_period_lower = float(100) if payback_period > 0 else -float(100)
        payback_period_upper = float(100) if payback_period > 0 else -float(100)

    roi_lower = round(roi - 0.5, 1)
    roi_upper = round(roi, 1)
    print(f"payback_period {payback_period}")

    if payback_period:
        print(f"Amortisationsdauer: {payback_period} Jahre")
    else:
        print("Die Investition amortisiert sich nicht innerhalb von 30 Jahren.")
    print(f"ROI is: {roi} %")

    #################   Sensitivity Analysis #######################################################################################################
    def levelized_cost_of_co2_with_modified_parameter(modified_param, param_type):
        capex = capex_capture_compression
        energy_consumption = capture_energy_consumption(co2_content)
        el_price = electricity_price

        # Modifiziere den relevanten Parameter basierend auf dem Parametertyp
        if param_type == "CAPEX":
            capex = modified_param
        elif param_type == "Energy demand":
            energy_consumption = modified_param
        elif param_type == "Electricity Price":
            el_price = modified_param

        OPEX_Energy_modified = (energy_consumption + compressor_power_per_ton) * el_price * captured_co2

        I = [capex] + [0] * (lifetime - 1)
        I_TS = [capex_storage_transport / lifetime] * lifetime
        O_M = [O_M_total + tanker_ship_total_O_M] * lifetime
        E = [OPEX_Energy_modified + tanker_total_fuel_cost] * lifetime
        m_dot = [captured_co2] * lifetime

        numerator = sum((I[t] + I_TS[t] + O_M[t] + E[t]) / (1 + discount_rate) ** t for t in range(lifetime))
        denominator = sum(m_dot[t] / (1 + discount_rate) ** t for t in range(lifetime))

        LC_CO2 = numerator / denominator
        return LC_CO2

    def calculate_cash_flows_with_modified_parameter(modified_param, param_type):
        capex = capex_capture_compression
        energy_consumption = capture_energy_consumption(co2_content)
        el_price = electricity_price
        co2_price_value = co2_price

        # Modifiziere den relevanten Parameter basierend auf dem Parametertyp
        if param_type == "CAPEX":
            capex = modified_param
        elif param_type == "Energy demand":
            energy_consumption = modified_param
        elif param_type == "Electricity Price":
            el_price = modified_param
        elif param_type == "CO2 Price":
            co2_price_value = modified_param

        OPEX_Energy_modified = (energy_consumption + compressor_power_per_ton) * el_price * captured_co2
        cumulative_cash_flow = -capex
        cash_flows = [-capex]

        for t in range(1, lifetime + 1):
            annual_revenue = captured_co2 * co2_price_value
            annual_cost = (OPEX_Energy_modified + tanker_total_fuel_cost) + (O_M_total + tanker_ship_total_O_M) + capex_storage_transport / lifetime
            discounted_cash_flow = (annual_revenue - annual_cost) / ((1 + discount_rate) ** t)
            cumulative_cash_flow += discounted_cash_flow
            cash_flows.append(cumulative_cash_flow)

        return cash_flows

    def sensitivity_analysis():
            if sensitivity_on.lower() == "true":
                change_factor = sensitivity_range
                results = {}

                if sensitivity_parameter == "CAPEX":
                    original_value = capex_capture_compression
                    for factor, color in zip([-change_factor, change_factor], ['orange', 'purple']):
                        capex_capture_compression_modified = original_value * (1 + factor)
                        LC_CO2_modified = levelized_cost_of_co2_with_modified_parameter(capex_capture_compression_modified,sensitivity_parameter)
                        cash_flows_modified = calculate_cash_flows_with_modified_parameter(capex_capture_compression_modified, sensitivity_parameter)
                        payback_period_modified, roi_modified = calculate_payback_period(cash_flows_modified)
                        results[f"CAPEX {factor * 100:+.0f}%"] = (
                        cash_flows_modified, color, LC_CO2_modified, payback_period_modified, roi_modified)
                        print(f"LC_CO2_modified {LC_CO2_modified}")

                elif sensitivity_parameter == "Energy demand":
                    original_value = capture_energy_consumption(co2_content)
                    for factor, color in zip([-change_factor, change_factor], ['orange', 'purple']):
                        energy_demand_modified = original_value * (1 + factor)
                        LC_CO2_modified = levelized_cost_of_co2_with_modified_parameter(energy_demand_modified,sensitivity_parameter)
                        cash_flows_modified = calculate_cash_flows_with_modified_parameter(energy_demand_modified, sensitivity_parameter)
                        payback_period_modified, roi_modified = calculate_payback_period(cash_flows_modified)
                        results[f"Energy demand {factor * 100:+.0f}%"] = (
                        cash_flows_modified, color, LC_CO2_modified, payback_period_modified, roi_modified)

                elif sensitivity_parameter == "CO2 Price":
                    original_value = co2_price
                    for factor, color in zip([-change_factor, change_factor], ['orange', 'purple']):
                        co2_price_modified = original_value * (1 + factor)
                        LC_CO2_modified = LC_CO2
                        cash_flows_modified = calculate_cash_flows_with_modified_parameter(co2_price_modified, sensitivity_parameter)
                        payback_period_modified, roi_modified = calculate_payback_period(cash_flows_modified)
                        results[f"CO2 price {factor * 100:+.0f}%"] = (
                        cash_flows_modified, color, LC_CO2_modified, payback_period_modified, roi_modified)

                elif sensitivity_parameter == "Electricity Price":
                    original_value = electricity_price
                    for factor, color in zip([-change_factor, change_factor], ['orange', 'purple']):
                        el_price_modified = original_value * (1 + factor)
                        LC_CO2_modified = levelized_cost_of_co2_with_modified_parameter(el_price_modified,sensitivity_parameter)
                        cash_flows_modified = calculate_cash_flows_with_modified_parameter(el_price_modified, sensitivity_parameter)
                        payback_period_modified, roi_modified = calculate_payback_period(cash_flows_modified)
                        results[f"Electricity Price {factor * 100:+.0f}%"] = (
                        cash_flows_modified, color, LC_CO2_modified, payback_period_modified, roi_modified)

                return results


    sensitivity_results = sensitivity_analysis()



    #################   Ausgabe #######################################################################################################
    print("Levelized Cost of CO2: {:.2f}".format(LC_CO2))
    print("Anteil der Investitionskosten an LC_CO2: {:.2f}".format(I_cost))
    print("Anteil der Investitionskosten (Transport und Speicherung) an LC_CO2: {:.2f}".format(I_TS_cost))
    print("Anteil der Betriebs- und Wartungskosten an LC_CO2: {:.2f}".format(O_M_cost))
    print("Anteil der Energiekosten an LC_CO2: {:.2f}".format(E_cost))

    print(f"CAPEX capture compression: {capex_capture_compression / 1_000_000:.3f} mio. €")
    print(f"Kompressor Kosten betragen: {compressor_calculation(captured_co2_change,rate,transport_type):.3f} mio. €")
    print(f"RB Kosten betragen: {RB_costs(captured_co2_change,rate,transport_type):.3f} mio. €")
    print(f"Transport & Storage kosten betragen: {capex_storage_transport / 1_000_000:.3f} mio. €")

    print(f"payback lower: {payback_period_lower}")
    print(f"payback upper: {payback_period_upper}")

    if sensitivity_on.lower() == "true":
        for param, (_, _, lc_co2, payback_period_mod, roi_mod) in sensitivity_results.items():
            print(f"Sensitivity result for {param}:")
            print(f"  Levelized Cost of CO2: {lc_co2:.2f}")
            if payback_period_mod is not None:
                print(f"  Payback Period: {payback_period_mod:.2f} Jahre")
            else:
                print("  Payback Period: N/A")
            if roi_mod is not None:
                print(f"  ROI: {roi_mod:.2f} %")
            else:
                print("  ROI: N/A")

    # Sensitivitätsergebnisse auf 0 setzen, wenn die Sensitivitätsanalyse deaktiviert ist
    if sensitivity_on.lower() == "false":
        payback_period_sensi_lower = 0
        payback_period_sensi_upper = 0
        roi_sensi_lower = 0
        roi_sensi_upper = 0
        lcoc_sensi_lower = 0
        lcoc_sensi_upper = 0
        sensitivity_results = {}

    else:
        payback_period_sensi_lower = min([payback_period] + [result[3] for result in sensitivity_results.values() if result[3] is not None]) - payback_period
        payback_period_sensi_upper = max([payback_period] + [result[3] for result in sensitivity_results.values() if result[3] is not None]) - payback_period
        roi_sensi_lower = min([roi] + [result[4] for result in sensitivity_results.values() if result[4] is not None]) - roi
        roi_sensi_upper = max([roi] + [result[4] for result in sensitivity_results.values() if result[4] is not None]) - roi
        lcoc_sensi_lower = min([LC_CO2] + [result[2] for result in sensitivity_results.values() if result[2] is not None]) - LC_CO2
        lcoc_sensi_upper = max([LC_CO2] + [result[2] for result in sensitivity_results.values() if result[2] is not None]) - LC_CO2

    lcoc_min = LC_CO2 * 0.95
    lcoc_max = LC_CO2 * 1.05

    print(f"lcoc_sensi_lower {lcoc_sensi_lower}")
    print(f"lcoc_sensi_upper {lcoc_sensi_upper}")

    #create_sankey(cumulative_OPEX, cumulative_O_M, cumulative_T_S, capex_without_subsidy, cumulative_revenue, subsidy)
    if payback_period < 0 or (payback_period > lifetime):
        payback_display = "∞"
        roi_display = "N/A"
    else:
        payback_display = f"{round(payback_period_lower,0)} - {round(payback_period_upper,0)}"
        roi_display =  f"{roi_lower} - {roi_upper}"

    print(f"payback_display: {payback_display}")
    results = {
        "Levelized_Cost_of_CO2": round(LC_CO2,1),
        "lcoc_min": round(lcoc_min,0),
        "lcoc_max": round(lcoc_max, 0),
        "lcoc_sensi_lower": round(lcoc_sensi_lower,1),
        "lcoc_sensi_upper": round(lcoc_sensi_upper, 1),
        "I_cost": I_cost,
        "I_TS_cost": I_TS_cost,
        "O_M_cost": O_M_cost,
        "E_cost": E_cost,
        "CAPEX_capture_compression": capex_capture_compression / 1_000_000,
        "Kompressor_Kosten": compressor_capex,
        "big_tanker_needed": big_tanker_needed,
        "small_tanker_needed": small_tanker_needed,
        "big_tanker_trips": big_tanker_trips,
        "small_tanker_trips": small_tanker_trips,
        "transport_CAPEX": capex_storage_transport / 1_000_000,
        "Payback_Period_lower": payback_period_lower,
        "Payback_Period": payback_period,
        "Payback_Period_upper": payback_period_upper,
        "payback_period_sensi_lower": round(payback_period_sensi_lower,1),
        "payback_period_sensi_upper": round(payback_period_sensi_upper,1),
        "ROI_lower": roi_lower,
        "ROI": roi,
        "ROI_upper": roi_upper,
        "roi_sensi_lower": round(roi_sensi_lower,1),
        "roi_sensi_upper":round( roi_sensi_upper,1),
        "cumulative_costs": cumulative_costs,
        "cumulative_revenues": cumulative_revenues,
        "cash_flows_lifetime": cash_flows_lifetime,
        "sensitivity_results": sensitivity_results,
        "cumulative_cash_flow": cumulative_cash_flow,
        "cumulative_OPEX": cumulative_OPEX,
        "cumulative_O_M": cumulative_O_M,
        "cumulative_T_S": cumulative_T_S,
        "capex_without_subsidy": capex_without_subsidy,
        "cumulative_revenue": cumulative_revenue,
        "subsidy": subsidy,
        "RB_flow": RB_flow,
        "RG_flow": RG_flow,
        "effiency_compression": effiency_compression,
        "compression_cost_benefit": compression_cost_benefit,
        "RB_framesize":RB_framesize,
        "RG_framesize":RG_framesize,
        "payback_display": payback_display,
        "roi_display": roi_display,
        "symbol_currency": symbol
    }

    return results

