import os,sys
import numpy as np
import torch
from torchvision import datasets,transforms

def get(seed=0,fixed_order=False,pc_valid=0):
    data={}
    taskcla=[]
    size=[3,32,32]
    task_count = 4
    task_names = [
        'CIFAR - 0,1,2,3,4 [1/2]',
        'CIFAR - 5,6,7,8,9 [1/2]',
        'CIFAR - 0,1,2,3,4 [2/2]',
        'CIFAR - 5,6,7,8,9 [2/2]'
    ]
    
    if not os.path.isdir('../dat/binary_cifar2/'):
        os.makedirs('../dat/binary_cifar2/')

        # MNIST
        mean=[x/255 for x in [125.3,123.0,113.9]]
        std=[x/255 for x in [63.0,62.1,66.7]]
        dat={}
        dat['train']=datasets.CIFAR10('../dat/',train=True,download=True,transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean,std)]))
        dat['test']=datasets.CIFAR10('../dat/',train=False,download=True,transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean,std)]))
        for i, name in enumerate(task_names):
            data[i]={}
            data[i]['name']=name
            data[i]['ncla']=5
        
        for s in ['train','test']:
            loader=torch.utils.data.DataLoader(dat[s],batch_size=1,shuffle=True)
            for i in range(4):
                data[i][s]={'x': [],'y': []}
             
            for i,(image,target) in enumerate(loader):
                offset = 0 if i < (len(loader)/2) else 2
                label=target.numpy()[0]
                if (label==0 or label==1 or label==2 or label==3 or label==4):
                    data[0+offset][s]['x'].append(image)
                    data[0+offset][s]['y'].append(label)
                elif (label==5 or label==6 or label==7 or label==8 or label==9):
                    data[1+offset][s]['x'].append(image)
                    data[1+offset][s]['y'].append(label-2)
            
        # "Unify" and save
        for i in range(task_count):
            for s in ['train','test']:
                data[i][s]['x']=torch.stack(data[i][s]['x']).view(-1,size[0],size[1],size[2])
                data[i][s]['y']=torch.LongTensor(np.array(data[i][s]['y'],dtype=int)).view(-1)
                torch.save(data[i][s]['x'],os.path.join(os.path.expanduser('../dat/binary_cifar2'), 'data' + str(i) + s + 'x.bin'))
                torch.save(data[i][s]['y'],os.path.join(os.path.expanduser('../dat/binary_cifar2'), 'data' + str(i) + s + 'y.bin'))
        print('Saved partition of CIFAR')

    else:

        # Load binary files
        for i,name in enumerate(task_names):
            data[i]={}
            data[i]['name']=name
            data[i]['ncla']=5
            for s in ['train','test']:
                data[i][s] = {'x': [], 'y': []}
                data[i][s]['x'] = torch.load(os.path.join(os.path.expanduser('../dat/binary_cifar2'), 'data' + str(i) + s + 'x.bin'))
                data[i][s]['y'] = torch.load(os.path.join(os.path.expanduser('../dat/binary_cifar2'), 'data' + str(i) + s + 'y.bin'))
        
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

