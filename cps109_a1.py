'''
Program description:
This program seeks to solve the issue of organizing, via a command line To Do List. The program offers functionalities for task management. Users can view, add, remove tasks, and change task statuses from pending to completed. Task details such as name, due date, priority, label, and status are stored in a text file named "tasks.txt". The view tasks option displays existing tasks in a table format. Colorfull text will be used to make it easier to read the comand line prompts
'''
import os
import colorama
from tabulate import tabulate

#Begin scanning for colorama front foreground and background functionality
colorama.init()

#Stores constant values for prgram state
CONST_START = 0
CONST_VEIW = 1
CONST_ADD_OR_REMOVE = 2
CONST_CHANGE_STATUS = 3
CONST_EXIT = 4

#Stores current state, set to start
global state
state = CONST_START

#Stores whether user has exited the program
isOn = True

#Stores all tasks from to do list
global tasks
name = []
date = []
priority = []
label = []
status = []

#Function clears screen
def clear():
  os.system('cls')

#Function welcomes user to program
def start():
  global state
  clear()

  #Display title
  print("-" * 25)
  print(colorama.Fore.BLUE + 'Welcome to the TO-DO List')
  print(colorama.Fore.RESET + "-" * 25)

  #Ask for input, until user enters valid input
  invalidInput = True

  while invalidInput:
    print(colorama.Fore.GREEN + "\nPress " + colorama.Fore.RED + "'1'" + colorama.Fore.GREEN + " to View Tasks \nPress " + colorama.Fore.RED + "'E'" + colorama.Fore.GREEN + " to Exit the program\n" + colorama.Fore.RESET)
    userInput = input()

    if userInput == '1':
      invalidInput = False
      #Set program state to view
      state = CONST_VEIW
    elif userInput == 'E' or userInput == 'e':
      invalidInput = False
      #Set program state to exit 
      state = CONST_EXIT
    else:
      clear()
      print("-" * 25)
      print(colorama.Fore.BLUE + 'Welcome to the TO-DO List')
      print(colorama.Fore.RESET + "-" * 25)
      print("\n" + colorama.Back.RED + "ERROR: Invalid Input. Try Again!" + colorama.Back.RESET)

#Function displays tasks in table format 
def veiw():
  global state
  global tasks
  global name

  #Display sub heading
  clear()
  print(colorama.Back.BLUE + colorama.Fore.YELLOW + "VEIW TASKS" + colorama.Back.RESET + colorama.Fore.RESET)

  #Reset all lists storing task details to avoid duplication 
  name.clear()
  date.clear()
  priority.clear()
  label.clear()
  status.clear()

  #Stores headers and formated tasks for outputing as table table
  headers = ["TASK", "DUE DATE", "PRIORITY", "LABEL", "STATUS", ""]
  formated_data = []

  #Access tasks file view tasks 
  try:
    f = open('tasks.txt', 'r')
    tasks = f.readlines()
    f.close()
  #Create tasks file if not found
  except FileNotFoundError:
    f = open("tasks.txt", 'x')
    print(colorama.Back.RED() + "\n\nTo Do List is empty, Add tasks to view" +
          colorama.Back.RESET)
    f.close()
    f = open('tasks.txt', 'w')
    #Add example data
    f.writelines("Test 1, 25, 11, 2023, High Priority, Family, Completed\nTest 2, 15, 01, 2024, Medium Priority, Recreational, Pending\nTest 3, 30, 12, 2023, Medium Priority, Work, Pending")
    f.close()

  #Check if tasks is empty
  if not tasks:
    print(colorama.Back.RED() + "\n\nTo Do List is empty, Add tasks to view" + colorama.Back.RESET)
  #If tasks isnt empty, format data and display
  else:
    for i in tasks:
      formated_data.append(i.strip().split(', '))
    for i in formated_data:
      if not i == "":
        name.append(i[0])
        date.append(str(i[1]) + ', ' + str(i[2]) + ', ' + str(i[3]))
        priority.append(i[4])
        label.append(i[5])
        status.append(i[6])

    table_data = list(zip(name, date, priority, label, status))
    print(tabulate(table_data, headers, tablefmt="grid"))

  #Ask user for further input
  invalidInput = True

  print(colorama.Fore.GREEN + "\nPress " + colorama.Fore.RED + "'1'" + colorama.Fore.GREEN + " to Add or Remove Tasks \nPress " + colorama.Fore.RED + "'2'" + colorama.Fore.GREEN + " to Change the Status of a Task" + "\nPress " + colorama.Fore.RED + "'3'" + colorama.Fore.GREEN + "to Return to Welcome Screen\n" + colorama.Fore.RESET)

  while invalidInput:
    userInput = input()

    if userInput == '1':
      invalidInput = False
      state = CONST_ADD_OR_REMOVE
    elif userInput == '2':
      invalidInput = False
      state = CONST_CHANGE_STATUS
    elif userInput == '3':
      invalidInput = False
      state = CONST_START
    else:
      clear()
      print(colorama.Back.BLUE + colorama.Fore.YELLOW + "VEIW TASKS" + colorama.Back.RESET + colorama.Fore.RESET)
      print(tabulate(formated_data, headers, tablefmt="grid"))
      print(colorama.Back.RED + "ERROR: Invalid Input. Try Again!\n" + colorama.Back.RESET + colorama.Fore.GREEN + "\nPress " + colorama.Fore.RED + "'1'" + colorama.Fore.GREEN + " to Add or Remove Tasks \nPress " + colorama.Fore.RED + "'2'" + colorama.Fore.GREEN + " to Change the Status of a Task" + "\nPress " + colorama.Fore.RED + "'3'" + colorama.Fore.GREEN + "to Return to Welcome Screen\n" + colorama.Fore.RESET)

