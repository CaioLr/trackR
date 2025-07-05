from . import data_formatter_monitor

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