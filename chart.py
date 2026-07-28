"""
chart.py — your job this week.

Goal: fetch prices for one company and save a line chart of its closing
price as a PNG file.

Fill in the TODOs. Run it with:  python chart.py
"""

import matplotlib
# Tells matplotlib "don't try to open a window, just save files".
# Without this you may get errors depending on your setup.
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from data import load_example_prices


SYMBOL = "AAPL"
DAYS = 90


def main():
    # 1. Get the data. This gives you a DataFrame with a "close" column
    #    and dates as the index.
    df = load_example_prices()

    # Uncomment these two lines to see what you're working with.
    # Do this first, before writing anything else.
    print(df.head())
    print(df.info())

    # 2. TODO: make the figure and axes.
    fig, ax = plt.subplots(figsize=(10, 5))

    # 3. TODO: plot the closing price.
    #    Hint: the x values are df.index, the y values are df["close"]
    ax.plot(df.index,df["close"],label="Example Co.",color="darkgreen")
    # 4. TODO: label it properly. A chart with no labels is not a chart.
    #    You want: a title, a y-axis label, and a legend.
    #    Hints: ax.set_title(...), ax.set_ylabel(...), ax.legend()
    ax.set_title("Closing Prices of Example Co. Share")
    ax.set_ylabel("Price (USD)")
    ax.legend()
    ax.grid(True,alpha=0.3) #true means grid lines show, alpha does the transparency
    df=df.tail(30) #shows last 30 days 
    # 5. TODO: save it to output/<SYMBOL>.png
    #    Hint: fig.savefig(...) — look up what bbox_inches="tight" does
    #    and decide whether you want it.
    ax.set_ylim(170,200) #upper and lower bound of y axis, INSTEAD OF SAVING 2 DIFFERENT FILES I JUST ADJUSTED IT AND USED SCREENSHOTS TO COMPARE 
    fig.savefig("output/AAPL.png", bbox_inches="tight", dpi = 150)
    print(f"Done — go and look at output/{SYMBOL}.png")


if __name__ == "__main__":
    main()
