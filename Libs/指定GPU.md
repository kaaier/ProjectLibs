1)终端中设定: CUDA_VISIBLE_DEVICES=1 python my_script.py

2)代码中设定：
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2"

3)set_device
import torch
torch.cuda.set_device(id)
