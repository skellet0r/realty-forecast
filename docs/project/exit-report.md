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

|     | ZipCode |     RMSE | Historic Median Value | Proj. Min (12m) | Proj. Max (12m) | Proj. Min Net Profit | Proj. Max Net Profit |
| --: | ------: | -------: | --------------------: | --------------: | --------------: | -------------------: | -------------------: |
|   1 |   80203 | 15,517.8 |             \$571,500 |       \$632,029 |       \$707,771 |           \$60,529.4 |            \$136,271 |
|   2 |   80218 | 28,192.7 |             \$773,400 |       \$868,125 |       \$961,875 |           \$94,725.4 |            \$188,475 |
|   3 |   80211 | 29,628.8 |             \$546,600 |       \$592,347 |       \$644,853 |           \$45,746.9 |           \$98,253.1 |
|   4 |   80220 | 31,763.1 |             \$561,100 |       \$609,286 |       \$664,114 |           \$48,186.1 |            \$103,014 |
|   5 |   80212 | 49,685.4 |             \$510,000 |       \$571,192 |       \$628,808 |           \$61,192.4 |            \$118,808 |

Our top 5 zip codes also had very good predictive accuracy as shown in tests, and with an RMSE score below our projected min profits, 
with a 95% confidence level, we can forecast that the future prices will be within the range predicted.

## Learnings

### Data science / Engineering

Time series modeling is a whole beast of its own, and this was just univariate time series forecasting. It is akin to regression in the sense that
we are predicting a continuous value (in this case we could also do classification). AR and MA are interesting components, you can determine p (AR) using
the pacf, and the MA using the acf.

Modeling for multiple time series could be a hassle, so utilizing libraries devoted to easing that pain such as pdarima definitely help.
Walk Forward validation is basically the best (kind of like K fold CV for a regression problem).

The further you project into the future the more your model's predictive ability degrades.

### What's unique about this project, specific challenges

The project is unique in that we were given an open ended question and given free reign to determine what it meant. We were tasked with
identifying the 5 best zip codes and as such their is a subjective nature to the term 'best'. Best is different depending on the circumstances, and the
financial situation of the client asking.

## Links

[Github Repo](https://github.com/Skellet0r/realty-forecast)

## Next Steps

Next steps include consistently updating the models, as data comes in it is imperative to update the models to get insight into where the market may be moving.
