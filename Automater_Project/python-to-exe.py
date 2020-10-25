from cx_Freeze import setup,Executable

setup(name = "config_maker",
      version ="1.0",
      description = "",
      executables = [Executable(r"config_maker\config_maker.py")]
      )