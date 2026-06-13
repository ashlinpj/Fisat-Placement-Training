def is_valid_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    return (
        len(password) >= 8 and
        has_upper and
        has_lower and
        has_digit and
        has_special
    )

# Example
pwd = input("Enter password: ")

if is_valid_password(pwd):
    print("Valid Password")
else:
    print("Invalid Password")