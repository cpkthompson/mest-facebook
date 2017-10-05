from post import Post, Author
# from user import User
# from fb_page import create_page
import csv
import os

def create_post(content, firstname="Anonymous"):
    '''User can create a post'''
    p = Post(firstname, content)
    p.save()
    print('Post created')

def display_posts(firstname):
    '''This displays users posts'''
    d = Post(firstname)
    d.show_all_posts(firstname)

def update_bio(bio_details, firstname='charles'):
    '''User can update their bio'''
    mybio = open('user.csv', 'r')
    read_user = csv.DictReader(mybio)
    for line in read_user:
        if line['firstname'] == firstname:
            line['bio'] = bio_details
            print('Success')

def create_pg():
    '''User can create a facebook page'''
    # fb_page.create_page()
    pass


if __name__ == '__main__':

    # This displays the users post. This function is called first in this class
    display_posts('charles')

    #We are asking the user what they want to do
    quit = True
    while quit:
        choice = input(" 1. to Create Post\n 2. to Update Bio\n 3. to Create a Page\n 4. to logout")
        if choice == '1':
            # This lets user creates a posts
            content = str(input('Enter post: '))
            create_post(content)

        elif choice=='2':
            # This let's the user update bio
            bio_details = input("What\'s your fun facts?: ")
            update_bio(bio_details)

        elif choice == '3':
            #This lets user create page
            create_pg()

        elif choice == '4':
            #This logs the user out of the application
            quit = False



