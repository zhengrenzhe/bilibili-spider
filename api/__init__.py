from utils.request import api_get


def get_video_data(vid: str):
    return api_get("http://api.bilibili.com/x/web-interface/view/detail?aid=%s" % vid)
