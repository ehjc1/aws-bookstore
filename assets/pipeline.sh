#! /usr/bin/bash
# npm install

python3 static_test.py
if [ $? = 0 ]; then

    echo "static test passed!"
    npm run build

    if [ $? = 0 ]; then
        npm run test
        
        if [ $? = 0 ]; then
            echo "test was a great success"
            git add .
            git commit -m "COMPX341-21:${1}"
            git push origin master
        else
            echo "test failed :("
        fi
    else
        echo "Build Unsuccessful"
    fi
else
    echo "static test failed!"
    exit -1
fi
