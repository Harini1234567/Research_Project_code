import statistics

"""The anova_test function takes two lists of values and a name as input arguments. The function converts the input 
lists into numpy arrays and applies the Mann-Whitney U test to them to determine if they come from the same 
distribution. The function then calculates the mean and standard deviation of each list using the statistics module. 
The function prints out the name of the input list, the Mann-Whitney U test statistics and p-value, as well as the 
mean and standard deviation of each list. Call this function using your data.  """

def anova_test(list1, list2,name):
    # Convert lists to numpy arrays
    from scipy.stats import mannwhitneyu
    stat, p_value = mannwhitneyu(list1, list2 )
    print(name, "Statistics=%.2f, p=%.2f" % (stat, p_value))
    mean1 = statistics.mean(list1)
    stdev1 = statistics.stdev(list1)
    mean2 = statistics.mean(list2)
    stdev2 = statistics.stdev(list2)

    print("Mean:", mean1)
    print("Standard deviation:", stdev1)

    print("Mean2:", mean2)
    print("Standard deviation2:", stdev2)


