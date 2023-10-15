# simple_ros_examples

simple docker try's with ros2

- minimal_pub_sub
  - minimal_publisher publishes hello with counting numbers to minimal topic 
  - minimal subscriber subscribes to minimal topc and publishes the message content 
  - minimal bagwrite   subscribes to minimal and writes all messages to a bag file otside docker
  - minimal topics list just  shows all available ros2 topics

## Howto

### store a rosbag on nfs

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
