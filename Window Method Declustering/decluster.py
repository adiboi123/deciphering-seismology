import numpy as np
import pandas as pd
import datetime

def loc_win(m: float):
    """Calculates the location window of a earthquake based on the magnitude as per Gardner & Knopoff's exponential relation
    
    Parameters:
    ----------
    m : magnitude value
    
    Returns:
    -------
    loc_win : (in km) radius of aftershock effect of input earthquake
    """
    return np.exp(-1.024+(0.804)*m)
def time_win(m: float):
    """Calculates the time window for an aftershock to occur for an input earthquake of given magnitude
    
    Parameters:
    ----------
    m : magnitude value of earthquake
    
    Returns:
    -------
    time_win : (in s (datetime object)) maximum time period within which afterschock will occur
    """
    return datetime.timedelta(np.exp(-2.87+(1.235)*m))
def distance(i_point: int,i_main: int,df: pd.DataFrame):
    """Calculates the distance between 2 earthquake locations from a given catalogue
    
    Parameters:
    ----------
    i_point : index of earthquake in catalogue which is being checked as aftershock
    i_main  : index of earthquake in catalogue which is being assumed as mainshock event
    df      : (dataframe object) earthquake catalogue
    
    Returns:
    -------
    distance : (in km) distance between the 2 earthquake locations
    """
    return 111*np.sqrt((df["lat"].to_numpy()[i_main]-df["lat"].to_numpy()[i_point])**2+(df["lon"].to_numpy()[i_main]-df["lon"].to_numpy()[i_point])**2)
def time_func(i_point: int,i_main: int,df: pd.DataFrame):
    """Calculates the time difference in between two earthquakes in catalogue
    
    Paramaters:
    ----------
    i_point : index of earthquake in catalogue which is being checked as aftershock 
    i_main  : index of earthquake in catalogue which is being assumed as mainshock event
    df      : (dataframe object) earthquake catalogue
    
    Returns:
    -------
    time : (in s (datetime object)) time difference between 2 earthquakes
    """
    return datetime.datetime.strptime(df["Date"][i_point]+df["Time"][i_point],"%d-%m-%Y%H:%M:%S")-datetime.datetime.strptime(df["Date"][i_main]+df["Time"][i_main],"%d-%m-%Y%H:%M:%S")

def window_declustering(df: pd.DataFrame):
    """Uses the window method of declustering to differentiate between mainshocks and aftershocks
    ***IMP: dataframe object must contain 'Mw' to denote magnitude of earthquake, 'Date' and 'Time' in separate columns, and Latitude ('lat'), Longitude ('long') in degrees.***
    
    Paramater(s):
    ------------
    df : input catalogue of earthquakes in dataframe format
    
    Returns:
    -------
    df : output catalogue with all necessary information, and a 'Remarks' section containing the nomenclature, as aftershock (A-Mn) or
         Mainshock (Mn)
    """
    main=[]
    after={}
    dist=[]
    time=[]
    for i in range(len(df)):
        if i==0:
            main.append(i)
            dist.append(loc_win(df["Mw"].to_numpy()[i]))
            time.append(time_win(df["Mw"].to_numpy()[i]))
        else:
            if df["Mw"].to_numpy()[i]>np.max(np.array(main)):
                main.append(i)
                dist.append(loc_win(df["Mw"].to_numpy()[i]))
                time.append(time_win(df["Mw"].to_numpy()[i]))
            else:
                dist_vals=[]
                time_vals=[]
                for j in range(len(main)):
                    dist_vals.append(distance(i,np.array(main)[j],df))
                    time_vals.append(time_func(i,np.array(main)[j],df))
                criterion=((np.array(dist_vals)<=np.array(dist)).astype(int)*(np.array(time_vals)<=np.array(time)).astype(int))*df["Mw"].to_numpy()[main]
                if np.sum(criterion)==0:
                    main.append(i)
                    dist.append(loc_win(df["Mw"].to_numpy()[i]))
                    time.append(time_win(df["Mw"].to_numpy()[i]))
                else:
                    x=np.argmax(criterion)
                    after.update({i:"A-M"+str(x+1)})
    main_data={np.array(main)[i]:"M"+str(i+1) for i in range(len(main))}
    main_data.update(after)
    indices=list(main_data.keys())
    indices.sort()
    sorted_events={i:main_data[i] for i in indices}
    df.insert(len(df.columns),"Remarks",list(sorted_events.values()),True)
    return df
