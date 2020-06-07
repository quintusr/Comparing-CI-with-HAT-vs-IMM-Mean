import os,sys
import numpy as np
import torch
from torchvision import datasets,transforms

def get(seed=0,fixed_order=False,pc_valid=0):
    data={}
    taskcla=[]
    size=[1,28,28]
    task_count = 10
    task_names = []
    for i in range(task_count):
        half = 1 if i < task_count/2 else 2
        i = i % (task_count/2)
        first = int(i*2)
        second = int(first + 1)
        task_names.append('FASHION-MNIST - {} and {} [{}/2]'.format(first,second,half))

 
    if not os.path.isdir('../dat/binary_fashionmnist/'):
        os.makedirs('../dat/binary_fashionmnist/')

        # MNIST
        mean=(0.1307,)
        std=(0.3081,)
        dat={}
        dat['train']=datasets.FashionMNIST('../dat/',train=True,download=True,transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean,std)]))
        dat['test']=datasets.FashionMNIST('../dat/',train=False,download=True,transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean,std)]))
        for i, name in enumerate(task_names):
            data[i]={}
            data[i]['name']=name
            data[i]['ncla']=2
        
        for s in ['train','test']:
            loader=torch.utils.data.DataLoader(dat[s],batch_size=100,shuffle=True)
            for i in range(task_count):
                data[i][s]={'x': [],'y': []}
             
            for i,(image,target) in enumerate(loader):
                offset = 0 if i < (len(loader)/2) else (task_count/2)
                label = target.numpy()[0]
                base = int(label/2)
                data[base+offset][s]['x'].append(image)
                data[base+offset][s]['y'].append(label-(base*2))            

        # "Unify" and save
        for i in range(task_count):
            for s in ['train','test']:
                data[i][s]['x']=torch.stack(data[i][s]['x']).view(-1,size[0],size[1],size[2])
                data[i][s]['y']=torch.LongTensor(np.array(data[i][s]['y'],dtype=int)).view(-1)
                torch.save(data[i][s]['x'],os.path.join(os.path.expanduser('../dat/binary_fashionmnist'), 'data' + str(i) + s + 'x.bin'))
                torch.save(data[i][s]['y'],os.path.join(os.path.expanduser('../dat/binary_fashionmnist'), 'data' + str(i) + s + 'y.bin'))
        print('Saved partition of FASHION-MNIST')

    else:

        # Load binary files
        for i,name in enumerate(task_names):
            data[i]={}
            data[i]['name']=name
            data[i]['ncla']=2
            for s in ['train','test']:
                data[i][s] = {'x': [], 'y': []}
                data[i][s]['x'] = torch.load(os.path.join(os.path.expanduser('../dat/binary_fashionmnist'), 'data' + str(i) + s + 'x.bin'))
                data[i][s]['y'] = torch.load(os.path.join(os.path.expanduser('../dat/binary_fashionmnist'), 'data' + str(i) + s + 'y.bin'))
        
    # Validation
    for t in data.keys():
        data[t]['valid']={}
        data[t]['valid']['x']=data[t]['train']['x'].clone()
        data[t]['valid']['y']=data[t]['train']['y'].clone()

    # Others
    n=0
    for t in data.keys():
        taskcla.append((t,data[t]['ncla']))
        n+=data[t]['ncla']
    data['ncla']=n

    return data,taskcla,size

