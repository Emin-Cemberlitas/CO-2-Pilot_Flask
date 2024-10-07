import plotly.graph_objects as go

def create_sankey(cumulative_OPEX, cumulative_O_M, cumulative_T_S, capex_without_subsidy, cumulative_revenue, subsidy):
    # Berechne den Net Profit
    net_profit = cumulative_revenue + subsidy - (cumulative_OPEX + cumulative_O_M + cumulative_T_S + capex_without_subsidy)

    print(f" Grafik cumulative_revenue: {cumulative_revenue}")
    print(f" Grafik subsidy: {subsidy}")
    print(f" Grafik capex_without_subsidy: {capex_without_subsidy}")
    print(f" Grafik cumulative_T_S: {cumulative_T_S}")
    print(f" Grafik cumulative_O_M: {cumulative_O_M}")
    print(f" Grafik cumulative_OPEX: {cumulative_OPEX}")
    print(f" Grafik net_profit: {net_profit}")

    fig = go.Figure(go.Sankey(
        node=dict(
            label=["Revenues", "Subsidy", "Total", "Net Profit", "CAPEX", "OPEX", "O&M", "T&S"],
            color=["rgb(255,188,0)", "rgb(243,109,30)", "rgb(255,188,0)", "rgb(115, 198, 125)",
                   "rgb(35,85,106)", "rgb(40,186,218)", "rgb(198,198,198)", "rgb(48,60,73)"]
        ),
        link=dict(
            source=[0, 1, 2, 2, 2, 2, 2],  # Revenue und Subsidy fließen in die Mitte (Costs)
            target=[2, 2, 3, 4, 5, 6, 7],  # Reihenfolge: Net Profit, CAPEX, OPEX, O&M, T&S
            value=[cumulative_revenue, subsidy, net_profit, capex_without_subsidy, cumulative_OPEX, cumulative_O_M, cumulative_T_S],
            color=["rgba(255,188,0,0.6)",  # Revenues Farbe, transparent
                   "rgba(243,109,30,0.6)",  # Subsidy Farbe, transparent
                   "rgba(115, 198, 125,0.6)",  # Net Profit Farbe, transparent
                   "rgba(35,85,106,0.6)",  # CAPEX Farbe, transparent
                   "rgba(40,186,218,0.6)",  # OPEX Farbe, transparent
                   "rgba(198,198,198,0.6)",  # O&M Farbe, transparent
                   "rgba(48,60,73,0.6)"]  # T&S Farbe, transparent
        )
    ))

    # Update layout for better readability
    fig.update_layout(
        title_text="CCUS business case sankey diagramm",
        font_size=14,
        autosize=False,
        width=1500,
        height=1000
    )
    fig.show()

