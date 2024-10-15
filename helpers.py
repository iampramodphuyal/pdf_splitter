import os

def check_folder(*args):
    for arg in args:
        if os.path.exists(arg):
            print("Path already exists")
        else:
            print("Path not found, creating one")
            # parentPath = os.path.dirname(path)
            os.mkdir(arg)

def create_basePaths():
    parentPath = os.getcwd()
    destPath = os.path.join(parentPath, 'dest')
    srcPath = os.path.join(parentPath,'src')
    print(f"destpath:{destPath} | srcPath: {srcPath}")
    check_folder(destPath, srcPath)
