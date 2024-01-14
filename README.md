# Job Analyser: Exploring the Data and AI Job Market in Egypt 

### Problem Statment:

Navigating the Data and Artificial Intelligence (AI) job market in Egypt can be confusing, particularly for newcomers, every job description feels like it with a new surprise and it seems like every company has their definition of roles like (ML engineer, data scientist, data analyst, ...). This project aims to systematically collect and analyze data related to the Data and AI job market in Egypt. The primary objective is to gain insights into key aspects of the market, including the common skills in demand.

### Running the project locally

1. Clone the project repo

2. Set up the project env, you can do that by following those steps

    * Install **pyenv**, follow the instructions from this: https://github.com/pyenv/pyenv-installer 
    Note: if you faced the following warning: warning: seems you still have not added **pyenv** to the load path. and you're not capable of using **pyenv** in the              terminal, you might need to check out this issue: https://github.com/pyenv/pyenv-installer/issues/112
    specifically try the following script:
    
    ```
    export PATH="$HOME/.pyenv/bin:$PATH"
    eval "$(pyenv init --path)"
    eval "$(pyenv virtualenv-init -)"
   ```
    
    * Install **poetry** at the system level following the instructions from here: https://python-poetry.org/docs/

    * Then install a version of Python of your choice via pyenv, eg: pyenv install 3.10.6

    * In the project directory where you can see pyproject.toml, write the following commands in your terminal:
    ```
    pyenv local 3.10.6
    poetry env use 3.10.6
    poetry install
    ```
    * Run `Poetry shell` in your terminal to activate the environment. 
    
