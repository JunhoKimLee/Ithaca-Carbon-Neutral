# Config Maker
This program lets you create configuration files for Grasshopper energy simulations. Designed for Mac OSX.

## How to setup Config Maker

Although various configuration options are available, the normal way of running
the Config Maker is to download this entire directory and ensure that it looks like this:

```
ROOT
  config_maker
  configs/
    [Empty]
  user_inputs/
    base_case.cfg
  ...
```

_Don't worry about the other files in the directory. They are important but you do not need to touch them at all. It should not affect the performance of the program. However, `configs` should be empty._


## How to run Config Maker

1. Set up the directory structure locally as above.

2. Open `base_case.cfg`. Follow the instructions and change parameters/variables as desired. Change nothing except what it says you are allowed to change.

3. Ensure that `configs` is an empty directory.

4. Run `config_maker` by double-clicking it with your mouse.

5. Repeat steps 2-3 as desired, updating `base_case.cfg` as you go. As long as you do not manually add files to `configs/`, the config files should all stack numerically (e.g. cons_1, cons_2, etc).

6. Your results will all be in `configs`.
