#!/usr/bin/env python3

# Created on 06/4/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: compute the wilcoxon signed ranked sum statistic (w- and w+)
# Explanation: 

def compute_treatment_diff(a, b):
    differences = []

    for i in range(len(a)):
        differences.append(b[i] - a[i])

    return differences

def rank_differences(differences):
    ranked = []
    rank = 1

    for diff in differences:
        if diff < 0:
            ranked.append([abs(diff), '-'])
        if diff == 0:
            ranked.append([0, ' '])
        if diff > 0:
            ranked.append([abs(diff), '+'])

    ranked.sort()

    for r in ranked:
        r.insert(0, rank)
        rank += 1

    return ranked

def compute_w_statistics(ranked):
    w_negative = 0
    w_positive = 0
    w = []

    for r in ranked:
        if r[2] == '-':
            w_negative += r[0]
        if r[2] == '+':
            w_positive += r[0]

    w = [w_negative, w_positive]

    return w

def main():
    treatment_a = [2.5, 3.5, 2.9, 2.1, 6.9, 2.4, 4.9, 6.6, 2.0, 2.0, 5.8, 7.5]
    treatment_b = [4.0, 5.6, 3.2, 1.9, 9.5, 2.3, 6.7, 6.0, 3.5, 4.0, 8.1, 19.9]
    w = []

    differences = compute_treatment_diff(treatment_a, treatment_b)
    ranked = rank_differences(differences)
    w = compute_w_statistics(ranked)

    #print("The differences are: {0}".format(differences))
    #print("\n")
    #print("The ranked differences are: {0}".format(ranked))
    #print("\n")
    print("The W- and W+ are: {0} ; {1}".format(w[0], w[1]))

main()