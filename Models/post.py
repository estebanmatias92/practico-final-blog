class Post:
    _id = None
    _titulo = None
    _content = None
    
    define get(id):
        post = {}
        return post

    define getAll():
        posts = []
        return posts

    define delete(id):
        ...

    define create(title, content):
        ...

    define update(id, post):
        ...


