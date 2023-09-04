import pyrebase

config = {
    'apiKey': "AIzaSyCICIwdzx1n1WdtLjifv6FBeuc74x4u3aU",
    'authDomain': "firstproject-1e6a8.firebaseapp.com",
    'projectId': "firstproject-1e6a8", 
    'storageBucket': "firstproject-1e6a8.appspot.com", 
    'messagingSenderId': "340435566363", 
    'appId': "1:340435566363:web:6984bd5e30ff35df5d5dbe", 
    'measurementId': "G-3WHWD7QLNX",
    'databaseURL': ''
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()

#Login function

def login():
    print("Log in...")
    email=input("Enter email: ")
    password=input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
        # print(auth.get_account_info(login['idToken']))
       # email = auth.get_account_info(login['idToken'])['users'][0]['email']
       # print(email)
    except:
        print("Invalid email or password")
    return

#Signup Function

def signup():
    print("Sign up...")
    email = input("Enter email: ")
    password=input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        ask=input("Do you want to login?[y/n]")
        if ask=='y':
            login()
    except: 
        print("Email already exists")
    return

#Main

ans=input("Are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()
