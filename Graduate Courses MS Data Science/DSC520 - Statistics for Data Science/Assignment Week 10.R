# Week 10 Assignment

library(dplyr)
library(ggplot2)

df <- read.csv('week-10-data.csv')

head(df)

df <- df %>% rename('DGN'=Column1, 'PRE4'=Column2, 'PRE5'=Column3, 
                    'PRE6'=Column4, 
              'PRE7'=Column5, 'PRE8'=Column6, 'PRE9'=Column7, 'PRE10'=Column8, 
              'PRE11'=Column9, 'PRE14'=Column10, 'PRE17'=Column11, 
              'PRE19'=Column12, 'PRE25'=Column13, 'PRE30'=Column14, 
              'PRE32'=Column15, 'Age'=Column16, 'Risk1Yr'=Column17)

# Checking for NA values
sum(is.na(df))

# Removing NA Values
dataset <- df[complete.cases(df), ]

head(df)

risk_model <- glm(Risk1Yr ~ PRE4 + PRE5 + PRE6 + PRE7 + PRE8 + PRE9 +
                   PRE10 + PRE11 + PRE14 + PRE17 + PRE19 + PRE25 + PRE30 + PRE32 
                  + Age, data = df, family = binomial)

summary(risk_model)
# The closer to zero the p-value is the more statistical significance

# The summary provides an easy to see significance code for variables

# In this model, the variable PRE9, which is described 
# as "Dyspnoea before surgery" is the most statistically significant variable

# Following the variable PRE9, PRE14 which is described as "T in clinical 
# TNM - size of the original tumour, from OC11 (smallest) to OC14 (largest)" 

# The variable PRE30 and PRE17 are the next most significant variables, PRE30 
# being described as "Smoking" the variable PRE17 being described as 
# Type 2 DM - diabetes mellitus


# Running data through the model
risk_predict <- predict(risk_model, type = 'response')

# Reviewing 
head(risk_predict)

# Validate the model - Confusion Matrix
confmatrix <- table(Actual_Value=dataset$Risk1Yr, 
                    Predicted_Value=risk_predict >0.5)

# Checking Accuracy
(confmatrix[[1,1]] + confmatrix[[2,2]]) / sum(confmatrix)

# Part 2 of Assignment

#Load data
binary_df <- read.csv("binary-classifier-data.csv")

head(binary_df)

# Creating the model
binary_model <- glm(label ~ x + y, data = binary_df, family = "binomial")

# Summary of model
summary(binary_model)

# Run Data through the model
binary_predict <- predict(binary_model, binary_df, type = 'response')

# Validate the model - Confusion Matrix
confmatrix <- table(Actual_Value=binary_df$label, 
                    Predicted_Value=binary_predict >0.5)
head(confmatrix)

# Accuracy
(confmatrix[[1,1]] + confmatrix[[2,2]]) / sum(confmatrix)
