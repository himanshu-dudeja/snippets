
# Context managers allow us to properly manage resources so that we can specify exactly what we want to set-up and teardown

def sample_context_manager():
    with open('sample.txt', 'w') as f:
        f.write("Data written to file")


# Writing own context Manager (with Class conecpt)

def custom_context_manager_with_class():

    class Open_File():

        def __init__(self, filename, mode):
            self.filename = filename
            self.mode = mode

        def __enter__(self):
            self.file = open(self.filename, self.mode)
            return self.file

        def __exit__(self, exc_type, exc_val, traceback):
            self.file.close()

    with Open_File('sample.txt', 'w') as f:
        f.write('Testing')

    print(f.closed)


# Writing own context Manager (with function conecpt)

def custom_context_manager_with_function():
    from contextlib import contextmanager

    @contextmanager
    def open_file(file, mode):
        try:
            f = open(file, mode)
            yield f
        finally:
            f.close()

    with open_file('sample.txt', 'w') as f:
        f.write('Testing - Function')

    print(f.closed)


# sample_context_manager()
# custom_context_manager()
# custom_context_manager_with_function()
