def validate(name):
    """
    Returns the length of you name
    """
    print("Hmmm validating... ", name)
    return len(name)

name_length = validate("Mike")
print("Length of name: ", name_length)
name_length = validate("Susan")
print("Length of name: ", name_length)
name_length = validate("Charlotte")
print("Length of name: ", name_length)
print(validate.__doc__)
