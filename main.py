### INF601 - Advanced Programming in Python
### Samuel Heinrich
### Mini Project 2

# Imports
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Check if charts folder exists, if not then create it
charts = Path('charts')
if not charts.exists():
    Path(r'charts').mkdir()

# Store the data from data.csv into a dataframe
df = pd.read_csv("./data/data.csv", index_col=0)

# Create a mapping of column names to column labels
columnUnits = {
    "tempo": "Tempo in BPM",
    "beats": "Number of Detected Beats",
    "chroma_stft": "Chroma Short-Time Fourier Transform",
    "rmse": "Root Mean Square Energy (dB)",
    "spectral_centroid": "Spectral Centroid (Hz)",
    "spectral_bandwidth": "Spectral Bandwidth (Hz)",
    "rolloff": "Spectral Rolloff Frequency (Hz)",
    "zero_crossing_rate": "Zero Crossing Rate (Fraction of Samples)",
    "mfcc1": "MFCC 1",
    "mfcc2": "MFCC 2",
    "mfcc3": "MFCC 3",
    "mfcc4": "MFCC 4",
    "mfcc5": "MFCC 5",
    "mfcc6": "MFCC 6",
    "mfcc7": "MFCC 7",
    "mfcc8": "MFCC 8",
    "mfcc9": "MFCC 9",
    "mfcc10": "MFCC 10",
    "mfcc11": "MFCC 11",
    "mfcc12": "MFCC 12",
    "mfcc13": "MFCC 13",
    "mfcc14": "MFCC 14",
    "mfcc15": "MFCC 15",
    "mfcc16": "MFCC 16",
    "mfcc17": "MFCC 17",
    "mfcc18": "MFCC 18",
    "mfcc19": "MFCC 19",
    "mfcc20": "MFCC 20",
}

# Get filtered lists of the columns
columns = df.columns.tolist()                                               # Get a list of all columns
mfccColumns = df.filter(regex="^mfcc").columns.tolist()                     # Filter the list into mfcc columns
trackColumns = [c for c in df.columns if c not in mfccColumns + ["label"]]  # Filter the list into not mfcc columns and not "label"

# Separate rows by genre
genres = df["label"].unique().tolist()                  # Get a list of unique values for 'label' (a list of genres)
genreDirectory = {}                                     # Initialize a dictionary of rows separated by genre
for genre in genres:                                    # For each genre
    genreDirectory[genre] = df[df["label"] == genre]    # Put the rows for that genre into that genre's entry in the dictionary

# Make a bar chart for each column, each of which shows the average value for each genre
for column in trackColumns:                                     # For each column that needs a bar chart
    averages = {}                                               # Initialize a dictionary that will contain the average of the current column for each genre
    for genre in genreDirectory:                                # For each genre
        averages[genre] = genreDirectory[genre][column].mean()  # Get the average value for the current column for the current genre
    plt.bar(                                                    # Make a bar chart
        averages.keys(),                                        # x-coordinates are genre names
        averages.values(),                                      # Heights are the average values
        color='m',                                              # Set bar color
        edgecolor='k',                                          # Set bar edge color
        linewidth=2                                             # Set bar edge width
    )
    plt.xlabel('Genres')                                        # Set the x-axis label
    plt.xticks(rotation=30)                                     # Set the labels to rotate slightly so they don't run into each other
    plt.ylabel(columnUnits.get(column, column))                 # Set the y-axis label
    plt.title(f'Average {column} Per Genre')                    # Set the chart title
    plt.savefig(f'charts/{column}.jpg')                         # Save the charts into the charts directory
    plt.show()                                                  # Display the charts