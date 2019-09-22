import os
import re

cur_tag = os.popen("git tag").read()
new_tag_num = int(re.search(r"v(\d)\s+$", cur_tag).groups()[0]) + 1
new_tag = "v%s" % new_tag_num

os.system("git tag %s" % new_tag)
os.system("git push --tags")
