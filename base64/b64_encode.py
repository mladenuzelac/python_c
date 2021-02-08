import base64

with open("files.zip", "rb") as f:
    bytes = f.read()
    encode_string = base64.b64encode(bytes)

with open('output_file.txt', 'wb') as result:
    result.write(encode_string)