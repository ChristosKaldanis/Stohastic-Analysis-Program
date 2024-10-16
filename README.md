# Stohastic-Analysis-Program


# Project Description
The Stohastic-Analysis-Program project involves the stochastic analysis of two Markov time series with positive and negative coefficients, as well as their inverses, using the Numpy, Matplotlib, and Statsmodels.api libraries.

# Methodology
First, after defining our coefficients, we set the number of samples (values) to be used. Next, we create noise with a standard deviation of 10. We generate our time series for α1 = 0.2 and β1 = -0.8, and correspondingly for α2 = -0.8 and β2 = 0.2. We compute the autocorrelation for 10 different lags (nlags = 10) at different time periods to see how each point is affected by its predecessor. Then, we calculate both the theoretical and empirical variance to assess if the coefficients we have chosen are suitable for analysis. For the coefficients to be suitable, the theoretical variance result should be as close as possible to the empirical variance result. Additionally, we calculate the mean for both time series. Finally, we visualize the autocorrelation for both cases, as well as the distribution of the values of the two time series.

# Implementation
This project was implemented by Christos Kaldanis, an undergraduate student at the Department of Informatics, Ionian University.

