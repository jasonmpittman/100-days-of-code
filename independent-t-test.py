#!/usr/bin/env python3

# Created on 05/27/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Calculate the T-test statistic for independent samples
# Explanation: Compare the means of two independent samples to determine statistical difference & significance
import math

def compute_group_sum(values):
    group_sum = 0

    for v in values:
        group_sum += v
    
    return group_sum


def compute_square(value):
    sqr = value**2
    return sqr

def compute_mean(values):
    m = 0

    for v in values:
        m += v
    
    m  = m / len(values)
    return m

def compute_sum_of_squares(values):
    s = 0

    for v in values:
        s += v**2
    
    return s

def compute_t_ratio(mean_group_a, mean_group_b, n_a, n_b, sum_of_squares_a, sum_of_squares_b, sqr_group_a, sqr_group_b):
    t = 0

    m = mean_group_a - mean_group_b
    a = (sum_of_squares_a - (sqr_group_a / n_a))
    b = (sum_of_squares_b - (sqr_group_b / n_b))

    #intermediate artithmetic for comprehension
    x = (a + b) / (n_a + n_b - 2)
    y = (1 / n_a) + (1 / n_b)
    z = x * y

    #t-ratio computation
    t = m / math.sqrt(z)

    return t

def compute_deg_freedom(n_a, n_b):
    df = (n_a - 1) + (n_b - 1)
    return df

def main():
    group_a = [1,2,2,3,3,4,4,5,5,6]
    group_b = [1,2,4,5,5,5,6,6,7,9]

    sum_group_a = compute_group_sum(group_a)
    sum_group_b = compute_group_sum(group_b)

    sqr_group_a = compute_square(sum_group_a)
    sqr_group_b = compute_square(sum_group_b)

    mean_group_a = compute_mean(group_a)
    mean_group_b = compute_mean(group_b)

    sum_of_squares_a = compute_sum_of_squares(group_a)
    sum_of_squares_b = compute_sum_of_squares(group_b)

    t = compute_t_ratio(mean_group_a, mean_group_b, len(group_a), len(group_b), sum_of_squares_a, sum_of_squares_b, sqr_group_a, sqr_group_b)
    df = compute_deg_freedom(len(group_a), len(group_b))
    
    print("The t-ratio is: {0}".format(t))
    print("The degrees of freedom is: {0}".format(df))

main()