# coding:utf-8
from camera_all import RGBD_Camera
from PIL import Image
from pylab import *
import numpy as np
import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import time
import carla

img = Image.open("depth_image.png")
img_np_array = np.array(img)
print(img_np_array)
width = img_np_array.shape[0]
height = img_np_array.shape[1]
frame = 1
fov = 30
depth_width = 8
print(width)
print(height)
print(img_np_array)

RGBD_Camera_img = RGBD_Camera(x_size=width, y_size=height, depth_width=depth_width, frame=frame, rgbd_data=img_np_array)

# carla_convert


class carla_Image():
    def __init__(self, fov, height, width, raw_data):
        self.fov = fov
        self.height = height
        self.width = width
        self.raw_data = raw_data


    def save_to_disk(self):
        img = self.raw_data
        img = Image.fromarray(img)
        img.save("D:\software\program\carla0.9.10\WindowsNoEditor\PythonAPI\data\\new_depth_image.png")


def img_process(data):
    carla_Image_test = carla_Image(height=RGBD_Camera_img.y_size, width=RGBD_Camera_img.x_size, raw_data=RGBD_Camera_img.rgbd_data, fov=fov)
    carla_Image_test.save_to_disk()



actor_list = []

try:
    client = carla.Client("127.0.0.1", 2000)
    client.set_timeout(5.0)
    world = client.get_world()
    blueprint_library = world.get_blueprint_library()
    v_bp = blueprint_library.filter("model3")[0]
    spawn_point = world.get_map().get_spawn_points()[50]
    vehicle = world.spawn_actor(v_bp, spawn_point)
    actor_list.append(vehicle)
    blueprint = world.get_blueprint_library().find('sensor.camera.depth')
    blueprint.set_attribute('image_size_x', '1920')
    blueprint.set_attribute('image_size_y', '1920')
    blueprint.set_attribute('fov', '110')

    blueprint.set_attribute('sensor_tick', '1.0')
    transform = carla.Transform(carla.Location(x=0.8, z=1.7))
    rgb_sensor = world.spawn_actor(blueprint, transform, attach_to=vehicle)
    actor_list.append(rgb_sensor)
    rgb_sensor.listen(lambda data: img_process(data))
    time.sleep(1)

finally:
    for actor in actor_list:
        actor.destroy()
    print("end")
