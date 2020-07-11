import os
from contextlib import contextmanager


def bad_way():
    cwd = os.getcwd()
    os.chdir('dummy_dir1')
    print(os.listdir())
    os.chdir(cwd)

    cwd = os.getcwd()
    os.chdir('dummy_dir2')
    print(os.listdir())
    os.chdir(cwd)


def context_manager_function():

    @contextmanager
    def change_dir(destination):
        try:
            cwd = os.getcwd()
            os.chdir(destination)
            yield
        finally:
            os.chdir(cwd)

    with change_dir('dummy_dir1'):
        print(os.listdir())

    with change_dir('dummy_dir2'):
        print(os.listdir())

def context_manager_class():

    class ChangeDir:

        def __init__(self, destination):
            self.destination = destination

        def __enter__(self):
            self.cwd = os.getcwd()
            os.chdir(self.destination)

        def __exit__(self, exc_type, exc_val, traceback):
            os.chdir(self.cwd)

    with ChangeDir('dummy_dir1'):
        print(os.listdir())

    with ChangeDir('dummy_dir2'):
        print(os.listdir())


bad_way()
context_manager_function()
context_manager_class()
