import yaml, time, subprocess
from string import Template
# Generate mappingtask.yaml according to template.yaml and config.yaml
config_raw = open("/slamhive/config.yaml",'r',encoding="UTF-8").read()
config_dict = yaml.load(config_raw, Loader=yaml.FullLoader)
algo_dict = config_dict["algorithm-parameters"]
datatset_dict = config_dict["dataset-parameters"]
all_dict = {}
for key, value in algo_dict.items():
    all_dict.update({key: value})
for key, value in datatset_dict.items():
    all_dict.update({key: value})
template_raw = Template(open("/slamhive/template.yaml",'r',encoding="UTF-8").read())
# template = template_raw.safe_substitute(config_parsed)#Replaces existing dictionary values, preserving non-existing replacement symbols.
template = template_raw.substitute(all_dict)
# Write template to mappingtask.yaml
with open("/slamhive/mappingtask.yaml","w") as f:
    f.write(template)

template_raw = Template(open("/slamhive/template_cam0_mei.yaml",'r',encoding="UTF-8").read())
template = template_raw.substitute(all_dict)
with open("/slamhive/cam0_mei.yaml","w") as f:
    f.write(template)

template_raw = Template(open("/slamhive/template_cam1_mei.yaml",'r',encoding="UTF-8").read())
template = template_raw.substitute(all_dict)
with open("/slamhive/cam1_mei.yaml","w") as f:
    f.write(template)

roslaunch_command = "roscore & rosrun vins vins_node /slamhive/mappingtask.yaml &\
    rosrun loop_fusion loop_fusion_node /slamhive/mappingtask.yaml "
subprocess.run("bash -c 'source /opt/ros/kinetic/setup.bash; \
                source /home/catkin_ws/devel/setup.bash; \
                rosparam set use_sim_time true; "
                + roslaunch_command 
                + " & sleep 10s ; \
                python3 /slamhive/dataset/rosbag_play.py; \
                rosnode kill -a ; \
                mv /home/output/vio_loop.csv /slamhive/result/traj.txt ; \
                mv /home/output/* /slamhive/result/ ;\
                touch /slamhive/result/finished'", shell=True)


