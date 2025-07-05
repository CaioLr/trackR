import sys
from multiprocessing import Process, Pipe
from utils.logger import setup_logger
import logging
#UI
from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
from ui.views.bridge import Bridge
#Monitors
from monitors.hardware_worker import hardware_worker

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

    app = QApplication(sys.argv)
    bridge = Bridge(parent_conn, p)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("bridge", bridge)
    engine.load(QUrl("app/ui/views/main_window.qml"))

    if not engine.rootObjects():
        log.error("Failed to load QML file")
        sys.exit(-1)

    app.exec()
    bridge.stop_process()

if __name__ == "__main__":
    main()
