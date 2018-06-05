#!/usr/bin/env python3

# Created on 06/4/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: compute the wilcoxon signed ranked sum statistic  
# Explanation: 

def compute_treatment_diff(a, b):
    differences = []

    for i in range(len(a)):
        differences.append(b[i] - a[i])

    return differences

def rank_differences(differences):
    ranked = []

    for d in differences:
        ranked.append(abs(d))
    
    ranked.sort()

    return ranked

def eval_signs():
    return 0

def compute_w_negative():
    w_negative = 0

    return w_negative

def compute_w_positive():
    w_positive = 0

    return w_positive

def main():
    treatment_a = [2.5, 3.5, 2.9, 2.1, 6.9, 2.4, 4.9, 6.6, 2.0, 2.0, 5.8, 7.5]
    treatment_b = [4.0, 5.6, 3.2, 1.9, 9.5, 2.3, 6.7, 6.0, 3.5, 4.0, 8.1, 19.9]

    differences = compute_treatment_diff(treatment_a, treatment_b)
    ranked = rank_differences(differences)

    print("The differences are: {0}".format(differences))
    print("The ranked differences are: {0}".format(ranked))

main()