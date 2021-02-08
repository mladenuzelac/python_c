import zipfile 

# with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
# 
#     my_zip.write('test.txt')
#     my_zip.write('bier.jpg')


with zipfile.ZipFile('files.zip', 'r') as my_zip:
    print(my_zip.namelist())