import glob, os, sys

searchString = '// Eugene Chew 1351553'
testPass = 0

for root, dirs, files in os.walk("./src"): # search the src directory
    for file in files:
        if file.endswith(".ts"):
            f = open(os.path.join(root, file))

            if searchString in f.read():
                print('found string in file %s' % file)
            else:
                print('string not found')
                sys.exit(-1)
                
            
            f.close()
     
    
