
def requiere_authentication(func):
    def wrapper(user):
        print("Autenticando...")
        if user.lower() != "admin":
            return "Usuario no autorizado"
        else:
            return func(user)
    return wrapper


@requiere_authentication
def admin_dashboard(user):
    return f"Welcome to the admin dashboard, {user}!"


# auth_view_dashboard = requiere_authentication(admin_dashboard)

# Output: Welcome to the admin dashboard, admin!
print(admin_dashboard("Admin"))
print(admin_dashboard("guest"))  # Output: Usuario no autorizado

# Output: Welcome to the admin dashboard, Admin!
print(requiere_authentication(admin_dashboard)("Admin"))
