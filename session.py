from datetime import datetime


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
        subject (str) - subject to focus on
    """

    def __init__(self, tutor, timeslot):
        """Create the session"""
        self.tutor = tutor
        self.timeslot = timeslot

        # Add these later
        self.student = None
        self.subject = None

    def __repr__(self):
        """Return string representation of the session"""
        return f"<Session on {repr(self.timeslot)} with Tutor {self.tutor} and Student {self.student}>"

    def __str__(self):
        """Return pretty-printed session description"""
        return f"{self.timeslot} with {self.tutor}{f' and {self.student} on {self.subject}' if self.student and self.subject else ''}"

    def set_subject(self, subject):
        """Set the subject of the tutoring session"""
        if subject in self.tutor.subjects:
            self.subject = subject
        else:
            print("Sorry, this subject is not valid.")

    def remove_subject(self):
        """Remove the subject attribute and set it to None"""
        if not self.is_complete():
            self.subject = None

    def set_student(self, student):
        """Sets the student of the session"""
        if self.is_booked():
            print("Sorry, this session is already booked.")
        elif self.is_complete():
            print("Sorry, this session is over.")
        else:
            self.student = student

    def remove_student(self):
        """Remove the student attribute and set to None"""
        if not self.is_complete():
            self.student = None

    def is_booked(self):
        return self.student is not None

    def is_complete(self):
        """Return True if the session is in the past"""
        return self.timeslot.end_time < datetime.today()

