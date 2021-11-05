"""Doctring."""
import cv2
import numpy


class CameraIP:
    """Uso de las cámaras IP por el prótocolo rtsp.

    El prótocolo rtsp permite enviar, via streaming, las
    imagenes que son captadas por un sistemas de cámaras IP.
    Para conectarse a la cámaras de la nave de Octopy, se debe estar
    conectado a la red "Moviles_5G".

    Argumentos:
        num_cam (int): Indica la cámara a leer en el sistema de cámaras.
        user (str): Nombre de usuario en el sistema de cámaras.
        password (str): Contraseña de usuario en el sistema de cámaras.
        channel (int): Selecciona la calidad del video,
                        1:alta calidad 2:baja calidad.
        ip (str): Direccón IP de la cámaras en la LAN.

    Atributos:
        cap (VideoCapture): Objeto que accede a las cámaras, se configura
                            para que solo guarde una imagen en su buffer.
    """

    def __init__(
        self,
        num_cam=1,
        user="Brito",
        password="Paco0908",
        channel=2,
        ip="192.168.1.72:554",
    ):
        """Docstring."""
        self.cap = cv2.VideoCapture(
            f"rtsp://{user}:{password}@{ip}/streaming/channels/{num_cam}{channel}"
        )
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    def get_frame(self) -> numpy.ndarray:
        """Lectura de los frames de la cámara seleccionada.

        Regresa:
            El último frame captado por la cámara.

        """
        _, frame = self.cap.read()
        return frame
