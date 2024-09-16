import re

def validate_password(password):
    invalid_passwords = ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"]

    if password in invalid_passwords:
        return "Error: Password is in the list of invalid passwords."

    if len(password) != 8:
        return "Error: Password must be exactly 8 characters long."

    if re.match(r'^[0-9\W]', password):
        return "Error: Password should not start with a number or special character."

    if not re.search(r'[A-Z]', password):
        return "Error: Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Error: Password must contain at least one lowercase letter."
    if not re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>/?\\|`~]', password):
        return "Error: Password must contain at least one special character."

    return "Password is valid."

# Example usage
passwords = ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f", "Valid1Pass@", "A1b@Cdef"]

for pwd in passwords:
    print(f"Password: {pwd} - {validate_password(pwd)}")
