import numpy as np
from scipy import stats
from scipy.stats import skew, kurtosis, norm


# Sample data
scores = [88, 45, 53, 86, 33, 86, 85, 30, 89, 53, 41, 96, 56, 38, 62,
          71, 51, 86, 68, 29, 28, 47, 33, 37, 25, 36, 33, 94, 73, 46,
          42, 34, 79, 72, 88, 99, 82, 62, 57, 42, 28, 55, 67, 62, 60,
          96, 61, 57, 75, 93, 34, 75, 53, 32, 28, 73, 51, 69, 91, 35]


# Length          
l = len(scores)

# Mode
mode = stats.mode(scores)

# Median
median = np.median(scores)

# Mean 
mean = np.mean(scores)
rounded_mean = round(mean, 3)

# Standard deviation
dev = np.std(scores)
rounded_dev = round(dev, 3)

# Variance
var = np.var(scores)

# Skewness
skew = skew(scores)
rounded_skew = round(skew, 3)

# Kurtosis
kurt = kurtosis(scores)
rounded_kurt = round(kurt, 3)

# Standard error of Skewness
x = len(scores)
std_skew = np.sqrt(6 * (x - 1) / ((x - 2) * (x + 1) * (x + 3)))
rounded_std_skew = round(std_skew, 3)

# Standard error of kurtosis
x = len(scores)
std_kurt = np.sqrt((24 * x * (x - 2) * (x - 3)) / ((x + 1) * (x - 1)**2 * (x - 3) * (x - 5)))
rounded_std_kurt = round(std_kurt, 3)

# Max and Min value
max_val =max(scores)
min_val =min(scores)

# Calculate 25th, 50th, 75th percentile
q1 = np.percentile(scores, 25)
q2 = np.median(scores)
q3 = np.percentile(scores, 75)

q1_rounded =round(q1, 3)
q2_rounded =round(q2, 3)
q3_rounded =round(q3, 3)

# 90th percentile
d9 = np.percentile(scores, 90)
d9_rounded =round(d9, 3)

# 95th percentile
p95 = np.percentile(scores, 95)
p95_rounded=round(p95, 3)


print("Valid", l)
print("Mode:", mode.mode[0])
print("Median:", median,)
print("Mean:", rounded_mean)
print("Std. Deviation:", rounded_dev)
print("Variance:", var)
print("Skewness: ", rounded_skew)
print("Std. Error of Skewness:", rounded_std_skew)
print("Kurtosis:", rounded_kurt)
print("Std. Error of Kurtosis:", rounded_std_kurt)
print("Minimum:", min_val)
print("Maximum:", max_val)
print("25th Percentile:", q1_rounded)
print("50th Percentile:", q2_rounded)
print("75th Percentile:", q3_rounded)
print("90th Percentile:", d9_rounded)
print("95th Percentile:", p95_rounded)
