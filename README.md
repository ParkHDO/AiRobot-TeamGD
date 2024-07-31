# 시각장애인을 위한 AI 기반 가이드 독

프로젝트 기간: 2024.06.10 ~ 2024.07

참여자이메일: gmleh9207@gmail.com,thdtmdrj000@gmail.com, 77578480jj@gmail.com, youjiwon1116@gmail.com, rty0408@gmail.com, hyunnuu@gmail.com

## 개요
> ### 자율주행 로봇의 필요성
> 1. 한 자리에 머물지 않기 때문에 사각지대가 존재하는 CCTV나 장소가 국한된 출입구 검사기의 단점을 보완할 수 있다.
> 2. 실시간 위치정보와 촬영 데이터를 시각화하여 관리자가 쉽게 확인할 수 있다.
> 3. 인력을 로봇으로 대체함으로써 코로나 확산 가능성을 최소화하고 인력 낭비를 방지할 수 있다.
> 4. 360도 카메라와 인공지능을 활용하여 마스크를 착용하지 않은 사람을 효율적으로 찾아내고 음성경고 및 기록을 할 수 있다.

## Train
    Just the head. Here I freeze all backbone layers and train only randomly initialized layers (i.e. layers that do not use pre-trained weights from MS COCO). 
    To train only the head layer, we passed layer='heads' to the train() function.

