# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:33:54 2020

@author: Edgar
"""

import pandas as pd

data = pd.read_csv('data/RAW_recipes.csv')

# %%

from spellchecker import SpellChecker
import inflect
p = inflect.engine()
import ast
from collections import Counter
import math


def define_ingredients():
    spell = SpellChecker()
    new_ingredients = input("Enter your ingredients, separated by a comma and without quantities: ")
    new_ingredients = new_ingredients.split(",")
    for i in range(len(new_ingredients)):
        ingredient = new_ingredients[i]
        ingredient = ingredient.strip()
        new_ingredients[i] = p.singular_noun(spell.correction(ingredient)) == False and spell.correction(ingredient) or p.singular_noun(spell.correction(ingredient)) 
    return new_ingredients
    
while True:
    new_ingredients = define_ingredients()
    while True:
        try:
            flag = False
            print("Your ingredients are:" + str(new_ingredients))
            x = input("Is this correct? (y/n) : ")
            x = x.lower()
            assert x == "y" or x == "n"
            if x == "y":
                flag = True
                break
            elif x == "n":
                break
        except:
            print("Invalid input")
            pass
        
    if flag:
        break

my_ingredients = new_ingredients
print("your ingredients are " + str(my_ingredients))

#%%


def counter_cosine_similarity(c1, c2):
    terms = set(c1).union(c2)
    dotprod = sum(c1.get(k, 0) * c2.get(k, 0) for k in terms)
    magA = math.sqrt(sum(c1.get(k, 0)**2 for k in terms))
    magB = math.sqrt(sum(c2.get(k, 0)**2 for k in terms))
    return dotprod / (magA * magB)
    
    
counterA =  Counter(my_ingredients)
recommendations = []
dot = "."
for i in range(len(data)):
    recipe_ingredients = data.loc[:, "ingredients"][i]
    recipe_ingredients = ast.literal_eval(recipe_ingredients)
    recipe_ingredients = [ing if p.singular_noun(ing) == False else p.singular_noun(ing) for ing in recipe_ingredients]
    counterB = Counter(recipe_ingredients)
    
    if counter_cosine_similarity(counterA, counterB) >= 0.6:
        recommendations.append(data.loc[i, ["name", "ingredients", "steps"]])
        
    if len(recommendations) == 1:
        break
    
    if  i%1000 == 0:
        print(dot)
        dot += "."
    
print(recommendations)





    
