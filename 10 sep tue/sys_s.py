#Key Features of sys Module
# sys.argv

import sys
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])


#sys.exit([arg])
if len(sys.argv) < 1:
    print("Not enough arguments.")
    sys.exit(1)
else:
    print("Arguments provided!")

#sys.path

print("Current module search path:")
for path in sys.path:
    print(path)

#sys.platform

print("Running on platform:", sys.platform)

#sys.version

print("Python version:", sys.version)

#sys.stdin, sys.stdout, sys.stderr

sys.stdout.write("This is printed to standard output.\n")
sys.stderr.write("This is an error message.\n")

#sys.getsizeof()

data = [1, 2, 3, 4, 5]
print("Size of the list:", sys.getsizeof(data), "bytes")
