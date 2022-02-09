# Created three functions that ran hypothesis tests and printed a string displaying the conclusion.
# Function 1.
import math

def t_test_two_tailed(x1,x2,x3,x4,mu,cl):
    """
    This is a function that will take in four observed values and the population mean (mu), and prints whether
    or not there is a statistically significant difference at the specified confidence level (cl).
    
    This is a two-tailed t-test, meaning that it assesses if there is a positive or negative difference.
    
    Examples:
    >>> t_test_two_tailed(10,11,15,17,12,99)
    There is not a statistically significant difference at the 99% confidence level.
    'There is not a statistically significant difference at the 99% confidence level.'
    >>> t_test_two_tailed(12,13,18,20,11,90)
    There is a statistically significant difference at the 90% confidence level.
    'There is a statistically significant difference at the 90% confidence level.'
    """
    mean = ((x1 + x2 + x3 + x4) / 4)
    standard_deviation = math.sqrt(((x1 - mean) ** 2 + (x2 - mean) ** 2 + (x3 - mean) ** 2 + (x4 - mean) ** 2) / 3)
    standard_error = standard_deviation / 2
    t_statistic = (mean - mu) / standard_error
    if (cl == 99) and (math.fabs(t_statistic > 5.84)):
        result = "There is a statistically significant difference at the 99% confidence level."
        print("There is a statistically significant difference at the 99% confidence level.")
    elif (cl == 99) and (math.fabs(t_statistic <= 5.84)):
        result = "There is not a statistically significant difference at the 99% confidence level."
        print("There is not a statistically significant difference at the 99% confidence level.")
    elif (cl == 95) and (math.fabs(t_statistic > 3.18)):
        result = "There is a statistically significant difference at the 95% confidence level."
        print("There is a statistically significant difference at the 95% confidence level.")
    elif (cl == 95) and (math.fabs(t_statistic <= 3.18)):
        result = "There is not a statistically significant difference at the 95% confidence level."
        print("There is not a statistically significant difference at the 95% confidence level.")
    elif (cl == 90) and (math.fabs(t_statistic > 2.35)):
        result = "There is a statistically significant difference at the 90% confidence level."
        print("There is a statistically significant difference at the 90% confidence level.")
    elif (cl == 90) and (math.fabs(t_statistic <= 2.35)):
         result = "There is not a statistically significant difference at the 90% confidence level."
         print("There is not a statistically significant difference at the 90% confidence level.")
    elif (cl != 90) or (cl != 95) or (cl != 99):
            result = "That confidence level is not supported."
            print("That confidence level is not supported.")
    return result

      
# Function 2.

def t_test_lower_tailed(x1,x2,x3,x4,mu,cl):
    """
    This is a function that will take in four observed values and the population mean (mu), and prints whether
    or not there is a statistically significant difference at the specified confidence level (cl).
    
    This is a lower-tailed t-test, meaning that it only assesses if there is a negative difference.
    
    Examples:
    >>> t_test_two_tailed(10,11,15,17,12,99)
    There is not a statistically significant difference at the 99% confidence level.
    'There is not a statistically significant difference at the 99% confidence level.'
    >>> t_test_two_tailed(12,13,18,20,11,90)
    There is not a statistically significant difference at the 90% confidence level.
    'There is not a statistically significant difference at the 90% confidence level.'
    """
    mean = ((x1 + x2 + x3 + x4) / 4)
    standard_deviation = math.sqrt(((x1 - mean) ** 2 + (x2 - mean) ** 2 + (x3 - mean) ** 2 + (x4 - mean) ** 2) / 3)
    standard_error = standard_deviation / 2
    t_statistic = (mean - mu) / standard_error
    if (cl == 99) and (t_statistic < -4.54):
        result = "There is a statistically significant difference at the 99% confidence level."
        print("There is a statistically significant difference at the 99% confidence level.")
    elif (cl == 99) and (t_statistic >= -4.54):
        result = "There is not a statistically significant difference at the 99% confidence level."
        print("There is not a statistically significant difference at the 99% confidence level.")
    elif (cl == 95) and (t_statistic < -2.35):
        result = "There is a statistically significant difference at the 95% confidence level."
        print("There is a statistically significant difference at the 95% confidence level.")
    elif (cl == 95) and (t_statistic >= -2.35):
        result = "There is not a statistically significant difference at the 95% confidence level."
        print("There is not a statistically significant difference at the 95% confidence level.")
    elif (cl == 90) and (t_statistic < -1.64):
        result = "There is a statistically significant difference at the 90% confidence level."
        print("There is a statistically significant difference at the 90% confidence level.")
    elif (cl == 90) and (t_statistic >= -1.64):
         result = "There is not a statistically significant difference at the 90% confidence level."
         print("There is not a statistically significant difference at the 90% confidence level.")
    elif (cl != 90) or (cl != 95) or (cl != 99):
            result = "That confidence level is not supported."
            print("That confidence level is not supported.")
    return result


# Function 3.
def t_test_upper_tailed(x1,x2,x3,x4,mu,cl):
    """
    This is a function that will take in four observed values and the population mean (mu), and prints whether
    or not there is a statistically significant difference at the specified confidence level (cl).
    
    This is an upper-tailed t-test, meaning that it only assesses if there is a positive difference.
    
    Examples:
    >>> t_test_two_tailed(10,11,15,17,12,99)
    There is not a statistically significant difference at the 99% confidence level.
    'There is not a statistically significant difference at the 99% confidence level.'
    >>> t_test_two_tailed(12,13,18,20,11,90)
    There is a statistically significant difference at the 90% confidence level.
    'There is a statistically significant difference at the 90% confidence level.'
    """
    mean = ((x1 + x2 + x3 + x4) / 4)
    standard_deviation = math.sqrt(((x1 - mean) ** 2 + (x2 - mean) ** 2 + (x3 - mean) ** 2 + (x4 - mean) ** 2) / 3)
    standard_error = standard_deviation / 2
    t_statistic = (mean - mu) / standard_error
    if (cl == 99) and (t_statistic > 4.54):
        result = "There is a statistically significant difference at the 99% confidence level."
        print("There is a statistically significant difference at the 99% confidence level.")
    elif (cl == 99) and (t_statistic <= 4.54):
        result = "There is not a statistically significant difference at the 99% confidence level."
        print("There is not a statistically significant difference at the 99% confidence level.")
    elif (cl == 95) and (t_statistic > 2.35):
        result = "There is a statistically significant difference at the 95% confidence level."
        print("There is a statistically significant difference at the 95% confidence level.")
    elif (cl == 95) and (t_statistic <= 2.35):
        result = "There is not a statistically significant difference at the 95% confidence level."
        print("There is not a statistically significant difference at the 95% confidence level.")
    elif (cl == 90) and (t_statistic > 1.64):
        result = "There is a statistically significant difference at the 90% confidence level."
        print("There is a statistically significant difference at the 90% confidence level.")
    elif (cl == 90) and (t_statistic <= -1.64):
         result = "There is not a statistically significant difference at the 90% confidence level."
         print("There is not a statistically significant difference at the 90% confidence level.")
    elif (cl != 90) or (cl != 95) or (cl != 99):
            result = "That confidence level is not supported."
            print("That confidence level is not supported.")
    return result

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    
t_test_two_tailed(10,12,14,18,15,95)

print(t_test_two_tailed(10,12,14,18,15,95))

