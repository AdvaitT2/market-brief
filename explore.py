from data import load_example_prices
df = load_example_prices()
print(df.head())
print("number of rows", len(df))
print("Firat Date: ",df.index[0].date())
print("Last closing price:", df["close"].iloc[-1])
print("Highest close:", df["close"].max())
#each row is the final daily price of the share 