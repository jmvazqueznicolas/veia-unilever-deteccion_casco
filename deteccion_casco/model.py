import cv2

class ReadCamera:
    def __init__(self, num_cam = 1):
        self.num_cam = num_cam
        self.vcap = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.vcap.read()
        return frame