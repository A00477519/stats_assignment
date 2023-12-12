#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 11:15:27 2023

@author: papantiamoah
question 2
"""

import pandas as pd

#read file into a df
df = pd.read_csv('data/titles.csv')



#counting number of vowels
def countVowels(t):
    t = str(t)
    t = t.lower()
    
    mainCount = sum(map(t.count, ['a', 'e', 'i', 'o', 'u']))    
    return mainCount


df['vowels'] = df.apply(lambda row: countVowels(row['title']), axis = 1)
print(df.head())

