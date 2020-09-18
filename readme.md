# Comparing Catastrophic Interference between Incremental Moment Matching and Hard Attention to the Task

## About
Degree Project in Computer Engineering.\
KTH Royal Institute of Technology,\
Stockholm, Sweden.\
June 2020.

## Authors
Quintus Roos and William Lilliesköld.

## Disclaimer
The code used in our thesis is based on the code from https://github.com/joansj/hat and their paper "Overcoming Catastrophic Forgetting with Hard Attention to the Task". 
All credit to the authors Joan Serra, Didac Suris, Marius Miron, & Alexandros Karatzoglou.

## Abstract
When neural networks trained on data to solve one problem are trained on new data to solve another problem they tend to forget what they have previously learned to solve the first problem. This phenomenon is called CI. This thesis compares two state-of-the-art algorithms for reducing Catastrophic Interference (CI) in Neural Networks, specifically Incremental Moment Matching-Mean (IMM-Mean) and Hard Attention to the Task (HAT). Images from three different datasets with increasing complexity, MNIST, Fashion-MNIST, and CIFAR-10, are used to train and test their performances. The algorithms are trained on data from each respective dataset, partitioned into subsets, structured so that new classes of data are introduced with each new problem the algorithms are trained on, an approach known as Incremental Class Learning (ICL). From our results, we conclude that HAT suffers significantly less CI than IMM. Future work should however explore to what extent our conclusion holds when changing some of the parameters used for the thesis.

## Installing
The software setup follows the recommendations from the repository on which the code for this thesis is based. Specifically, using PyTorch as the framework and a Conda virtual environment running Python 3.6.8 with additional required packages installed. For detailed information, visit https://github.com/joansj/hat.

## Reference and link to thesis
Harvard:
Roos, Q. and Lilliesköld, W., 2020. Comparing Catastrophic Interference between Incremental Moment Matching-Mean and Hard Attention to the Task.

BibTeX:
@misc{roos2020comparing,
  title={Comparing Catastrophic Interference between Incremental Moment Matching-Mean and Hard Attention to the Task},
  author={Roos, Quintus and Lilliesk{\"o}ld, William},
  year={2020}
}

Link to thesis: https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A1464868&dswid=8030.

## Notes
We do not provide any support or assistance, nor do we assume and responsibity for the code in this repository.






