Python sometimes keeps string literals in memory automatically, even if you didn’t assign them to a variable.

"nikhil" as a text is already an object in Python’s internal string pool.
So when you call sys.getrefcount("nikhil"), Python counts:
The internal reference to the cached string "nikhil"
The temporary reference created when passing it to getrefcount()
Possibly another internal reference used by the shell or memory management
That’s why you see a reference count of 3 even though you didn’t explicitly create any variable called "nikhil".

💡 Key idea:
Strings and small integers are interned in Python — Python keeps them in memory to reuse and save space.
This is why "nikhil" already exists internally.

<!-- ouput of scripts  -->
>>> import sys
>>> sys.getrefcount("nikhil")
3
>>> sys.getrefcount('nikhil')
3
>>> sys.getrefcount(123)
4294967295