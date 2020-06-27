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


filename = input("Filename: ");
passes = input("Passes: ");
try:
    passes = int(passes);
except:
    print("ERROR: Passes must be a number");
    exit();
if(not os.path.isfile(filename)):
    print("ERROR: File not found!");
    exit();
print("THIS ACTION CANNOT BE UNDONE!");
if(not confirm("Are you sure?")):
    exit();
print("Shredding file.....\nThis may take a while depending on how many passes you specified");
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
print("\nDone!");