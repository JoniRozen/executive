Executive
=========

Preserve your precious executive function with a command-line task system that decides for you.

**Requirements**
=========

Python 3.10 : https://www.python.org/downloads/release/python-3100/

pip : https://pip.pypa.io/en/stable/installation/

**Setup**
============
First, clone the Github repo:
`git clone https://github.com/JoniRozen/executive.git /path/to/executive`

Run the installation script:
`python3 -m install.py`

**Usage**
=========

`python3 executive/main.py`


**Backlog**
=========

Backlog

The team created a backlog with improvements and missing features they think are necessary. You can choose to pick up work from this list. It is too much work for one day, you’re not expected to do all of it. If you think there are more urgent changes necessary you can also choose to work on those.
- The code was written in Python 2, which is end-of life. Convert it to Python 3. -> Done?
- It's only a static database. A service that preloads all the data into RAM would be faster.
- It would be nice if, when asked for a project, there is already a list shown of projects -> Done
- If there are no actions, there is an error. It should congratulate the user instead.
- When adding a task a deadline before today shouldn't be accepted. -> Done
- When adding a task the date format should be clarified in the prompt. -> Done
- Using sql.py the error message could be cleaner if the input isn't valid SQL.
- add.py works with an interactive prompt, could also support a list of arguments from the command line. Could use Python argparse for this. -> Done
- A command line tool is a bit scary for most users. A GUI would be more friendly
- The installation is a bit cumbersome, and sometimes there are problems because of differences in environments. Write an installation script. Docker would be even better -> Done

**Future Improvements**
=========

- Authentication/Accounts: There exist functionality to assign actions to people, using accounts one could see all relevants tasks for a certain person. Users with higher accsess could monitor employee productivity by checking the time completed of certain actions.

- More general overview: Right now you can just see what you have to do next (Besides being able to add/complete actions), with a higher-level overview you can see not just what you are doing now but what working towards. This would make the app feel much better to use.




