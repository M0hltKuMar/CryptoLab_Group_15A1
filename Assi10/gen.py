import os

SIZE = 1024 * 1024  # 1 MB

with open("linux_urandom.bin", "wb") as f:
    f.write(os.urandom(SIZE))

print("Generated 1 MB using Linux OS random generator.")
