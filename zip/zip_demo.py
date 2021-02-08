import zipfile 

my_zip = zipfile.ZipFile('files.zip', 'w')

my_zip.write('test.txt')
my_zip.write('bier.jpg')

my_zip.close()