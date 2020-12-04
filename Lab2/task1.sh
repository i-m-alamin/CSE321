#! /bin/bash

read -p "Enter your annual income: " INCOME

TAX=0

if [ "$INCOME" -le 240000 ]
then
    echo "$TAX"
elif [ "$INCOME" -le 540000 ]
then
    echo "$(( (($INCOME-240000)*10)/100 ))"
elif [ "$INCOME" -le 720000 ]
then
    echo "$(( (($INCOME-540000)*20)/100 + 30000 ))"
else
    echo "$(( (($INCOME-720000)*30)/100+36000+30000 ))"
fi