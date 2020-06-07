#!/bin/sh
echo "Running MNIST with HAT 100 epochs"
python run.py --experiment mnist5 --approach hat --nepochs 100
sleep 1
echo "Running MNIST with EWC 100 epochs"
python run.py --experiment mnist5 --approach ewc --nepochs 100
sleep 1
echo "Running FASION-MNIST with HAT 100 epochs"
python run.py --experiment fashion5 --approach hat --nepochs 100
sleep 1
echo "Running FASION-MNIST with EWC 100 epochs"
python run.py --experiment fashion5 --approach hat --nepochs 100
sleep 1
echo "Running CIFAR with HAT 100 epochs"
python run.py --experiment cifar5 --approach hat --nepochs 100
sleep 1
echo "Running CIFAR with EWC 100 epochs"
python run.py --experiment cifar5 --approach hat --nepochs 100
echo "    "
sleep 1
echo "DONE   "
