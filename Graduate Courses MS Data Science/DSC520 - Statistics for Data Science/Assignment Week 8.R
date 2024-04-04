# Assignment Week 8 Version 2
library(readxl)
library(dplyr)
library(ggplot2)
library(coefplot)
library(Metrics)
housing_df <- read_xlsx('week-6-housing.xlsx')

# Reviewing the structure of the Data Frame
str(housing_df)

# Renaming 'Sale Price" and "Sale Date" to match the other "Sale Columns"
colnames(housing_df)[colnames(housing_df) == 'Sale Price'] <- 'sale_price'
colnames(housing_df)[colnames(housing_df) == 'Sale Date'] <- 'sale_date'

#Verify name changes are correct
str(housing_df)

#Checking values for sq_ft_lot with a histogram
ggplot(housing_df, aes(x=sq_ft_lot)) + geom_histogram(binwidth = 10) + 
  labs(x="Lot Square Footage")

#Checking values for sale_price with a histogram
ggplot(housing_df, aes(x=sale_price)) + geom_histogram(binwidth = 10) + 
  labs(x="Sale Price")

# Filtering results based on the histogram counts of values
housing <- housing_df %>% filter(sale_price <= 1200000, sq_ft_lot <= 30000)

#Explanation of Transformations

# Reviewing Data with a Scatter Plot
ggplot(housing, aes(x=sq_ft_lot, y=sale_price)) + geom_point() + 
  labs(x="Lot Square Footage", y="Sale Price")

# Plotting with the log of sq_ft_lot
ggplot(housing, aes(x=log(sq_ft_lot), y=sale_price)) + 
         geom_point() + labs(x="Lot Square Footage", y="Sale Price")

# Create a linear regression model where “sq_ft_lot” predicts "Sale Price".
#ggplot(housing, aes(x=log(sq_ft_lot), y=sale_price)) + geom_point() +
  #geom_smooth(method = "lm") + labs(x="Lot Square Footage", y="Sale Price")

# Create a linear regression model where “sq_ft_lot” predicts "Sale Price".
# Get a summary of your first model and explain your results
sale_price_1 <- lm(sale_price ~ sq_ft_lot, data = housing)
summary(sale_price_1) 

# My Understanding of the Summary:

# Get the residuals of your model (you can use ‘resid’ or ‘residuals’ functions)
# and plot them. 
res <- resid(sale_price_1) 
plot(fitted(sale_price_1), res)

# What does the plot tell you about your predictions?

# Use a qq plot to observe your residuals. 
# Do your residuals meet the normality assumption?
qqnorm(res)
qqline(res)
# The residuals appear to a show a light or medium tailed distribution
# This is not a normal distribution

# Now, create a linear regression model that uses multiple predictor 
# variables to predict Sale Price (feel free to derive new predictors from 
# existing ones). Explain why you think each of these variables may add 
# explanatory value to the model.

ggplot(housing_df, aes(x=square_feet_total_living)) + 
  geom_histogram(binwidth = 1) + labs(x="Living SqFt")

ggplot(housing_df, aes(x=bath_full_count)) + geom_histogram(binwidth = 1) + 
  labs(x="Number of Full Baths")

ggplot(housing, aes(x=square_feet_total_living, y=sale_price)) + geom_point() + 
  labs(x="Living SqFt", y="Sale Price")

ggplot(housing, aes(x=bedrooms, y=sale_price)) + geom_point() + 
  labs(x="Number of Bedrooms", y="Sale Price")

# Creating a multiple regression model
sale_price_2 <- lm(sale_price ~ sq_ft_lot + square_feet_total_living + bedrooms,
                   data = housing)

# Getting Summary of Model
summary(sale_price_2)
# Reviewing the coefficients from the summary
coef(sale_price_2)
# Plotting the coefficients to visualize the numbers (for myself)
coefplot(sale_price_2)

# 8. Get the residuals of your second model and plot them
# What the does the plot tell you about your predictions?
res_multi <- resid(sale_price_2) 
plot(fitted(sale_price_2), res_multi)

# 9. Use a qq plot to observe your residuals Do your residuals meet the 
# the normality assumption? 
qqnorm(res_multi)
qqline(res_multi)

anova(sale_price_1)
anova(sale_price_2)

3.69^14 > 1.75^14

preds <- predict(sale_price_1, housing)
num1 <- rmse(housing$sale_price, preds)

preds2 <- predict(sale_price_2, housing)
num2 <- rmse(housing$sale_price, preds2)

num3 <- num1-num2
num3
