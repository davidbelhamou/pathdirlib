import pathlib

"""
Way to create path objects:
    . From a string
    . With Path.home() and Path.cwd() class methods
    . With the / operator
    
"""

# From a string
# I use backslash because i'm working on Windows and r before string to make it raw string
my_path = pathlib.Path(r"/")
print(my_path)

# From home and cwd
# Print home directory
r"""
    Windows: C:\Users\<username>
    macOS: /Users/<username>
    Ubuntu Linux: /home/<username>
"""
print(pathlib.Path.home())

# current working directory
print(pathlib.Path.cwd())

# From /
print(pathlib.Path.home() / "Desktop" / "work" / "path-dir-file-python")

# another way to join path
print(pathlib.Path.home().joinpath("Desktop").joinpath("work").joinpath("path-dir-file-python"))

"""
    Checking whether a File path exist
        you can create a Path object whether or not the file path exists.
        .exists():  return True if the path exist, else False
"""

home = pathlib.Path.home()
desk = home / "Desktop"
docs = desk / "work/path-dir-file-python"
hi_desk = desk / "realPython.py"
hi_docs = docs / "realPython.py"

print(hi_docs.exists())
print(hi_desk.exists())

# check if a path is a File
print(hi_docs.is_file())
print(hi_desk.is_file())

# check if a path is dir
print(hi_docs.is_dir())
print(hi_desk.is_dir())

"""
Absolute vs Relative Path
    absolute: /Users/david/Desktop/hello.txt
    relative:
        . hello.txt
        . /Desktop/hello.txt
"""

my_abs_p = pathlib.Path(r"/")
print(my_abs_p.is_absolute())
my_rel_p = pathlib.Path(r"\Desktop\work\path-dir-file-python")
print(my_rel_p.is_absolute())
# add the home dir to the relative
print(my_rel_p.resolve())

# accessing file components
f = pathlib.Path().home() / "hello.txt"
for p in f.parents:
    print(p)

print(f.parent)
print(f.anchor) # print the root
print(f.name) # print nam of the file
print(f.stem)
print(f.suffix)

"""
.parents : Returns paths to all directories contained in the file path
.parent : Returns the path to the first parent directory
.anchor : Returns a string representing the root directory if the path is absolute, else an empty string
.name : Returns the name of the file or directory the path points to as a string
.stem : Returns the filename before the dot
.suffix : Returns the file extension
"""