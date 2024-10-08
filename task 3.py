import re

# Function to assess password strength
def assess_password_strength(password):
    # Initialize score
    score = 0
    strength = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digit": False,
        "special_char": False
    }

    # Criteria checks
    if len(password) >= 8:
        score += 1
        strength["length"] = True
    
    if re.search(r'[A-Z]', password):
        score += 1
        strength["uppercase"] = True
    
    if re.search(r'[a-z]', password):
        score += 1
        strength["lowercase"] = True
    
    if re.search(r'[0-9]', password):
        score += 1
        strength["digit"] = True
    
    if re.search(r'[\W_]', password):  # Checks for special characters
        score += 1
        strength["special_char"] = True
    
    # Determine the overall strength
    if score == 5:
        return "Very Strong", strength
    elif score == 4:
        return "Strong", strength
    elif score == 3:
        return "Moderate", strength
    elif score == 2:
        return "Weak", strength
    else:
        return "Very Weak", strength

# Function to print the criteria feedback
def print_feedback(strength_criteria):
    print("\nPassword Strength Criteria:")
    print(f"- Length >= 8 characters: {'✓' if strength_criteria['length'] else '✗'}")
    print(f"- Contains uppercase letters: {'✓' if strength_criteria['uppercase'] else '✗'}")
    print(f"- Contains lowercase letters: {'✓' if strength_criteria['lowercase'] else '✗'}")
    print(f"- Contains digits: {'✓' if strength_criteria['digit'] else '✗'}")
    print(f"- Contains special characters: {'✓' if strength_criteria['special_char'] else '✗'}")

# Main function
def password_tool():
    password = input("Enter your password: ")
    strength, criteria = assess_password_strength(password)
    
    print(f"\nPassword Strength: {strength}")
    print_feedback(criteria)

# Example usage
if __name__ == "__main__":
    password_tool()
