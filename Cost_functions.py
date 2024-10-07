import math
import numpy as np

# Data from the table
mtpa_values =      np.array([0.08, 0.10, 0.13, 0.16, 0.20, 0.26, 0.33, 0.41, 0.51, 0.65, 0.82, 1.04, 1.32, 1.63, 2.04, 2.54, 3.19, 4.01])
average_4_stages = np.array([5.24, 5.26, 5.35, 5.44, 5.50, 5.85, 6.21, 6.29, 6.62, 6.88, 6.98, 7.53, 8.14, 9.02, 11.37, 12.26, 13.10, 14.18])
average_6_stages = np.array([5.84, 5.86, 6.23, 6.61, 6.68, 6.99, 7.32, 7.42, 7.81, 8.13, 8.28, 9.15, 10.74, 11.79, 14.57, 16.39, 17.48, 18.90])
average_8_stages = np.array([6.46, 6.49, 7.14, 7.80, 7.89, 8.15, 8.43, 8.55, 8.99, 9.37, 9.55, 11.32, 13.26, 13.73, 17.52, 20.30, 21.59, 23.27])

power_4_stages = np.array([709, 864, 1073, 1409, 1727, 2136, 2727, 3318, 4091, 5136, 6500, 8182, 10273, 12682, 15819, 19682, 24591, 30864])
power_6_stages = np.array([982, 1227, 1500, 1864, 2318, 2909, 3682, 4500, 5636, 7045, 8909, 11273, 14136, 17409, 21773, 27091, 33909, 42636])
power_8_stages = np.array([1182, 1409, 1727, 2136, 2727, 3409, 4318, 5227, 6545, 8227, 10364, 13091, 16545, 20364, 25409, 31682, 39682, 49864])

RB_pipeline_power = np.array([819.169850555692, 1014.61662724939, 1267.27316788178, 1603.39116928254, 2034.3306168468, 2581.7541122429, 3272.94463641139, 4032.16547911662, 5054.93343652292, 6405.63383320377, 8130.40135870418, 10302.9039997524, 13034.6751881955, 16090.9045466899, 20179.4317441365, 25150.8965291853, 31517.836955407, 39651.1432390315])
RB_shipping_power = np.array([1023.81129361254, 1268.13254261077, 1584.03199729425, 2004.40131620884, 2543.43063236643, 3228.22513900601, 4092.92548244717, 5042.41932646271, 6321.85990234138, 8011.85145753723, 10170.0669757251, 12888.6792549734, 16307.3054996339, 20131.1579732544, 25247.573014736, 31468.7656762399, 39436.9165425501, 49616.4195530803])
RB_pipeline_supercritical_power = np.array([1214.25575435951,	1504.06081339784,	1878.81571047173,	2377.59141907683,	3017.21187859704,	3829.84729452528,	4856.02022862104,	5982.58690103323,	7500.89345480622,	9506.63787391074,	12068.2309679999,	15295.0665768054,	19352.8973679092,	23891.1191698209,	29964.1124255757,	37348.3332008221,	46806.6106722322,	58890.3556897419])

RB_pipeline_capex = np.array([5.1,	5,	4.96,	5.07,	5.15,	5.39,	5.65,	5.76,	6.01,	6.21,	6.2,	6.63,	7.06,	7.8,	9.78,	10.46,	11.09,	11.91])
RB_shipping_capex = np.array([5.27,	5.32,	5.68,	5.8,	5.78,	6.01,	6.16,	6.13,	6.29,	6.53,	6.5,	7.04,	8.1,	8.84,	10.82,	12.02,	12.66,	13.57])
RB_pipeline_supercritical_capex = np.array([6.15,	6.04,	6.68,	7.04,	7.17,	7.33,	7.42,	7.49,	7.78,	8.06,	8.11,	9.56,	11.09,	11.42,	14.35,	16.58,	17.61,	18.86])

