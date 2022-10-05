# coding:utf-8

from Abstract_p_c import VehicleIntegratedSensor

class Camera(VehicleIntegratedSensor):
    def __init__(self, iso, fstop, gamma):
        self.iso = iso
        self.fstop = fstop
        self.gamma = gamma

    def get_camera_config(self):
        pass

    def GetPosition(self):
        pass





class Monocular_Camera(Camera):
    def __init__(self, x_size, y_size, frame, rgb_data):
        self.x_size = x_size
        self.y_size = y_size
        self.frame = frame
        self.rgb_data = rgb_data

    def get_image_map(self):
        pass

    # def GetPosition(self):
    #     print("123")


class RGBD_Camera(Camera):
    def __init__(self, x_size, y_size, depth_width, frame, rgbd_data):
        self.x_size = x_size
        self.y_size = y_size
        self.depth_width = depth_width
        self.frame = frame
        self.rgbd_data = rgbd_data

    def get_depth(self, x, y):
        pass

    def get_depth_map(self):
        pass

    def get_image_map(self):
        pass


class Binocular_Camera(Camera):
    def __init__(self, x_size, y_size, camera_left_conf, camera_right_conf, raw_bi_camera_data):
        self.x_size = x_size
        self.y_size = y_size
        self.camera_left_conf = camera_left_conf
        self.camera_right_conf = camera_right_conf
        self.raw_bi_camera_data = raw_bi_camera_data

    def get_left_camera_image(self):
        pass

    def get_right_camera_image(self):
        pass

    def cal_depth(self, x : int , y : int):
        pass

    def cal_depth_map(self):
        pass



class Fisheye_Camera(Binocular_Camera):
    def __init__(self, lens_circle_falloff, lens_circle_multiplier, fov, raw_bi_camera_data):
        self.lens_circle_falloff = lens_circle_falloff
        self.lens_circle_multiplier = lens_circle_multiplier
        self.fov = fov
        self.raw_bi_camera_data = raw_bi_camera_data

    def get_camera_config(self):
        pass
