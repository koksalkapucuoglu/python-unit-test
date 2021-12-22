from app.utiliy import hash_password
def update_user_information(user, **kwargs):
    """These function update user information"""
    for key, value in kwargs.items():
        user[key] = value
        
    return user

def add_user(userlist, username, email, name, password):
    """Add new user to user list"""
    if username in userlist.keys():
        detail = "Adding user is failed because of existing username"
        userlist = userlist
    else:
        userlist[username] = {
                'username': username,
                'email': email,
                'name': name,
                'password': hash_password(password)
        }
        detail = "New user adding succesfully"
    
    return userlist, detail