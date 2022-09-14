import yaml 
import subprocess
config_raw = open("/slamhive/config.yaml",'r',encoding="UTF-8").read()
config_dict = yaml.load(config_raw, Loader=yaml.FullLoader)
remap_dict = config_dict["dataset-remap"]
topic_list = ["/kitti/camera_color_left/camera_info",
            "/kitti/camera_color_left/image",
            "/kitti/camera_color_right/camera_info",
            "/kitti/camera_color_right/image",
            "/kitti/camera_gray_left/camera_info",
            "/kitti/camera_gray_left/image",
            "/kitti/camera_gray_right/camera_info",
            "/kitti/camera_gray_right/image",
            "/kitti/oxts/gps/fix",
            "/kitti/oxts/gps/vel",
            "/kitti/oxts/imu",
            "/kitti/velo/pointcloud",
            "/tf",
            "/tf_static"]
remap_list = []
if remap_dict != None:
    for key, value in remap_dict.items():
        if value in topic_list:
            remap_list.append(value + ":=" + key)
remap = ' '.join(remap_list)
playrosbag_command = "rosbag play /slamhive/dataset/kitti_2011_09_30_drive_0020_synced.bag " \
                + remap  + " --clock "
print(playrosbag_command)
subprocess.run(playrosbag_command, shell=True)

