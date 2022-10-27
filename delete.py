#delete the file and directory:
#to delete the entire directory that contains files we must
# use import shutil

import os
import shutil
path = "folder"
try:
   #os.remove(path)
   #os.rmdir(path)
   shutil.rmtree(path)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You dont have the permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path + " was deleted")

