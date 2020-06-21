#! python3
# Import modules
import pyinputplus as pyip

cost = 0

# Create menu lists
breadType = ['wheat', 'white', 'sourdough']
proteinType = ['chicken', 'turkey', 'ham', 'tofu']
cheeseType = ['cheddar', 'Swiss', 'mozzarella']
toppingType = ['mayo', 'mustard', 'lettuce', 'tomato']

# Create dictionary to hold ingredient prices
ingredientPrices = {'wheat': 1.00, 'white': 0.85, 'sourdough': 1.25,
                    'chicken': 1.00, 'turkey': 0.97, 'ham': 0.91, 'tofu': 3.50,
                    'cheddar': 0.75, 'Swiss': 0.65, 'mozzarella': 0.97,
                    'mayo': 0.25, 'mustard': 0.20, 'lettuce': 0.68,
                    'tomato': 0.57}

# Get sandwich order from customer
bread = pyip.inputMenu(breadType)
protein = pyip.inputMenu(proteinType)
print('Would you like cheese on your sandwich?')

# if pyip.inputYesNo() == 'yes':
#     cheese = pyip.inputMenu(cheeseType)
# else:
#     cheese = ''

# Refactored
cheese = pyip.inputMenu(cheeseType) if pyip.inputYesNo() == 'yes' else ''

print('Would you like a topping on your sandwich?')
# if pyip.inputYesNo() == 'yes':
#     topping = pyip.inputMenu(toppingType)
# else:
#     topping = ''

# Refactored
topping = pyip.inputMenu(toppingType) if pyip.inputYesNo() == 'yes' else ''

sandwich = [bread, protein, cheese, topping]

# Calculate cost of sandwich
for ingredient in sandwich:
    cost += ingredientPrices.get(ingredient, 0)

# Print order
print('\nIngredients summary:')
print(bread, ingredientPrices[bread])
print(protein, ingredientPrices[protein])
if cheese:
    print(cheese, ingredientPrices[cheese])
if topping:
    print(topping, ingredientPrices[topping])

print(f'\nTotal sandwich cost: ${cost:.2f}')
