import sys
from encryptor import encrypt
from decryptor import decrypt
import cv2
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        scroll = QScrollArea()
        widget = QWidget()
        self.layout = QVBoxLayout(widget)
        self.add_img('./inputs/Mona_Lisa.jpg', 'input image')
        self.add_img('./outputs/cipher_img.bmp', 'cipher image')
        self.add_img('./outputs/decrypted.jpg', 'decrypted image')
        scroll.setWidget(widget)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setCentralWidget(scroll)
    
    def add_img(self, img_path, text):
        label = QLabel()
        self.layout.addWidget(label)
        label.setText(text)
        label = QLabel()
        self.layout.addWidget(label)
        input_img = cv2.imread(img_path)
        input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
        input_img_qt = QImage(input_img, input_img.shape[1], input_img.shape[0], QImage.Format.Format_RGB888)
        input_img_qpixmap = QPixmap.fromImage(input_img_qt)
        label.setPixmap(input_img_qpixmap)


if __name__ == "__main__":
    encrypt('./inputs/Mona_Lisa.jpg')
    decrypt('./outputs/cipher_img.bmp', './secret_key.npy')
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec()