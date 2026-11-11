# Haemoglobin by age: a small example for the Git demo
# Fictional data. Run with: Rscript haemoglobin_plot.R (or open it in RStudio)

# Create the data: one value per patient, in the same order in every list
age         <- c(34, 47, 52, 61, 70, 28, 45, 66)          # in years
sex         <- c("female", "male", "female", "male", "female", "male", "diverse", "female")
haemoglobin <- c(13.2, 14.1, 12.8, 13.5, 11.9, 14.6, 13.9, 12.4)   # in g/dL

# Draw a scatter plot: one dot per patient, with axis labels and a title
plot(age, haemoglobin,
     xlab = "Age (years)", ylab = "Haemoglobin (g/dL)",
     main = "Haemoglobin by age")
