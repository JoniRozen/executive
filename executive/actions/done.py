from sys import argv
from executive.actions.models import Action, ScheduledAction
from datetime import date
from pytz import timezone

class CompleteAction(object):
    def run(self, action_id, scheduled):
        if scheduled:
            action = ScheduledAction[action_id]
            action.lastcompleted = date.today()
        else:
            action = Action[action_id]
            action.completed = True
        action.save()
        self._reward(action)

    def _reward(self, action):
        print("Well done!")
        print("Set action '{action.name}' to completed.".format(**locals()))
        print("call decide.py for your next action")

