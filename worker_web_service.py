from flask import Flask, jsonify
from flask_cors import CORS

from infrastructure import postgres
from reports import spider, system, queue
from utils.cfg import get_cfg

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "api server index"


@app.route("/videos_count")
def videos_count():
    return jsonify({
        "count": postgres.video.get_videos_count()
    })


@app.route("/stat_info")
def stat_info():
    return jsonify({
        "system": {
            "disk": system.get_disk_info(),
            "cpu": system.get_cpu_info(),
            "memory": system.get_memory_info(),
            "swap": system.get_swap_info(),
            "network": system.get_network_info(),
            "boot_time": system.get_boot_time(),
        },
        "processes": {
            "ctrl": spider.get_supervisor_info(),
            "worker": spider.get_processes_info()
        }
    })


@app.route("/queue_info")
def queue_info():
    return jsonify(queue.get_queue())


@app.route("/start_process/<name>")
def start_process(name: str):
    return jsonify({
        "result": spider.start_processes(name)
    })


@app.route("/stop_process/<name>")
def stop_process(name: str):
    return jsonify({
        "result": spider.stop_processes(name)
    })


@app.route("/start_process_group/<name>")
def start_process_group(name: str):
    return jsonify({
        "result": spider.start_processes_group(name)
    })


@app.route("/stop_process_group/<name>")
def stop_process_group(name: str):
    return jsonify({
        "result": spider.stop_processes_group(name)
    })


@app.route("/start_all_processes")
def start_all_processes():
    return jsonify({
        "result": spider.start_all_processes()
    })


@app.route("/stop_all_processes")
def stop_all_processes():
    return jsonify({
        "result": spider.stop_all_processes()
    })


app.run("0.0.0.0", get_cfg("dashboard-api-dev.port"), __name__ == "__main__")
