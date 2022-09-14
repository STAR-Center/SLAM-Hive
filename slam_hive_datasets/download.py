import os
import urllib.request
import sys

url_list = ["https://vision.in.tum.de/rgbd/dataset/freiburg2/rgbd_dataset_freiburg2_desk.bag",
            "http://robotics.ethz.ch/~asl-datasets/ijrr_euroc_mav_dataset/machine_hall/MH_01_easy/MH_01_easy.bag",
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
    for url in url_list:
        dataset_name = url.split('/')[-1]
        dir = dataset_name.split('.')[0]
        path = os.path.join(os.getcwd(), dir + '/' + dataset_name)
        data_download(url, path, dataset_name)


