"""
Created on Sat Jun 6 

@author: koeifans
"""

from main import User
from superuser import SuperUser

superuser = SuperUser('jon', 'password', 'jon@some.com', '12/24/1999')

print(superuser)
print()
print(repr(superuser))