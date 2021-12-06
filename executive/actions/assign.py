from executive.actions.models import Action, AssignedAction
from executive.actions.add import AddAction

class AssignAction(AddAction):
    options = [
        'name', 'action_id', "time"]
    def _add(self, options):
        action = AssignedAction(**options) 
        action.save()

    def _get_assigned_to(self, name):
        if len(Action) < 1:
            print("Add some actions first")
        assigned = AssignedAction.select().filter(AssignedAction.name==name).order_by(AssignedAction.id.asc())
        if len(assigned) < 1:
            print("No action has been assigned to this person!")
        print("The Tasks assigned to {} are:".format(name))
        for a in assigned:
            print("{}, {}".format(a.id, Action.select().filter(Action.id==a.action_id)[0].name))















