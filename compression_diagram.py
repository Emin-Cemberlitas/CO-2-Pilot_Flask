import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io

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
    years = np.arange(len(RB_flow))
    RB_flow_mio = np.array(RB_flow) / 1_000_000  # Umwandlung in Millionen
    RG_flow_mio = np.array(RG_flow) / 1_000_000
    plt.rc('font', family='Arial')
    fig, ax = plt.subplots(figsize=(13, 8))



    # Plot für RB und RG
    ax.plot(years, RB_flow_mio, label='Costs for inline compressor', color=(35/255,85/255,106/255), marker='o', linewidth=2)
    ax.plot(years, RG_flow_mio, label='Costs for gear type compressor', color=(229/255,0/255,69/255), marker='o', linewidth=2)

    # Falls der Schnittpunkt gefunden wurde, füge ihn hinzu
    if intersection_x is not None and intersection_y is not None:
        ax.scatter([intersection_x], [intersection_y / 1_000_000], color='black', label='Point of cost benefit', zorder=5)
        ax.axvline(x=intersection_x, ymin=0, ymax=intersection_y / max(RB_flow_mio.max(), RG_flow_mio.max()),
                   color='black', linestyle='--', linewidth=2)


    # Anpassung der Achsenbeschriftungen (Schriftart, Größe, Fettgedruckt)
    ax.set_xlabel("Years", fontsize=16, fontweight='bold', fontfamily='Arial')  # X-Achse Beschriftung
    ax.set_ylabel(f"Discounted costs (mio. {symbol})", fontsize=16, fontweight='bold', fontfamily='Arial')  # Y-Achse Beschriftung
    ax.grid(True, which='both', linestyle='-', linewidth=0.5, color=(198/255,198/255,198/255))

    # Anpassung der Ticks (Werte auf der Achse)
    ax.tick_params(axis='x', labelsize=16, labelcolor='black',  width=2)  # X-Achse Werte
    ax.tick_params(axis='y', labelsize=16, labelcolor='black', width=2)  # Y-Achse Werte

    # Legende
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=2,  prop={'family': 'Arial', 'size': 14})
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    # Layout-Anpassungen
    plt.tight_layout()

    # Exportiere das Diagramm als SVG und speichere es als String
    img_data = io.StringIO()
    plt.savefig(img_data, format='svg', bbox_inches='tight')
    plt.close(fig)

    # SVG-String zurückgeben
    img_data.seek(0)
    svg_string = img_data.getvalue()
    return svg_string
