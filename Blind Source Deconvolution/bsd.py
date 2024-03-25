import numpy as np
import matplotlib.pyplot as plt
def blind_source_decon(x: np.ndarray,t: np.ndarray, epsilon: float=1.0,max_iter: int=200, plot: bool=False):
    """Calculates blind-source deconvolution of input time signal to give the optimum wavelet as per Neidel's wavelet model
    
    Parameters:
    ----------
    x        : amplitude values of time-domain signal
    t        : time value of input signal
    epsilon  : parameter used in Wiener filter construction
    max_iter : maximum number of iterations used
    plot     : takes 'True' or 'False' values. If 'True', it plots Cost Function v/s alpha values, else it returns the optimum 
               wavelet amplitude in an array
    """
    amp=abs(np.fft.rfft(x))[:int(x.size/2)]
    freq=np.fft.rfftfreq(x.size,int(len(t)/np.max(t)))[:int(x.size/2)]
    omega=2*np.pi*freq
    omega[0]=0.000001
    omega_p=2*np.pi*freq[np.argmax(amp)]
    alpha_vals,J=[],[]
    for i in range(1,max_iter):
        alpha=0.1*i
        alpha_vals.append(alpha)
        beta=alpha*(1+np.cos(omega_p))/(1-np.cos(omega_p))
        W=((1+np.exp(omega*1j))**beta)*((1-np.exp(omega*1j))**alpha)
        A=np.conj(W)/((abs(W)**2)+(epsilon**2))
        Y=A*(np.fft.rfft(x)[:int(x.size/2)])
        J.append(np.cov(abs(Y),cumulative_distribution_func(Y))[0][1])
    if plot==True:
        plt.plot(alpha_vals,J)
        plt.xlabel(r'$\alpha$ values')
        plt.ylabel(r'$J$ (Cost function)')
        plt.grid()
    else:
        alpha_optimum=alpha_vals[np.argmin(J)]
        beta_optimum=alpha_optimum*(1+np.cos(omega_p))/(1-np.cos(omega_p))
        W_optimum=((1+np.exp(omega*1j))**beta_optimum)*((1-np.exp(omega*1j))**alpha_optimum)
        optimum_wavelet=np.fft.irfft(W_optimum)
        return optimum_wavelet
def cumulative_distribution_func(y: np.ndarray):
    """Calculates the cumulative distribution function by using an indicator function
    
    Parameter(s):
    ------------
    y : input 1-D array containing the data
    
    Returns:
    -------
    f : output array containg the c.d.f. of the input data
    """
    f=np.zeros(len(y))
    for i in range(len(y)):
        f[i]=(1/len(y))*np.count_nonzero(y<=y[i])
    return f