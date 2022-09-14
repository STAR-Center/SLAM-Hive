import yaml 
import subprocess
config_raw = open("/slamhive/config.yaml",'r',encoding="UTF-8").read()
config_dict = yaml.load(config_raw, Loader=yaml.FullLoader)
remap_dict = config_dict["dataset-remap"]
topic_list = ["/cam0/image_raw",
            "/cam1/image_raw",
            "/fcu/imu",
            "/fcu/motor_speed",
            "imu0",
            "/vicon/firefly_sbx/firefly_sbx"]
remap_list = []
if remap_dict != None:
    for key, value in remap_dict.items():
        if value in topic_list:
            remap_list.append(value + ":=" + key)
remap = ' '.join(remap_list)
playrosbag_command = "rosbag play /slamhive/dataset/V1_03_difficult.bag " \
                + remap  + " --clock "
print(playrosbag_command)
subprocess.run(playrosbag_command, shell=True)