#Function enters add or remove state, providing user with options 1)add or 2)remove 
def addOrRemove():
  global state

  clear() 
  print(colorama.Back.BLUE + colorama.Fore.YELLOW + "ADD OR REMOVE TASKS" + colorama.Back.RESET + colorama.Fore.RESET)
  print(colorama.Fore.GREEN + "\nPress " + colorama.Fore.RED + "'1'" + colorama.Fore.GREEN + " to Add a Task \nPress " + colorama.Fore.RED + "'2'" + colorama.Fore.GREEN + " to Remove a Task\n" + "Press " + colorama.Fore.RED + "'3'" + colorama.Fore.GREEN + "to Return to Welcome Screen\n" + colorama.Fore.RESET)

  invalidInput = True

  while invalidInput:
    userInput = input()

    if userInput == '1':
      clear()
      invalidInput = False
      add()
    elif userInput == '2':
      clear()
      invalidInput = False
      remove()
    elif userInput == '3':
      clear()
      invalidInput = False
      state = CONST_VEIW
    else:
      clear()
      print(colorama.Back.BLUE + "ADD OR REMOVE TASKS" + colorama.Back.RESET + colorama.Fore.RESET)
      print(colorama.Fore.GREEN + "\nPress " + colorama.Fore.RED + "'1'" + colorama.Fore.GREEN + " to Add a Task \nPress " + colorama.Fore.RED + "'2'" + colorama.Fore.GREEN + " to Remove a Task\n" + "Press " + colorama.Fore.RED + "'3'" + colorama.Fore.GREEN + "to Return to Welcome Screen\n" + colorama.Fore.RESET)
      print(colorama.Back.RED + "ERROR: Invalid Input. Try Again!" + colorama.Back.RESET)

