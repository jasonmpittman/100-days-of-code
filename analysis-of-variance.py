#!/usr/bin/env python3

# Created on 05/29/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: compute the standard z score for a given sample
# Explanation:
import math

def compute_mean(sample):
    m = 0

    for s in sample:
        m += s
    
    m = m / len(sample)

    return m

def compute_group_mean(groups):
    m = 0

    for mean in groups:
        m += mean 

    m = m / len(groups)

    return m

def compute_sum_of_sqr_errors():

def compute_sum_of_sqr_treat():

def compute_degree_freedom():

def compute_mean_sqr():

def compute_f_statistic():


def main():
    group_a = [12, 9, 12]
    group_b = [7, 10, 13]
    group_c = [5, 8, 11]
    group_d = [5, 8, 8]    

    mean_a = compute_mean(group_a)
    mean_b = compute_mean(group_b)
    mean_c = compute_mean(group_c)
    mean_d = compute_mean(group_d)

    groups = [mean_a, mean_b, mean_c, mean_d]
    mean = compute_group_mean(groups)
    

    print("The mean is of group A is: {0}".format(mean_a))
    print("The mean is of group B is: {0}".format(mean_b))
    print("The mean is of group C is: {0}".format(mean_c))
    print("The mean is of group D is: {0}".format(mean_d))
    print("The total mean is: {0}".format(mean))

main()