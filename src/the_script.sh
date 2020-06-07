#!/bin/sh

<<COMMENT

NEPOCH=50
LR=0.05
BATCHSIZE=10

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach hat --nepochs $NEPOCH --output  '../res/mnist5_hat_$NEPOCH_$LR_$BATCHSIZE_’${i}’.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach imm-mean --nepochs $NEPOCH --output  '../res/mnist5_imm_mean_$NEPOCH_$LR_$BATCHSIZE_'${i}'.txt'; done


for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach hat --nepochs $NEPOCH --output  '../res/cifar5_hat_$NEPOCH_$LR_$BATCHSIZE_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach imm-mean --nepochs $NEPOCH --output  '../res/cifar5_imm_mean_$NEPOCH_$LR_$BATCHSIZE_'${i}'.txt'; done


for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach hat --nepochs $NEPOCH --output  '../res/fashion5_hat_$NEPOCH_$LR_$BATCHSIZE_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach imm-mean --nepochs $NEPOCH --output  '../res/fashion5_imm_mean_$NEPOCH_$LR_$BATCHSIZE_'${i}'.txt'; done

echo “Running with learning rate 0.05 and 10 epochs”

#!/bin/sh
for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach hat --nepochs 10 --output  '../res/mnist5_hat_10_0.05_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach imm-mean --nepochs 10 --output  '../res/mnist5_imm_mean_10_0.05_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach hat --nepochs 10 --output  '../res/cifar5_hat_10_0.05_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach imm-mean --nepochs 10 --output  '../res/cifar5_imm_mean_10_0.05_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach hat --nepochs 10 --output  '../res/fashion5_hat_10_0.05_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach imm-mean --nepochs 10 --output  '../res/fashion5_imm_mean_10_0.05_10_'${i}'.txt'; done

COMMENT

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach hat --nepochs 50 --lr 0.1 --output  '../res/mnist5_hat_50_0.1_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach imm-mean --nepochs 50 --lr 0.1  --output  '../res/mnist5_imm_mean_50_0.1_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach hat --nepochs 50 --lr 0.1  --output  '../res/cifar5_hat_50_0.1_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach imm-mean --nepochs 50 --lr 0.1  --output  '../res/cifar5_imm_mean_50_0.1_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach hat --nepochs 50 --lr 0.1  --output  '../res/fashion5_hat_50_0.1_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach imm-mean --nepochs 50 --lr 0.1  --output  '../res/fashion5_imm_mean_50_0.1_10_'${i}'.txt'; done


for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach hat --nepochs 50 --lr 0.01  --output  '../res/mnist5_hat_50_0.01_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment mnist5 --approach imm-mean --nepochs 50 --lr 0.01  --output  '../res/mnist5_imm_mean_50_0.01_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach hat --nepochs 50 --lr 0.01  --output  '../res/cifar5_hat_50_0.01_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment cifar5 --approach imm-mean --nepochs 50 --lr 0.01  --output  '../res/cifar5_imm_mean_50_0.01_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach hat --nepochs 50 --lr 0.01  --output  '../res/fashion5_hat_50_0.01_10_'${i}'.txt'; done

for i in 1 2 3 4 5 6 7 8 9 10; do python run.py --experiment fashion5 --approach imm-mean --nepochs 50 --lr 0.01  --output  '../res/fashion5_imm_mean_50_0.01_10_'${i}'.txt'; done
