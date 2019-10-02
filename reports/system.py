from datetime import datetime

import psutil


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
        "percent": psutil.cpu_percent(percpu=True),
    }


def get_memory_info():
    m = psutil.virtual_memory()
    return {
        "total": m.total,
        "available": m.available,
    }


def get_swap_info():
    m = psutil.swap_memory()
    return {
        "total": m.total,
        "used": m.used,
        "free": m.free,
    }


def get_network_info():
    n = psutil.net_io_counters(pernic=False)
    return {
        "bytes_sent": n.bytes_sent,
        "bytes_recv": n.bytes_recv,
        "packets_sent": n.packets_sent,
        "packets_recv": n.packets_recv,
    }


def get_boot_time():
    return str(datetime.now() - datetime.fromtimestamp(psutil.boot_time()))
