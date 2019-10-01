import re
from typing import List

from PyChakra import Runtime
from lxml.html import etree

JS_RUNTIME = Runtime()


def get_first(target: List, default=""):
    if len(target) == 0:
        return default
    return target[0]


def xpath(html: str):
    dom = etree.HTML(html)

    def _extract(xpath_expr: str, default="", always_list=False):
        result = dom.xpath(xpath_expr)
        if len(result) == 0:
            return []
        elif len(result) == 1:
            if always_list:
                return result
            else:
                return get_first(result, default)
        else:
            return result

    return _extract


def get_object(js_string: str, js_name: str):
    result = JS_RUNTIME.eval("""
    (function(){
        var window = {};
        var document = {
            currentScript: {
                parentNode: {
                    removeChild(){}
                }
            }
        };
        %s
        return window["%s"];
    })();
    """ % (js_string, js_name))
    if result[0]:
        return result[1]
    else:
        return None


def get_vid_from_url(url: str) -> str:
    s = re.search(r"bilibili.com/video/av(\d+)", url)
    if not s:
        return ""

    g = s.groups()
    if len(g) != 1:
        return ""

    return g[0]
