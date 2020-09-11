#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/final_results.py
#                                                                             
# PROGRAMMER: Siddarth Jain
# DATE CREATED: September 12th, 2020                                 
# REVISED DATE: September 12th, 2020
# PURPOSE: Run check_images.py for all the different models and compile the data.
from tabulate import tabulate

def final_result(results_dic, results_stats_dic, model):
    l1 = [["Total Images: ", results_stats_dic['n_images']], ["Dog Images: ", results_stats_dic['n_dogs_img']], ["Not-Dog Images: ", results_stats_dic['n_notdogs_img']]]
    table1 = tabulate(l1, tablefmt='orgtbl')
    print(table1, "\n")
    
    l2 = [[model, results_stats_dic['pct_correct_notdogs'], results_stats_dic['pct_correct_dogs'], results_stats_dic['pct_correct_breed'], results_stats_dic['pct_match']]]
    table2 = tabulate(l2, headers = ['CNN Model Architecture', '%Correct NotDogs', '%Correct Dogs', '%Correct Breed', '%Label Match'], tablefmt='orgtbl')
    print(table2)