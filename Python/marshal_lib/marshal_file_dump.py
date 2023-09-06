"""
Read python file and dump using marshal
"""

import marshal

with open('read_file.py', 'r') as f:
    python_file_read = f.read()

compiled_code = compile(python_file_read, "script", "exec")

wf = open("read_file.pyc",'wb')

marshal.dump(compiled_code, wf)

wf.close()
