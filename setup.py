from cx_Freeze import setup, Executable

setup(name="BlackJack",
      version="0.1",
      description="Play black Jack",
      executables=[Executable("BlackJack.py")])

# python setup.py build