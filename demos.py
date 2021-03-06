# demos.py - examples for how the classes work together
# Usage: python3 demos.py [student/tutor]
# The arguments determine which example runs


import sys
from datetime import datetime

from session import Session
from timeslot import TimeSlot
from person import Tutor, Student


def get_option(options, title="Select an option: "):
    """Get user's selection from a list of options

    Given a list of options, display each with numbers 
    next to them and allow the user to pick one of
    the options. Return the string of the option that
    the user picks. 

    Arguments:
        title (str) - title to be displayed at 
            the top of the list
        options (list) - list of options to 
            choose from, can be any object with 
            __str__ method

    Returns:
        object
    """
    print("\n" + title)
    for i in range(1, len(options) + 1):
        option = options[i - 1]
        print(f'{i}. {option}')
    while True:
        ans = input(f"Enter a number from 1 to {len(options)}: ")
        if ans.isdigit():
            if int(ans) <= len(options) and int(ans) >= 1:
                return options[int(ans) - 1]


def get_all_subjects(tutors):
    """Gets a list of subjects taught by tutors"""
    subjects = []
    for tutor in tutors:
        for subject in tutor.subjects:
            if subject not in subjects:
                subjects.append(subject)
    return subjects


def get_subject_sessions(tutors, subject):
    """Searches tutors with the appropriate subject for time slots available"""
    sessions = []
    for tutor in tutors:
        if subject in tutor.subjects:
            for session in tutor.sessions:
                if not session.is_booked() and not session.is_complete():
                    sessions.append(session)
    return sessions


def run_student_demo():
    """Run the demo from the student's POV"""
    # Create some fake tutors for the student to see
    t1 = Tutor("Brody", "Wilks", "brody@example.com", 10, ["Math", "Science"])
    t2 = Tutor("Mary", "Hagan", "mary@example.com", 12, ["English"])
    t3 = Tutor("Ray", "Maxwell", "ray@example.com", 13, ["English", "History", "Science"])
    tutors = [t1, t2, t3]

    # Create some fake time slots
    timeslots = []
    for start_hour in range(16, 20):
        ts_start = datetime(2020, 9, 1, start_hour, 0, 0)
        ts_end = datetime(2020, 9, 1, start_hour+1, 0, 0)
        timeslots.append(TimeSlot(ts_start, ts_end))

    # Add fake timeslots to the tutors
    for ts in timeslots:            # Tutor is free for all time slots
        tutors[0].add_session(ts)
    for ts in timeslots[:2]:        # Tutor is available for first two slots
        tutors[1].add_session(ts)
    for ts in timeslots[1:]:        # Tutor is available for last three
        tutors[2].add_session(ts)

    # Create fake student for demo
    student = Student("Test", "Student", "teststudent@example.com", 5)

    # Define the various menus the student will see
    action_menu = [
        "Upcoming Sessions", 
        "Book Session", 
        "Unbook Session", 
        "Exit"
    ]
    while True:
        action = get_option(action_menu)
        if action == action_menu[0]:
            # Display all sessions
            if student.get_upcoming_sessions():
                print("\nYour Upcoming Sessions: ")
                for session in student.get_upcoming_sessions():
                    print(session)
            else:
                print("\nYou have no sessions. Select 'Book Session' to get started.")
        elif action == action_menu[1]:
            # Student wants to book a session
            # Get all the info
            subject = get_option(get_all_subjects(tutors), title="What subject are you struggling with? ")
            sessions = get_subject_sessions(tutors, subject)
            session = get_option(sessions, title="Select a session: ")
            # Add student and subject to the  the session
            student.book_session(session, subject)
            # Get confirmation
            print(f"You are about to book {session}. ")
            confirm = input("Confirm? (y/n) ").lower().startswith("y")
            if confirm:
                print(f"Success! {session.tutor.get_contact_info()}.")
            else:
                print("Booking canceled.")
                student.unbook_session(session)
        elif action == action_menu[2]:
            # Student wants to unbook a session
            session = get_option(student.get_upcoming_sessions(), title="Which session would you like to unbook?")
            student.unbook_session(session)
        elif action == action_menu[3]:
            # Program is finished
            sys.exit()


def run_tutor_demo():
    """Run the demo from the tutor's POV"""
    # Create the tutor and some fake data
    tutor = Tutor("Test", "Tutor", "testtutor@example.com", 13, ["Math", "Science"])

    # Create some fake time slots
    timeslots = []
    for start_hour in range(16, 20):
        ts_start = datetime(2020, 9, 1, start_hour, 0, 0)
        ts_end = datetime(2020, 9, 1, start_hour+1, 0, 0)
        timeslots.append(TimeSlot(ts_start, ts_end))

    # Add the time slots to the tutor (as an example, this would be empty at first)
    for ts in timeslots:
        tutor.add_session(ts)

    # Fill some of the time slots (as an example, this would be empty at first)
    students = [Student("Ryan", "Choi", "ryan@example.com", 5), Student("Eliza", "Knox", "eliza@example.com", 7)]
    students[0].book_session(tutor.sessions[0], "Science")
    students[1].book_session(tutor.sessions[3], "Math")

    # Define the menus
    actions_menu = [
        "Add Session", 
        "Remove Session", 
        "See Booked Sessions", 
        "See Free Sessions", 
        "Exit"
    ]
    while True:
        action = get_option(actions_menu)
        if action == actions_menu[0]:
            # Add a session
            # Ask for data about the session
            session_data = {}
            for data in ["year", "month", "day", "hour", "minute"]:
                ans = ""
                while not ans.isdigit():
                    ans = input(f"Enter session {data}: ")
                session_data[data] = int(ans)

            # Create the datetime objects and timeslot
            start = datetime(
                session_data["year"], 
                session_data["month"], 
                session_data["day"], 
                session_data["hour"], 
                session_data["minute"]
            )
            end = datetime(
                session_data["year"], 
                session_data["month"], 
                session_data["day"], 
                session_data["hour"]+1, 
                session_data["minute"]
            )
            timeslot = TimeSlot(start, end)

            # Get conformation, then create the session
            session = Session(tutor, timeslot)  # Throwaway session
            confirm = input(f"You are about to create {session}.\nConfirm? (y/n) ").lower().startswith("y")
            if confirm:
                tutor.add_session(timeslot)
                print("Success!")
            else:
                print("No session created.")
        elif action == actions_menu[1]:
            # Remove a session
            session = get_option(tutor.get_free_sessions(), title="Which session would you like to remove?")
            # Confirmation
            confirm = input(f"You are about to delete {session}.\nConfirm? (y/n) ").lower().startswith("y")
            if confirm:
                tutor.remove_session(session)
                print("Session removed.")
            else:
                print("No session removed.")
        elif action == actions_menu[2]:
            # See booked sessions
            print("\nYour booked sessions:")
            for session in tutor.get_booked_sessions():
                print(session)
        elif action == actions_menu[3]:
            # See unbooked sessions
            print("\nYour unbooked sessions: ")
            for session in tutor.get_free_sessions():
                print(session)
        elif action == actions_menu[4]:
            sys.exit()


if __name__ == "__main__":
    args = sys.argv
    if len(sys.argv) < 2:
        print("Usage: python3 demos.py [student/tutor]")
    elif sys.argv[1] not in ["student", "tutor"]:
        print("Usage: python3 demos.py [student/tutor]")
    elif sys.argv[1] == "student":
        run_student_demo()
    elif sys.argv[1] == "tutor":
        run_tutor_demo()
