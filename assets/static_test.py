import glob, os, sys

searchString = input('// Eugene Chew 1351553')

for root, dirs, files in os.walk("./src"):
    for file in files:
        if file.endswith(".ts"):
            f = open(os.path.join(root, file))

            if searchString in f.read():
                print('found string in file %s' % file)
                sys.exit(0)
            else:
                print('string not found')
                sys.exit(-1)
            
            f.close()

        
    
