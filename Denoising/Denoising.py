import numpy as np
import scipy
def savgol(data: np.ndarray,m: int):
    """Savitsky-Golay filter used to denoise any discrete time series data
    
    Parameters:
    ----------
    data : input amplitude of discrete time-series data
    m    : odd-number; signifies the number of convolution coefficients used
    
    Returns:
    -------
    y : Denoised data
    """
    n=len(data)
    z=np.arange(int((1-m)/2),int((m+1)/2),1)
    # convolution coefficients:
    J=np.zeros((m,m-1))
    for i in range(m):
        for j in range(m-1):
            J[i][j]=z[i]**j
    C=np.matmul(np.linalg.inv(np.matmul(J.T,J)),J.T)
    mask=np.zeros(n);mask[n-m:]=1
    y=np.zeros(n)
    for i in range(n-m):
        y[i]=np.sum(np.matmul(C,data[i:i+m]))
    y=(1-mask)*y+mask*data
    return y

def envelope(x: np.ndarray,t: np.ndarray,kind: str):
    """Creates the envelope of any function (upper as well as lower as per user input) using cubic spline interpolation
    
    Parameters:
    ----------
    x    : input amplitude values of any time-series signal
    t    : input time values for corresponding data values
    kind : takes 'upper' and 'lower' to give the upper and lower envelopes
    
    Returns:
    -------
    y : gives the envelope as per user inputs
    """
    if kind=='upper':
        pos=x[x>0]
        pos_index=np.squeeze(np.array(np.where(x>0)).T)
        interp=scipy.interpolate.CubicSpline(t[pos_index],pos)
        return interp(t)
    elif kind=='lower':
        neg=x[x<0]
        neg_index=np.squeeze(np.array(np.where(x<0)).T)
        interp=scipy.interpolate.CubicSpline(t[neg_index],neg)
        return interp(t)
    
def hht_denoise(x: np.ndarray,t: np.ndarray,threshold: float =0.01):
    """Calculates the Hilbert-Huang Transform for any input function to denoise any signal
    
    Parameters:
    ----------
    x         : input amplitudes of time series data
    t         : corresponding time values of the time-series data
    threshold : threshold of s.d. acceptable for denoising
    
    Returns:
    -------
    x_ : returns the denoised signal
    """
    ue=envelope(x,t,'upper')
    le=envelope(x,t,'lower')
    x_=x-((ue+le)/2)
    sd=np.sqrt(np.sum((x-x_)**2/x**2))
    if (sd>threshold):
        return hht_denoise(x_,t,threshold)
    else:
        return x_
    
def rem_edge_effects(x: np.ndarray, y: np.ndarray):
    """Removes the edge effects caused by cubic spline interpolation caused due to imperfect maxima-minima calculation during envelope creation
    
    Parameters:
    ----------
    x : denoised signal data
    y : original signal data
    
    Returns:
    -------
    x_ : removes edge effects from the denoised signal
    """
    mask=(np.logical_or(x>np.max(y),x<np.min(y))).astype(np.int64)
    return (1-mask)*(x)+mask*(y)