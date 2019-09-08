import os

cur_tag = os.popen("git describe --abbrev=0 --tags").read()
new_tag_num = int(cur_tag.replace('v', '')) + 1
new_tag = "v%s" % new_tag_num

os.system("git tag %s" % new_tag)
os.system("git push --tags")
