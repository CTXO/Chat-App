# Chat-App
Project made in Django 

## Description
The project is a simulation of an instant messaging app. 
A simple schema was created to store the users, the messages and the relationships between them.

Right now, there are 8 requests availlabe:
1. Create Account
2. Show Users
3. Show Contacts (the contacts of a specific user)
4. Read Chat (One user sees their messages with another and visualize them)
5. Send Message
6. Add Contact
7. Delete Contact
8. Delete User

In the future there will be a web and mobile interface using React and React Native.

## Pre-Requisites
- Python 3 (3.9 or newer)
- Pipenv

- MySQL Server (or MariaDB)
- An empty database 



## Instalation
```bash
pip install pipenv
git clone https://github.com/CTXO/Chat-App.git
cd Chat-App
pipenv shell
pipenv update
```


## How to Use the API
### Connecting the database
Go to chat_backend/settings.py and change the following code:
```code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DBname',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
Change the fields 'myuser' and 'mypassword' to your user and password in MySQL server.
Change the field 'DBname' to the name of the database that you will connect to the application.
 
### Migrating the Database
On the terminal with the virtual environment active, run the following commands
``` bash
python3 manage.py makemigrations ## It might be only python instead of python3, depending on the computer
python3 manage.py migrate
```

### Making the API requests

First, run the server in the virtual environment with the command
``` bash
python3 manage.py runserver
```

It is recommended to use [insomnia](https://insomnia.rest/download) for this.
Just create a request collection and import the data from the json file inside the assets folder
and you will have all the requests available.

You can start by creating some accounts and send messages bewtween the accounts.



## TODO
- Web and Mobile interfaces



## What Can Be Improved
- Create an API request to delete messages
- Create unit tests
- Encrypt messages
- Make email field unique in the ChatUser model
- Refactor code
- Separate Model from helper methods



## What I have learned
- [Django](https://docs.djangoproject.com/en/3.2/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [Password Hashing and Salts](https://auth0.com/blog/hashing-passwords-one-way-road-to-security/)
- [REST API](https://restfulapi.net/)
- [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)
- [Entity Relationships](https://www.smartdraw.com/entity-relationship-diagram/)
