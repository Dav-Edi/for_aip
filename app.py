import sys
import os
import io
import warnings

from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

labels: dict = {
    'promt': 'promt',
    'promtExample': 'expansive landscape rolling greens with blue daisies and weeping willow trees under a blue sky ghibli',
    "generate": 'generate'
}


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App For AI(P)")
        self.setMinimumSize(720, 720)

        self.userPromt = labels['promtExample']

        self.labelPromt = QLabel(labels['promt'])
        self.labelPromt.setStyleSheet("color: red;")

        self.inputPromt = QLineEdit()
        self.inputPromt.setStyleSheet("color: red; background-color: gray")
        self.inputPromt.setPlaceholderText(labels['promtExample'])
        self.inputPromt.textChanged.connect(self.change_promt)

        generate = QPushButton(labels['generate'])
        generate.setStyleSheet('color: red;')
        generate.clicked.connect(self.save_promt)
        self.inputPromt.returnPressed.connect(self.save_promt)




        hlayout = QHBoxLayout()
        hlayout.addWidget(self.labelPromt)
        hlayout.addWidget(self.inputPromt)
        self.vlayout = QVBoxLayout()
        self.vlayout.addLayout(hlayout)
        self.vlayout.addWidget(generate)

        self.container = QWidget()

        self.container.setStyleSheet('background-color: black;')

        self.container.setLayout(self.vlayout)

        self.setCentralWidget(self.container)

    def change_promt(self):
        print("changing")
        self.userPromt = self.inputPromt.text()

    def save_promt(self):
        print(self.userPromt)
        os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'


        os.environ['STABILITY_KEY'] = 'sk-e4e7uYDTTRXFnTEHWnECZHPWjQ8CaMPWzh7mCNlfOOfPEjk2'

        stability_api = client.StabilityInference(
            key=os.environ['STABILITY_KEY'],
            verbose=True,
            engine="stable-diffusion-v1-5"
        )

        answers = stability_api.generate(
            prompt=self.userPromt,
            seed=123456789,
            steps=30,
            cfg_scale=8.0,
            width=512,
            height=512,
            samples=1,
            sampler=generation.SAMPLER_K_DPMPP_2M
        )

        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    img.save("imageAI.png")


        image = QPixmap()
        image.load("imageAI.png")
        label = QLabel()
        label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        label.setPixmap(image)
        self.vlayout.addWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()