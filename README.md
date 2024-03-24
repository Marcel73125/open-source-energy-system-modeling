# TU Wien Open-Source Energy System Modeling

[![license](https://img.shields.io/badge/license-Apache%202.0-black)](https://github.com/Marcel73125/open-source-energy-system-modeling/blob/main/LICENSE)

This is the first homework for the open-source energy system modelling course at TU Wien

The repository is licensed under the Apache License, Version 2.0 (the "License");
see LICENSE for details.

The function glucoselevel calculates the glucose level in mg/dl at the handed over time in minutes with the given positive initial glucose level and returns that value; 
If the input initial glucose level is negative the function returns -1;

The function printglucoselevel calculates the glucose level in mg/dl at the handed over time in hours with a modeled threshold of 70mg/dl at the given initial glucose level and plots it in the interval [0,time];
Returns 0 if inputs were valid; If either g_init or time_hours is negative -1 is returned;
