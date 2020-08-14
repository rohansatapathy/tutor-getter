from datetime import datetime

from person import Tutor, Student
from timeslot import TimeSlot


class Session():
    """A class to handle tutoring sessions

    This class is created when a student
    decides to book a session with a tutor. 
    It stores all the relevant information
    about the session, including the student, 
    tutor, and timeslot. 
    
    Attributes:
        student (Student) - the student of the 1-on-1 session
        tutor (Tutor) - the tutor of the session
        timeslot (TimeSlot) - when the session takes place

    """

    def __init__(self, tutor, timeslot):
        """Create the session"""
        self.tutor = tutor
        self.timeslot = timeslot
        self.student = None  # Student is to be added later

    def __repr__(self):
        """Return string representation of the session"""
        return f"<Session at {repr(timeslot)} with Tutor {tutor} and Student {student}>"

    def __str__(self):
        """Return pretty-printed session description"""
        

    def is_booked(self):
        return self.student is not None

    def is_complete(self):
        """Return True if the session is in the past"""
        return self.timeslot.end_time < datetime.today()

