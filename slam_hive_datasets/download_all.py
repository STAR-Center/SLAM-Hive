import os
import urllib.request
import sys

euroc_url_list = [ 
    # EuRoC MAV dataets:
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_01_easy/MH_01_easy.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_02_easy/MH_02_easy.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_03_medium/MH_03_medium.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_04_difficult/MH_04_difficult.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_05_difficult/MH_05_difficult.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/vicon_room1/V1_01_easy/V1_01_easy.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/vicon_room1/V1_02_medium/V1_02_medium.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/vicon_room1/V1_03_difficult/V1_03_difficult.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/vicon_room2/V2_01_easy/V2_01_easy.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/vicon_room2/V2_02_medium/V2_02_medium.bag",
    "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/vicon_room2/V2_03_difficult/V2_03_difficult.bag"]

tum_rgbd_url_list = [   
    # TUM RGB-D dataets:
    # TESTING AND DEBUGGING
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_xyz.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_rpy.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_xyz.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_rpy.bag",
    #HANDHELD SLAM
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_360.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_floor.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_desk.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_desk2.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_room.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_360_hemisphere.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_360_kidnap.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_desk.bag", 
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_large_no_loop.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_large_with_loop.bag",
    "https://vision.in.tum.de/rgbd/dataset/freiburg3/rgbd_dataset_freiburg3_long_office_household.bag"    
     ]

tum_rgbd_gt_url_list = [
    # TUM RGB-D dataets:
    # TESTING AND DEBUGGING
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_xyz-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_rpy-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_xyz-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_rpy-groundtruth.txt",
    #HANDHELD SLAM
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_360-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_floor-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_desk-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_desk2-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg1/rgbd_dataset_freiburg1_room-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_360_hemisphere-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_360_kidnap-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_desk-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_large_no_loop-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_large_with_loop-groundtruth.txt",
    "https://vision.in.tum.de/rgbd/dataset/freiburg3/rgbd_dataset_freiburg3_long_office_household-groundtruth.txt"
]


def _progress(block_num, block_size, total_size):
    '''callback function
       @block_num: downloaded chunks
       @block_size: the size of the data block
       @total_size: size of remote file
    '''
    sys.stdout.write('\r>> Downloading %s %.1f%%' % ("datatset",
                     float(block_num * block_size) / float(total_size) * 100.0))
    sys.stdout.flush()

# download dataset
def data_download(url, path, dataset_name):
    if not os.path.isfile(path):
        print("Dataset: " + dataset_name + " is downloading...")
        urllib.request.urlretrieve(url, path, _progress)
        print("\nDownload finished!\n")
    else:
        print("The dataset: " + dataset_name +" exists!\n")


if __name__ == "__main__":
    # EuRoC MAV dataets
    for url in euroc_url_list:
        dataset_name = url.split('/')[-1]
        dir = dataset_name.split('.')[0]
        path = os.path.join(os.getcwd(), dir + '/' + dataset_name)
        data_download(url, path, dataset_name)

    # TUM RGB-D dataets and groundtruth:
    for url in tum_rgbd_url_list:
        dataset_name = url.split('/')[-1]
        dir = dataset_name.split('.')[0]
        path = os.path.join(os.getcwd(), dir + '/' + dataset_name)
        data_download(url, path, dataset_name)  

        gt_url = tum_rgbd_gt_url_list[tum_rgbd_url_list.index(url)]
        gt_name = gt_url.split('/')[-1]
        gt_path = os.path.join(os.getcwd(), dir + '/groundtruth.txt')
        data_download(gt_url, gt_path, gt_name)

     
     
     
