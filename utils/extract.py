import re


def get_vid_from_url(url: str) -> str:
    s = re.search(r"bilibili.com/video/av(\d+)", url)
    if not s:
        return ""

    g = s.groups()
    if len(g) != 1:
        return ""

    return g[0]
