from post import Post, Author
# from user import User
# from fb_page import create_page

"""
- Update bio
- create post (Done)
- display posts (Done)
- call method to create page: 
- set photo
- create friends
- display friends
"""

def create_post(content, firstname="Anonymous"):
    p = Post(firstname, content)
    p.save()
    print('Post created')

def display_posts(firstname):
    d = Post(firstname)
    d.show_all_posts(firstname)

def bio(firstname):
    pass

def create_pg():
    pass


if __name__ == '__main__':

    # This creates the posts
    content = str(input('Enter post: '))
    create_post(content)

    #This displays the post based on the user's first name
    display_posts('charles')

    #This update bio

    # author = Author('Ehi Aig')
    # arthur.show_all_posts(arthur.email)

    # new_user = User()

    # new_post = Post(new_user.firstname, 'It\'s a good day')
    # new_post.save()
    # author = new_user.firstname



