# Notebooks

Python notebooks used in the course Interactive Machine Learning of University Paris-Saclay. 

## Installation

Choose the option that applies to you.

### Option 1 
If you already have python 3 (version 3.7.X) installed and you are comfortable with installing python packages, please make sure that you have the following packages installed.
- pandas
- scikit-learn
- matplotlib
- numpy
- jupyter
- keras 

For example, you can install these packages using pip in one command: 

`pip install pandas scikit-learn matplotlib numpy jupyter keras`


### Option 2
If you don't already have python installed (or you want to start fresh), you want to get everything you need in one shot, and you have plenty of available storage on your laptop, download Anaconda for python 3.7
here: https://www.anaconda.com/download  

### Option 3 
If you don't want all 720 packages that come with Anaconda, download miniconda for python 3.7 here:  https://conda.io/miniconda.html  

Once miniconda is installed, you can install all the packages you need with conda, the package and environment manager that comes with miniconda. Run the following command install the above packages along with a number of additional dependencies:

`conda install python=3.7 pandas scikit-learn matplotlib numpy jupyter keras`

## Test

On Linux or Max, `cd` in this folder and run in the terminal:
`jupyter notebook` 


## Description

- Basics of ML Part-1
    - Machine Learning
    - Machine learning in python
    - Toy datset: The Iris Dataset
    - Training a Classifier on the Iris Dataset
    - Testing a Classifier on the Iris Dataset
- Basics of ML Part-2
    - Realworld dataset
    - Performance metrics in classification
    - Model selection
    - Another supervised learning task: Regression
