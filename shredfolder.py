import os

def confirm(txt):
    while True:
        data = input(txt + "[y/n]: ");
        if(not data.lower() in ["y", "n"]):
            print("Invalid option!");
            continue;
        if(data.lower() == "y"):
            return True;
        else:
            return False;

def shred_file(filename, passes):
    print("Shredding file " + filename)
    passesDone = 0;
    fileSize = os.path.getsize(filename);
    while True:
        if(passesDone == passes):
            os.remove(filename);
            break;
        # Write random bytes to file
        random_bytes = os.urandom(fileSize);
        with open(filename, "wb") as f:
            f.write(random_bytes);
            f.close();
        passesDone += 1;
        print("Passes done: {0}".format(passesDone), end="\r");
    print("Shredding file {0} completed!".format(filename));
def shred_directory(directory, passes):
    for i in os.listdir(directory):
        path = os.path.join(directory);
        if(os.path.isdir(path)):
            # The path is a directory, execute this function again with the directory path
            print("Shredding directory {0}".format(i));
            shred_directory(path, passes);
            print("Done!");
            continue;
        try:
            shred_file(path, passes);
        except:
            print("Skipping file {0}".format(path));
dirname = input("Folder path: ");
passes = input("Passes: ");
try:
    passes = int(passes);
except:
    print("ERROR: Passes must be a number");
print("THIS ACTION CANNOT BE UNDONE! All data stored in that folder INCLUDING SUBFOLDERS will be shredded.");
if(not confirm("Are you sure?")):
    exit();
print("Shredding folder.....");
shred_directory(dirname, passes);
print("Done!");