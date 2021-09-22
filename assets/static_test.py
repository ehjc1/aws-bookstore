import glob, os, sys

searchString = '// Eugene Chew 1351553'
testPass = 0

for root, dirs, files in os.walk("./src"): # search the src directory
    for file in files: # search every file in directory

        if file.endswith(".ts"): # check if file type is .ts
            f = open(os.path.join(root, file))

            if searchString in f.read():
                print('found string in file %s' % file)
            else:
                print('string not found')
                sys.exit(-1)
                
            
            f.close()
    sys.exit(0)
