# main script
# 2020-7-2 15:12:09

import os
# import matlab.engine

print("Douban books crawler.")

os.system("python ./p1_doulists_unique.py")
os.system("python ./p1_doulists.py")

os.system("python ./p1_tags_unique.py")
os.system("python ./p1_tags.py")

# eng = matlab.engine.start_matlab()
# eng.main