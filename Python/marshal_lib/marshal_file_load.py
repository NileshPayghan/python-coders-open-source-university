import marshal

f = open('read_file.pyc', 'rb')

code = marshal.load(f)

print(code)

exec(code)