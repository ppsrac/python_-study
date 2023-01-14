import subprocess
import glob
import time
fi_list=glob.glob("input.*")
fo_list=glob.glob("output.*")
for i,file in enumerate(fi_list):
    f=open(file,"r")
    g=open(fo_list[i],"r")
    data=f.read()
    data_o=g.read()
    st=time.time()
    p=subprocess.run(['python','codeforce1.py'],input=data,capture_output=True, text=True)
    fi=time.time()
    print(str(i)+"th test")
    print("execution time:"+str((fi-st)/1.5)+"s")
    data_o=data_o.split('\n')
    for i, item in enumerate(p.stdout.split('\n')):
        if i>10:
            break
        if data_o[i]!=item:
            print("Wrong for "+str(i)+" th line.")
            print(data_o[i], item)
