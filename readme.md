# Comparing Catastrophic Interference between Incremental Moment Matching and Hard Attention to the Task

## About
Degree Project in Computer Engineering.\
KTH Royal Institute of Technology,
Stockholm, Sweden.\
June 2020

## Authors
Quintus Roos and William Lilliesköld

## Disclaimer
The code used in our thesis is based on the code from https://github.com/joansj/hat and their paper "Overcoming Catastrophic Forgetting with Hard Attention to the Task". 
All credit to the authors Joan Serra, Didac Suris, Marius Miron, & Alexandros Karatzoglou.

## Abstract
When neural networks trained on data to solve one problem are trained onnew data to solve another problem they tend to forget the previous knowl-edge they had that was needed to solve the first problem. This phenomenonis called CI. This thesis compares two state-of-the-art algorithms for reducingCatastrophic Interference (CI) in Neural Networks, specifically IncrementalMoment Matching-Mean (IMM-Mean) and Hard Attention to the Task (HAT).Images from three different datasets with increasing complexity, MNIST, Fashion-MNIST, and CIFAR-10, are used to train and test their performances. Thealgorithms are trained on data from each respective dataset, partitioned intosubsets, structured so that new classes of data are introduced with each newproblem the algorithms are trained on, an approach known as IncrementalClass Learning (ICL). From our results, we concluded that HAT suffers sig-nificantly less CI than IMM. Future work should however explore whether thisis the case when changing some of the parameters used for the thesis.

## Installing
The software setup follows the recommendations from the repository on which the code for this thesis is based. Specifically, using PyTorch as the framework and a Conda virtual environment running Python 3.6.8 with additional required packages installed. For detailed information, visit https://github.com/joansj/hat.

## Reference and link to thesis
TO DO.

## Notes
We do not provide any support or assistance, nor do we assume and responsibity for the code in this repository.






