# from imagepreprocessing.darknet_functions import yolo_annotation_tool
# yolo_annotation_tool("/Users/elifcelik/Desktop/aa", "/Users/elifcelik/Desktop/obj.names.txt")


# from imagepreprocessing.darknet_functions import create_training_data_yolo

# source_path = "/Users/elifcelik/Desktop/train"
# create_training_data_yolo(source_path, percent_to_use=1, validation_split=0.2, 
# create_cfg_file=True, train_machine_path_sep="/", 
# shuffle=True, files_to_exclude=[".DS_Store","train.txt","test.txt","obj.names","obj.data","yolo-obj.cfg"])


# from imagepreprocessing.darknet_functions import create_cfg_file_yolo
# save_path = "/Users/elifcelik/Desktop/"
# create_cfg_file_yolo(save_path, classes=12, batch=64, sub=16, width=416, height=416)

from imagepreprocessing.darknet_functions import make_prediction_from_directory_yolo


make_prediction_from_directory_yolo(images_path, 
darknet_path, save_path="detection_results", 
darknet_command="./darknet detector test data/train/obj.data data/train/yolo-obj.cfg backup/yolo_obj_last.weights {0} -i 0 -thresh 0.2 -dont_show", 
files_to_exclude=[".DS_Store",""])