def convert(grams):
    ounces = grams / 28.3495231 
    return ounces

gramms = float(input("Enter the weight in grams:"))

result = convert(gramms)

print(f"{gramms} grams is equal to {result:.4f} ounces.")
