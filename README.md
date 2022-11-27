# mertserbes_case
Firstly,I installed Noetic Ninjemys (latest LTS) in Ubuntu 20.04.5 according to http://wiki.ros.org/noetic/Installation/Ubuntu.                               
Then,I created catkin_ws workspace in this way: 

	  mkdir -p ~/catkin_ws/src 
	  cd ~/catkin_ws/
	  catkin_make
The catkin_make command is a convenience tool for working with catkin workspaces. Running it the first time in your workspace, it will create a CMakeLists.txt link in your 'src' folder.
 
  ### My catkin workspace 
![ERD with colored entities example (UML notation)](https://user-images.githubusercontent.com/72387579/204131161-8ee9a1ff-09e9-4c06-81d9-3171a366afec.jpeg)

### Create ROS Package
To create a new ROS package I used this way:
	
	  cd ~/catkin_ws/src
	  catkin_create_pkg composiv_tryouts std_msgs rospy roscpp
--std_msgs indicates that we will be using standard message types like int 8, int 64, string or float  
--roscpp indicates usage of C++ code  
--rospy indicates usage of Python code  
to build the packages in the catkin workspace:
	
	  cd ~/catkin_ws
	  catkin_make
To make the workspace and its packages visible to the file system so that I can access these packages from anywhere, I would have to run the following command:

	 . ~/catkin_ws/devel/setup.bash
	
Then,I implemented a publisher and subscriber In my package  
composiv_talker  
composiv_listener 
I created python file in src according to  python file from http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29  
and I made it executable the following command:
         
	 cd catkin_ws
	 cd src
	 cd composiv_tryouts
	 cd src
	 chmod +x composiv_talker.py
	 chmod +x composiv_listener.py  

	
In order for ROS is active , the "roscore" command is written, which activates the ROS Master.
to run publisher:

	rosrun composiv_tryouts composiv_talker.py

     
	
	
	

