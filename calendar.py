"""Simple command line calendar that allows you to view, add events, update events and delete events."""

from time import sleep, strftime

NAME = "Edward"

calendar = {}

def welcome():
  print "Welcome to PyCal" + NAME + "."
  print "The calendar is now loading..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print "The time is: " + strftime("%I:%M:%S")
  sleep(1)
  print "What would you like to do?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Please enter A to Add, U to Update, V to View, D to Delete and X to Exit: ")
    user_choice = user_choice.upper()

    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "Your calendar is empty"
      else:
        print calendar

    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Your update was successfull!"
      print calendar

    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "Unfortunately that is an invalid date"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Your event was successfully added!"
        print calendar

    elif user_choice == "D":
      if (len(calendar.keys()) < 1):
        print "The calender is empty"
      else:
        event = raw_input("What event would you like to delete?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print "That event was successfully deleted"
            print calendar
          else:
            print "Im sorry that event is not in your calendar"

    elif user_choice == "X":
      start = False

    else:
      print "Im sorry that is not a valid command"
      start = False

start_calendar()



     
