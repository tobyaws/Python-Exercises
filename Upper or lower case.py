def upper_or_lower():
    string = input("Enter a string: ")
    lower_count = sum(map(str.islower, string))
    upper_count = sum(map(str.isupper, string))
    print("Lowercase letters: {0}   Uppercase letters: {1}".format(lower_count, upper_count))

upper_or_lower()



