# A Series Of Correlated Events - Part 2
### Analyzing Real World Economics Time Series With Autoregressive Models

<br>

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/panic.jpg", width="300">
  <br>
  <i> A crowd forms outside a Wall Street bank during the Panic of 1907. Photo from <a href="https://digitalcollections.nypl.org/items/510d47dd-5b2c-a3d9-e040-e00a18064a99">New York Public Library</a>. </i>
</p>

## Status
Work in progress. Last update: 18 August 2018.

### Table of contents

- [Tools and Techniques](#tools-and-techniques)
- [Motivation And Project Description](#motivation-and-project-description)
- [Introduction to Time Series Analysis](#introduction-to-time-series-analysis)
- [Virtual Currency Dataset](#virtual-currency-dataset)
- [Construction Price Dataset](#construction-price-dataset)

## Tools and Techniques

Python, Matplotlib, Statsmodel, Time Series Analysis, Autoregressive Model

## Motivation And Project Description

I was briefly exposed to time series analysis during an undergraduate econometrics class. I recently took a data science challenge that requires fitting an autoregressive model, which piqued my interest in the topic once again.

In this project, I will be applying the so-called "Box–Jenkins method" to two real world datasets. Before that, I will briefly decribe the method with an artificial toy dataset.

For a more in-depth and mathematical introduction, I highly recommend "<i> Time Series Analysis: Forecasting and Control, 5th Edition </i>" by George E. P. Box and Gwilym M. Jenkins et al. Alternatively, Wikipedia has a nice summary of the method with references. [(link to Wikipedia article)](https://en.wikipedia.org/wiki/Box%E2%80%93Jenkins_method)

## Introduction to Time Series Analysis

In this section, I will generate a set of data from a simple toy autoregressive model, defined by the equation shown below. The Python code to do this is simple and can be found here: [generate_data.py](generate_data.py).

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/example_ar3.gif">
</p>

In this model, time t is discrete. The variable X at time t are positively related to its value at time t-1, t-2 and t-3 (these are known as lagged variables), plus an error term epsilon that is drawn from a standard normal distribution. The first three values of X at time t = 1,2,3 are initialized to zero. 

The toy data consists of values for 30,000 time steps, the first 200 time steps is illustrated below using the [Matplotlib package](https://matplotlib.org/). Due to the positive relationship to previous values, a positive (negative) value of X tend to be followed by a positive (negative) one, until a big enough error comes by the break the trend. This give rise to the interesting "cyclic" pattern in the figure.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/fig1.png", height="300">
</p>

An important assumption of our analysis is [stationarity](https://en.wikipedia.org/wiki/Stationary_process), which means that the mean and the variance of X does not depend on time t. That is, the mean and variance remains constant over time. Stationarity is strong assumption that is often not met by real data. However, as we will see later, there are ways to transform data into a stationary one. 

As for our toy model, a mathematical result tells us that we can check for stationarity by writing down an associated polynomial equation, and checking that all of its (possibly complex) roots are outside the unit circle. Again, I will skip the details, but Wikipedia has a nice  [summary with references](https://en.wikipedia.org/wiki/Autoregressive_model#Definition). If you do this for our toy model, you will see that all of its roots are indeed outside the unit circle.

The next step in the Box-Jenkins method is to select a model by looking at the autocorrelation and partial autocorrelation functions. I did this using the [statsmodel package](https://www.statsmodels.org/stable/index.html) and the output, along with 99% confidence regions in blue, are shown below. The Python code is very simple and can be found here: [plot_data.py](plot_data.py). In this case, I already know what the underlying model is, but it is still interesting to see how the behavior of these functions agree with mathematical predictions.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/fig2.png", height="300">
</p>

The autocorrelation plot shows the correlation between X and lagged/past values of itself. Mathematical results says that this should decrease exponentially for an autoregressive model, which fits what we see in the figure.

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/fig3.png", height="300">
</p>

The partial autocorrelation plot also shows the correlation between X and lagged values of itself, <b>after</b> removing the effects of correlations with all earlier lagged values. That is, the correlation between X and a lagged value of itself that is not accounted for by earlier lags. Mathematical resuls says that for an autoregressive model, this plot would be zero from some point onwards. This is what we see in the figure: only the first four terms are significantly different from zero at a 99% level of confidence, which matches up exactly with how we specified our model.

Finally, I use statsmodel again to fit an autoregressive model to the data. Code for this can be found here: [fit_data.py](fit_data.py)

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/coeffs.png", height="300">
</p>

The list above shows the fitted cofficients for the first 10 lagged terms. The first three are almost equal to the 0.40, 0.20 and 0.10 in the toy model that the data was generated from. Due to the randomness in the data, 

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/pvalues.png", height="300">
</p>

Above shows the p-values for each of the fitted coefficients, which have the [Student's t-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution). The first three are p-values are tiny and statistically significant

While this was a straightforward exercise, it is nice to see how everything works under ideal conditions, and that our code actually works!

## Virtual Currency Dataset

The market for virtual goods is a challenging but exciting frontier for modern economics. For me, oe of the most interesting intersection between virtual goods and economics happened when the online game "Eve Online" hired an economist, Dr Eyjolfur Gudmundsson, as their chief economist and head of analytics.

So of course, I went out and collected time series data on the price of the game's virtual currency, "PLEX". This currency is sold by the game company for real world money and is used for various profit generating in-game microtransactions. Note that the "price" here is the price of this virtual currency in terms of a resource (ISK) that is found within the game. This resource can only be obtained by playing the game and cannot be bought with real world money.

The data consists of the number of orders in the market, quantity of PLEX sold, lowest buy price, highest sell price, and daily average price. There are 5010 data points, ranging from 1 April 2016 to 13 July 2018. The full set of data can be found here: [full_PLEX_data.xlsx](full_PLEX_data.xlsx)

I extracted the price column into a .csv file and flipped it so that time t = 1 is 1 April 2016. A quick look at the plot

## Construction Price Dataset


