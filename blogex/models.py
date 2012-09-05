class BlogexUser(object):
    def __init__(self, username=None, email=None, password=None, posts=[]):
        self.username = username
        self.email = email 
        self.password = password
        self.posts = posts

    def is_authenticated(self):
        return True

    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

class Post(object):
    def __init__(self, id=None, title=None, author=None, text=None,
            post_date=None, posts=None):
        self.id = id
        self.title = title
        self.author = author
        self.text = text
        self.post_date = post_date

    def __repr__(self):
        return "%s - %s" % (self.author, self.title)
