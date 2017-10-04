import user
import sign_in
#This is for sign up and sign in


while True:
    register = int(input('Type 1 to sign up as a new user, 2 to sign in: '))

    if register == 1:
        firstname = input("Enter your firstname: ")
        lastname = input("Enter your lastname: ")
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        birthday = input("Enter your birthday: ")
        gender = input("Enter your gender: ")

        new_user = user.User(firstname, lastname, email, password, birthday, gender)
        print(new_user.verify_email())
        new_user.save_to_csv()

    elif register == 2:

        email = input("Enter your email: ")
        password = input("Enter your password: ")

        old_user = sign_in.SignIn(email, password)
        print(old_user.verify_sign_in())



    else:
        print("End here")
        break
