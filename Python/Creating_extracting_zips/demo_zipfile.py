import zipfile

# # Without context manager
# my_zip = zipfile.ZipFile('files.zip', 'w')

# my_zip.write('demo.txt')
# my_zip.write('image.png')

# my_zip.close()

# # With context manager (No compression as of now)
# with zipfile.ZipFile('files.zip', 'w') as my_zip:
#     my_zip.write('demo.txt')
#     my_zip.write('image.png')

# # With context manager (With Compression)
# with zipfile.ZipFile('files1.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
#     my_zip.write('demo.txt')
#     my_zip.write('image.png')

# Extratic the zip file
with zipfile.ZipFile('files1.zip', 'r') as my_zip:
    # Printing all the files inside the zip
    print(my_zip.namelist())
    # Extracting all files
    my_zip.extractall('extracted')
    # Extracting only 1 file
    # my_zip.extract('image.png')
