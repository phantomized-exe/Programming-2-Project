import cx_Freeze

executables = [cx_Freeze.Executable("main.py")]

cx_Freeze.setup(
    name="Celeste 2 client side",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["Test Sprites"]}},
    executables = executables

    )