library(ggplot2)

df <- read.csv("scores.csv") # Save the .csv file as a variable once read
head(df) # Calling head on the data frame to see a section of the contents
# 1. What are the observational units in this study?
# The observational units of the study are "Scores" and "Counts"
colnames(df) # Calling colnames to see the variables 
# 2. Identify the variables mentioned in the narrative paragraph and determine 
# which are categorical and quantitative?
# Variables include "Count", "Score", and "Section"
# "Count" is quantitative, "Score" is quantitative, "Section" is categorical
# 3. Create one variable to hold a subset of your data set that contains only 
# the Regular Section and one variable for the Sports Section.
regular <- subset(df, Section == "Regular") # Creates a subset of data from the 
# original data frame that only includes the "Regular" section scores and counts
sports <- subset(df, Section == "Sports") # Creates a subset of data from the 
# original data frame that only includes the "Sports" section of scores and 
# counts
# 4. Use the Plot function to plot each Sections scores and the number of 
# students achieving that score.
regular_plot <- ggplot(data=regular) + # Plotting regular data frame
  geom_point(mapping=aes(Score,Count)) + 
  ggtitle("Scores for Regular Section")
regular_plot
sports_plot <- ggplot(data=sports) + # Plotting sports data frame
  geom_point(mapping=aes(Score,Count)) +
  ggtitle("Scores for Sports Section")
sports_plot
combined_plot <- ggplot() + # Combining the data frames to plot
  geom_point(data=regular, aes(Score, Count),
             fill = "green", color = "black",
             size = 2, shape =21) +
  geom_point(data=sports, aes(Score,Count),
             fill = "red", color = "black",
             size = 2, shape = 21) +
  geom_vline(xintercept = regular_mean, color = "green") + # Adds a vertical 
  # mean line for the regular scores
  geom_vline(xintercept = sports_mean, color = "red") + # Adds a vertical mean
  # line for the sports scores
  labs(x="Number of Students Scoring", y="Scores") +
  ggtitle("Combined Plots")
combined_plot
regular_mean <- mean(regular$Score) # Calculates the mean of the "Regular"
# section scores
sports_mean <- mean(sports$Score) # Calculates the mean of the "Sports" 
# section scores
# 4a. Comparing and contrasting the point distributions between the two section, 
# looking at both tendency and consistency: Can you say that one section tended 
# to score more points than the other?
# Based on the plots, it appears that the "Sports" section has scored more 
# points overall. This can be observed by the number of red dots over the mean 
# line versus green dots over the mean line for the regular section.
# 4b. Did every student in one section score more points than every student in 
# the other section? If not, explain what a statistical tendency means in 
# this context.
# No, every student in one section did not score more than every student in the 
# other section. There would be a clear divide and separation between the colors
# of the dots in the combined plot. Statistical tendency in this context refers
# to mean of the scores for each section. With the "sports" section there tends
# to be more scores above the mean.
# 4c. What could be one additional variable that was not mentioned in the 
# narrative that could be influencing the point distributions between the 
# two sections?
# Another variable that was not mentioned, that could be influencing the point 
# distribution, is the exact examples used in the "Regular" section. By dividing 
# the sections further a better analysis and data points can be gained. 

