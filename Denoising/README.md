### Documentation:
<br>
<br>
This is a demonstration of various signal processing techniques used to denoise electrical signals. Two major methods have been used:
<br>
<br>
- <u><b>Savitzky Golay Filter</b></u>: It mainly finds its use in "smoothening" digital data by implementing polynomial spline fitting. It deduces a Vandermonde Matrix from convolution coefficents to convolve with the original signal to reduce noise.
<br>
<br>
- <u><b>Empirical Mode Decomposition</b></u>: It uses the Hilbert-Huang Transform to reduce noise from electric signals. It calculates the upper and lower envelopes of any input signal and reduces noise in an iterative manner to keep reducing error until some threshold value. (I have implemented recursion here to hasten the process)
<br>
<br>
I have observed that this hasn't been used much in seismological signal processing, hence I made in-built functions from scratch to reduce noise.
<br>
<br>

### Explaining the code:
<br>
<br>

The `savgol()` function takes in 2 inputs:
<br>
- `data` : the amplitudes of the imput signal is given here.
- `m`    : the number of convolution coefficients the user wants- this will affect the shape of the Vandermonde Matrix.
<br>
<br>

The `hht_denoise()` function takes in 3 inputs:
<br>
- `data`      : the amplitudes of the input signal is given here.
- `t`         : the corresponding time data for the signal (in s) is given here.
- `threshold` : the threshold value for the recursion to work to reduce noise
<br>
<br>

The `envelope()` function takes in 3 inputs:
<br>
- `x`    : the amplitudes of the input signal is given here.
- `t`    : the corresponding time data as a numpy array is given here.
- `kind` : takes "upper" and "lower" to classify upper and lower envelope and calculate it as per user.
<br>
<br>

For more info, check the docstring of the functions and `Example.ipynb`
