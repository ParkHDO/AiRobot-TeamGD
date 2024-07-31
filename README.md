# 시각장애인을 위한 AI 기반 가이드 독

프로젝트 기간: 2024.06.10 ~ 2024.07

참여자이메일: gmleh9207@gmail.com,thdtmdrj000@gmail.com, 77578480jj@gmail.com, youjiwon1116@gmail.com, rty0408@gmail.com, hyunnuu@gmail.com

## Train
    Just the head. Here I freeze all backbone layers and train only randomly initialized layers (i.e. layers that do not use pre-trained weights from MS COCO). 
    To train only the head layer, we passed layer='heads' to the train() function.

