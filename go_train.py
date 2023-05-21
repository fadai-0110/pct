import os
os.system("python ./test/train.py --data ./test/data/my_data.yaml --cfg ./test/models/yolov5s.yaml --weights ./test/pretrained/yolov5s.pt --epoch 100 --batch-size 4 --device 0")
# os.system("python train.py --data my_data.yaml --cfg yolov5m.yaml --weights pretrained/yolov5m.pt --epoch 100 --batch-size 4")
# os.system("python train.py --data my_data.yaml --cfg yolov5l.yaml --weights pretrained/yolov5l.pt --epoch 100 --batch-size 4")

