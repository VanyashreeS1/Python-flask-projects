import os
if os.path.exists("file2.txt"):
  os.remove("file2.txt")
else:
  print("The file does not exist")