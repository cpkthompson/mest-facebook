from post import Post, Author
# from user import User
# from fb_page import create_page
import csv
import os

"""
- Update bio (Done)
- create post (Done)
- display posts (Done)
- call method to create page (Done)
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
    file_exist = os.path.isfile('posts.csv')
    with open('posts.csv', 'a') as my_file:
        fieldnames = ['bio']
        writer = csv.DictWriter(my_file, fieldnames=fieldnames)

        if not file_exist:
            writer.writeheader()
        writer.writerow({'bio': firstname})


    with open('user.csv', 'r') as file:
        # nw_user = input('Supply username: ')
        reader = csv.DictReader(file)
        for pr in reader:
            if pr['firstname'] == firstname:
                choice = input(
                    ' a to update first name\n b to update last name \n c to update bio d. update date of birth\n e to update password').lower()
                if choice == 'a':
                    new_firstname = input('Supply new first name: ')
                    pr['first name'] = new_firstname
                    print("--- Your First Name is now " + str(pr['first name']))
                elif choice == 'b':
                    new_lastname = input('Supply new last name: ')
                    pr['last name'] = new_lastname
                    print("--- Your Last Name is now " + str(pr['last name']))
                elif choice == 'c':
                    new_bio = input('Supply new bio: ')
                    pr['bio'] = new_bio
                    print("Bio updated successfully")
                elif choice == 'd':
                    new_dob = input('Supply new date of birth: ')
                    pr['date_of_birth'] = new_dob
                    print("--- Your Date-of-Birth is now " + str(pr['last name']))
                elif choice == 'e':
                    new_password = input('Supply new password: ')
                    pr['password'] = new_password
                    print('Password changed successfully')
            else:
                print('That username does not exist in our record ')

    pass

def create_pg():
    # fb_page.create_page()
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



