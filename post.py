# import user
import csv
import os

class Post:

    def __init__(self,  firstname, content=""):
        self.firstname = firstname
        self.content = content


    def save(self):
        file_exist = os.path.isfile('posts.csv')
        with open('posts.csv', 'a') as my_file:
            fieldnames = ['username', 'content']
            writer = csv.DictWriter(my_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow({'username': self.firstname, 'content': self.content})

    def show_all_posts(self, firstname):
        post = open('posts.csv', 'r')
        post_reader =  csv.DictReader(post)
        for line in post_reader:
            #print(line)
            if firstname in line.values():
                print (line)

class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name