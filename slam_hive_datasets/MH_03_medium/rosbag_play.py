import yaml 
import subprocess
config_raw = open("/slamhive/config.yaml",'r',encoding="UTF-8").read()
config_dict = yaml.load(config_raw, Loader=yaml.FullLoader)
remap_dict = config_dict["dataset-remap"]
topic_list = ["/cam0/image_raw",
            "/cam1/image_raw",
            "/imu0",
            "/leica/position"]
remap_list = []
if remap_dict != None:
    for key, value in remap_dict.items():
        if value in topic_list:
            remap_list.append(value + ":=" + key)
remap = ' '.join(remap_list)
playrosbag_command = "rosbag play /slamhive/dataset/MH_03_medium.bag " \
                + remap  + " --clock "
print(playrosbag_command)
subprocess.run(playrosbag_command, shell=True)