import sys
import os

from executive.actions.models import Action
sys.path.append(os.getcwd())
from peewee import SqliteDatabase
import pyfiglet
from actions.decide import DecisionMaker
from actions.done import CompleteAction
from actions.add import AddAction
from actions.assign import AssignAction
from actions.schedule import ScheduleAction
from actions.models import Project
from actions.sql import RawSQL
'''
Main method
'''
def main():
    dm = DecisionMaker()
    done = CompleteAction()
    assign = AssignAction()
    ascii_banner = pyfiglet.figlet_format("Executive")
    print(ascii_banner)
    print("Welcome to Executive, GBNs Productivity App!\n")
    while True:
        input("Press Enter to continue...")
        print("The options are: \n" +
                "1. Decide what to do next\n" +
                "2. Add a new project to the list\n" +
                "3. Add new a action to one of the projects\n" +
                "4. List all actions and their ids\n"
                "4. Mark action as done\n" +
                "5. Assign action to a person\n" +
                "6. Quit\n")
        option = input("Pick an option: ")
        if option == '1':
            dm.run()
        elif option == '2':
            name = input("What would you like to call the project? \n >")
            sub = input("Is this a subproject? If so give the ID of the parent project, else leave this empty \n >")
            p = Project(name=name.strip())
            try:
                if sub != '':
                    p.parent = Project[int(sub.strip())]
                    print("created subproject {p.id} with parent {p.parent.id}: {p.name}".format(**locals()))
            except:
                print("Invalid ID")
            print("created project {p.id}: {p.name}".format(**locals()))
            p.save()
        elif option == '3':
            print("The available projects are:")
            for p in Project:
                print("{p.id}, {p.name}")
            s = input("Is the action scheduled [Y/N]?")
            if s.lower() == 'y':
                ScheduleAction().run()
            else:
                AddAction().run()
        elif option == '4':
            if len(Action) > 0:
                for p in Action:
                    print("{a.id}, {a.name}")
            else:
                print("congratulations, There are no actions left!")
        elif option == '5':
            action_id = input("Please input the ID of the completed action: \n >")
            scheduled = input("Is the action scheduled [Y/N]?")
            done.run(action_id, scheduled=(scheduled.lower() == 'y'))
        elif option == '6':
            assign.run()   
        elif option == '7':
            break
        else:
            print("Please input a from 1-7 number")
    input("Press Enter to continue...")
main()
