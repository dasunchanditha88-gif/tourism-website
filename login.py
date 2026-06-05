# =====================================================================
# KAVISHAGINI'S CODE: AUTHENTICATION & SESSION MANAGEMENT MODULE
# =====================================================================

# Global variable acting as the system session to track the active user
current_logged_in_user = None 


def login_user(email, password, all_tourists):
    """
    Handles verifying user credentials and initiating a session.
    Loops through the system records provided by the data module.
    """
    global current_logged_in_user
    
    for tourist in all_tourists: 
        # Compares user input against the record data
        if tourist.email == email and tourist.password == password: 
            # Capture the entire object into the session
            current_logged_in_user = tourist 
            print(f"[AUTH] Success: Session started for {current_logged_in_user.name}.")
            return True
            
    print(f"[AUTH] Failed: Invalid email or password.")
    return False


def logout_user():
    """
    Clears the active user session safely.
    """
    global current_logged_in_user
    
    if current_logged_in_user is not None:
        print(f"[AUTH] Ending session for {current_logged_in_user.name}...")
        current_logged_in_user = None
        print("[AUTH] Success: User logged out.")
        return True
    
    print("[AUTH] Notice: No active session to terminate.")
    return False