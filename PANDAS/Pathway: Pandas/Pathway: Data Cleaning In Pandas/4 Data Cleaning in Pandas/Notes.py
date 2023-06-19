import pandas as pd
import numpy as np
from datetime import datetime

#pd.set_option('display.max_columns', None)
flights_df = pd.read_csv("flights.txt", sep="|")

#print(flights_df.head())
#print(flights_df)
#print(flights_df.dtypes)
#print(flights_df.info())

#print(flights_df["DISTANCE"][0:10].sum())

flights_df["DISTANCE"] = flights_df["DISTANCE"].str.strip("miles")
flights_df["DISTANCE"] = flights_df["DISTANCE"].astype("int64")
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
original_states = pd.Series(flights_df["ORIGINSTATENAME"].unique())
# Change a specific item
flights_df.iat[1, flights_df.columns.get_loc("ORIGINSTATENAME")] = "Fakestate"
# Find all unique items
states = pd.Series(flights_df["ORIGINSTATENAME"].unique())
# Find the difference between the origin states
inconsistent_categories = original_states[original_states.isin(states)]
inconsistent_rows = flights_df[~flights_df["ORIGINSTATENAME"].astype(str).isin(inconsistent_categories.astype(str))]
# Remove/drop the inconsistent rows
flights_df = flights_df.drop(inconsistent_rows.index)



# REMAPPING CATCGORIES
flights_df["CANCELLED"].value_counts()
flights_df["CANCELLED"].replace("0", "False", inplace=True)
flights_df["CANCELLED"].replace("F", "False", inplace=True)
flights_df["CANCELLED"].replace("1", "True", inplace=True)
flights_df["CANCELLED"].replace("T", "True", inplace=True)

# Using a dictionary
flights_df["DIVERTED"].value_counts()
mapping = {"F": "False", "0": "False", "1": "True", "T": "True"}
flights_df["DIVERTED"] = flights_df["DIVERTED"].replace(mapping)

# Using NumPy
bins = [0, 1000, 2500, np.inf]
labels = ["short", "medium", "long"]
flights_df["DISTANCE_CATEGORY"] = pd.cut(flights_df["DISTANCE"], bins=bins, labels=labels)
flights_df[["DISTANCE", "DISTANCE_CATEGORY"]]
flights_df[flights_df["DISTANCE_CATEGORY"] == "long"]

# Date Time
flights_df = pd.read_csv('flights.txt', sep='|')
## Assign date_format
date_format = "%Y%m%d"
# date_format = "%d-%m-%Y"
#flights_df = pd.to_datetime(flights_df["FLIGHTDATE"], format=date_format)



# Challenge
# Modify CRSDEPTIME and CRSARRTIME to be in a datetime format. 
# Notice that the days might tick over on to the next day... 
# Which column can you use to help you infer whether this could be the case?
challange_df = pd.DataFrame({
    'CRSDEPTIME': flights_df['CRSDEPTIME'],
    'CRSARRTIME': flights_df['CRSARRTIME'],
    'FLIGHTDATE': flights_df['FLIGHTDATE']
})

#challange_df = challange_df.convert_dtypes()

# Convert FLIGHTDATE column to datetime format
#challange_df['FLIGHTDATE'] = pd.to_datetime(challange_df['FLIGHTDATE'], format=date_format)

# Convert CRSDEPDATETIME to a datetime object
#challange_df["CRSDEPTIME"] = pd.to_datetime(challange_df["CRSDEPTIME"], infer_datetime_format=True, errors='coerce')
#challange_df["CRSARRTIME"] = pd.to_datetime(challange_df["CRSARRTIME"], infer_datetime_format=True, errors='coerce')

# Extract CRSARRDATE from CRSARRTIME
#challange_df['CRSARRDATE'] = challange_df['CRSARRTIME'].dt.floor('D')



# CROSS VALIDATION
html_table = """
<table>
    <tr>
        <td><b>Name</b></td>
        <td><b>D.O.B</b></td>
        <td><b>Age</b></td>
        <td><b>Deceased</b></td>
        <td><b>U.G Loan (£)</b></td>
        <td><b>P.G Loan (£)</b></td>
        <td><b>Total Loan (£)</b></td>
    </tr>
    <tr>
        <td>Idaline</td>
        <td>19710427</td>
        <td>50</td>
        <td>F</td>
        <td>24100</td>
        <td>11900</td>
        <td>36000</td>
    </tr>
    <tr>
        <td>Freddie</td>
        <td>19621227</td>
        <td>58</td>
        <td>F</td>
        <td>26600</td>
        <td>12600</td>
        <td>39200</td>
    </tr>
    <tr>
        <td>Debee</td>
        <td>19701119</td>
        <td>49</td>
        <td>F</td>
        <td>32400</td>
        <td>97000</td>
        <td><i>42100</i></td>
    </tr>
    <tr>
        <td>Joyann</td>
        <td>19570124</td>
        <td><i>41</i></td>
        <td>T</td>
        <td>24400</td>
        <td>11500</td>
        <td>35900</td>
    </tr>
    <tr>
        <td>Ajay</td>
        <td>19600512</td>
        <td><i>50</i></td>
        <td>F</td>
        <td>25500</td>
        <td>18800</td>
        <td>44300</td>
    </tr>
    <tr>
        <td>Emelia</td>
        <td>19571123</td>
        <td><i>57</i></td>
        <td>T</td>
        <td>34000</td>
        <td>17500</td>
        <td><i>0</i></td>
    </tr>
            
</table>
"""

html_df = pd.read_html(html_table, header=0)[0]
# Before we attempt this, we'll rename the rows to something that's easier to work with
html_df.columns = ["name", "dob", "age", "deceased", "ug_loan", "pg_loan", "total_loan"]
## Convert 'dob' into a date object
html_df['dob'] = pd.to_datetime(html_df['dob'], format='%Y%m%d')
html_df['dob'] = html_df['dob'].dt.year
# Creates a new column 'now_date' populated with the now datetime
html_df["now_date"] = pd.Timestamp(datetime.now()).year
## Calculate the difference between the 'dob' and 'now_date' and return the value as years
now_date_dob_difference = (html_df['now_date'] - html_df['dob'])
# This line changes the the timedelta objects to a floating point year, which we then convert to an in
# Convert the total seconds to years
#now_date_dob_difference = now_date_dob_difference / (365.25 * 24 * 60 * 60)



print(html_df['dob'])
print("hello world")