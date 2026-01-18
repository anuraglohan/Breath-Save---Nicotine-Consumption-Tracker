import hashlib
import json
import os

def hash_password(password):
    """
    Hash password using SHA-256 for secure storage.
    
    Args:
        password (str): Plain text password
        
    Returns:
        str: SHA-256 hashed password
    """
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    """
    Load user credentials from JSON file.
    
    Returns:
        dict: Dictionary of username -> hashed_password mappings
    """
    if os.path.exists('users.json'):
        with open('users.json', 'r') as f:
            return json.load(f)
    return {}

def save_users(users):
    """
    Save user credentials to JSON file.
    
    Args:
        users (dict): Dictionary of username -> hashed_password mappings
    """
    with open('users.json', 'w') as f:
        json.dump(users, f)

def register_user(username, password):
    """
    Register new user with hashed password validation.
    
    Args:
        username (str): New username
        password (str): Plain text password
        
    Returns:
        tuple: (success: bool, message: str)
    """
    users = load_users()
    if username in users:
        return False, "Username already exists"
    users[username] = hash_password(password)
    save_users(users)
    return True, "Registration successful!"

def verify_user(username, password):
    """
    Verify user login credentials.
    
    Args:
        username (str): Username
        password (str): Plain text password
        
    Returns:
        bool: True if credentials match, False otherwise
    """
    users = load_users()
    if username not in users:
        return False
    return users[username] == hash_password(password)

def update_password(username, current_password, new_password):
    """
    Update user password after verification.
    
    Args:
        username (str): Username
        current_password (str): Current plain text password
        new_password (str): New plain text password
        
    Returns:
        tuple: (success: bool, message: str)
    """
    if not verify_user(username, current_password):
        return False, "Current password is incorrect"
    
    users = load_users()
    users[username] = hash_password(new_password)
    save_users(users)
    return True, "Password updated successfully!"
