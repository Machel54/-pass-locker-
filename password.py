#/usr/bin/env python3.6
from user import User

def create_user(user_name,password):
    '''
    Function to create a new user
    '''
    new_user = User(user_name,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(name):
    '''
    Function that finds a user by name and returns the user
    '''
    return User.find_by_name(name)

def check_existing_users(name):
    '''
    Function that check if a user exists with that user and return a Boolean
    '''
    return User.user_exist(name)

def display_users():
    '''
    Function that returns all the saved user
    '''
    return User.display_user()
