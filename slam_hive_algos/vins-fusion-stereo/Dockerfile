FROM ros:kinetic-perception

ENV CERES_VERSION="1.12.0"
ENV CATKIN_WS=/home/catkin_ws

      # set up thread number for building
RUN   if [ "x$(nproc)" = "x1" ] ; then export USE_PROC=1 ; \
      else export USE_PROC=$(($(nproc)/2)) ; fi && \
      apt-get update && apt-get install -y \
      cmake \
      libatlas-base-dev \
      libeigen3-dev \
      libgoogle-glog-dev \
      libsuitesparse-dev \
      python-catkin-tools \
      ros-${ROS_DISTRO}-cv-bridge \
      ros-${ROS_DISTRO}-image-transport \
      ros-${ROS_DISTRO}-message-filters \
      ros-${ROS_DISTRO}-tf && \
      rm -rf /var/lib/apt/lists/* 


RUN   git clone https://github.com/ceres-solver/ceres-solver.git && \
      cd ceres-solver && \
      git checkout tags/${CERES_VERSION} && \
      mkdir build && cd build && \
      cmake .. && \
      # make -j$(USE_PROC) install && \
      make install && \
      rm -rf ../../ceres-solver 

WORKDIR $CATKIN_WS
RUN   mkdir src
COPY  VINS-Fusion $CATKIN_WS/src/VINS-Fusion


# Build VINS-Fusion
ENV TERM xterm
ENV PYTHONIOENCODING UTF-8
RUN catkin config \
      --extend /opt/ros/$ROS_DISTRO \
      --cmake-args \
        -DCMAKE_BUILD_TYPE=Release && \
    catkin build && \
    sed -i '/exec "$@"/i \
            source "/home/catkin_ws/devel/setup.bash"' /ros_entrypoint.sh

RUN apt-get update && apt-get install -y \
	python3-pip \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/* 
RUN pip3 install pyyaml