# import User

class Post:

    def __init__(self, title, body, author):
        self.title = title
        self.body = body
        self.author = author

    def save(self):
        with open('posts.csv', 'w') as file:
            file.write('{},{},{}'.format(self.title, self.body, self.author))

class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name