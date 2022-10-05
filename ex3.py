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
import random
import carla
import numpy as np
from PIL import Image

def img_process(data):
    # print(data)
    # print(type(data))
    # print(data.raw_data)
    # print(type(data.raw_data))
    img = np.array(data.raw_data)
    print(len(img))
    # # 原有图像被压缩
    img = img.reshape((1920, 1920, 4))
    # # 将RGBA的数据变为RGB 删除每个像素的第四个索引alpha
    img = img[:, :, :3]
    print(len(img))
    im = Image.fromarray(img)
    print(type(im))
    im.save("D:\software\program\carla0.9.10\WindowsNoEditor\PythonAPI\data\%d.png' % data.frame_number")

actor_list = []

try:
    client = carla.Client("127.0.0.1", 2000)
    client.set_timeout(5.0)
    # 获取当前世界
    world = client.get_world()
    # 创建通过蓝图小车
    blueprint_library = world.get_blueprint_library()
    v_bp = blueprint_library.filter("model3")[0]
    # 将小车生成在地图265个点位中的50
    spawn_point = world.get_map().get_spawn_points()[50]
    vehicle = world.spawn_actor(v_bp, spawn_point)
    # 将生成的每一个actor放到actor_list列表中，最后在finally里循环销毁
    actor_list.append(vehicle)

    # 官方文档 从蓝图创建传感器并设置传感器基本参数
    # Find the blueprint of the sensor.
    # rgb相机
    blueprint = world.get_blueprint_library().find('sensor.camera.rgb')
    # Modify the attributes of the blueprint to set image resolution and field of view.
    blueprint.set_attribute('image_size_x', '1920')
    blueprint.set_attribute('image_size_y', '1920')
    blueprint.set_attribute('fov', '110')
    # Set the time in seconds between sensor captures
    blueprint.set_attribute('sensor_tick', '1.0')
    # 设定传感器的相对位置
    transform = carla.Transform(carla.Location(x=0.8, z=1.7))
    # 将传感器附在小车上
    rgb_sensor = world.spawn_actor(blueprint, transform, attach_to=vehicle)
    # 将生成的每一个actor放到actor_list列表中，最后在finally里循环销毁
    actor_list.append(rgb_sensor)

    # 传感器监听，获取数据，保存数据
    rgb_sensor.listen(lambda data: img_process(data))
    # rgb_sensor.listen(lambda data: data.save_to_disk(
    #     'D:\software\program\carla0.9.10\WindowsNoEditor\PythonAPI\data\%d.png' % data.frame_number))
    vehicle.set_autopilot(enabled=True)
    time.sleep(10)

finally:
    for actor in actor_list:
        actor.destroy()
    print("end")