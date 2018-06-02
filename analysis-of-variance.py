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

def compute_group_mean(group_means):
    m = 0

    for mean in group_means:
        m += mean 

    m = m / len(group_means)

    return m

def compute_sum_of_sqr_errors(groups, group_means):
    sse = 0

    for i in range(len(groups)):
        sum = 0
        for value in groups[i]:
            sum += (value - group_means[i])**2
        
        sse += sum 

    return sse

def compute_sum_of_sqr_treat(group_mean, group_means):
    sqt = 0

    for mean in group_means:
        sqt += (mean - group_mean)**2

    sqt = 3 * sqt
    return sqt

def compute_degree_freedom_treat(sample_size):
    dfe = sample_size - 1
    return dfe

def compute_degree_freedom_error(value_size, sample_size):
    dft = value_size - sample_size
    return dft

def compute_mean_sqr_error(dfe, sse):
    msqre = sse / dfe
    return msqre

def compute_mean_sqr_treat(dft, sst):
    print(dft)
    msqrt = sst / dft
    return msqrt

def count_values(groups):
    count = 0

    for group in groups:
        for value in group:
            count += 1

    return count

def compute_f_statistic(msqre, msqrt):
    f = msqrt / msqre
    return f


def main():
    group_a = [12, 9, 12]
    group_b = [7, 10, 13]
    group_c = [5, 8, 11]
    group_d = [5, 8, 8]    

    mean_a = compute_mean(group_a)
    mean_b = compute_mean(group_b)
    mean_c = compute_mean(group_c)
    mean_d = compute_mean(group_d)

    groups = [group_a, group_b, group_c, group_d]
    sample_size = len(groups)
    value_size = count_values(groups)
    group_means = [mean_a, mean_b, mean_c, mean_d]
    

    group_mean = compute_group_mean(group_means)
    sse = compute_sum_of_sqr_errors(groups, group_means)
    sst = compute_sum_of_sqr_treat(group_mean, group_means)
    dfe = compute_degree_freedom_error(value_size, sample_size)
    dft = compute_degree_freedom_treat(sample_size)

    msqre = compute_mean_sqr_error(dfe, sse)
    msqrt = compute_mean_sqr_treat(dft, sst)
    f = compute_f_statistic(msqre, msqrt)

    print("The mean is of group A is: {0}".format(mean_a))
    print("The mean is of group B is: {0}".format(mean_b))
    print("The mean is of group C is: {0}".format(mean_c))
    print("The mean is of group D is: {0}".format(mean_d))
    print("The total mean is: {0}".format(group_mean))
    print("\n")
    print("The sum of square errors is: {0}".format(sse))
    print("The sum of square treatment is: {0}".format(sst))
    print("The degrees of freedom of error is: {0}".format(dfe))
    print("The degrees of freedom of treatment is: {0}".format(dft))
    print("\n")
    print("The mean square of errors is: {0}".format(msqre))
    print("The mean square of treatments is: {0}".format(msqrt))
    print("\n")
    print("The f statistics is: {0}".format(f))
    

main()