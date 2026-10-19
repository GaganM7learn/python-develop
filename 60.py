age = input("Enter your age")
banned = input("Are you banned? (Yes/No)")

if banned != "Yes" and age >= 18:
    print("Entry denied")
else:
    print("Entry allowed")