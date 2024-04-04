---
title: "Week 6 Assignment"
author: "Ruben Brionez Jr"
date: "January 21, 2024"
output: pdf()
---

library(datasets)
library(dplyr)
library(ggplot2)
data("iris")

df <- iris
head(df)
df %>% mean(Sepal.Length) 
str(df)
df %>% group_by(Species) %>% summarize(mean(Sepal.Length,na.rm=TRUE)) 

ggplot(df, aes(x=Petal.Length)) + 
  geom_histogram(bins=30, fill="Blue", color="black") +
  ggtitle("Count of Petal Lengths for All Species") +
  theme_minimal()

ggplot(df, aes(x=Petal.Width)) + 
  geom_histogram(bins=25, fill="Blue", color="black") +
  ggtitle("Count of Petal Width for All Species") +
  theme_minimal() 

ggplot(df, aes(x=Sepal.Length)) + 
  geom_histogram(bins=30, fill="Cyan", color="black") +
  ggtitle("Count of Sepal Length for All Species") +
  theme_minimal() 

ggplot(df, aes(x=Sepal.Width)) + 
  geom_histogram(bins=20, fill="Cyan", color="black") +
  ggtitle("Count of Sepal Width for All Species") +
  theme_minimal() 
  

ggplot(data=df, mapping=aes(x=Species, y=Petal.Width, fill="blue"))+
  geom_boxplot() + stat_summary(fun = "mean", geom = "point", 
               shape = 8,size = 2, color = "blue")


