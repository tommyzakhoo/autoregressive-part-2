# A Series Of Correlated Events - Part 2
### Analyzing Virtual Currency Time Series Data With Autoregressive Models

<br>

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/panic.jpg", width="300">
  <br>
  <i> A crowd forms outside a Wall Street bank during the Panic of 1907. Photo from <a href="https://digitalcollections.nypl.org/items/510d47dd-5b2c-a3d9-e040-e00a18064a99">New York Public Library</a>. </i>
</p>

## Status
Completed on 5 September 2018.

### Table of contents

- [Tools, Techniques and Concepts](#tools-techniques-and-concepts)
- [Motivation And Project Description](#motivation-and-project-description)
- [Virtual Currency Dataset](#virtual-currency-dataset)
- [Cleaning and Wrangling the Data](#cleaning-and-wrangling-the-data)
- [Stationarity, Differencing and the Augmented Dickey-Fuller Test](#stationarity-differencing-and-the-augmented-dickey-fuller-test)
- [Autocorrelation and Partial Autocorrelation Functions](#autocorrelation-and-partial-autocorrelation-functions)
- [Forecasting](#forecasting)
- [Evaluating the Accuracy of Forecasts](#evaluating-the-accuracy-of-forecasts)

## Tools, Techniques and Concepts

Python, Matplotlib, Statsmodel, Time Series Analysis, Autoregressive Model, Stationarity, Variance-Stabilizing Transformations, Augmented Dickey-Fuller Test, Autocorrelation, Partial Autocorrelation, Correlation Coefficient, Root Mean Square Errorr

## Motivation And Project Description

In part 1, I gave an introduction to time series analysis, and fitting an autoregressive model to data, using the Box-Jenkins method. Here, I am going to collect two real world economics-related time series data, and apply these techniques to them.

## Virtual Currency Dataset

The market for virtual goods is a challenging but exciting frontier for modern economics. For me, one of the most interesting intersection between virtual goods and economics happened when the online game "Eve Online" hired an economist, Dr Eyjolfur Gudmundsson, as their chief economist and head of analytics.

So of course, I went out and collected time series data on the price of the game's virtual currency, "PLEX". This currency is sold by the game company for real world money and is used for various profit generating in-game microtransactions. 

Note that the "price" here is the price of this virtual currency in terms of a resource (ISK) that is found within the game. This resource can only be obtained by playing the game and cannot be bought with real world money. The price of PLEX in terms of real world dollars has interestingly been kept constant by the company for the last 15 years!

The data consists of the number of orders in the market, quantity of PLEX sold, lowest buy price, highest sell price, and daily average price. There are 5010 data points, ranging from 1 April 2016 to 13 July 2018. The full set of data can be found here: [full_PLEX_data.xlsx](full_PLEX_data.xlsx)

## Cleaning and Wrangling the Data

I extracted the price column into a .csv file and flipped it so that time t = 1 is 1 April 2016.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/plex1.png", width="600">
</p>

A simple plot of the price time series shows severe outliers in the data that are probably erroneous.

```Python
plex = data.iloc[:,0].values
plex.argsort()
```
After reading the csv file into a dataframe "data", I turned it into a numpy array, and used argsort() to get a list of indices that would sort the array. Using this list, I was able to look at the values in order, starting from the largest, until I reach a value that makes sense.

| Index | Value    |
| :-:   | :-:      |
| 405   | 10083786 |
| 482   | 5788621  |
| 420   | 5028172  |
| 403   | 4671374  |
| 622   | 3256621  |
| 623   | 3255644  |
| 621   | 3248608  |

So the erroneous values appear to be in indices 405, 482, 420, 403. After dropping these, the plot look like this.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/plex2.png", width="600">
</p>

There seems to be two more outliers at indices 247 and 388, which I chose to remove.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/plex3.png", width="600">
</p>

The time series looks to be error free now. The cleaned data can be found here: [cleaned_PLEX_data.csv](cleaned_PLEX_data.csv)

## Stationarity, Differencing and the Augmented Dickey-Fuller Test

As mentioned in part 1, [stationarity](https://en.wikipedia.org/wiki/Stationary_process) is an important assumption of the autoregressive model. I am going to use the [Augmented Dickey-Fuller test](https://en.wikipedia.org/wiki/Augmented_Dickey%E2%80%93Fuller_test) and visual inspection to check for stationarity.

A time series is stationary if the joint cumulative probability distribution for any number of values consecutive in time does not depend on time: [see this definition](https://en.wikipedia.org/wiki/Stationary_process#Definition). I did a rough visual inspection of this, by splitting the time series into two and plotting the histogram.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/hist1.png", width="600">
</p>

It is pretty clear that the distribution changed over time. One possible remedy for non-stationarity is [differencing](https://en.wikipedia.org/wiki/Stationary_process#Differencing), where the time series of differences between consecutive values is used instead.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/hist2.png", width="600">
</p>

Much better! However, the histogram for the second half looks like it might have a higher variance. A way to fix this is to use a [variance-stabilizing transformation](https://en.wikipedia.org/wiki/Variance-stabilizing_transformation) such the natural logarithm, before I take the difference.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/hist3.png", width="600">
</p>

The two histograms now looks roughly smiliar. A math joke goes: "The similarities between these two are close enough. close enough in terms of what distance? Eyeball distance." 

More evidence for stationarity is given by the Augmented Dickey-Fuller test, which can be found in the statsmodels package. The results of the test on the log-differenced time series is shown below.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/adfuller.png">
</p>

The second number "1.3239e-29" is the p-value, which is miniscule, and would lead to me rejecting the null hypothesis of non-stationarity at even 0.1% level of significance. The first number "-16.7552" is the test statistic, while the percentages and numbers in braces { } are the critical values of the test statistic for various significance level.

The code for all of these stationarity checks can be found here: [stationarity_check.py](stationarity_check.py). The log-differenced time series data can be found here: [plex_diff.csv](plex_diff.csv)

## Autocorrelation and Partial Autocorrelation Functions

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/plex_acf.png", width="600">
</p>

The autocorrelation function looks like a funnel: starts out wide, and then taper off. This is normal behavior for a stationarity autoregressive time series, and so is good news for us. The blue region is the 99% confidence region.

The negative "spike" for the first time lag suggests incorporating a [moving-average term](https://en.wikipedia.org/wiki/Moving-average_model) into my autoregressive model.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/plex_pacf.png", width="600">
</p>

The partial autocorrelation has negative spikes among the first five lagged terms, while the rest looks like they might not be statistical significant. Again, the 99% confidence region is colored blue.

This suggests that the average daily price of the virtual currency is negatively related to some of its average daily values in the last 5 days.

## Fitting the Autoregressive Model

```Python
import pandas as pd
from pandas import Series
from statsmodels.tsa.ar_model import AR

df = pd.read_csv('plex_diff.csv',header=None) # load the data from .cvs file
plex = df.squeeze() # convert dataframe to pandas series

model = AR(plex) # input series into AR class
model_fit = model.fit() # fit the AR model
```

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/plex_fit.png">
</p>

I chose to use a stringnent p-value cut off of 0.01, which leaves only the 1st, 2nd and 15th lagged terms as statistically significant.

## Forecasting

My fitted autoregressive model is given by the equation below. The expected value is given because the mean of the error term is assumed to be zero. This assumption looks reasonable based on visual inspection of previously drawn histograms.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/model.gif">
</p>

Given data on the time series, I can use my model to try and forecast what the expected value will be 1 day ahead, using the above equation. Forecasted values can then be used recursively for the expected values that are 2,3,4, or more days ahead. Of course, the errors get propagated forward, and so the n day's forecast gets worse for larger n.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/forecast.png">
</p>

## Evaluating the Accuracy of Forecasts

Using the numpy function numpy.corrcoef(A,B), I obtained the Pearson correlation coefficient between my forecast and the actual log-differences, which is 0.3969. Not ideal, but there is at least some correlation.

Another way I evaluated the accuracy is to check the errors, which is equal to the actual values minus predicted ones. It is a good idea to plot them out and see how severe the assumptions of stationarity and normality has been violated. There doesn't seem to be major problems within the plot of my residual errors below.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive-part-2/master/errors.png">
</p>

The root mean square error is a popular measure of accuracy.

1386356.933

## Summary and Final Thoughts

In part 1 of this project, I gave a basic introduction to time series analysis and autoregressive models. Here, I applied those techniques to a set of real world time series data. The following is a list of what I have done for this part of the project.

- Collected, cleaned and wrangled a set of time series data for a virtual currency.
- Check for stationarity with visual inspection of histograms and the augmented Dickey-Fuller test.
- Remedy the non-stationarity with a variance stabilizing transformation and differencing.
- Analyze the autocorrelation and partial autocorrelation functions.
- Fitted an autoregressive model to the data, filter out coefficients with low p-values.
- Generated 1-day ahead forecasts and checked the residual errors for possible problems.
- Evaluated the forecast accuracy with the Pearson correlation coefficiewnt and root mean square error.
- Despite rudimentary methods and a challenging low sign high noise data set, was able to obtain a 0.3969 correlation between the actual log-differenced time series and the 1 day ahead forecast.

This is a basic attempt at building a model that generates 1 day ahead forecasts for this time series. There are a lot more that can be done to improve the accuracy or our model. 

In particular, I have not tried to de-noise the data, and the autocorrelation function suggests incorporating a moving-average model. These will be further explored, when I return to write a part 3 to this project.







