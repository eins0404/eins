git readme.md
# eins


###### basrc 설정
vim ~/.bashrc

echo “ROS2 jazzy is activated”
source /opt/ros/humble/setup.bash

alias sb="source ~/.bashrc; echo \”bahrc is reloaded\” “

alias ros_domain="export ROS_DOMAIN_ID=13;"
alias jazzy="source /opt/ros/jazzy/setup.bash; ros_domain; echo \”ROS2 is activated\” “

alias ros2sutdy="cd ~/ros2_study; source ~/ros2_study/install/local_setup.bash; echo \”ros2study is reloaded! \””


## 프로그램 list 확인 ###
ls /etc/apt/sources.list.d


## == colcon 설치 ==
mkdir -p ~/ros2study/src
sudo apt install python3-colcon-common-extensions
## 잘못된 빌드 삭제
sudo lrm -r build install log
## colcon  code --> colcon build --> ros2_ws 설정 
