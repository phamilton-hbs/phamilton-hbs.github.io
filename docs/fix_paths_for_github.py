import os
import glob

for filepath in glob.iglob('./**/*.md', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('\\..\\_media\\', '\\..\\pages\\DSM\\DSM.github.io\\_media\\')
    with open(filepath, "w") as file:
        file.write(s)

