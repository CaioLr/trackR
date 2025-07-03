from ui.views import main_window
from PySide6.QtWidgets import QApplication
from monitors import data_formatter_monitor
from multiprocessing import Process, Pipe
from utils.logger import setup_logger
import logging

def hardware_worker(conn,log) -> None:
    while True:
        cmd = conn.recv()
        data = data_formatter_monitor.get_data()
        try:
            conn.send(data)
        except Exception as e:
            log.info(f"Fail to send data through hardware_worker: {e}")
            log.info(f"Fail to send data through hardware_worker: {e}")
        if cmd == "stop":
            break

def main() -> None:
    setup_logger()
    log = logging.getLogger(__name__)

    parent_conn, child_conn = Pipe()
    p = Process(target=hardware_worker, args=(child_conn,log))
    try:
        p.start()
    except Exception as e:
        log.error(f"Failed to start hardware_worker process: {e}")
    else:
        log.info("Hardware_worker started successfully")

    app = QApplication()
    base = main_window.MainWindow(parent_conn, p)
    try:
        base.show()
    except Exception as e:
        log.error(f"Failed to start the application: {e}")
    else:
        log.info("Application started successfully")

    app.exec()

if __name__ == "__main__":
    main()
