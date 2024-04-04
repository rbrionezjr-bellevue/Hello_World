# Final Project R Script

# Loading Libraries Needed
library(dplyr)
library(ggplot2)
library(coefplot)
library(lubridate)

# Loading Original Data
background_df <- read.csv("nics-firearm-background-checks.csv")
population_df <- read.csv("acs2017_census_tract_data.csv")
deaths_df <- read.csv("gun_deaths_us_1999_2019.csv")


# Reviewing data from Florida FBI Background checks
flBackChecks <- background_df %>% group_by(state) %>% 
  filter(state == "Florida", grepl('2017', month))

# Filter by all years
all_flBackChecks <- background_df %>% group_by(state) %>% 
  filter(state == "Florida")

# Reviewing data for Florida from Population Data Frame and 
# saving to new data frame
flPop <- population_df %>% group_by(State) %>% filter(State == "Florida")

#Reviewing data from deaths_df and saving to a new data frame
flDeaths <- deaths_df %>% group_by(State_Name) %>% 
  filter(State_Name == "Florida")

head(flDeaths)
head(flPop)
head(flBackChecks)

flBackChecks

all_flBackChecks

all_flBackChecks$month <- substr(all_flBackChecks$month, 1,4)

all_flBackChecks$month <- format(as.Date(all_flBackChecks$month, format="%Y"),"%Y")

all_flBackChecks$month <- as.numeric(all_flBackChecks$month)

tail(all_flBackChecks)

# This provides the sum of all firearms per month
totalFirearms <- flBackChecks$handgun + flBackChecks$long_gun + 
  flBackChecks$other + flBackChecks$multiple

# Converting back to a matrix
totalFirearms <- matrix(totalFirearms, ncol = 12)
colnames(totalFirearms) <- c("December", "November", "October", "September",
                             "August", "July", "June", "May", "April", "March", 
                             "February", "January")
totalFirearms
# Provides total of all firearm sales for 2017
sum(totalFirearms)

ggplot(flBackChecks, aes(x=month, y=handgun)) + geom_point() + 
  labs(title="Handgun Sales by Month",x="Month", y="Handgun") +
  theme(axis.text = element_text(angle=30, hjust =1))

bgchecks <- lm(totals ~ month, data = all_flBackChecks)
summary(bgchecks) 
bgchecks

ggplot(all_flBackChecks, aes(x=month, y=totals)) + 
  geom_jitter(width = 0.5, height = 0.5) + 
  geom_smooth(method = "lm") +
  labs(title="Total Background Checks by Year in FL",x="Years", 
       y="Number of Background Checks") +
  theme(axis.text = element_text(angle=45, hjust =1))

tail(flDeaths)

ggplot(flDeaths, aes(x=Year, y=Deaths)) + 
  geom_jitter(width = 0.5, height = 0.5) +
  geom_smooth(method = "lm") +
  labs(title="Total Gun Deaths by Year in FL", x="Year", 
       y="Number of Gun Deaths") +
  theme(axis.text = element_text(angle=45, hjust =1))

deathsModel <- lm(Deaths ~ Year, data = flDeaths)
summary(deathsModel) 
deathsModel
