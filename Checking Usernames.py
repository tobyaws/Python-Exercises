current_users = ["Steve", "John", "Eric", "Phil", "Tom"]
new_users = ["Alice", "JOHN", "Bob", "phIl", "Dan"]
for user in new_users:
    if user.capitalize() not in current_users:
        print("The username %s is available" % user)

