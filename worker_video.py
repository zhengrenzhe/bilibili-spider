from api import get_video_data
from utils.extract import get_vid_from_url


def spider_job(url: str):
    vid = get_vid_from_url(url)
    print(vid)
    ok, data = get_video_data("69132113")
    print(ok)


if __name__ == "__main__":
    spider_job("https://www.bilibili.com/video/av69230639/?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.21")
