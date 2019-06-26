from fetch import fetch_video_page
from db.video import create_videos_item

url = "https://www.bilibili.com/video/av56617044/?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.21"

r = fetch_video_page(url)

print(r)
