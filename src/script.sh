#!/bin/sh
echo " MNIST with HAT and 100 epochs "
counter_1=1
until [ $counter_1 -gt 10 ]
do
    python run.py --experiment mnist5 --approach hat --nepochs 100
    sleep 1
    ((counter_1++))
done
echo " MNIST with IMM-MEAN and 100 epochs "
counter_2=1
until [ $counter_2 -gt 10 ]
do
    python run.py --experiment mnist5 --approach imm-mean --nepochs 100
    sleep 1
    ((counter_2++))
done
echo " MNIST with IMM-MODE and 100 epochs "
counter_3=1
until [ $counter_3 -gt 10 ]
do
    python run.py --experiment mnist5 --approach imm-node --nepochs 100
    sleep 1
    ((counter_3++))
done
echo " CIFAR with HAT and 100 epochs "
counter_4=1
until [ $counter_4 -gt 10 ]
do
    python run.py --experiment cifar5 --approach hat --nepochs 100
    sleep 1
    ((counter_4++))
done
echo " CIFAR with IMM-MEAN and 100 epochs "
counter_5=1
until [ $counter_5 -gt 10 ]
do
    python run.py --experiment mnist5 --approach imm-mean --nepochs 100
    sleep 1
    ((counter_5++))
done
echo " CIFAR with IMM-MODE and 100 epochs "
counter_6=1
until [ $counter_6 -gt 10 ]
do
    python run.py --experiment mnist5 --approach imm-node --nepochs 100
    sleep 1
    ((counter_6++))
done
echo "           "
echo "           "
echo "           "
echo " DONE "