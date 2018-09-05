
import numpy as np

from matplotlib import pyplot as plt # tools for plotting figures
plt.rcParams.update({'font.size': 22}) # set font size for plots

import pandas as pd
from pandas import Series # time series data structure

# package for augemented dickey fuller test
from statsmodels.tsa.stattools import adfuller

plex = pd.read_csv('cleaned_PLEX_data.csv',header=None) # load the data
plex = plex.squeeze() # convert dataframe to a pandas series


''' Uncomment for histograms without transformations

plex_top = plex[0:400] # first half of time series
plex_bottom = plex[400:828] # second half of time series

plex_top.hist(alpha=0.4) # plot the histograms
plex_bottom.hist(alpha=0.4)

plt.title('Histogram of PLEX time series')
plt.legend(['first half','second half'])
plt.show()

'''

plex = plex.apply(np.log) # take log to stabilize variance

plex_diff = plex.diff() # get the consecutive differences
plex_diff = plex_diff[1:] # remove the first NaN entry

plex_top = plex_diff[0:400] # first half of time series
plex_bottom = plex_diff[400:827] # second half of time series

plex_top.hist(alpha=0.4) # plot the histograms
plex_bottom.hist(alpha=0.4)

plt.title('Histogram of log-differenced time series')
plt.legend(['first half','second half'])
plt.show()

adfuller(plex_diff) # perform Augmented Dickey-Fuller test
