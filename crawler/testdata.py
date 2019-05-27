import pandas as pd
import cv2
import tensorflow
import keras
# DONE
data = pd.read_csv("cho-thue-can-ho-chung-cu_detail.csv",sep="\t")
# data = pd.read_csv("cho-thue-cua-hang-ki-ot.csv",sep="\t")
# data = pd.read_csv("cho-thue-kho-nha-xuong-dat.csv",sep="\t")
# data = pd.read_csv("cho-thue-nha-tro-phong-tro.csv",sep="\t")
# data = pd.read_csv("cho-thue-van-phong.csv",sep="\t")
# data = pd.read_csv("cho-thue-nha-mat-pho_detail.csv",sep="\t")
# data = pd.read_csv("cho-thue-nha-rieng.csv",sep="\t")
print(data)