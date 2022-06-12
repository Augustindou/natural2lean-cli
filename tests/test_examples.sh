#!/bin/bash

echo "\n---------------------"
echo "Testing main examples"
echo "---------------------"
for filename in tests/examples/*.tex; do
    echo "\n--- Testing $filename"
    natural2lean f $filename
done

echo "\n------------------"
echo "Testing variations"
echo "------------------"
for filename in tests/examples/variations/*.tex; do
    echo "\n--- Testing $filename"
    natural2lean f $filename
done