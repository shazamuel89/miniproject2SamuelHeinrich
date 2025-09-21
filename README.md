### INF601 - Advanced Programming in Python
### Samuel Heinrich
### Mini Project 2

# Miniproject 2: Attributes of the Sounds of Genres
 
## Description



This program gets data from a .csv file which contains a number of rows of tracks and a 'label' column which designates
the track's genre. There are other columns for various attributes of the sound, which are listed below (if you want to
include more or different columns in your data, you can simply add them and the program will account for them):

* **tempo**: BPM of the track (higher = faster, lower = slower)
* **beats**: Measures number of detected beats, usually tracked by looking for periodic rhythmic swells or accents in
             the waveform, then counting the number of them throughout the track.
* **chroma_stft**: Chroma Short-Time Fourier Transform measures how energy is distributed across the 12 semitone pitch
                   classes (captures harmonic content, useful for chord recognition and tonality)
* **rmse**: Root Mean Square Energy measures the loudness/energy of the signal over time (higher = louder/denser sound,
            lower = quieter/sparser)
* **spectral_centroid**: Measures the center of mass of the spectrum - often perceived as the brightness of the sound
                         (high = bright/sharp, low = dark/mellow).
* **spectral_bandwidth**: Measures the spread of the spectrum around the centroid (high = wide/noisy/full spectrum,
                          low = narrow/pure tone or focused sound).
* **rolloff**: Measures the frequency below which a certain %, usually 85%, of spectral energy lies (high = more high
               frequency content).
* **zero_crossing_rate**: Measures how often the waveform crosses the zero line (high = noisy/percussive/distorted/higher
                          frequency, low = smoother tones/lower frequencies).
* **mfcc1-mfcc20**: A set of 20 coefficients (each a separate column) that summarize the timbre of the sound. Comes from
                    mapping the spectrum onto the mel scale. Lower order MFCCs (mfcc1-mfcc3) capture broad spectral shape
                    (like brightness/energy). Higher order MFCCs (mfcc10-20) capture finer details of the timbre (like
                    texture, resonances).

After loading the data, the program makes bar charts for each column listed above (or others if you change the data to
include them), excluding the mfcc# columns. Each bar chart takes the average of that column's value for each genre. The
idea is to compare the differences in various auditory qualities for different genres.

At some point in the future, I would like to add a scatterplot creation for the 20 mfcc# columns to get a good visual
representation of the differences in timbre for each genre.

## Getting Started
 
### Dependencies

This program was designed with this dataset in mind:
[Kaggle: Music features](https://www.kaggle.com/datasets/insiyeah/musicfeatures?resource=download)
Put the .csv from this dataset or a similar dataset into a directory titled 'data' in the project directory, and make sure
the .csv file is titled 'data.csv'.

Please install the pip requirements by running the following in a terminal:
```
pip install -r requirements.txt
```
 
### Installing

To download the program, run the following in a terminal in the directory you would like to contain the program:
```
git clone https://github.com/shazamuel89/miniproject2SamuelHeinrich.git
```

### Executing program

To run the program, run the following command in a terminal in the program's directory:
```
python main.py
```
 
## Author

Samuel Heinrich
 
## Version History

* 0.1
    * Initial Release
 
## Acknowledgments

* [Pandas Documentation](https://pandas.pydata.org/docs/)
* [Matplotlib Documentation](https://matplotlib.org/stable/index.html)
* [Kaggle: Music features](https://www.kaggle.com/datasets/insiyeah/musicfeatures?resource=download)