def vatCal(total):
    result = total+(total*7/100)
    return result

total = int(input("enter total number: "))
print(vatCal(total))