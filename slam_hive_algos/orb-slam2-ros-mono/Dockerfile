FROM ros:melodic-perception

RUN rm -r /etc/apt/sources.list.d && \
	sh -c "echo 'deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic main restricted universe multiverse\n\
	deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-updates main restricted universe multiverse\n\
	deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-backports main restricted universe multiverse\n\
	deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-security main restricted universe multiverse\n\
	deb https://mirrors.tuna.tsinghua.edu.cn/ubuntu/ bionic-proposed main restricted universe multiverse' > /etc/apt/sources.list"

# Get dependencies
RUN apt-get update && apt-get install -y \
	git libgtk2.0-dev \
    libgtk-3-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev python-dev python-numpy \
    libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libdc1394-22-dev wget gdb vim zip \
    libglu1-mesa-dev freeglut3-dev mesa-common-dev libgl1-mesa-dev libglew-dev \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* 

RUN cd /tmp && wget https://github.com/stevenlovegrove/Pangolin/archive/refs/tags/v0.6.zip
RUN cd /tmp && unzip v0.6.zip && cd Pangolin-0.6 &&  mkdir build && cd build && cmake  .. \
&& make && make install 


ENV OPENCV 3.4.15
RUN cd /tmp && wget https://codeload.github.com/opencv/opencv/zip/$OPENCV -O opencv.zip \
&& unzip opencv.zip \
&& cd opencv-$OPENCV && mkdir build && cd build \
&& cmake -D CMAKE_BUILD_TYPE=RELEASE -D WITH_CUDA=OFF -D WITH_OPENGL=OFF .. \
&& make && make install 

RUN cd /tmp && wget https://gitlab.com/libeigen/eigen/-/archive/3.1.0/eigen-3.1.0.zip
RUN cd /tmp && unzip eigen-3.1.0.zip  && cd eigen-3.1.0 && mkdir build && cd build \
&& cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=RELEASE .. \
&& make install \
&& rm -rf /tmp/*


WORKDIR /home
COPY ORB_SLAM2 /home/ORB_SLAM2
RUN cd ORB_SLAM2 && chmod +x build.sh && sh build.sh

RUN echo "export ROS_PACKAGE_PATH=/opt/ros/melodic/share:/home/ORB_SLAM2/Examples/ROS" >> /opt/ros/melodic/setup.bash \
&& echo "export ROS_PACKAGE_PATH=/opt/ros/melodic/share:/home/ORB_SLAM2/Examples/ROS" >> /$HOME/.bashrc \
&& /bin/bash -c "source /opt/ros/melodic/setup.bash \
&& source /$HOME/.bashrc \
&& echo $ROS_PACKAGE_PATH \
&& cd ORB_SLAM2 && chmod +x build_ros.sh && sh build_ros.sh"

RUN apt-get update && apt-get install -y \
	python3-pip \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* 
# RUN pip3 install pyyaml
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pyyaml
