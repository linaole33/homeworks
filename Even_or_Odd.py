import math
def even_or_odd(number):
     if number/2 != math.ceil (number/2):
        return "Odd"
     else:
        return "Even"