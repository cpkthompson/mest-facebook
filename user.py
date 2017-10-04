import csv
import os


class User:
    def __init__(self, firstname='', lastname='', email='', password='', birthday='', gender=''):

        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        self.birthday = birthday
        self.gender = gender

    def save_to_csv(self):

        # create a csv file that contains users content
        file_exist = os.path.isfile('user.csv')
        with open('user.csv', 'a') as csv_file:
            fieldnames = ['firstname', 'lastname', 'email', 'password', 'birthday', 'gender']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exist:
                writer.writeheader()
            writer.writerow(
                {'firstname': self.firstname, 'lastname': self.lastname, 'email': self.email, 'password': self.password,
                 'birthday': self.birthday, 'gender': self.gender})

    def verify_email(self):

        # reading the user details in the csv and spliting it to make a list to get index of email
        with open('user.csv', 'r') as csv_file:
            users = csv.DictReader(csv_file)

            for user in users:
                if self.email == user['email']:
                    return print("Sorry email already exist")

                else:
                    return 'Welcome {}'.format(self.firstname)



