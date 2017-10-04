import csv
import os
import re

class Newfeed:
    def __init__(self):
        self.show_posts()

    def show_posts(self):
        with open("posts.csv", 'r') as file:
            reader = csv.DictReader(file)
            for post_obj in reader:

                index = post_obj['index']
                name = post_obj['user']
                post = post_obj['post']
                print("{}. {} posted: {}".format(index, name, post))
            self.show_post_detail()

    def show_post_detail(self):
        post_index = int(input("Enter index: "))

        with open("posts.csv", 'r') as file:
            reader = csv.DictReader(file)
            for post_obj in reader:
                if post_index == int(post_obj['index']):
                    print(post_obj['post'])

        post_action = int(input("Enter 1 to like posts and 2 to comment: "))

        if post_action == 1:
            print("Post liked")
        elif post_action == 2:
            comment = input("Enter comment: ")
            print("Your comment has been posted")

    
if __name__ == '__main__':
    new_feed = Newfeed()