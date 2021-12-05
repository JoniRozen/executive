from executive.actions.models import Action, Project
from datetime import date, datetime

class AddAction(object):
    options = [
        'name', 'deadline', 'project', 'context']
    def run(self):
        self.options = self._getoptions()
        self._add(self.options)

    def _getoptions(self):
        options = {}
        today = date.today()
        for option in self.options:
            if option == 'deadline':
                curr = datetime.strptime(input('Specify deadline in the following format: YYYY-MM-DD \n >'), "%Y-%m-%d")
                while curr.date() < today:
                    print('The deadline should cannot be a day before today!')
                    input("Press Enter to continue...")
                    curr = datetime.strptime(input('Specify deadline in the following format: YYYY-MM-DD \n >'), "%Y-%m-%d")
                    
                options[option] = curr
            elif option == 'time':
                options[option] = today
            else:
                options[option] = input("{option}? \n > ".format(**locals())).strip()
        if 'project' in options.keys():
            if options['project']:
                options['project'] = Project[options['project']]
            else:
                options['project'] = None
        return options
    

    def _add(self, options):
        action = Action(**options)
        action.save()

if __name__ == "__main__":
    a = AddAction()
    a.run()
    














