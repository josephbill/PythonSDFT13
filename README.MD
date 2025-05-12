## INSTALLATION GUIDE PYTHON 
1. python --version
   python3 --version
   pip --version 

2. .py extension. 
3. Python Virtual Environment :: 
   - avoid conflicts between projects :: pytest
   - protect the system python 
   - cleaner , reproducible environment i.e. requirements.txt 
   - smoother deployment 
           WINDOWS 
   - python -m venv venv  : scratch projects 
   - venv\Scripts\activate :: activating the virtual environment
           UBUNTU 
   - sudo apt update 
   - sudo apt install python3-venv 
   - python3 -m venv venv : creates the virtual environment in project
   - source venv/bin/activate : activates the environment 

4. Installation of dependencies : pip install  .....
                                  pip3 install ..... 
                                  pip install pytest

5. Labs : pip install Pipfile  : install the dependencies 
                                     = activate the virtual environment 
                                     = pip install Pipfile 
                                     = pip install ..... 
                                     = pytest 
                                     = python -m pytest



TEST DRIVEN DEVELOPMENT 
- software development approach :: 
  1. write a test for a small unit of functionality 
  2. Write minimum code needed to make the test pass 
  3. Refactor the code for cleanliness or corrections while keeping the test green (pass)

  RED -> GREEN -> REFACTOR CYCLE 

TIPS 
1. Dont just write code that passes the visible test the idea is to generate the same output as the test assertions but 
keep in mind assumptions that are not considered 
2. Think about edge cases (invalid data , null inputs)
