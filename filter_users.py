import json


def load_users():
    """Load all users from users.json."""
    with open("users.json", "r") as file:
        return json.load(file)


def print_users(users):
    """Print each user on its own line."""
    for user in users:
        print(user)


def filter_users_by_name(name):
    users = load_users()
    filtered_users = [
        user for user in users
        if user["name"].lower() == name.lower()
    ]
    print_users(filtered_users)


def filter_users_by_age(age):
    users = load_users()
    filtered_users = [user for user in users if user.get("age") == age]
    print_users(filtered_users)


def filter_users_by_email(email):
    users = load_users()
    filtered_users = [
        user for user in users
        if user.get("email", "").lower() == email.lower()
    ]
    print_users(filtered_users)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? "
        "(Currently, only 'name' is supported): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    else:
        print("Filtering by that option is not yet supported.")