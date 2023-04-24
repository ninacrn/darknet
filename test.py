import os
import subprocess

# set the path to the darknet folder
darknet_folder = './'

# set the path to the test images folder
test_images_folder = 'data/our_test'

# set the paths to the data files
data_file = 'data/yolo-obj.data'
config_file = 'yolo-obj.cfg'
weights_file = 'backup/yolo-obj_final.weights'

# set the threshold
threshold = '0.7'

# loop through all files in the test images folder
for file in os.listdir(test_images_folder):
    # check if the file is an image file
    if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
        # set the path to the image file
        image_file = os.path.join(test_images_folder, file)
        # call the darknet executable on the image file
        subprocess.run(['./darknet', 'detector', 'test', data_file, config_file, weights_file, image_file, '-thresh', threshold, '-ext_output'], cwd=darknet_folder)

