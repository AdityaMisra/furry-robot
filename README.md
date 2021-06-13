# furry-robot

### Python setup
    https://realpython.com/installing-python/

    https://www.python.org/downloads/

### Setup the Project
```
pip install . 
```

#### Then you do,
After copying the folder or code base
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