from email_validator import validate_email, EmailNotValidError

def is_valid_email(email):
    try:
        # Validate the email address
        valid = validate_email(email)
        # Update with the normalized form of the email
        email = valid.email
        return True
    except EmailNotValidError:
        return False

def strenght_password(password: str) -> str:
    if len(password) < 7:
        return "Password too short"
    
    if not any(char.isupper() for char in password):
        return "Password must have uppercase letters"
    
    if not any(char.islower() for char in password):
        return "Password must have lowercase letters"
    
    if not any(char.isdigit() for char in password):
        return "Password must have digits"
    
    special_chars = "!@#$%^&*()-_=+\\|?<>"
    if not any(char in special_chars for char in password):
        return "Password must have a special character"
    
    return "Strong"
