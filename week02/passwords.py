def word_in_file(word, filename, case_sensitive):
    """
    Reads a file and checks if the word exists in it.
    Returns True if found, False otherwise.
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if case_sensitive:
                    if word == line:
                        return True
                else:
                    if word.lower() == line.lower():
                        return True
        return False
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return False


def word_has_character(word, character_list):
    """
    Checks if any character in the word is in the character_list.
    Returns True if found, False otherwise.
    """
    for char in word:
        if char in character_list:
            return True
    return False


def word_complexity(word):
    """
    Calculates complexity score based on character types.
    Returns a score from 0 to 4.
    """
    LOWER = "abcdefghijklmnopqrstuvwxyz"
    UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGITS = "0123456789"
    SPECIAL = "!@#$%^&*()_+-=[]{}|;:',.<>?/\\\"~`"
    
    complexity = 0
    
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    
    return complexity


def password_strength(password, min_length=10, strong_length=16):
    """
    Calculates password strength score from 0 to 5.
    """
    # Check if password is in dictionary (case-insensitive)
    if word_in_file(password, "dictionary.txt", False):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    # Check if password is in top passwords list (case-sensitive)
    if word_in_file(password, "toppassword.txt", True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    # Check if password is too short
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    # Check if password is long enough to be strong
    if len(password) > strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    # Calculate complexity-based strength
    complexity = word_complexity(password)
    strength = 1 + complexity
    
    return strength


def main():
    """
    Main function to run the password strength checker.
    """
    print("=" * 50)
    print("Password Strength Checker")
    print("=" * 50)
    print("Enter a password to check its strength.")
    print("Enter 'q' or 'Q' to quit.\n")
    
    while True:
        password = input("Enter password: ")
        
        # Check if user wants to quit
        if password.lower() == 'q':
            print("Thank you for using the Password Strength Checker. Goodbye!")
            break
        
        # Calculate and display password strength
        strength = password_strength(password)
        print(f"Password Strength: {strength} out of 5\n")


# Run the program
if __name__ == "__main__":
    main()