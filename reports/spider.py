from xmlrpc.client import ServerProxy, Fault

server = ServerProxy("http://localhost:9001/RPC2")


def get_supervisor_info():
    return {
        "supervisor_state": server.supervisor.getState(),
        "supervisor_pid": server.supervisor.getPID(),
    }


def get_processes_info():
    return server.supervisor.getAllProcessInfo()


def start_processes(name: str):
    try:
        return server.supervisor.startProcess(name)
    except Fault as err:
        return str(err.faultString)


def start_all_processes():
    try:
        return server.supervisor.startAllProcesses()
    except Fault as err:
        return str(err.faultString)


def stop_processes(name: str):
    try:
        return server.supervisor.stopProcess(name)
    except Fault as err:
        return str(err.faultString)


def stop_all_processes():
    try:
        return server.supervisor.stopAllProcesses()
    except Fault as err:
        return str(err.faultString)


def start_processes_group(name: str):
    try:
        return server.supervisor.startProcessGroup(name)
    except Fault as err:
        return str(err.faultString)


def stop_processes_group(name: str):
    try:
        return server.supervisor.stopProcessGroup(name)
    except Fault as err:
        return str(err.faultString)
