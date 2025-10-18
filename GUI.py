import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*
from PyQt6.QtGui import*
class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(50, 50, 250, 400)
        self.setWindowTitle("2.1 - User Profile GUI")

        self.setUpMainWindow()
        self.show()


    def createImageLabels(self):
        images = ["images/skyblue.png", "images/p.png"]
        for image in images:
            try:
                with open(image):
                    label = QLabel(self)
                    pixmap = QPixmap(image)
                    label.setPixmap(pixmap)
                    if image == 'images/p.png':
                        label.move(80,20)
            except FileNotFoundError as error:
                    print(f"Image not found.\nError: {error}")

    def setUpMainWindow(self):
        self.createImageLabels()
        user_label = QLabel(self)
        user_label.setText('Никита Гусев')
        user_label.setFont(QFont('Arial', 20))
        user_label.move(85, 140)

        bio_label = QLabel(self)
        bio_label.setText('Биография')
        bio_label.setFont(QFont('Arial', 17))
        bio_label.move(15, 170)

        about_label = QLabel(self)
        about_label.setText('Я студент 2-го курса БВО МАИ / Инноватика')
        about_label.setWordWrap(True)
        about_label.move(15, 190)

        skills_label = QLabel(self)
        skills_label.setText('Умения')
        skills_label.setFont(QFont('Arial', 17))
        skills_label.move(15, 240)

        languages_label = QLabel(self)
        languages_label.setText("Python |  SQL")
        languages_label.move(15, 260)

        experience_label = QLabel(self)
        experience_label.setText("Опыт работы")
        experience_label.setFont(QFont("Arial", 17))
        experience_label.move(15, 290)

        developer_label = QLabel(self)
        developer_label.setText("Python Developer")
        developer_label.move(15, 310)

        dev_dates_label = QLabel(self)
        dev_dates_label.setText("May 2022 - Present")
        dev_dates_label.setFont(QFont("Arial", 10))
        dev_dates_label.move(15, 330)

        driver_label = QLabel(self)
        driver_label.setText("Самокат")
        driver_label.move(15, 350)

        driver_dates_label = QLabel(self)
        driver_dates_label.setText("Jun 2025 - Aug 2025")
        driver_dates_label.setFont(QFont("Arial", 10))
        driver_dates_label.move(15, 370)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())