import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import numpy as np
from matplotlib.ticker import MaxNLocator


def cash_flow_chartz(cash_flows_lifetime, symbol):
    years = np.arange(len(cash_flows_lifetime))
    cash_flows = np.array(cash_flows_lifetime) / 1_000_000

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

    plt.rc('font', family='Arial')
    # Erstellen des Diagramms
    fig, ax = plt.subplots(figsize=(13, 4.5))

    # Zeichne den Cash Flow Verlauf
    ax.plot(years, cash_flows, label='Cumulative cash flow', color=(40/255, 186/255, 218/255), linewidth=2)

    # Füge den Break-even-Punkt hinzu, wenn er existiert
    if payback_index is not None:
        ax.scatter(payback_index, 0, color='green', label='Break-even point', zorder=5)
        # Statt ymin und ymax in relativen Werten zu verwenden, lasse die Linie von 0 bis zum Minimum der Cashflow-Daten verlaufen
        ax.vlines(x=payback_index, ymin=min(cash_flows), ymax=0, color='green', linestyle='--', linewidth=2,
                  label='Payback period')
        # Füge eine schwarze Linie bei Y=0 hinzu
    ax.axhline(0, color='black', linewidth=1, linestyle='-')

    ax.set_xlim(left=0)
    # Anpassung der Achsenbeschriftungen (Schriftart, Größe, Fettgedruckt)
    ax.set_xlabel("Years", fontsize=14, fontweight='bold', fontfamily='Arial')  # X-Achse Beschriftung
    ax.set_ylabel(f"Discounted cash flow (mio. {symbol})", fontsize=14, fontweight='bold', fontfamily='Arial')  # Y-Achse Beschriftung

    # Anpassung der Ticks (Werte auf der Achse)
    ax.tick_params(axis='x', labelsize=14, labelcolor='black',  width=0)  # X-Achse Werte
    ax.tick_params(axis='y', labelsize=14, labelcolor='black', width=2)  # Y-Achse Werte

    # Dynamische Anpassung der X-Achse Ticks mit MaxNLocator (0 wird immer dabei sein)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True, prune='lower', nbins=6))  # Prune entfernt überflüssige Ticks, nbins setzt das Maximum der Ticks

    # Dynamische Anpassung der Y-Achse Ticks (für weniger Gitterlinien)
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5))  # Beschränkt die Anzahl der Ticks auf der Y-Achse auf maximal 5

    # Gitterlinie anpassen
    ax.grid(True, which='both', linestyle='-', linewidth=0.5, color=(198/255,198/255,198/255))
    # Entferne die oberen und rechten Spines (Linien des "Kastens")

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # SVG-Export
    img_data = io.StringIO()
    plt.savefig(img_data, format='svg', bbox_inches='tight')
    plt.close(fig)

    # SVG-String zurückgeben
    img_data.seek(0)
    svg_string = img_data.getvalue()
    return svg_string
