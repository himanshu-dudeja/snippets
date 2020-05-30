import shutil

# # Creating a Zip file
# shutil.make_archive('another', 'zip', 'extracted')
shutil.make_archive('another', 'gztar', 'new_dir')

# # Extracting the ZIP file
# shutil.unpack_archive('files1.zip', 'new_dir')
