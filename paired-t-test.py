#!/usr/bin/env python3

# Created on 05/27/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Calculate a paired t-test statistic for matched pairs, two conditions, two time points, and so forth.
# Explanation: 
import math

def compute_differences(group_a, group_b, pairs):
    differences = []

    for i in range(pairs):
        differences.append(group_a[i] - group_b[i])

    return differences

def compute_diff_mean(differences):
    m = 0

    for d in differences:
        m += d
    
    m = m / len(differences)
    return m

def compute_sqr_diff(differences, mean_differences):
    sqr_differences = []

    for d in differences:
        x = d - mean_differences
        sqr_differences.append(x**2)
    
    return sqr_differences

def compute_sqr_diff_mean(sqr_differences):
    m = 0
    
    for s in sqr_differences:
        m += s
    
    m = (1 / (len(sqr_differences) - 1)) * m

    return m

def compute_sample_std_dev(mean_sqr_differences):
    std_dev = math.sqrt(mean_sqr_differences)

    return std_dev


def compute_std_error(std_dev, pairs):
    std_error = std_dev / math.sqrt(pairs)
    return std_error

def compute_t_statistic(mean_differences, std_error):
    t = mean_differences / std_error

    return t


def main():
    group_a = [312, 242, 340, 388, 296, 254, 391, 402, 290] #before group
    group_b = [300, 201, 232, 312, 220, 256, 328, 330, 231] #after group
    pairs = 9

    differences = compute_differences(group_a, group_b, pairs)
    mean_differences = compute_diff_mean(differences)
    sqr_differences = compute_sqr_diff(differences, mean_differences)
    mean_sqr_differences = compute_sqr_diff_mean(sqr_differences)
    std_dev = compute_sample_std_dev(mean_sqr_differences)
    std_error = compute_std_error(std_dev, pairs)
    t = compute_t_statistic(mean_differences, std_error)

    print("The mean of differences is: {0}".format(mean_differences))
    print("The standard deviation is: {0}".format(std_dev))
    print("The standard error is: {0}".format(std_error))
    print("The t statistics is: {0}".format(t))

main()