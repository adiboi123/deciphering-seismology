### Documentation:
<br>
<br>

This is a demonstration of blind source deconvolution of any seismic signal. Due to non-availability of actual seismic data, `Example.ipynb` uses random-generated signal. This project has been inspired by (*Wang et.al., 2018*):<br>
https://academic.oup.com/jge/article/15/1/286/5112897
<br>

The objective of this project is to create a function from scratch that will take seismic data as input and try to estimate the input using an algorithm proposed by *Wang et.al.,2018*. The program uses a cost function which uses the *Gini correlation* between the a frequency transform of the seismic signal and its cumulative distribution function. The multi-objective function `blind_source_decon()` calculates the optimum wavelet, as well as plotting the aforementioned cost function with the $\alpha$ values- which is used to deduce the optimum wavelet. The code uses mainly *`Numpy`* to calculate fast fourier transforms to convert time-domain data to frequency-domain.
<br>
<br>

### Explaining the code:
<br>
<br>

The `blind_source_decon()` function takes in 5 inputs:
<br>
- `x`       : the amplitudes of the imput signal is given here.
- `t`       : the corresponding time data for the signal (in s) is given here.
- `epsilon` : a Wiener filter construction parameter, default set to 1.0
- `max_iter`: maximum number of iterations needed for the cost function generation, default set to 200
- `plot`    : takes *bool* values of `True` and `False` from user to create plots, default set to `False`
<br>
<br>

The `cumulative_distribution_func()` function takes in 1 input(s):
<br>
- `y`      : the data values are given here, the function computes the cumulative distribution function using an indicator function
<br>
<br>

For more info, check the docstring of the functions and `Example.ipynb`
