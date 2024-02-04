# Assignment: Week 5 Assignment
# Name: Ruben Brionez Jr
# Date: 01/14/2024
library(dplyr)
library(purrr)
library(tibble)
library(xml2)
library(stringr)
library(readxl)

# Read the excel file and save to a variable 
housing_df <- read_xlsx(path = "week-6-housing.xlsx")
# Review the data frame and types
str(housing_df)
# Renaming 'Sale Price' to remove quotes
colnames(housing_df)[colnames(housing_df) == 'Sale Price'] <- 'sale_price'
# Verifying name change
str(housing_df)
# Using SELECT square_feet_total_living column
housing_df %>% select(square_feet_total_living)
# Using SUMMARIZE to find the average sale price
housing_df %>% summarize(AvgPrice=mean(sale_price))
# Using FILTER and then SELECT to specify results
housing_df %>% filter(square_feet_total_living >= 2000) %>% select(
  sale_price, addr_full, square_feet_total_living)
# Chaining Pipes to refine results 
housing_df %>% select(sale_price, addr_full, 
  ctyname, square_feet_total_living) %>% filter(square_feet_total_living < 1500)
# Using MUTATE to find price per sq ft
housing_df %>% select(sale_price, square_feet_total_living) %>%
  mutate(price_sq_ft=sale_price/square_feet_total_living)
# Creating a new variable for cbind() 
price_sqft <- housing_df$sale_price/housing_df$square_feet_total_living
price_sqft <- round(price_sqft, 2)
new_df <- cbind(housing_df,price_sqft)
# Using GROUP_BY to group by bedrooms and SUMMARIZE to find 
# the mean price by bedroom and then ARRANGE by AvgPrice
housing_df %>% group_by(bedrooms) %>% summarize(AvgPrice=mean(sale_price)) %>%
  arrange(desc(AvgPrice))
# Using KEEP()
even_sales <- keep(housing_df$sale_price, function(x) x %% 2 == 0)
# Using DISCARD()
odd_built_years <- discard(housing_df$year_built, function(x) x %% 2 == 0)
# Using MAP_INT
housing_df %>% map_int(NROW)
housing_df %>% map_int(NCOL)
# SPLIT, CONCATENATE strings
addr_dir <- str_split(string = housing_df$addr_full, pattern = " ")
combined <- paste(addr_dir, sep = " ")

