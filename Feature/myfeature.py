def greet(name):
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    print(greet(user_name))
    print("Welcome to DevAsc")