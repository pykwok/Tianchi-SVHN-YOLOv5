## 将txt中的结果按识别出的字符按从左到右的顺序排序，保存到提交文件
import os 
import numpy as np
import pandas as pd
from tqdm import tqdm


# detect后，存放label的文件夹路径
file_path=r'.\runs\detect\exp\labels\\'

txt_file = sorted(os.listdir(file_path))

# 提交文件的路径
result = pd.read_csv(r'./mchar_sample_submit_A.csv')

for i, name in tqdm(enumerate(txt_file)):
    if name[-3:] == 'txt':
        # 读取文本文件
        txt = np.loadtxt(file_path + txt_file[i])
        # 如果图片里的数字，不止一个
        if txt.ndim != 1:
            # 根据 bbox的 横坐标x值排序， idx是根据x值从小到大的序列号
            idx = np.lexsort([txt[:,1]])
            txt = txt[idx, :]
            # 储存检测出来的数字
            t = ''
            for k in range(len(txt)):
                t = t + (str(np.int(txt[k][0])))
            # print('i, name, t', i, name, t)
            result.loc[result.file_name == name[:-3] + 'png', 'file_code'] = t
        else: # 如果图片里的数字只有一个数字
            t = ''
            t = t + (str(np.int(txt[0])))
            # print('i, name, t', i, name, t)
            result.loc[result.file_name == name[:-3] + 'png', 'file_code'] = t


result.to_csv(r'./mchar_sample_submit_A_result.csv',
              index = None)
