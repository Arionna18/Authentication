# users with roles
users = {
    "Karen": "admin",
    "Ashley": "user"
}

#login (no password, just username)
def login(username):
    if username in users:
        role = users[username]
        print(f"Logged in as {username} with role: {role}")
        return role
    else:
        print("User not found")
        return None

# admin only
def admin_dashboard(role):
    if role == "admin":
        print("Access granted to admin dashboard.")
    else:
        print("Access denied. Admins only.")

# user only
def user_profile(role):
    if role == "user":
        print("Access granted to user profile.")
    else:
        print("Access denied. Users only.")

# --- Simulation ---
current_role = login("Ashley")  # change to "Ashley" to test user role

if current_role:
    admin_dashboard(current_role)
    user_profile(current_role)
    
