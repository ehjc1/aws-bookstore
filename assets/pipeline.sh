#! /usr/bin/bash
# npm install

python3 static_test.py
if [ $? = 0 ]; then

    echo "static test passed!"
    npm run build

    if [ $? = 0 ]; then
            git add .
            git commit -m "COMPX341 Commit aws-bookstore:$1"
            git push origin master
    else
        echo "Build Unsuccessful"
    fi
else
    echo "static test failed!"
    exit -1
fi
