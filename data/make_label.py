import cv2
import json


# 1. 训练集图片和标签
train_image_path = './data/mchar_train/'
train_annotation_path = './data/mchar_train.json'

# 2. 验证集图片和标签
val_image_path = './data/mchar_val/'
val_annotation_path = './data/mchar_val.json'

# 3. 修改后的标签存放目录
# 训练集标签
train_label_path = './data/train_label/'
# 验证集标签
val_label_path = './data/val_label/'



train_data = json.load(open(train_annotation_path))
val_data = json.load(open(val_annotation_path))



# 一、处理训练集的标签
for img_id in train_data:
    f = open(train_label_path + img_id.replace('.png', '.txt'), 'w')
    img = cv2.imread(train_image_path + img_id)
    shape = img.shape

    label = train_data[img_id]['label']
    left = train_data[img_id]['left']
    top = train_data[img_id]['top']
    height = train_data[img_id]['height']
    width = train_data[img_id]['width']

    for i in range(len(label)):
        # 1. 中心点 （x_center, y_center）∈ [0, 1]
        # x1 加上（bbox的宽的一半）， 再除以 图片宽度shape[1]
        x_center = 1.0 * (left[i] + width[i] / 2) / shape[1]
        # y1 加上（bbox的高的一半）， 再除以 图片高度shape[0]
        y_center = 1.0 * (top[i] + height[i] / 2) / shape[0]

        # 2. 宽w、高h ∈ [0, 1]
        w = 1.0 * width[i] / shape[1]
        h = 1.0 * height[i] / shape[0]

        # label, x_center, y_center, w, h
        f.write(str(label[i]) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(w) + ' ' + str(h) + '\n')
    f.close()



# 二、处理验证集的标签
for key in val_data:
    f = open(val_label_path + key.replace('.png', '.txt'), 'w')
    img = cv2.imread(val_image_path + key)
    shape = img.shape

    label = val_data[key]['label']
    left = val_data[key]['left']
    top = val_data[key]['top']
    height = val_data[key]['height']
    width = val_data[key]['width']

    for i in range(len(label)):
        x_center = 1.0 * (left[i] + width[i]/2) / shape[1]
        y_center = 1.0 * (top[i] + height[i]/2) / shape[0]
        w = 1.0 * width[i] / shape[1]
        h = 1.0 * height[i] / shape[0]

        # label, x_center, y_center, w, h
        f.write(str(label[i]) + ' ' + str(x_center) + ' ' + str(y_center) + ' ' + str(w) + ' ' + str(h) + '\n')
    f.close()

