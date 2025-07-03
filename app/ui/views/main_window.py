from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QWidget,
)
from PySide6.QtGui import QFont
from PySide6.QtCore import QTimer

import logging
log = logging.getLogger(__name__)

class MainWindow(QMainWindow):
    def __init__(self,parent_conn, proc):
        super().__init__()
        self.conn = parent_conn
        self.proc = proc

        base = QWidget()
        layout = QVBoxLayout()

        font = QFont()
        font.setPixelSize(20)
        self.setFont(font)

        self.label = QLabel("Teste")
        layout.addWidget(self.label)


        base.setLayout(layout)
        self.setCentralWidget(base)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_temp)
        self.timer.start(1000)

    def update_temp(self) -> None:
        try:
            self.conn.send("update")
            data = self.conn.recv()
        except Exception as e:
            data = None
            log.info(f"Error receiving data: {e}")
        if data:
            self.label.setText(str(data['cpu']))

    def closeEvent(self, event) -> None:
        self.conn.send("stop")
        self.proc.join()
        event.accept()