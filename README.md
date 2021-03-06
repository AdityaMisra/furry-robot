# furry-robot

### Python setup

**Python 3.7** is used in the project.

```
https://www.python.org/downloads/release/python-370/

https://realpython.com/installing-python/
```

### Setup the Project

#### Good coding practice is to create a virtualenv with **python 3.7**, activate it

* Virtual env setup - https://stackoverflow.com/questions/23842713/using-python-3-in-virtualenv

#### After copying the folder or code base

```  

$ cd furry-robot 
$ python setup.py install

```

#### Instead, if you don't want to actually install it but still would like to use it. Then do,

```

$ python setup.py develop

```

### Run the Project using run.sh

* Input commands can be added in the `run.sh` file

```

yes | sh run.sh | python input_reader.py

```

### Run from command line

```

$ python input_reader.py

# <Enter the command here>

```

### How to run the tests

* This command runs the unit test in verbose mode & also reports the coverage

```
pytest --cov . -v
```