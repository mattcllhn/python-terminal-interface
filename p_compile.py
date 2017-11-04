import py_compile
import os
import sys

print('compiling '+sys.argv[2])

print(os.system("py_compile.compile("+sys.argv[2]+")"))
