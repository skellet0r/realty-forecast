# Project Charter

## Business background

- Who is the client, what business domain the client is in.
  - Our client for this project is XYZ Realty, LLC. They're primarily
    a real estate company based in the west coast. They make profits
    by "flipping" houses, that is buying a house at a low value and
    selling at a higher value.
- What business problems are we trying to address?
  - XYZ Realty, LLC, is seeking to expand their portfolio, and are
    looking for areas in the United States with the best opportunity for
    them to make a profit. They have asked a pretty open ended question,
    what are the 5 best zip codes?

## Scope
- What data science solutions are we trying to build?
  - We plan to develop a set of forecasting models.
- What will we do?
  - We will develop a catalogue of forecasting models for the zip codes
    provided to us.
- How is it going to be consumed by the customer?
  - Our customer will have a report delivered to them, recommending the
    best zip codes to invest in, balancing both risk and profit.

## Metrics
- What are the qualitative objectives? (e.g. reduce user churn)
  - Develop models with low forecasting errors
- What is a quantifiable metric  (e.g. reduce the fraction of users with 4-week inactivity)
  - Our quantifiable metric is RMSE (model errors), and AIC (model complexity)
- Quantify what improvement in the values of the metrics are useful for the customer scenario (e.g. reduce the  fraction of users with 4-week inactivity by 20%) 
  - Reduce our baseline RMSE and AIC scores by 25%.
- What is the baseline (current) value of the metric? (e.g. current fraction of users with 4-week inactivity = 60%)
  - Current baseline value of the metric is +Infinity. This is a new project.
- How will we measure the metric? (e.g. A/B test on a specified subset for a specified period; or comparison of performance after implementation to baseline)
  - We'll measure the metric by doing walk-forward validation (RMSE), and by getting the AIC of our model.

## Plan
- Phases (milestones), timeline, short description of what we'll do in each phase.
  - Processing
  - EDA
  - Baseline Modeling
  - ARIMA
  - SARIMA

## Architecture
- Data
  - What data do we expect? Raw data in the customer data sources (e.g. on-prem files, SQL, on-prem Hadoop etc.)
    - We expect to receive flat files with the median market value of houses by zipcode over time.
- What tools and data storage/analytics resources will be used in the solution e.g.,
  - Python for feature construction, aggregation, and modeling.

