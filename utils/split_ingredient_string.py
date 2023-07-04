import re

unit_correlation = {
    # Odd Cookery Units
    "thumb": ["thumb"],
    "can ": ["can ", "400g can", "15-16oz can"],
    "spears": ["spears"],
    # Volume units
    "tsp": ["tsp", "tsps", "teaspoon", "teaspoons"],
    "tbsp": ["tbsp", "tbsps", "tablespoon", "tablespoons"],
    "cup": ["cup", "cups"],
    # Leaves is a weird unit but I need to check cups before leaves so it's down here
    "leaves": ["leaves"],
    "oz ": ["oz ", "ounce", "ounces"],
    "fl_oz": ["fl oz", "fluid ounce", "fluid ounces"],
    "pt": ["pt", "pint", "pints"],
    "qt": ["qt", "quart", "quarts"],
    "gal": ["gal", "gallon", "gallons"],
    "ml": ["ml", "milliliter", "milliliters"],
    "litre": ["litre", "litres", "liter", "liters"],
    # Weight units
    "mg": ["mg", "milligram", "milligrams"],
    "g": ["g ", "gram", "grams"],
    "kg": ["kg", "kilogram", "kilograms"],
    "lb": ["lb", "pound", "pounds"],
    "oz_weight": ["oz", "ounce", "ounces"],
    # Count units
    "piece": ["piece", "pieces"],
    "slice": ["slice", "slices"],
    "whole": ["whole"],
    "package": ["package", "packages"],
    "can": ["can", "cans"],
    "jar": ["jar", "jars"],
}


def split_ingredient_string(ingredient_string):
    ingredient_string = ingredient_string.lower()

    name = ""
    amount = ""
    units = ""

    for unit_key, unit_values in unit_correlation.items():
        found_unit = [unit for unit in unit_values if unit in ingredient_string]

        if found_unit:
            units = unit_key
            ingredient_string = re.sub(units, " ", ingredient_string)
            break

    print(units, ingredient_string)

    parts = ingredient_string.split()
    split = 0
    while re.search("\d", parts[split]):
        split += 1

    amount = " ".join(parts[0:split])
    name = " ".join(parts[split:])

    return {name, amount, units}


split_ingredient_string("1 tsp butter")
