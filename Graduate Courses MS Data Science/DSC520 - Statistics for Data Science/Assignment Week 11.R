# Week 11 Assignment

# Part 1 

library(dplyr)
library(ggplot2)
library(class)
library(e1071) 
library(caTools) 
library(proxy)


binary_df <- read.csv("binary-classifier-data.csv")
trinary_df <- read.csv("trinary-classifier-data.csv")

# Plot the data from each data set using a scatter plot.
# Plotting the binary data frame
ggplot(binary_df, aes(x=x, y=y)) + geom_point()

# Plotting the trinary data frame
ggplot(trinary_df, aes(x=x, y=y)) + geom_point()

# Checking for NA values
sum(is.na(binary_df))

# Splitting data into train and test data sets
split <- sample.split(binary_df, SplitRatio = 0.7) 
train_cl <- subset(binary_df, split == "TRUE") 
test_cl <- subset(binary_df, split == "FALSE")

# Feature Scaling
train_scale <- scale(train_cl[, 2:3]) 
test_scale <- scale(test_cl[, 2:3])

# Running head function on both test and train to review data frames
head(test_scale)
head(train_scale)

# Running KNN model on data sets at k = 3
classifier_knn3 <- knn(train = train_scale, test = test_scale, 
                      cl = train_cl$label, k = 3) 

# Printing classifier_knn3
classifier_knn3

# Confusion Matrix 
cm <- table(test_cl$label, classifier_knn3) 
cm 

# Data preparation

# Creating a vector of k-values
k_values <- c(3, 5, 10, 15, 20, 25)

# Calculate accuracy for each k value
accuracy_values <- sapply(k_values, function(k) {
  classifier_knn <- knn(train = train_scale, 
                        test = test_scale, 
                        cl = train_cl$label, 
                        k = k)
  1 - mean(classifier_knn != test_cl$label)
})

# Create a data frame for plotting
accuracy_data <- data.frame(K = k_values, Accuracy = accuracy_values)

accuracy_data

# Plotting
ggplot(accuracy_data, aes(x = K, y = Accuracy)) +
  geom_line(color = "lightblue", size = 1) +
  geom_point(color = "lightgreen", size = 3) +
  labs(title = "Model Accuracy for Different K Values",
       x = "Number of Neighbors (K)",
       y = "Accuracy")

# Trinary Data KNN 

# Checking for NA values
sum(is.na(trinary_df))

# Splitting trinary data into train and test data sets
trinary_split <- sample.split(trinary_df, SplitRatio = 0.7) 
trinary_train_cl <- subset(trinary_df, split == "TRUE") 
trinary_test_cl <- subset(trinary_df, split == "FALSE")

# Feature Scaling
trinary_train_scale <- scale(trinary_train_cl[, 2:3]) 
trinary_test_scale <- scale(trinary_test_cl[, 2:3])

# Running head function on both test and train to review data frames
head(trinary_test_scale)
head(trinary_train_scale)

# Running the KNN model and calculating accuracies
trinary_accuracy_values <- sapply(k_values, function(k) {
  trinary_classifier_knn <- knn(train = trinary_train_scale, 
                        test = trinary_test_scale, 
                        cl = trinary_train_cl$label, 
                        k = k)
  1 - mean(trinary_classifier_knn != test_cl$label)
})

# Create a data frame for plotting
trinary_accuracy_data <- data.frame(K = k_values, 
                                    Accuracy = trinary_accuracy_values)

trinary_accuracy_data

# Plotting
ggplot(trinary_accuracy_data, aes(x = K, y = Accuracy)) +
  geom_line(color = "lightblue", size = 1) +
  geom_point(color = "lightgreen", size = 3) +
  labs(title = "Model Accuracy for Different K Values",
       x = "Number of Neighbors (K)",
       y = "Accuracy")

# K Means Cluster

# Part 2

library(cluster)
library(ClusterR)

# Loading Data
cluster <- read.csv("clustering-data.csv")

# Reviewing Data
str(cluster)

# Plotting the "cluster" data
ggplot(cluster, aes(x=x, y=y)) + geom_point()
# Love this easter egg

# Fitting K-Means clustering Model to training data set
set.seed(240) # Setting seed
kmeans.2 <- kmeans(cluster, centers = 2, nstart = 20)


# lst1 <- lapply(2:13, function(i) kmeans(cluster[1:2], i, iter.max = 20, nstart = 10))
# names(lst1) <- paste0("cluster_cluster", 2:13)


# for (i in lst1) {
  #print(ggplot((lst1, aes(x = Comp.1, y = Comp.2, color = as.factor(A.cluster, 
                         #fill = as.factor(A.cluster))) + geom_point() + 
          #stat_ellipse(type = "t",geom = "polygon",alpha = 0.4))))
# }


summary(kmeans.2)



# Cluster identification for  
# each observation 
kmeans.2$cluster 

# Confusion Matrix 
cm <- table(cluster$x, kmeans.2$cluster) 
cm 

# Model Evaluation and visualization 
plot(cluster[c("x", "y")]) 
plot(cluster[c("x", "y")],  
     col = kmeans.2$cluster) 
plot(cluster[c("x", "y")],  
     col = kmeans.2$cluster,  
     main = "K-means with 2 clusters")

## Plotting cluster centers 
kmeans.2$centers 
kmeans.2$centers[, c("x", "y")]

# cex is font size, pch is symbol 
points(kmeans.2$centers[, c("x", "y")],  
       col = 1:3, pch = 8, cex = 3) 


y_kmeans <- kmeans.2$cluster 
clusplot(cluster[, c("x", "y")], 
         y_kmeans, 
         lines = 0, 
         shade = TRUE, 
         color = TRUE, 
         labels = 2, 
         plotchar = FALSE, 
         span = TRUE, 
         main = paste("Cluster Data"), 
         xlab = 'X', 
         ylab = 'Y') 


ggplot(kmeans.3, aes(x=x, y=y)) + geom_point()




kmdist <- function(data,km) {
  sqrt(rowSums((data[,colnames(km$centers)] - fitted(km))^ 2))
}
kmdist.2 <- kmdist(cluster, kmeans.2)

head(kmeans.2)


# Decide how many clusters to look at
n_clusters <- 12

# Initialize total within sum of squares error: wss
wss <- numeric(n_clusters)

set.seed(123)

# Look over 1 to n possible clusters
for (i in 1:13) {
  # Fit the model: km.out
  km.out <- kmeans(cluster, centers = i, nstart = 20)
  # Save the within cluster sum of squares
  wss[i] <- km.out$tot.withinss
}

# Produce a scree plot
wss_df <- tibble(clusters = 1:13, wss = wss)

scree_plot <- ggplot(wss_df, aes(x = clusters, y = wss, group = 1)) +
  geom_point(size = 4)+
  geom_line() +
  scale_x_continuous(breaks = c(2, 4, 6, 8, 10, 12)) +
  xlab('Number of clusters')
scree_plot

help("kmeans")
