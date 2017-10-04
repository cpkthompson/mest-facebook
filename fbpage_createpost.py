import sign_up.py
import csv

class User:
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

    email = input("Enter Your Email")
    password = input("Enter Your Password")
    print("Verification In Progress")

        def verify_user(self, user):
            
            if self.email == SignUp(user.email)
                print("Welcome Page Admin")

            else:
                self.email != user.email
                print("Access Denied!!!")
    
    def create_post():

        return 'Whats on your mind'

    def save_to_csv(self):
        file_exist = os.path.isfile('saved_posts.csv')
        with open('saved_posts.csv', 'a') as csv_file:
            savedposts = ['postcontent', 'datecreated', 'likes', 'shares', 'reached']
            writer = csv.DictWriter(csv_file, savedposts=savedposts)

            if not file_exist:
                writer.writeheader()
            writer.writerow({'datecreated': , 'likes': , 'shares': , 'reached':})

            
    def edit_post():

        for savedposts in saved_posts.csv:
            return 'Edit Post'
    
    def delete_post():
        for savedposts in saved_posts.csv:
            return 'Delete Post'

Admin = User()

class Page(User):
    
    def __init__(self):
        pass

    def post_details(self, content):
        self.content = content
        
    
    def delete_post(self):
        pass
    
    def create_post():
        

class Page_Details:
    
    def __init__(self, content):
        self.content = content

class Users:

    def __init__(self):
        pass

    def like_or_dislike_page(self):
        
    
    def follow_page(self):
        pass
    
    def share_page(self):
        pass