#Function adds task to to do list
def add():
  global state

  print(colorama.Back.BLUE + colorama.Fore.YELLOW + "ADD TASKS" + colorama.Back.RESET + colorama.Fore.RESET)
  print(colorama.Fore.GREEN + "\nEnter Task Name" + colorama.Fore.RESET)
  addName = input()

  print(colorama.Fore.GREEN +
        "\nEnter to Due Date - Day (must be 2 digit number (00,01,02))" + colorama.Fore.RESET)

  invalidInput = True

  while invalidInput:
    userInput = input()

    if userInput.isdigit():
      if int(userInput) <= 31:
        invalidInput = False
        addDay = userInput
    else:
      print(colorama.Back.RED + "ERROR: Invalid Input. Try Again!" + colorama.Back.RESET)

  print(colorama.Fore.GREEN +
        "\nEnter to Due Date - Month (must be 2 digit number (00,01,02))" + colorama.Fore.RESET)

  invalidInput = True

  while invalidInput:
    userInput = input()

    if userInput.isdigit():
      if int(userInput) <= 12:
        invalidInput = False
        addMonth = userInput
    else:
      print(colorama.Back.RED + "ERROR: Invalid Input. Try Again!" + colorama.Back.RESET)

  print(colorama.Fore.GREEN +
        "\nEnter to Due Date - Year (must be 4 digit number after 2022)" + colorama.Fore.RESET)

  invalidInput = True

  while invalidInput:
    userInput = input()

    if userInput.isdigit() and len(str(userInput)) >= 4:
      if int(userInput) >= 2023:
        invalidInput = False
        addYear = userInput
    else:
      print(colorama.Back.RED + "ERROR: Invalid Input. Try Again!" + colorama.Back.RESET)

  print(colorama.Fore.GREEN + "\nSelect " + colorama.Fore.RED + "'1'" + colorama.Fore.GREEN + " to Seclect Low Priority" + colorama.Fore.RESET)
  print(colorama.Fore.GREEN + "Select " + colorama.Fore.RED + "'2'" + colorama.Fore.GREEN + " to Seclect Medium Priority" + colorama.Fore.RESET)
  print(colorama.Fore.GREEN + "Select " + colorama.Fore.RED + "'3'" + colorama.Fore.GREEN + " to Seclect High Priority" + colorama.Fore.RESET)

  invalidInput = True

  while invalidInput:
    userInput = input()

    if userInput == '1':
      addPriority = "Low Priority"
      invalidInput = False
    elif userInput == '2':
      addPriority = "Medium Priority"
      invalidInput = False
    elif userInput == '3':
      addPriority = "High Priority"
      invalidInput = False
    else:
      print(colorama.Back.RED + "ERROR: Invalid Input. Try Again!" + colorama.Back.RESET + "\n")

  print(colorama.Fore.GREEN + "\nSelect " + colorama.Fore.RED + "'1'" + colorama.Fore.GREEN + " to Label as Work " + colorama.Fore.RESET)
  print(colorama.Fore.GREEN + "Select " + colorama.Fore.RED + "'2'" + colorama.Fore.GREEN + " to label as Recreational" + colorama.Fore.RESET)
  print(colorama.Fore.GREEN + "Select " + colorama.Fore.RED + "'3'" + colorama.Fore.GREEN + " to label as Family" + colorama.Fore.RESET)

  invalidInput = True

  while invalidInput:
    userInput = input()

    if userInput == '1':
      addLabel = "Work"
      invalidInput = False
    elif userInput == '2':
      addLabel = "Recreational"
      invalidInput = False
    elif userInput == '3':
      addLabel = "Family"
      invalidInput = False
    else:
      print(colorama.Back.RED + "ERROR: Invalid Input. Try Again!\n" + colorama.Back.RESET)

  try:
    f = open('tasks.txt', 'a')
    f.writelines(addName + ", " + addDay + ", " + addMonth + ", " + addYear + ", " + addPriority + ", " + addLabel + ", " + "Pending" + "\n")
    f.close()

  except FileNotFoundError:
    f = open("tasks.txt", 'x')
    f.close()

    f = open('tasks.txt', 'a')
    f.writelines(addName + ", " + addDay + ", " + addMonth + ", " + addYear + ", " + addPriority + ", " + addLabel + ", " + "Pending" + "\n")
    f.close()

  state = CONST_VEIW

