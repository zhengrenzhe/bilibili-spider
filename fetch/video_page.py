import json

from utils.request import get
import lxml.html


def fetch_page(url: str):
    html = get(url)

    dom = lxml.html.etree.HTML(html)

    scripts_content = dom.xpath("/html/head/script/text()")

    for js in scripts_content:
        js = js.strip()
        if js.startswith("window.__INITIAL_STATE__"):
            js_obj = js.replace("window.__INITIAL_STATE__=", "").replace("")
            print(js)
