import os,sys
import numpy as np
import torch
from torchvision import datasets,transforms

def get(seed=0,fixed_order=False,pc_valid=0):
    data={}
    taskcla=[]
    size=[1,28,28]
    task_count = 10
    task_names = [
        'MNIST - 0 and 1 [1/2]',
        'MNIST - 2 and 3 [1/2]',
        'MNIST - 4 and 5 [1/2]',
        'MNIST - 6 and 7 [1/2]',
        'MNIST - 8 and 9 [1/2]',   
        'MNIST - 0 and 1 [2/2]',
        'MNIST - 2 and 3 [2/2]',
        'MNIST - 4 and 5 [2/2]',
        'MNIST - 6 and 7 [2/2]',
        'MNIST - 8 and 9 [2/2]'
    ]
    
    if not os.path.isdir('../dat/binary_mnist/'):
        os.makedirs('../dat/binary_mnist/')

        # MNIST
        mean=(0.1307,)
        std=(0.3081,)
        dat={}
        dat['train']=datasets.MNIST('../dat/',train=True,download=True,transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean,std)]))
        dat['test']=datasets.MNIST('../dat/',train=False,download=True,transform=transforms.Compose([transforms.ToTensor(),transforms.Normalize(mean,std)]))
        for i, name in enumerate(task_names):
            data[i]={}
            data[i]['name']=name
            data[i]['ncla']=2
        
        for s in ['train','test']:
            loader=torch.utils.data.DataLoader(dat[s],batch_size=100,shuffle=True)
            for i in range(task_count):
                data[i][s]={'x': [],'y': []}
             
            for i,(image,target) in enumerate(loader):
                offset = 0 if i < (len(loader)/2) else 5
                label=target.numpy()[0]
                if (label==0 or label==1):
                    data[0+offset][s]['x'].append(image)
                    data[0+offset][s]['y'].append(label)
                elif (label==2 or label==3):
                    data[1+offset][s]['x'].append(image)
                    data[1+offset][s]['y'].append(label-2)
                elif (label==4 or label==5):
                    data[2+offset][s]['x'].append(image)
                    data[2+offset][s]['y'].append(label-4)            
                elif (label==6 or label==7):
                    data[3+offset][s]['x'].append(image)
                    data[3+offset][s]['y'].append(label-6)
                elif (label==8 or label==9):
                    data[4+offset][s]['x'].append(image)
                    data[4+offset][s]['y'].append(label-8)
            
        # "Unify" and save
        for i in range(task_count):
            for s in ['train','test']:
                #print('Unifying i = {}, s = {}'.format(i,s))
                data[i][s]['x']=torch.stack(data[i][s]['x']).view(-1,size[0],size[1],size[2])
                data[i][s]['y']=torch.LongTensor(np.array(data[i][s]['y'],dtype=int)).view(-1)
                torch.save(data[i][s]['x'],os.path.join(os.path.expanduser('../dat/binary_mnist'), 'data' + str(i) + s + 'x.bin'))
                torch.save(data[i][s]['y'],os.path.join(os.path.expanduser('../dat/binary_mnist'), 'data' + str(i) + s + 'y.bin'))
        print('Saved partition of MNIST')

    else:

        # Load binary files
        for i,name in enumerate(task_names):
            data[i]={}
            data[i]['name']=name
            data[i]['ncla']=2
            for s in ['train','test']:
                #print('Loading binary i: {} and s: {}'.format(i,s))
                data[i][s] = {'x': [], 'y': []}
                data[i][s]['x'] = torch.load(os.path.join(os.path.expanduser('../dat/binary_mnist'), 'data' + str(i) + s + 'x.bin'))
                data[i][s]['y'] = torch.load(os.path.join(os.path.expanduser('../dat/binary_mnist'), 'data' + str(i) + s + 'y.bin'))
        
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

