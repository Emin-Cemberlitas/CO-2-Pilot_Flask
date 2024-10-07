import pandas as pd
import itertools

# Defining the final reduced ranges for each variable
lifetime_range = [5, 20, 30, 50]
operation_hours_range = [ 4000, 6000, 8760]
captured_co2_range = [0.5, 1,2,4 ,5,8, 10]
co2_content_range = [10,15,20, 30, 50, 70]
transport_type_range = ["Shipping", "Pipeline","Pipelineg"]
co2_price_range = [60,70,80,90, 100, 120,150,200,250]
electricity_price_range = [10,20,50,100,150, 200]
discount_rate_range = [4, 8, 12]
distance_storage = [100, 200, 400,800]

# Generate all combinations
combinations = list(itertools.product(lifetime_range, operation_hours_range, captured_co2_range, co2_content_range,
                                      transport_type_range, co2_price_range, electricity_price_range, discount_rate_range,distance_storage))

# Create a DataFrame
columns = ['lifetime', 'operationHours', 'captured_co2', 'co2_content', 'transport_type', 'co2Price', 'electricityPrice', 'discount_rate','distance_storage']
df_combinations = pd.DataFrame(combinations, columns=columns)

# Save to Excel file
file_path = "./combinations_final2.xlsx"
df_combinations.to_excel(file_path, index=False)

import plotly.graph_objects as go
import plotly.io as pio

def cash_flow_chart(cash_flows_lifetime, symbol, sensitivity_results=None):
    # Daten für das Diagramm vorbereiten
    years = list(range(len(cash_flows_lifetime)))
    cash_flows = [round(value / 1_000_000, 1) for value in cash_flows_lifetime]

    # Grundlinie für Cash Flow
    chart_data = [go.Scatter(
        x=years,
        y=cash_flows,
        mode='lines',
        name='Cumulative Cash Flow',
        line=dict(color='rgb(40,186,208)')
    )]

    # Suche nach dem Schnittpunkt (Y = 0) und berechne die X-Koordinate
    payback_index = None
    for i in range(1, len(cash_flows_lifetime)):
        if cash_flows_lifetime[i - 1] < 0 and cash_flows_lifetime[i] >= 0:
            previous_value = cash_flows_lifetime[i - 1]
            current_value = cash_flows_lifetime[i]
            interpolation = -previous_value / (current_value - previous_value)
            payback_point_x = years[i - 1] + interpolation
            payback_index = payback_point_x
            break

    shapes = []

    if payback_index is not None:
        chart_data.append(go.Scatter(
            x=[payback_index],
            y=[0],
            mode='markers',
            name='Break-even point',
            marker=dict(color='rgb(115, 198, 125)', size=10, symbol='circle')
        ))

        # Füge die gestrichelte Linie hinzu
        shapes.append({
            'type': 'line',
            'x0': payback_index,
            'y0': 0,
            'x1': payback_index,
            'y1': min(cash_flows),
            'line': {
                'color': 'rgb(115, 198, 125)',
                'width': 2,
                'dash': 'dash'
            }
        })

    # Layout des Diagramms
    layout = go.Layout(
        title=dict(
            text="Cumulative cash flow",
            font=dict(
                family="Arial",
                size=24,
                color="black",
                weight="bold")
        ),
        xaxis=dict(
            title="Years",
            titlefont=dict(family="Arial", size=18),
            tickfont=dict(family="Arial", size=18),
            nticks=5,
            showgrid=True,
            gridwidth=1,
            gridcolor="rgba(200,200,200,0.5)"
        ),
        yaxis=dict(
            title=f"Discounted cash flow (mio. {symbol})",
            titlefont=dict(family="Arial", size=18),
            tickfont=dict(family="Arial", size=18),
            nticks=5,
            showgrid=True,
            gridwidth=1,
            gridcolor="rgba(200,200,200,0.5)"
        ),
        width=1000,
        height=500,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
    shapes=[
        dict(
            type="line",
            x0=0,
            y0=0,
            x1=1,
            y1=0,
            xref="paper",
            yref="y",
            line=dict(
                color="rgb(0, 0, 0)",
                width=1,
            ),
        ),
        # Gestrichelte Linie für den Break-even-Punkt
        dict(
            type="line",
            x0=payback_index,
            y0=0,
            x1=payback_index,
            y1=min(cash_flows),
            line=dict(
                color="rgb(115, 198, 125)",
                width=2,
                dash="dash"
            ),
        )
    ]
    )

    fig = go.Figure(data=chart_data, layout=layout)

    # Exportiere das Diagramm als SVG und speichere es als String
    svg_string = pio.to_image(fig, format="svg", engine="kaleido")
    return svg_string.decode('utf-8')

import plotly.graph_objects as go
import plotly.io as pio

