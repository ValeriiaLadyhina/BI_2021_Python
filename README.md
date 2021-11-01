#### System: Windows 10, Platform: win-64
#### Python 3.9, Conda 4.10.3

## Create a folder, put into this folder pain.py and requirements.txt
## Use commands written below to run pain.py:
### Create environment (for example, env)
* conda create -n env python=3.9
### Activate created environment
* conda activate env
### Add conda-forge channel to download required libraries
* conda config --add channels conda-forge
### Add required libraries
* conda install --file requirements.txt
### Run the programme
* python pain.py 
### Deactivate environment
* conda deactivate
### Remove environment
* conda env remove -n env 
