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
trackColumns = [c for c in df.columns if c not in mfccColumns + ["label"]] # Filter the list into not mfcc columns and not "label"

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
    # Now make the chart.
    plt.bar(averages.keys(), averages.values())
    plt.xlabel('Genres')
    plt.xticks(rotation=30)
    plt.ylabel(columnUnits.get(column, column))
    plt.title(f'Average {column} Per Genre')
    plt.savefig(f'charts/{column}.jpg')
    plt.show()

# plt.savefig(str(charts / 'gender_count.jpg'))
# plt.show()


# (10 / 10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build
# some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10 / 10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the
# project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10 / 10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10 / 10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt file
# which contains all the packages that need installed. You can create this file with the output of pip freeze at the terminal prompt.
# (20 / 20 points) There should be a README.md file in your project that explains what your project is, how to install the
# pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.


# tempo: BPM of the track (higher = faster, lower = slower)
# beats: rhythmic regularity, usually tracked by looking for periodic rhythmic swells or accents in the waveform, then counting the number of them throughout the track.
# chroma_stft (Chroma Short-Time Fourier Transform): measures how energy is distributed across the 12 semitone pitch classes (captures harmonic content, useful for chord recognition and tonality)
# rmse (Root Mean Square Energy): measures the loudness/energy of the signal over time (higher = louder/denser sound, lower = quieter/sparser)
# spectral_centroid: the center of mass of the spectrum - often perceived as the brightness of the sound (high = bright/sharp, low = dark/mellow).
# spectral_bandwidth: the spread of the spectrum around the centroid (high = wide/noisy/full spectrum, low = narrow/pure tone or focused sound).
# rolloff: The frequency below which a certain %, usually 85%, of spectral energy lies (high = more high frequency content).
# zero_crossing_rate: how often the waveform crosses the zero line (high = noisy/percussive/distorted/higher frequency, low = smoother tones/lower frequencies).
# mfcc1-mfcc20: A set of 20 coefficients that summarize the timbre of the sound. Comes from mapping the spectrum onto the mel scale. Lower order MFCCs (mfcc1-mfcc3) capture broad spectral shape (like brightness/energy). Higher order MFCCs (mfcc10-20) capture finer details of the timbre (like texture, resonances).
