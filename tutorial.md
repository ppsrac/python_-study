# 시작 전에

알고리즘 공부를 하다 보면 틀린 문제에 대해서 왜 틀린지 모르는 경우가 생깁니다. 이러한 경우 본인 풀이에 대한 반례가 꼭 필요한데요. 가급적 알고리즘 문제를 공유할 때에는 여러분들도 확인하실 수 있도록 테스트 케이스(가능한 반례 모음) 또한 가급적 공유하도록 하겠습니다. (어려운 문제들은 힘들수도 있어요...ㅠㅠ)
<br/>
<br/>
테스트 케이스가 많은 경우엔 일일히 테스트 케이스를 넣고 돌려보는 것도 일인데, 저는 테스트 케이스를 넣고 한번에 돌려주는 코드를 사용하고 있습니다. 코드가 지저분하지만, 사용하신다면 도움 되실 수도 있겠다 하여 공유합니다. 

```python
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
    p=subprocess.run(['python','cf133.py'],input=data,capture_output=True, text=True)
    fi=time.time()
    print(str(i)+"th test")
    print("Time:"+str((fi-st)/1.5)+"s")
    data_o=data_o.split('\n')
    for i, item in enumerate(p.stdout.split('\n')):
        if i>10:
            break
        if data_o[i]!=item:
            print("Wrong for "+str(i)+" th line.")
            print(data_o[i], item)

```
이걸 바로 쓰신다고 하면 에러가 뜨실텐데요, 제가 알려드리는대로 사용해주시면 나름 편리하게 사용하실 수 있을 거라고 생각합니다. 
<br/>
<br/>
세번째,네번째 줄에 보면
```python
fi_list=glob.glob("input.*")
fo_list=glob.glob("output.*")
```
이라는 문구가 있는데, 이 곳은 테스트 케이스(확인해보려고 하는 입력 예시)들과(`input.*`) 그에 대한 정답들을 불러오는 `output.*` 두 가지에 대한 목록을 불러오는 코드입니다. 이건 여러분이 저장하시는 테스트 케이스 혹은 정답 목록들에 대한 형식에 따라 달라지는데, 테스트 케이스 목록이 ['input1.txt','input2.txt',...]로 되어 있다면 `input*.txt` 형태로 `glob.glob("input.*")` 문구를 `glob.glob("input*.txt")`로 수정해주세요. 정답 목록을 적어놓는 문구도 마찬가지입니다. 
<br/>
<br/>
12번째 줄에 있는 
```python
p=subprocess.run(['python','cf133.py'],input=data,capture_output=True, text=True)
```
문구도 안의 'cf133.py'가 소스코드 파일명인데 이것 역시 본인의 소스 코드 제목으로 바꿔서 집어 넣으시면 사용할 수 있습니다.
<br/>
<br/>
본인이 본인의 소스코드를 `ssafy1.py`로 저장하셨다면 `['python','cf133.py']`를 `['python','ssafy1.py']`로 수정해주시면 작동합니다.

마지막으로, 소스코드와 테스트케이스, 그리고 정답 코드는 모두 같은 폴더에 저장해주세요. 안 그러면 오류가 발생한답니다...

그럼 서울 2반 화이팅!

