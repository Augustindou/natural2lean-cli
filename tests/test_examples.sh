#!/bin/bash

# Run this file from the root of the project
# `sh tests/test_examples.sh``

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

echo "\n---------------------------------------"
echo "Testing different methods for 1 theorem"
echo "---------------------------------------"
for filename in tests/examples/m-sqr-even-different-proofs/*.tex; do
    echo "\n--- Testing $filename"
    natural2lean f $filename
done