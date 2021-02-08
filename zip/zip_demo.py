import zipfile 

with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
 
    my_zip.write('test.txt')
