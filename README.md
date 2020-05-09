# RefrigeratorRecipes
Recommends recipes based on the ingredients you give it, along with the steps to make it


In order to execute this script, you will need:
- RAW_recipes.csv from https://www.kaggle.com/shuyangli94/food-com-recipes-and-user-interactions#RAW_recipes.csv
- pandas, spellchecker, inflect libraries installed for spelling checking and plural/singular converison


The program guarantess similarty between your ingredients and the recipe up to 60%

Ex:

Input:
['apple', 'orange', 'pear', 'lemon', 'beer', 'wine']

Output:
[name                                    apple orange blend juice
ingredients                ['apples', 'pear', 'orange', 'lemon']
steps          ['wash apples , pear and lemon', 'core apples ...
Name: 7640, dtype: object]
