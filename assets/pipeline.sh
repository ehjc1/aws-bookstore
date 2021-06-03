#! /usr/bin/bash

# npm install

npm run build
if [ $? = 0 ]; then
    git add .
    git commit -m "COMPX341 Commit aws-bookstore:$1"
    git push origin master
else
    echo "Build Unsuccessful"
fi
