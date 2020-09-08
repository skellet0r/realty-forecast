# Exit Report of Project Realty Forecasting for Customer XYZ Realty LLC

Customer: XYZ Realty LLC

Team Members:

- Edward Amor

## Overview

Given a the historical median price of zip codes across the United States, we were tasked with identifying the 5 best zip codes to invest in
for our client. The term 'best' was left open ended, we took it to mean minimizing risk while also maximizing profit. We therefore forecasted the
value of zip codes 1 year into the future seeking to identify which ones would satisfy our goals. The further ahead we project the more our models degrade,
1 year was an arbitrary point into the future.

## Business Domain

Our client is a Real Estate Business and as such they focus on buying and selling properties. The goal of our client is to make profitable investments both in
the short term and the long term. Since our client is seeking to expend their reach into territories they've yet to purchase in, we opted to forecast with
a short term time horizon.

## Business Problem

<Business problem and exact use case(s), why it matters\>
The business problem our client is facing is, the market they are in is saturated with competition, seeking to expand their portfolio in other regions
they are looking to identify profitable investments in markets outside of their foothold. The client has a sizeable portion of capital available to invest
in other markets, but wants to be in a market with relatively lower risk, yet still maintain a high return on investment.

## Data Processing

Our data was collected from the Zillow Research Page, and came in wide form. We melted our data, and for modeling only used
the time series values, not any extraneous features such as State or Metro.

## Modeling, Validation

For modeling we performed a grid search through hyperparameters for each time series, our goal was to minimize the AIC on our training data,
we then performed out of sample walk forward validation to get an insight into our RMSE for each of our final models. We used training sets of
80% of our total data,

Our results for each of the 61 models can be inspected in our 4th notebook, but of the top 5 models we chose, our RMSE scores for all were below ~\$60k.

## Learnings

### Data science / Engineering

Time series modeling is a whole beast of its own, and this was just univariate time series forecasting. It is akin to regression in the sense that
we are predicting a continuous value (in this case we could also do classification). AR and MA are interesting components, you can determine p (AR) using
the pacf, and the MA using the acf.

Modeling for multiple time series could be a hassle, so utilizing libraries devoted to easing that pain such as pdarima definitely help.
Walk Forward validation is basically the best (kind of like K fold CV for a regression problem).

The further you project into the future the more your model's predictive ability degrades.

### What's unique about this project, specific challenges

<Specific issues or setup, unique things, specific challenges that had to be addressed during the engagement and how that was accomplished\>
The project is unique in that we were given an open ended question and given free reign to determine what it meant. We were tasked with
identifying the 5 best zip codes and as such their is a subjective nature to the term 'best'. Best is different depending on the circumstances, and the
financial situation of the client asking.

## Links

[Github Repo](https://github.com/Skellet0r/realty-forecast)

## Next Steps

Next steps include consistently updating the models, as data comes in it is imperative to update the models to get insight into where the market may be moving.
