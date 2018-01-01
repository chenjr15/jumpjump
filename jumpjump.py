import os
import time

def jump(dis=0,magic = 1.38):
    cmd = " adb shell input swipe 540 960 540 960 {duration}"
    duration = int(dis*magic)
    print(duration)
    os.system(cmd.format(duration =duration))
    
def getpng():
    os.system("adb shell screencap -p /sdcard/cap.png")
    os.system("adb pull /sdcard/cap.png")
    os.system("cap.png")

def getpos():
    
    os.system("getpos")
    time.sleep(2)
    pointstr = ""
    with open("point.txt") as f:
        pointstr = f.read()
    coord =  (pointstr.split(','))
    return (int(coord[0]),int(coord[1]),)
def getdistance():
    point = []
    point.append(getpos())
    print("Got point 1",point)
    point.append(getpos())
    print("Got point 2",point)
    distance = ((point[0][0]-point[1][0])**2+(point[0][1]-point[1][1])**2)**(1/2)
    return distance
def main():
    while True:
        getpng()
        time.sleep(1)
        print("Please be prepared.")
        distance = getdistance()
        jump(int(distance))
        time.sleep(2)
if __name__ == '__main__':
    main()