def create_sankey_diagram_svg(cumulative_revenue, subsidy, cumulative_OPEX, cumulative_O_M, cumulative_T_S, capex_without_subsidy):
    net_profit = cumulative_revenue + subsidy - (cumulative_OPEX + cumulative_O_M + cumulative_T_S + capex_without_subsidy)

    sankey_data = go.Sankey(
        node=dict(
            label=["Revenues", "Subsidy", "Total", "Net Profit", "CAPEX", "OPEX", "O&M", "T&S"],
            color=["rgb(171,0,52)", "rgb(243,109,30)", "rgb(228,246,250)", "rgb(115, 198, 125)",
                   "rgb(35,85,106)", "rgb(40,186,218)", "rgb(198,198,198)", "rgb(48,60,73)"],
            thickness=10,
            pad=10,
        ),
        link=dict(
            source=[0, 1, 2, 2, 2, 2, 2],
            target=[2, 2, 3, 4, 5, 6, 7],
            value=[cumulative_revenue, subsidy, net_profit, capex_without_subsidy, cumulative_OPEX, cumulative_O_M, cumulative_T_S],
            color=[
                "rgba(171,0,52,0.6)",
                "rgba(243,109,30,0.6)",
                "rgba(115, 198, 125,0.6)",
                "rgba(35,85,106,0.6)",
                "rgba(40,186,218,0.6)",
                "rgba(198,198,198,0.6)",
                "rgba(48,60,73,0.6)"
            ]
        )
    )

    fig = go.Figure(sankey_data)

    # Setze die globale Schriftart auf Arial im Layout
    fig.update_layout(
        title_text="Your cash flows over project lifetime",
        title_font=dict(
            family="Arial",
            size=24,
            color="black",
            weight="bold"
        ),
        font=dict(
            family="Arial",
            size=16,
            color="white",
            weight="bold"
        ),
        width=1000,
        height=500,

    )

    # Exportiere das Diagramm als SVG und speichere es als String
    svg_string = pio.to_image(fig, format="svg", engine="kaleido")
    return svg_string.decode('utf-8')


import plotly.graph_objects as go
import plotly.io as pio

def compression_technology_chart(RB_flow, RG_flow, symbol):
    # Interpolationsfunktion zum Finden des Schnittpunkts
    def find_intersection(RB_flow, RG_flow):
        for i in range(1, len(RB_flow)):
            if (RB_flow[i - 1] < RG_flow[i - 1] and RB_flow[i] > RG_flow[i]) or \
               (RB_flow[i - 1] > RG_flow[i - 1] and RB_flow[i] < RG_flow[i]):
                x1 = i - 1
                x2 = i
                y1_rb = RB_flow[i - 1]
                y2_rb = RB_flow[i]
                y1_rg = RG_flow[i - 1]
                y2_rg = RG_flow[i]

                slope_rb = (y2_rb - y1_rb) / (x2 - x1)
                slope_rg = (y2_rg - y1_rg) / (x2 - x1)

                intersection_x = (y1_rg - y1_rb) / (slope_rb - slope_rg) + x1
                intersection_y = slope_rb * (intersection_x - x1) + y1_rb

                return intersection_x, intersection_y
        return None, None

    # Berechne den Schnittpunkt
    intersection_x, intersection_y = find_intersection(RB_flow, RG_flow)

    # Daten für das Diagramm vorbereiten
    years = list(range(len(RB_flow)))
    RB_flow_mio = [round(value / 1_000_000, 2) for value in RB_flow]
    RG_flow_mio = [round(value / 1_000_000, 2) for value in RG_flow]

    chart_data = [
        go.Scatter(
            x=years,
            y=RB_flow_mio,
            mode='lines+markers',
            name='Costs for inline compressor',
            line=dict(color='rgb(40,186,208)')
        ),
        go.Scatter(
            x=years,
            y=RG_flow_mio,
            mode='lines+markers',
            name='Costs for gear type compressor',
            line=dict(color='rgb(229,0,69)')
        )
    ]

    shapes = []

    # Falls der Schnittpunkt gefunden wurde, füge ihn hinzu
    if intersection_x is not None and intersection_y is not None:
        chart_data.append(go.Scatter(
            x=[intersection_x],
            y=[round(intersection_y / 1_000_000, 2)],
            mode='markers',
            name='Point of cost benefit',
            marker=dict(color='rgb(0,0,0)', size=10, symbol='circle')
        ))

        # Füge eine gestrichelte Linie vom Schnittpunkt zur X-Achse hinzu
        shapes.append({
            'type': 'line',
            'x0': intersection_x,
            'y0': 0,
            'x1': intersection_x,
            'y1': round(intersection_y / 1_000_000, 2),
            'line': {
                'color': 'rgb(0,0,0)',
                'width': 2,
                'dash': 'dash'
            }
        })

    # Layout für das Diagramm
    layout = go.Layout(
        title=dict(
            text="Compression technology discounted costs",
            font=dict(
                family="Arial",
                size=24,
                color="black",
                weight="bold"
            )
        ),
        xaxis=dict(
            title="Years",
            titlefont=dict(
                family="Arial, sans-serif",
                size=18
            ),
            tickfont=dict(
                family="Arial, sans-serif",
                size=18
            )
        ),
        yaxis=dict(
            title=f"Discounted costs (mio. {symbol})",
            titlefont=dict(
                family="Arial, sans-serif",
                size=18
            ),
            tickfont=dict(
                family="Arial, sans-serif",
                size=18
            ),
            tickformat=',.0f'
        ),
        legend=dict(
            orientation='h',
            x=0.5,
            xanchor='center',
            y=-0.2,
            font=dict(  # Schriftgröße der Legende festlegen
            family="Arial, sans-serif",
            size=18,  # Hier die gewünschte Schriftgröße einstellen
            color="black"
        )
        ),
        margin=dict(
            l=50, r=50, t=50, b=50
        ),
        shapes=shapes,
        width=1000,
        height=600,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig = go.Figure(data=chart_data, layout=layout)

    # Exportiere das Diagramm als SVG und speichere es als String
    svg_string = pio.to_image(fig, format="svg", engine="kaleido")
    return svg_string.decode('utf-8')
