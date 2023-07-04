def split_ingredient_string(ingredient_string):
    ingredient_string = ingredient_string.lower()

    name = ""
    amount = ""
    units = ""

    return {name, amount, units}


unitCorrelation = {
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
