# A Series Of Correlated Events - Part 2
### Analyzing Real World Economics Time Series With Autoregressive Models

<br>

<p align="left">
  <img src="https://raw.githubusercontent.com/tommyzakhoo/autoregressive/master/panic.jpg", width="300">
  <br>
  <i> A crowd forms outside a Wall Street bank during the Panic of 1907. Photo from <a href="https://digitalcollections.nypl.org/items/510d47dd-5b2c-a3d9-e040-e00a18064a99">New York Public Library</a>. </i>
</p>

## Status
Work in progress. Last update: 3 September 2018

### Table of contents

- [Tools, Techniques and Concepts](#tools-techniques-and-concepts)
- [Motivation And Project Description](#motivation-and-project-description)
- [Virtual Currency Dataset](#virtual-currency-dataset)
- [Cleaning and Wrangling the Data](#cleaning-and-wrangling-the-data)
- [Construction Price Dataset](#construction-price-dataset)

## Tools, Techniques and Concepts

Python, Matplotlib, Statsmodel, Time Series Analysis, Autoregressive Model

## Motivation And Project Description

In part 1, I gave an introduction to time series analysis, and fitting an autoregressive model to data, using the Box-Jenkins method. Here, I am going to collect two real world economics-related time series data, and apply these techniques to them.

## Virtual Currency Dataset

The market for virtual goods is a challenging but exciting frontier for modern economics. For me, one of the most interesting intersection between virtual goods and economics happened when the online game "Eve Online" hired an economist, Dr Eyjolfur Gudmundsson, as their chief economist and head of analytics.

So of course, I went out and collected time series data on the price of the game's virtual currency, "PLEX". This currency is sold by the game company for real world money and is used for various profit generating in-game microtransactions. 

Note that the "price" here is the price of this virtual currency in terms of a resource (ISK) that is found within the game. This resource can only be obtained by playing the game and cannot be bought with real world money. The price of PLEX in terms of real world dollars has interestingly been kept constant by the company for the last 15 years!

The data consists of the number of orders in the market, quantity of PLEX sold, lowest buy price, highest sell price, and daily average price. There are 5010 data points, ranging from 1 April 2016 to 13 July 2018. The full set of data can be found here: [full_PLEX_data.xlsx](full_PLEX_data.xlsx)

## Cleaning and Wrangling the Data

I extracted the price column into a .csv file and flipped it so that time t = 1 is 1 April 2016. A simple plot of the time series 

## Construction Price Dataset


