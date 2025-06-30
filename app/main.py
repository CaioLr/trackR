from ui.views import mainWindow
from PySide6.QtWidgets import QApplication
from utils import collectData
from multiprocessing import Process, Pipe

def hardware_worker(conn):
    while True:
        cmd = conn.recv()
        data = collectData.get_data()
        conn.send(data)
        if cmd == "stop":
            break


def main():
    parent_conn, child_conn = Pipe()
    p = Process(target=hardware_worker, args=(child_conn,))
    p.start()

    app = QApplication()
    base = mainWindow.MainWindow(parent_conn, p)
    base.show()
    app.exec()

if __name__ == "__main__":
    main()
