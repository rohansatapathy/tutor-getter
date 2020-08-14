# demos.py - examples for how the classes work together
# Usage: python3 demos.py [student/tutor]
# The arguments determine which example runs


import sys

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
            choose from

    Returns:
        str
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


def run_student_demo():
    """Run the demo from the student's POV"""
    pass


def run_tutor_demo():
    """Run the demo from the tutor's POV"""
    pass


if __name__ == "__main__":
    args = sys.argv
    if not sys.argv[1]:
        print("Usage: python3 demos.py [student/tutor]")
    elif sys.argv[1] not in ["student", "tutor"]:
        print("Usage: python3 demos.py [student/tutor]")
    elif sys.argv[1] == "student":
        run_student_demo()
    elif sys.argv[1] == "tutor":
        run_tutor_demo()
