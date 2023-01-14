import sys
import random
import subprocess
from tqdm import tqdm, trange
input_file=['./Hard1/input'+str(i+1).zfill(2)+'.txt' for i in range(10)]
output_file=['./Hard1/output'+str(i+1).zfill(2)+'.txt' for i in range(10)]

def putting():
    p=subprocess.run(['python','a.py'],input='',capture_output=True, text=True)
    txt=p.stdout
    return txt+'\n'

def inpu():
    txt='10\n'
    a=random.randint(0,1)
    for t in range(10):
        if a==0:
            txt+=putting()
        else:
            k=random.randint(0,8)
            arr=putting().rstrip().split('\n')
            for i in range(9):
                arr[i]=arr[i].split('\n')
            random.shuffle(arr[k])
            for i in range(9):
                txt+=(' '.join(arr[i])+'\n')
    return txt
for i in trange(0,10):
    inp=inpu() 
    with open(input_file[i],'w') as input_i:
        input_i.write(inp)
    p=subprocess.run(['python','codeforce.py'],input=inp,capture_output=True, text=True)
    print(p.stdout)
    with open(output_file[i],'w') as output_i:
        output_i.write(p.stdout)