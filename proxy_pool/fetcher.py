import lxml.html
import requests

from utils.http_header import create_header


def fetch_goubanjia():
    def extract_ip(sets):
        ip = "".join(sets[:-1])
        port = sets[-1]
        return "%s:%s" % (ip, port)

    r = requests.get("http://www.goubanjia.com", headers=create_header("www.goubanjia.com"))
    r.encoding = "utf-8"

    html = lxml.html.etree.HTML(r.content)
    p = ["%s://%s" % ("".join(x.xpath("td[3]/a/text()")), extract_ip(x.xpath('td[1]//*[name(.)!="p"]/text()')))
         for x in html.xpath('//tr')[1:]]

    return p
