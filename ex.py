#Classes for Exceptions
class DuplicateUsernameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class UnderAgeError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

#A class for User

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
my_contact_list = [
    ("rudebouy", "123@gmail.com", 26),
    ("lorreta", "jlor_@gmail.com", 24),
    ("marvin", "mav@hotmail.com", 15),
    ("_", "_ahg", 30),
    ("kevin", "kevin@yahoo.com", -1)
    ]

directory = {}

for username, email, age in my_contact_list:
    try:
        if username in directory:
            raise DuplicateUsernameError()
            
        if age < 0:
            raise InvalidAgeError()
            
        if age < 16:
            raise UnderAgeError()
            
        auth_email = email.split('@')
        if len(auth_email) != 2 or not auth_email[0] or not auth_email[1]:
            raise InvalidEmailError()
            
    except DuplicateUsernameError:
        print("Username '%s' is in use." % username)
        
    except InvalidAgeError:
        print("'%s' is only '%s' invalid years." % (username, age))
        
    except UnderAgeError:
        print("'%s' is only '%s' years old." % (username, age))
        
    except InvalidEmailError:
        print("'%s' is not a valid email." % email)
        
    else:
        directory[username] = User(username, email)