from datetime import datetime


class TimeSlot:
    """A class to handle information about
    a tutor's time slot. 

    Attributes:
        start_time (datetime) - the starting time
            of the tutoring session
        end_time (datetime) - the ending time of
            the tutoring session

    """
    
    def __init__(self, start_time, end_time):
        """Create a TimeSlot object"""
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        """Return full string representation of time slot"""
        start_str = self.start_time.strftime("%b %d, %Y %H:%M:%S %p")
        end_str = self.end_time.strftime("%b %d, %Y %H:%M:%S %p")
        return f"<TimeSlot {start_str} - {end_str}>"

    def __str__(self):
        """Return string representation of time slot"""
        start_str = self.start_time.strftime("%b %d %H:%M %p")
        end_str = self.end_time.strftime("%H:%M %p")
        return f"{start_str} - {end_str}"
