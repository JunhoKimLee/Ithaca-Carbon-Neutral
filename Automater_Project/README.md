# Automater Project

This directory contains the following contents:

`ICN_Automater.gh` is a grasshopper template injected with Python code that allows you to run automated multiple energy simulations given a directory full of construction/window configuration files. The grasshopper template works for any Rhino model that contains 1 construction and 1 window brep.

`config_maker` is a program that takes a user-input and converts it into a construction/window configuration file. It creates configuration files of the same format that can be fed directly into the grasshopper template.