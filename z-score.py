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

def compute_variance(sample, mean):
    variance = 0

    for s in sample:
        variance += (s - mean)**2
    
    variance = variance / (len(sample) - 1)

    return variance

def compute_std_dev(variance):
    std_dev = math.sqrt(variance)

    return std_dev

def compute_z_score(x, mean, std_dev):
    z = 0

    z = (x - mean) / std_dev

    return z

def main():
    sample = [7, 8, 8, 7.5, 9]
    x = 7.5

    mean = compute_mean(sample)
    variance = compute_variance(sample, mean)
    std_dev = compute_std_dev(variance)
    z = compute_z_score(x, mean, std_dev)

    print("The mean is: {0}".format(mean))
    print("The variance is: {0}".format(variance))
    print("The standard deviation is: {0}".format(std_dev))
    print("The standard score (z) is: {0}".format(z))

main()

    