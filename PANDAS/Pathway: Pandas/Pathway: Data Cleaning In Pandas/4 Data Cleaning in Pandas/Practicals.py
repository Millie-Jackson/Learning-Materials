import pandas as pd

#pd.set_option('display.max_columns', None)
flights_df = pd.read_csv("flights.txt", sep="|")

#print(flights_df.head())
#print(flights_df)
#print(flights_df.dtypes)
#print(flights_df.info())

#print(flights_df["DISTANCE"][0:10].sum())

#flights_df["DISTANCE"] = flights_df["DISTANCE"].str.strip("miles")
#flights_df["DISTANCE"] = flights_df["DISTANCE"].astype("int64")
#print(flights_df["DISTANCE"])

#flights_df['AIRLINECODE'].describe()
flights_df['AIRLINECODE'] = flights_df['AIRLINECODE'].astype('category')
#print(flights_df['AIRLINECODE'])

duplicates = flights_df[["ORIGAIRPORTNAME", "DESTAIRPORTNAME", "AIRLINECODE", "FLIGHTDATE", "CRSDEPTIME", "DEPTIME", "ARRTIME"]].duplicated(keep=False)
flights_df[duplicates]
#print(flights_df[duplicates])
#sort = duplicates.sort_values(ascending=False)
#print(sort)

summaries = {"CRSARRTIME": "mean", "ARRTIME": "mean", "ARRDELAY": "mean", "CRSELAPSEDTIME": "mean", "ACTUALELAPSEDTIME": "mean"}

grouped_duplicates = flights_df[duplicates].groupby(["FLIGHTDATE", "AIRLINECODE", "ORIGAIRPORTNAME", "DESTAIRPORTNAME"], observed=True)
grouped_duplicates_min_transactionid = grouped_duplicates["TRANSACTIONID"].min().reset_index()

f_df_duplicates = pd.merge(
    grouped_duplicates_min_transactionid,
    grouped_duplicates.agg(summaries).reset_index(),
    how="inner").sort_values("TRANSACTIONID")

f_df_duplicates

f_df_duplicates = f_df_duplicates.dropna().reset_index(drop=True)
flights_df['TRANSACTIONID'] = flights_df['TRANSACTIONID'].astype('int64')
#print(f_df_duplicates)
#print(remove_nan)




# Set index to a common column
flights_df = flights_df.set_index("TRANSACTIONID")
f_df_duplicates = f_df_duplicates.set_index("TRANSACTIONID")

# Update old df with new data
flights_df.update(f_df_duplicates)

# Reset to original index
flights_df.reset_index(inplace=True)


# Find all unique items
flights_df.at[0, "ORIGINSTATENAME"] = "FAKESTATE"
states = flights_df["ORIGINSTATENAME"].unique()

# Change a specific item
#.iat[1, 0] = "FAKESTATE"


print(type(flights_df))
print(states)
#print(states.iat[1, 1])
#print(flights_df.iat[1, 1])

print("hello world")