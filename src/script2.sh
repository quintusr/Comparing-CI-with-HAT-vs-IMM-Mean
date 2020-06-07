#!/bin/sh
for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach hat --nepochs 50 --output  '../res/mnist5_hat_50_0.05_100_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach imm-mean --nepochs 50 --output  '../res/mnist5_imm_mean_50_0.05_100_'${i}'.txt'; done


for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach hat --nepochs 50 --output  '../res/cifar5_hat_50_0.05_100_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach imm-mean --nepochs 50 --output  '../res/cifar5_imm_mean_50_0.05_100_'${i}'.txt'; done


for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach hat --nepochs 50 --output  '../res/fashion5_hat_50_0.05_100_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach imm-mean --nepochs 50 --output  '../res/fashion5_imm_mean_50_0.05_100_'${i}'.txt'; done

