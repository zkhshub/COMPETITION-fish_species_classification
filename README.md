# [2023 제3회 K-water AI 경진대회] 어종(魚種) 식별 및 분류 알고리즘 개발
- 대회기간 : 2023-10-30 ~ 2023-11-13
- Team : 김다현, 최희영, 지경호
- Topic : Object Detection
<br/>
<p align="center">
<img src="https://github.com/MrSteveChoi/AI_projects/assets/132117793/4c3dee4d-aae9-41fb-8ac0-3a45a16ff8a6" width=60% height=60%>
</p>
<br/>

## 대회주제 <br/>
낙동강 하굿둑 물고기 영상에서 수조 내에 찍힌 물고기의 어종을 식별하고 분류하는 AI 모델을 개발합니다. <br/>

---
## 대회 진행 과정 <br/>
### 1. DATA 준비
Data set | 개수  
:---: | :---: | 
train | 104,875
test | 44,946
Label이 존재하는 data | 5,561
<br/>
EDA 결과를 토대로 label이 존재하는 이미지를 학습 이미지로 사용하되, Class imbalance 문제와 특정 Class에 대해 높은 mAP값이 나오는 문제를 해결하기 위한 Augmentation 방법을 적용하였습니다.<br/>
<img src="https://github.com/MrSteveChoi/AI_projects_Balchi/assets/132117793/a0866158-5868-45ce-9100-791377583640" width=70% > <br/>

### 2. 훈련 데이터 명세
Num total | TrainSet | ValidSet
:---: | :---: | :---: |
18,752 | 15,001(80%) | 3,751(20%)
<br/>

### 3. 모델 학습 과정
<img src="https://github.com/MrSteveChoi/AI_projects_Balchi/assets/132117793/ef01b326-9957-449f-95e3-c6b812a2f216" width=70% > <br/>
<br/>

### 4. 결과
Metric: Macro F1 Score <br/>
Public Score : 40th(%) / 0.5030873813 <br/>
Private Score: 44th(%) / 0.5214107843 <br/>
https://aifactory.space/task/2600/leaderboard <br/>

---

### 회고
- 아쉬운 점
    - YOLOv8의 tarin 과정에서 augmentation을 적용시키는데 시간이 많이 소요된 점이 아쉬웠습니다.
    - 물고기를 bbox로 crop하여 background image와 합성하는 cutmix 방식을 사용했는데 SAM등을 활용해서 깔끔하게 segmentation 후에 합성하는 copy-paste augmentation을 사용했다면 결과가 더 좋았을 것이라는 생각이 들었습니다.
    - 배경과 물고기를 무작위로 합성하는것이 아닌, 추론에 약한 특정 환경(녹조 등)을 파악 후 해당 환경과 비슷한 합성 이미지를 만들었다면 결과가 더 좋았을 것 같습니다.
    - 물고기를 crop한 후 새로운 이미지를 생성하는 방법 외에도 SCUMBLE, REMEDIAL, MLSOL, MLSMOTE 등의 OD-task에서 한 데이터에 multi-class가 있는 경우의 stratify 방법론들을 적용해 보았으면 좋았을 것 같습니다.
    - train data에서 부족한 label만 추출 후 합성을 통해 추가적인 학습용 이미지를 만들었으나 예상보다 결과가 좋지 않아서 아쉬웠습니다.
    - 단일 모델에서 soft-NMS를 적용해 보았다면 좋았을 것 같습니다.
    - YOLOv8을 포함한 여러 모델들의 WBF(Weighted Boxes Fusion)앙상블을 시도해 보았다면 더 좋은 결과를 얻을 수 있었을것 같습니다.
- 느낀 점
    - YOLO와 같이 만들어져 있는 모델을 가져다가 baseline code를 만드는 것도 생각보다 쉽지 않다는걸 느꼈습니다.
    - 2-stage detector가 1-stage detector보다 성능이 좋을것 이라고 생각했는데 결과는 2-stage 인 YOLO가 더 좋았음. 최신 모델이면 1-stage가 2-stage보다 성능이 좋을 수 있다는 걸 배웠습니다.
    - 단순히 Augmentation을 한다고 무조건 성능이 오르는게 아
- 얻은 것
    - YOLOv8과 Detectron2로 OD가 가능한 end-to-end Pipeline 구축에 성공한 점이 만족스러웠습니다.
    - 복잡한 COCO.json 파일을 pycocotools를 이용해 파싱하는 법을 연습할 수 있었습니다.
    - COCO dataset과 YOLO dataset의  bbox format이 다르고, 이를 변환하는 방법에 대해 알 수 있었습니다.
- 다음에 할 것
    - 물고기를 bbox로 crop하여 background image와 합성하는 cutmix 방식을 사용했는데 SAM등을 활용해서 깔끔하게 segmentation 후에 합성하는 copy-paste 방식을 사용했다면 결과가 더 좋았을 것이라는 생각이 들었습니다.
- 아직도 모르겠는 점
    - 2-stage detector인 fast-RCNN이 1-stage detector인 YOLO보다 성능이 낮게 나온 것을 보고 DL의 결과는 데이터 마다 다르다는 것을 실감했습니다.
---

### 기술스택
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
---

### Refernce
- 어종분류를 위한 CNN적용 <br/>
    - https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO201912261948910 <br/>
- 딥러닝을 이용한 어종 판별 시스템 <br/>
    - https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=DIKO0015305668  <br/>

### 주관 / 주최
- 주최 : 한국수자원공사(K-water)
- 주관 : 인공지능팩토리

