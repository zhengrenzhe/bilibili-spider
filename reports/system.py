import threading
import time
from datetime import datetime

import psutil

network_speed = [0, 0]
last_bytes = [0, 0]
last_time = time.time()


def calc_network_speed(_speed, _last_bytes, _last_time):
    while True:
        total = psutil.net_io_counters(pernic=False)

        # kbps
        cur_time = time.time()
        speed_upload = round((total.bytes_sent - _last_bytes[0]) / 1024, 2)
        speed_download = round((total.bytes_recv - _last_bytes[1]) / 1024, 2)

        _last_bytes.clear()
        _last_bytes.append(total.bytes_sent)
        _last_bytes.append(total.bytes_recv)
        _speed.clear()
        _speed.append(speed_upload)
        _speed.append(speed_download)
        _last_time = cur_time
        time.sleep(1)


t = threading.Thread(target=calc_network_speed, args=(network_speed, last_bytes, last_time,))
t.daemon = True
t.start()


def get_disk_info():
    return [{
        "device": d.device,
        "mount_point": d.mountpoint,
        "fs": d.fstype,
        "total": psutil.disk_usage(d.mountpoint).total,
        "used": psutil.disk_usage(d.mountpoint).used,
    } for d in psutil.disk_partitions(all=False)]


def get_disk_usage_info():
    d = psutil.disk_io_counters(perdisk=True)
    return [{
        "disk": k,
        "read_count": d.get(k).read_count,
        "write_count": d.get(k).write_count,
        "read_bytes": d.get(k).read_bytes,
        "write_bytes": d.get(k).write_bytes,
    } for k in d.keys()]


def get_cpu_info():
    return {
        "core_count": psutil.cpu_count(logical=False),
        "total_percent": psutil.cpu_percent(),
        "percent": psutil.cpu_percent(percpu=True),
    }


def get_memory_info():
    m = psutil.virtual_memory()
    return {
        "used": m.used,
        "total": m.total
    }


def get_swap_info():
    m = psutil.swap_memory()
    return {
        "used": m.used,
        "total": m.total,
    }


def get_network_info():
    return {
        "upload": network_speed[0],
        "download": network_speed[1],
    }


def get_boot_time():
    return str(datetime.now() - datetime.fromtimestamp(psutil.boot_time()))
