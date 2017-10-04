from post import Post, Author
# import User

"""
- Update bio
- create post
- display posts
- call method to create page
- set photo
- display friends
"""

def create_post(title, body, author):

    # if not isinstance(author, Author):
    #     raise ValueError('Bad input, author should be an object')

    p = Post(title, body, author)
    p.save()
    print('Post created')

if __name__ == '__main__':
    # author = Author('Ehi Aig')
    create_post('Ehi is awesome', '''Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam''', "Sam")
