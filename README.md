# jackknife
A Python implementation of the jackknife method described in Pearson et al

[Predicting species distributions from small numbers of occurrence records] (http://www.researchgate.net/publication/227714587_ORIGINAL_ARTICLE_Predicting_species_distributions_from_small_numbers_of_occurrence_records_a_test_case_using_cryptic_geckos_in_Madagascar)

This is designed to be a command line tool used by researchers. The following use instructions will be for Mac/Linux terminal but the Windows one is probably similar.

1. Create a csv file with two named columns, "trials" and then "probabilities". Each element of trials should be either a 0 or a 1, and each element of probabilities should be some number between 0 and 1 inclusive.

2. Copy/download the script from this repository into your computer.

3. In the terminal run "python path/to/script.py path/to/my_file.csv", where path/to/script.py is the path to the script and path/to/my_file.csv is the path to your csv file.

4. Output is the test statistic.

Implementation details: If you have n trials, this algorithm achieves O(2<sup>n + 1</sup>) via dynamic programming. The brute force method is O(n2<sup>n</sup>).

In the future? This would make more sense implemented in NumPy, but that would add another burden to researchers who don't know how to use Pip/find packages. This is designed to be easy to use out of the box. Would also make more sense in a compiled language if you were doing a large amount of trials (in the name of speed). Perhaps I will create a C version at some point.