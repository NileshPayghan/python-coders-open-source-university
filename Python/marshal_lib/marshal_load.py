
import marshal


f = open('marshal_1.pyc', 'rb')

# load byte code object
byte_code = marshal.load(f)

# execute the byte code directly using exec function
exec(byte_code)
