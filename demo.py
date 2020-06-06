"""
Created on Sat Jun 6 

@author: koeifans
"""

from main import User
from superuser import SuperUser

def main():

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

    superuser = SuperUser('jon', 'password', 'jon@some.com', '12/24/1999', 'admin')

    print(superuser)
    print()
    print(repr(superuser))

    print('ran demo.main')

if __name__ == '__main__':
    main()