import sys

class quit(object):

    def execute(self):
        confirm = raw_input("Are you sure you want to quit (Yes/No)? Make sure you save! ")  # Input for quit
        end = confirm.lower()  # Lowercases the string
        if end[0] == 'y':  # Checks that first letter is Y, if yes
            print "Thanks for playing!"
            sys.exit()