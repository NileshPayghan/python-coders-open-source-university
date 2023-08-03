import marshal

script = """
a = 10
b = 20
print(a+b)
"""

compiled_script = compile(script, "script", "exec")

# dumps function to return byte stream
byte_code = marshal.dumps(compiled_script)
print(byte_code)

f = open("marshal_1.pyc", "wb")
marshal.dump(compiled_script, f)
f.close()
