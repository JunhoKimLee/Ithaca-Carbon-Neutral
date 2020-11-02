# python python-to-exe.py build
from cx_Freeze import setup,Executable

setup(name = "config_maker",
      version ="1.0",
      description = "",
      executables = [Executable(r"config_maker.py")]
      )
