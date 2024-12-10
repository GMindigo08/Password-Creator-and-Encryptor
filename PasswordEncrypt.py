
#NAME:  Michael Gage

#PROGRAM INFO: This program can be utilized to set and encrypt a user password based on specified criteria. A user
# will input their password, prompting either a "VALID" or "INVALID" response. If invalid, the criteria broken
# will be listed.




#----------------------------------WELCOME AND PASSWORD INPUT-----------------------------------

# welcome message for password program
print("\n\n------------------------------------------------\n"
      "WELCOME TO THE PASSWORD CREATOR!\n"
      "------------------------------------------------\n")

# description of password requirements
print("THE FOLLOWING CRITERIA IS REQUIRED: \n "
      "1) password is at least eight characters long\n "
      "2) password has at least one uppercase and one lowercase letter\n "
      "3) password has at least one digit\n "
      "4) password has at least one of these characters: ! @ # $\n ")

# input for the user password variable
password = input("Please Enter Your New Password: ")




#--------------------------------TESTING THE PASSWORD CRITERIA-------------------------------------

# password should be at least eight characters long
def length_test(password):
 if len(password) >= 8:
    return True
 return False


# password should contain at least one uppercase letter
def uppercase_test(password):
    for char in password:
        if char.isupper():
             return True
    return False

# password should contain at least one lowercase letter
def lowercase_test(password):
    for char in password:
        if char.islower():
            return True
    return False

# password should contain at least one digit
def digit_test(password):
    for char in password:
        if char.isdigit():
            return True
    return False

# password must contain !, @, #, or $
def special_character_test(password):
    special_characters = "!@#$"
    for char in password:
        if char in special_characters:
            return True
    return False




#-------------------------OUTPUT FOR INVALID PASSWORD ENTRY-------------------------------

invalid_reasons = [] #creating a list to store invalid password reasons as strings

# Check each criterion and append reasons if not met
if not length_test(password):
    invalid_reasons.append("Password must be at least eight characters long.")
if not uppercase_test(password):
    invalid_reasons.append("Password must contain at least one uppercase letter.")
if not lowercase_test(password):
    invalid_reasons.append("Password must contain at least one lowercase letter.")
if not digit_test(password):
    invalid_reasons.append("Password must contain at least one digit.")
if not special_character_test(password):
    invalid_reasons.append("Password must contain at least one of these special characters: !, @, #, $.")

# assigning index number to reasons in invalid_reasons list.
# calling INVALID reasons from list with associated index number, depending on invalid criteria.
if invalid_reasons:
    print("\n⦻ ---INVALID PASSWORD--- ⦻")
    for i, reason in enumerate(invalid_reasons, start=1):
        print(f"Reason {i}: {reason}")




#-----------------------OUTPUT FOR VALID PASSWORD ENTRY (WITH ENCRYPTION)-------------------------

# password encryption algorithm
def encrypt_password(password):
    encrypted_password = "" #creating the encrypted password variable
    for char in password:
        if char.isalnum():  # If the character is alphanumeric
            encrypted_password += chr(ord(char) + 1)  # +1 to ASCII value
        elif char in "!@#$":  # If the character is a special character
            encrypted_password += chr(ord(char) - 1)  # -1 to ASCII value
        else:
            encrypted_password += char  # Non-alphanumeric/special characters remain unchanged
    return encrypted_password

# output for VALID password (with encryption)
if not invalid_reasons:
    encrypt_password = encrypt_password(password) #redefining the encrypted password
    print("\n✓ ---VALID PASSWORD--- ✓\n")
    print("Your Password:", password)
    print("Encrypted Password:", encrypt_password)

input("Press Enter to exit...")