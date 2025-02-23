import shutil
import os

src_dir = "ch10/tmp"
dst_dir = "ch10/myvideo"
os.makedirs(dst_dir, exist_ok=True)

files = [f for f in os.listdir(src_dir) if f.endswith((".mp4", ".avi", ".mov"))]

for i, file in enumerate(files):
    new_name = f"你的姓名_{i}.mp4"  # 這裡改成自己的名字
    shutil.copy(os.path.join(src_dir, file), os.path.join(dst_dir, new_name))

print("影片已複製並重新命名")