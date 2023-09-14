# simple_ros_example

# simple rosbag write

start somewhere here with rosbag storing

sofar no custom messages

...a lot to do

also not sure where to get the ubuntu docker images ! 

# store a rosbag on nfs

to store a rosbag file on the nfs store basically these steps has to be followed.

1. IP of Docker host has to be granted on nfs
2. Docker volume has to be created with a mount to nfs
3. The image run needs to mount the docker volume
4. store the rosbag in the mount path of the docker file

e.g.

``` bash
docker volume create --driver local \
  --opt type=nfs \
  --opt o=addr=nfsurl.com,rw \
  --opt device=:/storeroot/storefolder \
  nfsrosbagstore
```

``` bash
docker run --name bag_try \
  --mount source=nfsrosbagstore,target=/home/rosuser/bagstore \
  -it ros_bagwrite bash
```

``` bash
ros2 bag record simple_topic -o /home/rosuser/bagstore/subfolder/bag_name
```
