import re
def verify_email(email):
    pattern = r"^\b\w+@\w+\.\w+\b$"
    if re.fullmatch(pattern,email):
        print(f"\nEmail: '{email}' válido!")
    else:
        print("\nemail invalido")