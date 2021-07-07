# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 16:46:28 2021

@author: Alexis Drugeon
"""

import csv
import numpy as np
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt

inputt = pd.read_csv('input.csv')


#Quelques print de test et affichage de panda.head()
print(inputt.head())
print(len(inputt['User_ID'].unique()))
print(len(inputt['Product_ID'].unique()))
print(inputt['Gender'].unique())

# Qui est le plus susceptible de dépenser entre les Hommes et les Femmes
sns.set(style='darkgrid')
sns.countplot(x="Gender", data=inputt)
plt.show()

#Plutot que de supprimer les colonnes, je créé un nouveau fichier qui gardde les colonnes voulues
#Garde_col = [User_ID,Product_ID,Gender,Age,Occupation,City_Category,Stay_In_Current_City_Years,Marital_Status,Product_Category_1,Product_Category_2,Product_Category_3]
#toutes les colonnes existantes ci-dessus. On enlève User et product ID, on gard les autres avc les guillemets
Garde_col = ['Gender','Age','Occupation','City_Category','Stay_In_Current_City_Years','Marital_Status','Product_Category_1','Product_Category_2','Product_Category_3']
new_inputt = inputt[Garde_col]
new_inputt.to_csv("newInput.csv", index=False)