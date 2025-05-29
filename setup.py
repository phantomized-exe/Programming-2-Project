import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Celeste 2 client side",
    options={"build_exe": {"packages":["pygame","os","json","random","subprocess","socket","network","pathlib","sys","_thread"],
                           "include_files":["Test Sprites","server.py","network.py","Resources.txt","README.md"]}},
    executables = executables

    )
# python setup.py build
# pyinstaller myscript.py