#!/usr/bin/env python3

# Created on 05/25/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Calculator the effect size for two groups when using independent T-test statistic
# Explanation: Group A is the treatment group and Group B is the control group
import math

def compute_mean(values):
    mu = 0
    
    for v in values:
        mu += v
    
    mu = mu / len(values)
    return mu

def compute_sample_mean(values):
    s = 0

    for v in values:
        s += v
    
    s = s / (len(values) - 1)

    return s

def compute_squared_diff(values, mu):
    sqr_diffs = []

    for v in values:
        sqr_diffs.append((v - mu)**2)
    
    return sqr_diffs

def compute_pooled_std_dev(std_dev_a, std_dev_b):
    pooled = math.sqrt((std_dev_a**2 + std_dev_b**2) / 2)
    return pooled

def compute_effect_size(mean_a, mean_b, pooled_std_dev):
    
    effect_size = ((mean_b - mean_a) / pooled_std_dev)

    return effect_size

def main():
    group_a = [1, 2, 3, 4, 5, 6]
    group_b = [4, 5, 6, 7, 8, 9]

    #compute means of the groups
    mean_a = compute_mean(group_a)
    print("Group A M is: {0}".format(mean_a))
    mean_b = compute_mean(group_b)
    print("Group B M is: {0}".format(mean_b))

    #compute the pooled standard deviation 
    sqr_diffs_a = compute_squared_diff(group_a, mean_a)
    sqr_diffs_b = compute_squared_diff(group_b, mean_b)
    variance_a = compute_sample_mean(sqr_diffs_a)
    variance_b = compute_sample_mean(sqr_diffs_b)
    
    std_dev_a = variance_a**(1/2) #validated std dev calc
    print("Group A SD is: {0}".format(std_dev_a))
    std_dev_b = variance_b**(1/2)
    print("Group B SD is: {0}".format(std_dev_b))

    pooled_std_dev = compute_pooled_std_dev(std_dev_a, std_dev_b)

    #compute and output effect size
    effect = compute_effect_size(mean_a, mean_b, pooled_std_dev)
    print("Cohen's d is: {0}".format(effect))

main()