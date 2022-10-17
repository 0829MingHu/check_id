import os

rootpath=r"/home/chenj0g/rgb_flow/rgb_feature_npz"#文件路径
r1=r"/home/chenj0g/rgb_flow/rgbflow1"
r2=r"/home/chenj0g/rgb_flow/rgbflow2"
r3=r"/home/chenj0g/rgb_flow/rgbflow3"
r4=r"/home/chenj0g/rgb_flow/rgbflow4"#四个文件夹路径
s=set()
for curdir,roots,files in os.walk(r1):
    s.add(curdir.split('/')[-1])
for curdir,roots,files in os.walk(r2):
    s.add(curdir.split('/')[-1])
for curdir,roots,files in os.walk(r3):
    s.add(curdir.split('/')[-1])
for curdir,roots,files in os.walk(r4):
    s.add(curdir.split('/')[-1])


for curdir,roots,files in os.walk(rootpath):
    for file in files:
        filename=file.replace('-rgb.npz','')
        if not filename in s:
            print(file)
            print(curdir+'/'+file)