#Function removes a task from the list
def remove():
  global name
  global tasks
  global state

  print(colorama.Back.BLUE + "REMOVE TASKS" + colorama.Back.RESET + colorama.Fore.RESET)

  x = 0
  print(colorama.Fore.GREEN + "Enter the corresponding " + colorama.Fore.RED + "number (0,1,2...)" + colorama.Fore.GREEN +
        " for the Task you want to Remove\n" + colorama.Fore.RESET)
  for i in name:
    print(colorama.Fore.RED + str(x) + colorama.Fore.RESET + ". " + i)
    x += 1

  invalidInput = True

  while invalidInput:
    userInput = input()

    try:
      if int(userInput) <= len(name):
        f = open("tasks.txt", "w")

        for i in range(len(tasks)):
          if not (name[i] == name[int(userInput)]):
            f.writelines(tasks[i])
        f.close()

        invalidInput = False
      else:
        clear()
        print(colorama.Back.BLUE + "REMOVE TASKS" + colorama.Back.RESET + colorama.Fore.RESET)

        x = 0
        print(colorama.Fore.GREEN + "Enter the corresponding " +
              colorama.Fore.RED + "number (0,1,2...)" + colorama.Fore.GREEN + " for the Task you want to Remove\n" + colorama.Fore.RESET)
        for i in name:
          print(colorama.Fore.RED + str(x) + colorama.Fore.RESET + ". " + i)
          x += 1
        print("\n" + colorama.Back.RED + "ERROR: Invalid Input. Try Again!" + colorama.Back.RESET)
    except:
      clear()
      print(colorama.Back.BLUE + "REMOVE TASKS" + colorama.Back.RESET + colorama.Fore.RESET)

      x = 0
      print(colorama.Fore.GREEN + "Enter the corresponding " +
            colorama.Fore.RED + "number (0,1,2...)" + colorama.Fore.GREEN + " for the Task you want to Remove\n" + colorama.Fore.RESET)
      for i in name:
        print(colorama.Fore.RED + str(x) + colorama.Fore.RESET + ". " + i)
        x += 1
      print("\n" + colorama.Back.RED + "ERROR: Invalid Input. Try Again!" + colorama.Back.RESET)

  state = CONST_VEIW

#Function changes the status of a pending task to completed
def changeStatus():
  global tasks
  global name
  global status
  global state

  clear()
  print(colorama.Back.BLUE + "MARK TASK AS COMPLETED" + colorama.Back.RESET + colorama.Fore.RESET)

  x = 0
  xlist = []
  print(colorama.Fore.GREEN +
        "The Following are your PENDING Tasks \nEnter the corresponding " + colorama.Fore.RED + "number (0,1,2...)" + colorama.Fore.GREEN + " for the Task you want to mark as Done\n" + colorama.Fore.RESET)

  for i in name:
    if "Pending" in tasks[x]:
      print(colorama.Fore.RED + str(x) + colorama.Fore.RESET + ". " + i)
      xlist.append(x)
    x += 1

  if len(xlist) > 0:
    invalidInput = True

    while invalidInput:
      userInput = input()

      try:
        if int(userInput) in xlist:
          task_index = int(userInput)
          status[task_index] = "Completed"
          try:
            f = open('tasks.txt', 'w')
            for i in range(len(tasks)):
              f.writelines(name[i] + ", " + date[i] + ", " + priority[i] + ", " + label[i] + ", " + status[i] + "\n")
            f.close()

          except FileNotFoundError:
            f = open("tasks.txt", 'x')
            f.close()

            f = open('tasks.txt', 'a')
            f.writelines(name[i] + ", " + date[i] + ", " + priority[i] + ", " + label[i] + ", " + status[i] + "\n")
            f.close()

          invalidInput = False

      except:
        print(colorama.Back.RED + "ERROR: Invalid Input. Try Again!\n" + colorama.Back.RESET)

  state = CONST_VEIW

#Loop through program until user exits
while isOn:
  if state == CONST_START:
    start()
  if state == CONST_VEIW:
    veiw()
  if state == CONST_ADD_OR_REMOVE:
    addOrRemove()
  if state == CONST_CHANGE_STATUS:
    changeStatus()
  elif state == CONST_EXIT:
    exit()