import plotly.graph_objects as go
import plotly.io as pio

def sankey_diagram_svg(cumulative_revenue, subsidy, cumulative_OPEX, cumulative_O_M, cumulative_T_S, capex_without_subsidy):
    net_profit = cumulative_revenue + subsidy - (cumulative_OPEX + cumulative_O_M + cumulative_T_S + capex_without_subsidy)

    sankey_data = go.Sankey(
        node=dict(
            label=["Revenues", "Subsidy", "Total", "Net Profit", "CAPEX", "OPEX", "O&M", "T&S"],
            color=["rgb(171,0,52)", "rgb(243,109,30)", "rgb(228,246,250)", "rgb(115, 198, 125)",
                   "rgb(35,85,106)", "rgb(40,186,218)", "rgb(198,198,198)", "rgb(48,60,73)"],
            thickness=8,
            pad=30,
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
            ],
            line=dict(color="rgba(0,0,0,0)", width=0)
        )
    )

    fig = go.Figure(sankey_data)

    # Setze die globale Schriftart auf Arial im Layout
    fig.update_layout(
        font=dict(
            family="Arial",
            size=16,
            color="white",
            weight="bold"
        ),
        width=1100,
        height=450,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin = dict(t=0, b=0)
    )

    # Exportiere das Diagramm als SVG und speichere es als String
    svg_string = pio.to_image(fig, format="svg", engine="kaleido")
    return svg_string.decode('utf-8')



