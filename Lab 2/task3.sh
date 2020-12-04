#! /bin/bash

read -p "Enter a number: " NUM

I=2
FLAG=0

while [ $I -le $(( $NUM/2 )) ]
do
    if [ $(( $NUM%$I )) == 0 ]
    then
        FLAG=1
    fi
    ((I++))
done

if [ $NUM -le 1 ] || [ $FLAG == 1 ]
then
    echo "Not Prime"
else
    echo "Prime"
fi