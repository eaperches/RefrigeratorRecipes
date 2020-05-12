# RefrigeratorRecipes
Recommends recipes based on the ingredients you give it, along with the steps to make it using Food.com dataset


In order to execute this script, you will need:
- RAW_recipes.csv from https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions#RAW_recipes.csv
- pandas, spellchecker, inflect libraries installed for spelling checking and plural/singular converison


Ex:

Input:
['apple', 'orange', 'pear', 'lemon', 'beer', 'wine']

Output:
[name                                    apple orange blend juice
ingredients                ['apples', 'pear', 'orange', 'lemon']
steps          ['wash apples , pear and lemon', 'core apples ...
Name: 7640, dtype: object]
