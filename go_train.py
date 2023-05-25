import os
os.system("python ./pct/train.py --data ./pct/data/my_data.yaml --cfg ./pct/models/yolov5s.yaml --weights ./pct/pretrained/yolov5s.pt --epoch 200 --batch-size 32 --device 0,1")
# os.system("python train.py --data my_data.yaml --cfg yolov5m.yaml --weights pretrained/yolov5m.pt --epoch 100 --batch-size 4")
# os.system("python train.py --data my_data.yaml --cfg yolov5l.yaml --weights pretrained/yolov5l.pt --epoch 100 --batch-size 4")

