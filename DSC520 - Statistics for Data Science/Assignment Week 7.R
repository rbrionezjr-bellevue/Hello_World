# Assignment Week 7
library(ggplot2)

#Reading csv and saving to a variable
student_survey <- read.csv("student-survey.csv.crdownload")
student_survey

# Scatter plot of TimeReading VS TimeTV
ggplot(student_survey, aes(x = TimeReading, y = TimeTV)) +
  geom_point() + ggtitle(" TimeReading Vs TimeTV")

# Scatter plot of TimeReading VS Happiness
ggplot(student_survey, aes(x = TimeReading, y = Happiness)) +
  geom_point() + ggtitle("TimeReading Vs Happiness")

#Scatter plot of TimeTV VS Happiness
ggplot(student_survey, aes(x = TimeTV, y = Happiness)) +
  geom_point() + ggtitle(" TimeTV Vs Happiness")


