def validate_usr(username):
    if not 4 <= len(username) <= 16:
        return False
    allowed = "abcdefghijklmnopqrstuvwxyz0123456789_"
    for char in username:
        if char not in allowed:
            return False
    return True