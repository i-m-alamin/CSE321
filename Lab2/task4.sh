#! /bin/bash

function addition() {
    echo "The result is $(($1 + $2))"
}
function subtraction() {
    echo "The result is $(($1 - $2))"
}
function multiplication() {
    echo "The result is $(($1 * $2))"
}
function division() {
    echo "The result is $(($1 / $2))"
}

echo "Which operation would you like to do?" 
read OP
read -p "Operand 1: " VAR1
read -p "Operand 2: " VAR2
if [ "$OP" == "+" ]
then
    addition VAR1 VAR2
elif [ "$OP" == "-" ]
then
    subtraction VAR1 VAR2
elif [ "$OP" == "*" ]
then
    multiplication VAR1 VAR2
elif [ "$OP" == "/" ]
then
    division VAR1 VAR2
else
    echo "Invalid operation" 
fi
