#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  rec_vals = list(recipe.values())
  ing_vals = list(ingredients.values())
  rec_keys = recipe.keys()
  ing_keys = ingredients.keys()
  result = ing_vals[0] / rec_vals[0]
  if rec_keys != ing_keys:
  	return 0
  for i in range(0, len(rec_keys) - 1):
  	x = ing_vals[i] / rec_vals[i]
  	if x < result:
  		result = x
  return int(result)

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))