# Automater Project

The `src` directory contains the following contents:

`ICN_Automater.gh` is a grasshopper template injected with Python code that allows you to run automated multiple energy simulations given a directory full of construction/window configuration files. The grasshopper template works for any Rhino model that contains 1 construction and 1 window brep.

`ICN_Automater_2win.gh` is the same as above, except that it works for Rhino models that contain 1 construction brep and 2 window breps.

`config_maker` is a program that takes a user-input and converts it into a construction/window configuration file. It creates configuration files of the same format that can be fed directly into `ICN_Automater.gh`.

`config_maker_osx` is the same as above, except compiled for OSX users.

`config_maker_2win` is the same as `config_maker` except it produces configs that can be fed directly into `ICN_Automater_2win.gh`.

Tutorial: https://www.youtube.com/playlist?list=PLoaFv2gYinC0LBc5kYs4vZM8LJxTpw9Ge
