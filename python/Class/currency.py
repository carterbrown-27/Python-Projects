relToCAD = {"cad":1.00, "usd":1.32, "eur":1.45, "gbp":1.63, "jpy":0.0123}
print("Currently supported currencies are: ")
for key in relToCAD: print(key, end=" ")
print()

while(True):
    fromCurrency = input("From which currency are you converting? ").lower()
    toCurrency = input("To which currency are you converting? ").lower()

    if(fromCurrency not in relToCAD or toCurrency not in relToCAD):
        print("Invalid input, one or more currencies are not supported.")
        continue

    fromAmt = input("How much "+fromCurrency+" is to be converted? ")
    try:
        fromAmt = float(fromAmt)
    except:
        print("Invalid input: amount is not a number.")
        continue
    print(round(fromAmt*relToCAD[fromCurrency]/relToCAD[toCurrency],2))
    break
