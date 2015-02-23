# jackknife
A Python implementation of the jackknife method described in Pearson et al (Predicting species distributions from small numbers of occurrence records)
[Link to the paper] (http://www.researchgate.net/publication/227714587_ORIGINAL_ARTICLE_Predicting_species_distributions_from_small_numbers_of_occurrence_records_a_test_case_using_cryptic_geckos_in_Madagascar)
This is designed to be a command line tool used by researchers. The following use instructions will be for Mac/Linux terminal but the Windows one is probably similar.

Implementation details: If you have n trials, this algorithm achieves O(2<sup>n + 1</sup>) via dynamic programming. The brute force method is O(n2<sup>n</sup>).