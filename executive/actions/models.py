import peewee as orm

db = orm.SqliteDatabase('executive.db')

class BaseModel(orm.Model):
    class Meta:
        database = orm.SqliteDatabase('executive.db')

class Project(BaseModel):
    name = orm.CharField()
    parent = orm.ForeignKeyField('self', null=True, backref='children')

class Action(BaseModel):
    name = orm.CharField()
    deadline = orm.DateField()
    project = orm.ForeignKeyField(Project, null=True)
    completed = orm.BooleanField(default = False)
    context = orm.CharField(null = True)

class ScheduledAction(BaseModel):
    """Scheduled action have a period within which they are active."""
    name = orm.CharField()
    cron = orm.CharField()
    lastcompleted = orm.DateTimeField(null = True)

class AssignedAction(BaseModel):
    """Assigned Actions keep track of who is assigned to what action."""
    name = orm.CharField()
    action_id = orm.ForeignKeyField(Action, null=True)
    time = orm.DateField()


db.connect()
db.create_tables([Project, Action, ScheduledAction, AssignedAction])