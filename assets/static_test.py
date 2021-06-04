import glob, os, sys

searchString = input('// Eugene Chew 1351553')
testPass = 0

for root, dirs, files in os.walk("./src"):
    for file in files:
        if file.endswith(".ts"):
            f = open(os.path.join(root, file))

            if searchString in f.read():
                print('found string in file %s' % file)
                testPass = 0
            else:
                testPass = -1
                print('string not found')
                
            
            f.close()

if testPass == 0:
    sys.exit(0)
else:
    sys.exit(-1)        
    
