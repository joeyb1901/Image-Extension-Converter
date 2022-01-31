import cv2
import os

dir_path = r'C:\tensorflow1\models\research\object_detection\images\test'  # r'Targeted directory'

for filename in os.listdir(dir_path):
    if filename.endswith('.jfif'):  # Targeted extension
        img = cv2.imread(os.path.join(dir_path, filename))
        output_dir = os.path.splitext(filename)[0] + '.jpeg'  # New desired extension
        cv2.imwrite(os.path.join(dir_path, output_dir), img)
        os.remove(os.path.join(dir_path, filename))  # Delete old file