mass_flow_tons = np.array([9.4,	11.645,	14.55,	18.42,	23.385,	29.695,	37.665,	46.405,	58.195,	73.78,	93.69,	118.775,	150.325,	185.585,	232.8,	290.205,	363.755,	457.745])
RB_frame_size = ["RB28","RB28",	"RB28",	"RB35",	"RB35",	"RB45",	"RB45",	"(RB45 + RB28)",	"(RB56 + RB28)",	"(RB63 + RB28)",	"(RB71 + RB28)",	"(RB80 + RB35)",	"(RB90 + RB35)",	"(RB90 + RB 45)",	"(RB112 + RB45)",	"(RB125 + RB56)",	"(RB140 + RB56)",	"(RB160 + RB63)"]
RG_frame_size = ["RG20","RG22",	"RG25",	"RG28",	"RG31",	"RG35",	"RG40",	"RG45",	"RG50",	"RG56",	"RG63",	"RG71",	"RG80",	"RG90",	"RG100","RG112","RG125","RG140"]

import numpy as np

def calculate_framesize(x):
    max_capacity = 457.745  # Maximale Kapazität eines Kompressors [t CO2/h]

    # Anzahl der benötigten Kompressoren berechnen
    num_compressors = int((x - 1) // max_capacity + 1)

    # Kapazität pro Kompressor berechnen
    compressor_capacity = min(x / num_compressors, max_capacity)

    # Nächsten höheren Wert im mass_flow_tons-Array finden
    mtpa_per_compressor = np.ceil(compressor_capacity)  # Zuerst auf nächste Ganzzahl aufrunden
    next_higher_value = min(filter(lambda y: y >= mtpa_per_compressor, mass_flow_tons), default=max(mass_flow_tons))

    # Index des aufgerundeten Wertes in mass_flow_tons finden
    index = np.where(mass_flow_tons == next_higher_value)[0][0]  # Index des nächsten höheren Werts finden

    # Entsprechenden Wert aus RB_frame_size und RG_frame_size anhand des Indexes holen
    RB_value = RB_frame_size[index]
    RG_value = RG_frame_size[index]

    # Rückgabewerte im gewünschten Format
    rb_return = f"{num_compressors} x {RB_value}"
    rg_return = f"{num_compressors} x {RG_value}"

    return rb_return, rg_return



def compressor_power_consumption(x, transport_type):
    max_capacity = 4_000_000  # Maximale Kapazität eines Kompressors [mtpa]

    num_compressors = int((x - 1) // max_capacity + 1)  # Anzahl der benötigten Kompressoren

    total_compressor_power = 0

    for i in range(num_compressors):
        # Kapazität, die dieser Kompressor verarbeitet
        compressor_capacity = min(x / num_compressors, max_capacity)
        mtpa = compressor_capacity / 1_000_000

        # Interpolierten Leistungsbedarf für diesen Kompressor berechnen
        if transport_type == "Shipping":
            selected_stage = power_6_stages
        elif transport_type == "Pipeline":
            selected_stage = power_8_stages
        elif transport_type == "Pipelineg":
            selected_stage = power_4_stages
        else:
            raise ValueError("Invalid transport type")

        interpolated_value = np.interp(mtpa, mtpa_values, selected_stage)

        total_compressor_power += interpolated_value

    return total_compressor_power / 1000  # Umrechnung in MW

def RB_power_consumption(x, transport_type):
    max_capacity = 4_000_000  # Maximale Kapazität eines Kompressors [mtpa]

    num_compressors = int((x - 1) // max_capacity + 1)  # Anzahl der benötigten Kompressoren

    total_compressor_power = 0

    for i in range(num_compressors):
        # Kapazität, die dieser Kompressor verarbeitet
        compressor_capacity = min(x / num_compressors, max_capacity)
        mtpa = compressor_capacity / 1_000_000

        # Interpolierten Leistungsbedarf für diesen Kompressor berechnen
        if transport_type == "Shipping":
            selected_stage = RB_shipping_power
        elif transport_type == "Pipeline":
            selected_stage = RB_pipeline_supercritical_power
        elif transport_type == "Pipelineg":
            selected_stage = RB_pipeline_power
        else:
            raise ValueError("Invalid transport type")

        interpolated_value = np.interp(mtpa, mtpa_values, selected_stage)

        total_compressor_power += interpolated_value
    return total_compressor_power / 1000  # Umrechnung in MW

def calculate_co2_share(co2_share_flue_gas):
    if co2_share_flue_gas < 0.15:
        return 0.25
    elif co2_share_flue_gas > 0.75:
        return -0.6
    elif co2_share_flue_gas > 0.50:
        return -0.4
    elif co2_share_flue_gas > 0.25:
        return -0.2
    else:
        return 0

def capture_energy_consumption(co2_share_flue_gas):
    if co2_share_flue_gas < 40:
        energy_consumption = (3.1897 * np.power(co2_share_flue_gas, -0.203))
    else:
        energy_consumption = 20.05 * np.power(co2_share_flue_gas, -0.7)
    return energy_consumption/3.6



#Formel für Capture Anlage
def calculate_cap_cost(m_dot,co2_content):
    # Berechnung der Basis-CAPEX-Kosten basierend auf x
    capture_cost = 265.6 * (m_dot / 32) ** 0.6
    capture_reduction = 3.7405 * np.power(co2_content, -0.515)

    # Anpassung der CAPEX-Kosten durch den Skalierungsfaktor
    adjusted_capex = capture_cost * capture_reduction

    return adjusted_capex*1_000_000

#Formel für RG Kompressoren
def compressor_calculation(x, rate, transport_type):
    max_capacity = 4_000_000  # Maximale Kapazität eines Kompressors [mtpa]
    mtpa= x/1_000_000
    # Skaleneffekte als Dictionary definieren
    scale_effects = {
        2: 0.86,  # 14% Reduktion
        3: 0.81,  # 19% Reduktion
        4: 0.78,  # 22% Reduktion
        5: 0.77,  # 23% Reduktion
        6: 0.75   # 25% Reduktion
    }

    def get_interpolated_value(mtpa, transport_type):
        if transport_type == "Shipping":
            selected_stage = average_6_stages
        elif transport_type == "Pipeline":
            selected_stage = average_8_stages
        elif transport_type == "Pipelineg":
            selected_stage = average_4_stages
        else:
            raise ValueError("Invalid transport type")

        # Interpolate the value
        interpolated_value = np.interp(mtpa, mtpa_values, selected_stage)
        return interpolated_value

    num_compressors = int((x - 1) // max_capacity + 1)  # Die (x-1) sorgt dafür, dass volle Kapazitäten richtig behandelt werden
    print(f"Nummer Kompressoren: {num_compressors}")
    capacity_per_compressor = x / num_compressors  # Gleichmäßige Aufteilung der Gesamtkapazität auf alle Kompressoren

    # Kosten für jeden Kompressor basierend auf interpolierten Werten berechnen und summieren
    cost_compressor = 0
    interpolated_value = get_interpolated_value(mtpa, transport_type)
    for _ in range(num_compressors):
        cost_compressor += interpolated_value

    # Skaleneffekte anwenden, falls zutreffend
    if num_compressors in scale_effects:
        cost_compressor *= scale_effects[num_compressors]
    elif num_compressors > 6:
        cost_compressor *= scale_effects[6]  # Für 6 oder mehr Kompressoren

    return cost_compressor * rate




    # Formel für CO2 Transport CAPEX Pipeline
def pipeline_capex(m_dot, storage_distance,rate, transport_type):
    if transport_type == "Pipelineg":
        pipeline_capex = 892.94 * np.power(m_dot, -0.831)  # gas
    else:
        pipeline_capex = 818.38 * np.power(m_dot, -0.868) #super critical

    return pipeline_capex * storage_distance *1000 * rate * m_dot

# Funktion zur Berechnung der benötigten Tanker und Fahrten mit Optimierung
def calculate_tanker_requirements(co2_mtpa, distance_storage, tanker_speed, tanker_loading, small_capacity,
                                  big_capacity, tanker_ship_small_energy, tanker_ship_big_energy, fuel_cost_tanker,rate):
    # Duration for transport to storage and back plus loading/unloading times
    tanker_route_duration = distance_storage / tanker_speed  # h (one way)
    tanker_total_time = tanker_route_duration * 2 + tanker_loading * 2  # h (round trip)

    # Annual transport capacity and trips per year for big tanker
    big_trips_per_year = math.floor(8760 / tanker_total_time)
    big_annual_capacity = big_trips_per_year * big_capacity

    # Annual transport capacity and trips per year for small tanker
    small_trips_per_year = math.floor(8760 / tanker_total_time)
    small_annual_capacity = small_trips_per_year * small_capacity

    # Initialize the best combination with a large number (to find minimum)
    best_combination = (float('inf'), 0, 0)  # (total_tankers, big_tankers, small_tankers)

    # Try combinations of big and small tankers
    big_tanker_needed = 0
    while big_tanker_needed * big_annual_capacity <= co2_mtpa:
        remaining_capacity = co2_mtpa - (big_tanker_needed * big_annual_capacity)
        small_tanker_needed = math.ceil(remaining_capacity / small_annual_capacity)

        # Total number of tankers in this combination
        total_tankers = big_tanker_needed + small_tanker_needed

        # Update the best combination if this one uses fewer tankers
        if total_tankers < best_combination[0]:
            best_combination = (total_tankers, big_tanker_needed, small_tanker_needed)

        big_tanker_needed += 1

    # Extract the best combination
    big_tanker_needed = best_combination[1]
    small_tanker_needed = best_combination[2]

    # Calculate trips per year for each tanker type based on the final combination
    big_tanker_trips = big_tanker_needed * big_trips_per_year
    remaining_capacity_after_big = co2_mtpa - (big_tanker_needed * big_annual_capacity)
    small_tanker_trips = math.ceil(remaining_capacity_after_big / small_capacity) if small_tanker_needed > 0 else 0

    big_tanker_travelling_time = big_tanker_needed * big_tanker_trips * tanker_route_duration * 2
    small_tanker_travelling_time = small_tanker_needed * small_tanker_trips * tanker_route_duration * 2

    big_tanker_fuel_cost = big_tanker_travelling_time * tanker_ship_big_energy * fuel_cost_tanker
    small_tanker_fuel_cost = small_tanker_travelling_time * tanker_ship_small_energy * fuel_cost_tanker

    tanker_total_fuel_cost = (big_tanker_fuel_cost + small_tanker_fuel_cost)*rate


    return big_tanker_needed, small_tanker_needed, big_tanker_trips, small_tanker_trips, tanker_total_fuel_cost

def RB_costs(x, rate, transport_type):
    max_capacity = 4_000_000  # Maximale Kapazität eines Kompressors [mtpa]
    mtpa= x/1_000_000
    # Skaleneffekte als Dictionary definieren
    scale_effects = {
        2: 0.86,  # 14% Reduktion
        3: 0.81,  # 19% Reduktion
        4: 0.78,  # 22% Reduktion
        5: 0.77,  # 23% Reduktion
        6: 0.75   # 25% Reduktion
    }

    def get_interpolated_value(mtpa, transport_type):
        if transport_type == "Shipping":
            selected_stage = RB_shipping_capex
        elif transport_type == "Pipeline":
            selected_stage = RB_pipeline_supercritical_capex
        elif transport_type == "Pipelineg":
            selected_stage = RB_pipeline_capex
        else:
            raise ValueError("Invalid transport type")

        # Interpolate the value
        interpolated_value = np.interp(mtpa, mtpa_values, selected_stage)
        return interpolated_value

    num_compressors = int((x - 1) // max_capacity + 1)  # Die (x-1) sorgt dafür, dass volle Kapazitäten richtig behandelt werden
    print(f"Nummer Kompressoren: {num_compressors}")
    capacity_per_compressor = x / num_compressors  # Gleichmäßige Aufteilung der Gesamtkapazität auf alle Kompressoren

    # Kosten für jeden Kompressor basierend auf interpolierten Werten berechnen und summieren
    cost_compressor = 0
    interpolated_value = get_interpolated_value(mtpa, transport_type)
    for _ in range(num_compressors):
        cost_compressor += interpolated_value

    # Skaleneffekte anwenden, falls zutreffend
    if num_compressors in scale_effects:
        cost_compressor *= scale_effects[num_compressors]
    elif num_compressors > 6:
        cost_compressor *= scale_effects[6]  # Für 6 oder mehr Kompressoren

    return cost_compressor * rate