# AI 알고리즘을 활용한 쓰레기 멀티라벨링 프로젝트 
- IITP AI Challenge에 제출했던 모델을 활용([챌린지 후기보기])
- https://multilabel4waste.herokuapp.com/firstapp/upload/

### 사용한 기술 스택
- Django
- Python
- pgsql
- pytorch(fastai)
 
# heroku 배포시 주의사항
### slug size
- heroku는 slug size를 500M이하로 제한하고 있어서 torch/torchvision 을 cpu 용으로 설치를 해야한다. 
- 기본으로 설정하면 slug size가 1G가 넘는다

### fastai 설치
- fastai의 경우 colab에서 버전1을 사용하는데 pip 를 이용하여 설치할 경우에는 버전2가 설치 된다. 
- fastai github에 v1을 다운로드 받아서 설치해야한다. 
- 컴파일은 정상적으로 되나 predict함수 실행시, interpolate() got an unexpected keyword argument 'recompute_scale_factor'에러 발생했다
- IITP AI Challenge에서 모델을 제출할때, nsml 플랫폼에서 같은 에러(unexpected keyword argument)가 발생했었다.
- 같은 팀원(@soykim-snail)께서 오픈라이브러리(매개변수삭제)를 수정하여 정상적으로 동작했었다.
- heroku에서는 자동으로 디펜던시를 설치하므로, fastai version1을 fork하여 해당 라이브러리를 수정하여 문제를 해결하였다.

```
# requirements.txt
...
-f https://download.pytorch.org/whl/torch_stable.html
torch==1.4.0+cpu 
-f https://download.pytorch.org/whl/torch_stable.html
torchvision==0.5.0+cpu 
git+git://github.com/k1msu2/fastai1.git
...
```
## 추가 개발 사항 
- 정답/오답 기능을 추가해야함(현재 버튼만 있음..)
- 추후에 모델 데이터 학습용으로 사용할 데이터 축척(파일다운로드기능)
