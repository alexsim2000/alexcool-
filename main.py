from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import  QFileDialog, QButtonGroup, QApplication, QWidget, QPushButton, QGroupBox,  QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QListWidget, QTextEdit, QLineEdit
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter
app = QApplication([])

win = QWidget()
win.resize(500,300)
line_main= QHBoxLayout()
line_v2=QVBoxLayout()
line_v3=QVBoxLayout()
line_h1=QHBoxLayout()


class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dr=None
        self.filename=None
        self.save_dir='modified/'

    def loadImage(self, filname):
        self.filename=filname
        image_path=os.path.join(workdir, filname)
        self.image =Image.open(image_path)

    def showImage(self, path):
        kar.hide()
        pixmapimage=QPixmap(path)
        w, h=kar.width(), kar.height()
        pixmapimage=pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        kar.setPixmap(pixmapimage)
        kar.show()

    def do_bw(self):
        
        self.image = self.image.convert("L")
        self.saveImage()
        image_path=os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)
    def saveImage(self):
        path=os.path.join(workdir, self.save_dir)    
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        image_path = os.path.join(path, self.filename)
        self.image.save(image_path)

    def do_flip(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.saveImage()
        image_path=os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)

    def de_blur(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.saveImage()
        image_path=os.path.join(workdir, self.save_dir, self.filename)
        self.showImage(image_path)


    




def showChosenImage():
    if okno.currentRow()>=0:
        filename = okno.currentItem().text()
        workimage.loadImage(filename)
        image_path=os.path.join(workdir, workimage.filename)
        print(workimage.image)
        workimage.showImage(image_path)

workimage=ImageProcessor()
workdir=''
def chooseworkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result=[]
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def show_list_files():
    extensions = ['png', 'jpg', 'bmp', 'gif']
    chooseworkdir()
    files=os.listdir(workdir)
    filenames =filter(files, extensions)
    okno.clear()
    
    for file in filenames:
        okno.addItem(file)



bth_left=QPushButton('ЛЕВО')
bth_right=QPushButton('ПРАВО')
bth_zerkal=QPushButton('ЗЕРКАЛО')
bth_rezkost=QPushButton('РЕЗКОСТЬ')
bth_black=QPushButton('Ч/Б')
bth_papka=QPushButton('ПАПКА')
okno=QListWidget()
kar=QLabel('КАРТИНКА')

line_v3.addWidget(kar)
line_v3.addLayout(line_h1)
line_main.addLayout(line_v2)
line_main.addLayout(line_v3)


line_h1.addWidget(bth_left)
line_h1.addWidget(bth_right)
line_h1.addWidget(bth_zerkal)
line_h1.addWidget(bth_rezkost)
line_h1.addWidget(bth_black)
line_v2.addWidget(bth_papka)
line_v2.addWidget(okno)

win.setLayout(line_main)

okno.currentRowChanged.connect(showChosenImage)

win.show()
bth_papka.clicked.connect(show_list_files)
bth_black.clicked.connect(workimage.do_bw)
bth_right.clicked.connect(workimage.do_flip)
bth_rezkost.clicked.connect(workimage.de_blur)
app.exec_()






