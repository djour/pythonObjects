"""
Created on Sat Jun 6 

@author: koeifans
"""

from main import User

class SuperUser(User):
    
    def __init__(self, username, password, email, birthday, role=None):
        self.role = role
        super().__init__(username, password, email, birthday)

    def __str__(self):
        return super().__str__() + f"\nRole: {self.role}"

if __name__ == '__main__':
    main()