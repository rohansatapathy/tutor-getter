from timeslot import TimeSlot
from session import Session


class Person:
    """Store information about a person"""

    def __init__(self, first, last, email, grade):
        """Initialize the person
        
        Store name, email and grade information for
        a person in the tutor system.

        Params:
        first (str) - first name of the person
        last (str) - last name of the person
        email (str) - person's email
        grade(int) - person's grade level, must 
            be from 1-12

        Returns: Person
        """
        self.first_name = first
        self.last_name = last
        self.email = email
        self.grade = grade

    def __repr__(self):
        """Return string representation of the person"""
        return f"<Person {self.first_name.title()} {self.last_name.title}>"

    def __str__(self):
        """Return person's name"""
        return f"{self.first_name.title()} {self.last_name.title()}"
    
    def get_contact_info(self):
        """Return email as contact info"""
        return f"Contact {self} at {self.email}"


class Tutor(Person):
    """Class to store and change tutor information
    
    This class stores information about tutors and 
    contains methods that allows the tutor to change
    their time slots. 

    Attributes:
        first_name (str)
        last_name (str)
        email (str)
        grade (int) - grade level for tutor (must be 
            9 or above)
        timeslots (list) - list of available time
            slots, each item must be of the type
            TimeSlot.
    
    """

    def __init__(self, first, last, email, grade):
        """Initialize the tutor object
        
        Store name, email and grade information for
        a tutor in the system.

        Params:
        first (str) - first name of the tutor
        last (str) - last name of the tutor
        email (str) - tutor's email
        grade(int) - tutor's grade level, must 
            be from 1-12

        Returns: Tutor
        """
        super().__init__(first, last, email, grade)
        # Add sessions later
        self.sessions = []

    def __repr__(self):
        """Return string representation of the object"""
        return f"<Tutor {self.first_name.title()} {self.last_name.title}>"

    def add_session(self, timeslot):
        """Add a session to the list with the given timeslot"""
        new_session = Session(self, timeslot)
        self.sessions.append(new_session)

    def remove_session(self, session):
        """Remove the session from the list"""
        pass
        


class Student(Person):
    """A class to hold student information

    Attributes:
        first_name (str)
        last_name (str)
        email (str)
        grade (int) - must be a value from
            1 to 8, high schoolers are not
            guaranteed help since they are
            the same level as the tutors
    """

    def __init__(self, first, last, email, grade):
        """Initialize the tutor object
        
        Store name, email and grade information for
        a student in the system.

        Params:
        first (str) - first name of the tutor
        last (str) - last name of the tutor
        email (str) - student's email
        grade(int) - student's grade level, must 
            be from 1-12

        Returns: Student
        """
        super().__init__(first, last, email, grade)
        self.sessions = []

    def book_session(self, session):
        """Set student attribute in given session and add to our list"""
        if session.student is None and not session.is_complete():
            session.student = self
            self.sessions.append(session)
        else:
            print("This session is already booked.")

    def unbook_session(self, session):
        """Remove student attribute from session

        Before removing attribute, also makes sure that
        the student does not clear a session that is not
        theirs
        """
        if session.student == self and session in self.sessions and not session.is_complete():
            confirm = input("Are you sure you want to unbook this session? (y/n) ")
            if confirm.lower().startswith("y"):
                session.student = None
        else:
            print("You can't unbook this session.")
