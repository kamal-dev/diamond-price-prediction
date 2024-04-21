# Create the Virtual Environment:
    1. conda create -p venv python==3.8
    2. conda activate venv/

# Setup the project:
    - python setup.py install

# Directory Structure
    |- artifacts            ''' All the pickle files will be stored in this directory '''
    |- notebooks            ''' We will write all the Jupyter notebook in notebook '''
        |- data             ''' All the files will be present in the data dir '''
    |- src                  ''' The entire end to end machine learning model will be present here '''
        |- components       ''' All the components of pipeline comes in this '''
        |- pipelines        ''' Both the pipeline is present here - Training Pipeline, Prediction Pipeline '''
        |- exceptions.py    ''' All the exceptions will be present here '''
        |- logger.py        ''' Logging will be done here '''
        |- utils.py         ''' Contains all the common functionality - Reading csv file, Creating a pickle file, upload the file in some database, etc. '''
    |- .gitignore
    |- README.md
    |- requirements.txt
    |- setup.py
