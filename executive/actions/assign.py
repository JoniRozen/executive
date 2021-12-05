from executive.actions.models import AssignedAction
from executive.actions.add import AddAction

class AssignAction(AddAction):
    options = [
        'name', 'action_id', "time"]
    def _add(self, options):
        action = AssignedAction(**options) 
        action.save()

if __name__ == "__main__":
    AssignAction().run()














