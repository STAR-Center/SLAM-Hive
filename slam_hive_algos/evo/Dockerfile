# This file is part of evo (github.com/MichaelGrupp/evo).
# 
# evo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# evo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with evo.  If not, see <http://www.gnu.org/licenses/>.

FROM  ros:noetic

RUN   sed -i s/archive.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list && \
      sed -i s/security.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list

# Copy the whole tree into the container.
RUN   apt-get update && apt-get -y install \
      apt-utils \
      git && \
      git clone https://github.com/MichaelGrupp/evo.git  container-local     
# COPY . container-local/

# In case an image of this container gets executed, source ROS environment.
# In here, for 'docker build', we have to do it manually.
ENTRYPOINT ["container-local/.ci/ros_entrypoint.sh"]

# Install tf2
RUN   apt-get update && apt-get -y install ros-noetic-tf2-ros 

# Use Python 3.x for ROS Noetic.
RUN   container-local/.ci/debian_install_pip3.sh

# RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U && \
# pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install -U pip

# Build and install.
RUN   pip3 install /container-local --upgrade --no-binary evo
RUN   evo_config show --brief --no_color

# Run tests.
RUN   pip3 install pytest --upgrade
RUN   /container-local/.ci/ros_run_tests.sh /container-local
