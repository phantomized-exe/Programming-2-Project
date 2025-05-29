import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Celeste 2 client side",
    options={"build_exe": {"packages":["pygame","os","json","random","subprocess","socket"],
                           "include_files":["Test Sprites","server.py","network.py"]}},
    executables = executables

    )
# python setup.py build