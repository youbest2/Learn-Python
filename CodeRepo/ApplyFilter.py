import pandas as pd
import os
import webbrowser

# Define the ranges
ranges = [
    {"start": 15634, "end": 15645},
    {"start": 15687, "end": 15842},
    {"start": 15884, "end": 15895},
    {"start": 15937, "end": 16091},
    {"start": 16133, "end": 16144},
    {"start": 16186, "end": 16339},
    {"start": 16670, "end": 16762},
    {"start": 28668, "end": 28702},
    {"start": 28744, "end": 28941},
    {"start": 28983, "end": 29078},
    {"start": 29120, "end": 29483}
]

# Load the data
df = pd.read_excel("new_misra_report.xlsx")

# Check if 'E' is a valid column in the DataFrame
if 'Line' in df.columns:
    # Apply the filter
    filtered_df = df[df['Line'].apply(lambda x: any([x >= r["start"] and x <= r["end"] for r in ranges]))]

    # Save the filtered data to a new Excel file
    filtered_df.to_excel("filtered_new_misra_report.xlsx", index=False)

    # Open the newly created file in the default application
    webbrowser.open("filtered_new_misra_report.xlsx")
else:
    print(f"'E' is not a column in the DataFrame. The columns in the DataFrame are: {df.columns.tolist()}")
