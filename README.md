# TU Wien Open-Source Energy System Modeling

[![license](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/Marcel73125/open-source-energy-system-modeling/blob/main/LICENSE)

This is the first homework for the open-source energy system modelling course at TU Wien.
In this project, two python functions are provided to calculate/visualize the glucose level in the human body using the Sympy library.
For each commit automatic tests are ran to verify the behavior of the functions. Additionally ruff is executed for each commit to check the code style.

The repository is licensed under the Apache License, Version 2.0 (the "License");
see LICENSE for details.

## utils.py

[utils.py](/utils.py) provides two functions to calculate the glucose level in mg/dl in the human body, one which returns the value at the input time in minutes
and one which has an additional threshold modeled in that also plots a graph from t=0 to the input time in hours.

* #### glucoselevel(g_init, time):

The function glucoselevel calculates the glucose level in mg/dl at the handed over time in minutes with the given positive initial glucose level and returns that value; 
If the input initial glucose level is negative the function returns -1;

* #### printglucoselevel(g_init, time_hours): 

The function printglucoselevel calculates the glucose level in mg/dl at the handed over time in hours and at the given initial glucose level with a modeled threshold of 70mg/dl and plots it in the interval [0,time];
Returns 0 if inputs were valid; If either g_init or time_hours is negative -1 is returned;

## test_utils.py

The two functions in [utils.py](/utils.py) are tested using pytest in [test_utils.py](/test_utils.py).

## requirements.txt

[requirements.txt](/requirements.txt) lists all needed packages.

## pytest.yaml

Automatic actions for testing are set up in [pytest.yaml](/.github/workflows/pytest.yaml).

## ruff.yaml

Ruff is set up in [ruff.yaml](/.github/workflows/ruff.yaml) to check the code style.
