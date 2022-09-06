class Post:
    _id = None
    _username = None
    _password = None
    _isAdmin = None
    
    define get(id):
        user = {}
        return user

    define create(title, content):
        ...