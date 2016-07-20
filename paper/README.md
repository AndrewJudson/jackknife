The following are instructions for how to use the script as it is used in the paper (link here).
We have also provided relevant data from the paper.

# Directions for implementing our program for statistical test described in Pearson et al 2006:

With Maxent output data:

1. For each location used in the jackknife model, obtain test omission with chosen cutoff (ex. minimum training presence test omission), which represents success/failed trials, and area of model with chosen cutoff (ex. minimum training presence area), which represents probability of success.


The file “Sample data from Judson et al 2016” contains sample raw Maxent output data from Judson et al 2016 to use as an example

2. For the statistical program, make a csv file with a column labeled “trials” and include 1 for a successful prediction, and 0 if the prediction was omitted (this requires switching 0s to 1s and vice versa from the Maxent output).

Make a second column labeled “probabilities” with corresponding probabilities of success (area).

A csv sample file for each species, EBOV and SUDV, from Judson et al 2016 are included as examples of what the final csv file should look like.

3. Run the program as described in the README using the csv file made

Our program will calculate the test statistic, and output a p-value.

For SUDV you should get ~ 3.345968e-05, EBOV ~ 2.857739e-19.
