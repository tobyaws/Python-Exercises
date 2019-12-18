username = ["admin", "Toby", "Eric", "Phil", "Tom"]
for user in username:
    if user is "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello %s, thank you for logging in again." % user)
