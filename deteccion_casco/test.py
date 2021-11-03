import cv2
from deteccion_casco.model import ReadCamera

cam = ReadCamera(0)
frame = cam.get_frame()
cv2.imshow("Camara", frame)
print("Presiona cualquier tecla para salir")
cv2.waitKey(0)