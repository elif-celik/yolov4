from imagepreprocessing.darknet_functions import create_training_data_yolo, create_cfg_file_yolo
'''
source_path = "/Users/elifcelik/Desktop/train"
create_training_data_yolo(source_path, percent_to_use=1, validation_split=0.2, 
create_cfg_file=True, train_machine_path_sep="/", 
shuffle=True, files_to_exclude=[".DS_Store","train.txt","test.txt","obj.names","obj.data","yolo-obj.cfg"])'''

create_cfg_file_yolo("",12,yolo_version=4)
