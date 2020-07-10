import os
import time

for i in range(100):

    os.popen('adb shell input tap 292 753')

    time.sleep(1)

    os.popen('adb shell input tap 63 133')

    time.sleep(1)

    print(i)