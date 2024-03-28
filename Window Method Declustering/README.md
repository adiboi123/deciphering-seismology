### Window Declustering Algorithm
<br>
<br>

### Documentation:
<br>

This is a demonstration of window-method declustering of any seismic catalogue. `Window_Method.ipynb` uses a synthetic catalogue: `Synthetic_Catalogue.csv` to demonstrate the window method algorithm (*Gardner & Knopoff, 1972*):<br>
<u>**Citation**</u>:
<br>
Knopoff, L., and J. Gardner (1972), Higher Seismic Activity During Local Night on the Raw Worldwide Earthquake
Catalogue, Geophys. J. R. astr. Soc., 28, 311–313. 9, 10, 11
<br>

The objective of this project is to create a declustering function from scratch that will take seismic catalogue dataframe as input and separate it into *Mainshocks* and *Aftershocks* as per time and distance windows. Though the original paper discusses about depth-windows too, this has not been implemented in the code. The function `window_declustering()` creates a dataframe from the input dataframe containing the catalogue, containg a "Remarks" column to classify the Mainshocks and Aftershocks.
<br>
<br>
Check out the documentation and use-cases of the functions in the `Window_Method.ipynb` file.
