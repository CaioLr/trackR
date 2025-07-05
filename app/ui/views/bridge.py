from PySide6.QtCore import QObject, Slot, Signal
import logging

log = logging.getLogger(__name__)

class Bridge(QObject):
    data_updated = Signal(dict)

    def __init__(self, parent_conn, proc):
        super().__init__()
        self.conn = parent_conn
        self.proc = proc

    @Slot()
    def update_data(self) -> None:
        try:
            self.conn.send("update")
            data = self.conn.recv()
            if data:
                self.data_updated.emit(data)
        except Exception as e:
            log.error(f"Error receiving data: {e}")
            self.data_updated.emit({})

    @Slot()
    def stop_process(self) -> None:
        self.conn.send("stop")
        self.proc.join()