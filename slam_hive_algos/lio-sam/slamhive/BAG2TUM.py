import os
import rosbag

def extract(bagfile):
    n = 0
    f = open('/slamhive/result/traj.txt', 'w')
    f.write('# timestamp tx ty tz qx qy qz qw\n')
    with rosbag.Bag(bagfile, 'r') as bag:
        for (topic, msg, ts) in bag.read_messages(topics="/lio_sam/mapping/odometry"):
            f.write('%.12f %.12f %.12f %.12f %.12f %.12f %.12f %.12f\n' %
                (msg.header.stamp.to_sec(),
                    msg.pose.pose.position.x, msg.pose.pose.position.y,
                    msg.pose.pose.position.z,
                    msg.pose.pose.orientation.x, msg.pose.pose.orientation.y,
                    msg.pose.pose.orientation.z, msg.pose.pose.orientation.w))
            n +=1
        print('wrote ' + str(n) + ' messages to the file: ')

if __name__ == '__main__':
    extract("/root/.ros/traj.bag")