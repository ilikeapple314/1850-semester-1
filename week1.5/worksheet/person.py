# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)

    def __init__(self, name, birth):
        """
        Initializes a person
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        elif (name == ""):
            raise ValueError("Name must not be empty.")
        elif not isinstance(birth, date):
                    raise TypeError("Birth must be a date.")
        else:
              self.name = name
              self.birth = birth

        

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)

    def initials(self):
        """
        Finds the initials of the persons name
        """
        initials = ""
        cappedName = (self.name.lower()).title()
        cappedNameList = list(cappedName) 
        for letter in cappedNameList:
             if letter.isupper() == True:
                  initials = initials + letter

        return initials

    def is_birthday(self):
        """
        Checks if it is persons birthday
        """
        today = date.today()
        if ((self.birth.day == today.day) and (self.birth.month == today.month)):
             return True
        else:
             return False

