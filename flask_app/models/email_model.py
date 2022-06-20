import re
from unittest import result
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:
    def __init__( self , data ):
        self.id = data['id']
        self.email_address = data['email_address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create_one(cls,data):
        query = "INSERT INTO emails(email_address) VALUES (%(email_address)s) "

        return connectToMySQL('emails_schema').query_db(query,data)

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM emails WHERE email_address=%(email_address)s;"
        return connectToMySQL('emails_schema').query_db(query,data)



    @classmethod
    def get_all(cls):
        query ="SELECT * FROM emails;"
        result = connectToMySQL('emails_schema').query_db(query)
        print(result)

        all_emails = []
        for row in result:
            all_emails.append(cls(row))
        return all_emails

    @staticmethod
    def validate(email):
        is_valid = True
        if Email.get_one(email):
            flash("This email is already taken")
            is_valid = False
        if not EMAIL_REGEX.match(email['email_address']):
            flash("Invalid email address")
            is_valid = False
        return is_valid