#Functions I use to make the plots and also preprocess the data
import numpy as np
import pandas as pd
from scipy.stats import multivariate_normal
from scipy.stats import poisson
from scipy.interpolate import interp1d
from tqdm import tqdm
from scipy import stats
from scipy.ndimage import gaussian_filter1d
from scipy import ndimage
from math import remainder, tau
import math


#Functions to get grid coordinates
def get_v(df,predicted=True):
    
    if predicted:
        v0 = np.arctan2(df['v0_sin_smooth'],df['v0_cos_smooth'])  
        v1 = np.arctan2(df['v1_sin_smooth'],df['v1_cos_smooth'])
    else: 
        v0 = np.arctan2(df['lv0_sin_smooth'],df['lv0_cos_smooth'])
        v1 = np.arctan2(df['lv1_sin_smooth'],df['lv1_cos_smooth'])
    
    return v0, v1


def get_double_v(df,predicted=True):
    
    if predicted:
        v0 = list(np.arctan2(df['v0_sin_smooth'],df['v0_cos_smooth']))
        v1 = list(np.arctan2(df['v1_sin_smooth'],df['v1_cos_smooth']))
    else: 
        v0 = list(np.arctan2(df['lv0_sin_smooth'],df['lv0_cos_smooth']))
        v1 = list(np.arctan2(df['lv1_sin_smooth'],df['lv1_cos_smooth']))
    
    return [v+2*np.pi for v in v0]+[v+2*np.pi for v in v0]+v0+v0,\
           [v+2*np.pi for v in v1]+v1+[v+2*np.pi for v in v1]+v1

    
remainder_fn = lambda x: math.remainder(x, tau)
    
def get_lever_v(df,predicted=True):
    
    if predicted:
        v0 = np.arctan2(df['v0_sin_smooth'],df['v0_cos_smooth']) + df['vectorToLever_v0']
        v1 = np.arctan2(df['v1_sin_smooth'],df['v1_cos_smooth']) + df['vectorToLever_v1']
    else: 
        v0 = np.arctan2(df['lv0_sin_smooth'],df['lv0_cos_smooth']) + df['vectorToLever_v0']
        v1 = np.arctan2(df['lv1_sin_smooth'],df['lv1_cos_smooth']) + df['vectorToLever_v1']
    
    v0 = np.array(list(map(remainder_fn, v0)))
    v1 = np.array(list(map(remainder_fn, v1)))
    
    return v0, v1

def get_double_lever_v(df,predicted=True):
    
    if predicted:
        v0 = list(np.arctan2(df['v0_sin_smooth'],df['v0_cos_smooth']) + df['vectorToLever_v0'])
        v1 = list(np.arctan2(df['v1_sin_smooth'],df['v1_cos_smooth']) + df['vectorToLever_v1'])
    else: 
        v0 = list(np.arctan2(df['lv0_sin_smooth'],df['lv0_cos_smooth']) + df['vectorToLever_v0'])
        v1 = list(np.arctan2(df['lv1_sin_smooth'],df['lv1_cos_smooth']) + df['vectorToLever_v1'])
        
    v0 = list(map(remainder_fn, v0))
    v1 = list(map(remainder_fn, v1))
    
    return [v+2*np.pi for v in v0]+[v+2*np.pi for v in v0]+v0+v0,\
           [v+2*np.pi for v in v1]+v1+[v+2*np.pi for v in v1]+v1

#Plotting Function
def plot_heatmap(ax,va,vb,x_label,y_label,title):
    
    smoothing =2
    heatmap, xedges, yedges = np.histogram2d(va,vb,bins=40)
    heatmap = ndimage.gaussian_filter(heatmap,sigma=smoothing,mode="wrap")
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    ax.imshow(heatmap.T,origin="lower",extent=[-np.pi,np.pi,-np.pi,np.pi])
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.grid(False)
    ax.set_title(f'{title}')
    

    ax.set_xticks(ticks=[-np.pi, 0, np.pi])
    ax.set_xticklabels([r'-$\pi$', "0", "$\pi$"])
    ax.set_yticks(ticks=[-np.pi, 0, np.pi])
    ax.set_yticklabels([r'-$\pi$', "0", "$\pi$"])
    
