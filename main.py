"""
Created on Sat Jun 6 

@author: koeifans
"""

import datetime as dt
import dateutil.parser
import hashlib

class User:
    def __init__(self, username=None, password=None,
                email=None, birthday=None):
        self._username = username
        self.password = self._encrypt_password(password)
        self.email = email
        self.birthday = birthday

    def __str__(self):
        age = self.get_age()
        return f"Username: {self.username}\nPassword: {self.password}\nEmail: {self.email}\nAge: {age}"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"
    
    def __eq__(self, other):
        return self.username == other.username

    def _encrypt_password(self, password):
        password = password.encode('utf-8')
        return hashlib.sha256(password).hexdigest()
    
    def check_password(self, password):
        password = self._encrypt_password(password)
        return password == self.password
    
    def get_age(self):
        b_day = dateutil.parser.parse(self.birthday)
        return int((dt.datetime.now() - b_day).days // 365)
    
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not username:
            raise Exception("Username cannot be empty.")
        else:
            self._username = username

user = User('John', 'password', 'john@some.come', '12/25/1999')
print(user.username)
print(user.password)
print(user)
print()
print(repr(user))

user2 = User("John", "password", "john@some.come", "12/25/1999")
print(user == user2)
print(user.check_password('1234'))

user.username = 'Jonathan'
print(user.username)

if __name__ == '__main__':
    main()