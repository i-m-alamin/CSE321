#! /bin/bash

read -p "Enter a number: " NUM

DIGITS=${#NUM}
while [ $DIGITS -gt 1 ]
do
    I=0
    SUM=0
    while [ $I -lt $DIGITS ]
    do
        D=$(($NUM%10));
        NUM=$(($NUM/10))
        SUM=$(($SUM+($D*$D)))
        ((I++))
    done
    NUM=$SUM
    DIGITS=${#NUM}
done

if [ $NUM == 1 ]
then
    echo "Happy Number"
elif [ $NUM == 4 ]
then
    echo "Not Happy Number"
fi