import re
def verify_email(email):
    pattern = r"^\b\w+@\w+\.\w+\b$"
    if re.fullmatch(pattern,email):
        return 0
    else:return"\nEste formato não é um email válido" 