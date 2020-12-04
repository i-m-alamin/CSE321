#! /bin/bash

read -p "Enter a number: " NUM
if [ $(( NUM%5 )) == 0 ] && [ $(( NUM%2 )) == 0 ]
then
    echo "NO"
elif [ $(( NUM%5 )) == 0 ] || [ $(( NUM%2 )) == 0 ]
then
    echo "YES"
else
    echo "IGNORE"
fi