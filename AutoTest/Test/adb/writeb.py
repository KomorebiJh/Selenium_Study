import os
import time


os.popen('adb connect 172.18.141.54' )
'''
#白板启动退出
while True:

    os.popen('adb shell input tap 800 520')

    time.sleep(3)

    os.popen('adb shell input swipe 100 100 200 500')
    time.sleep(3)

    os.popen('adb shell input tap 50 1050')

    time.sleep(2)

    os.popen('adb shell input tap 75 960')
    time.sleep(2)

'''
'''
#侧边栏开启关闭功能验证

for i in range(1000):
  os.popen('adb shell input tap 4.8 695')

  time.sleep(1)

  os.popen('adb shell input tap 25 695')
  time.sleep(1)
'''
''' 
for i in range(100):
    os.popen('adb shell input tap 3238 422')

    time.sleep(1)
'''
for i in range(100):
    os.popen('adb shell input tap 6.8 1284')
    time.sleep(1)

    os.popen('adb shell input tap 47.7 1650')
    time.sleep(1)

    os.popen('adb shell input tap 661 1036')
    time.sleep(5)

    os.popen('adb shell input tap 2142 1323')
    time.sleep(1)

    os.popen('adb shell input tap 86 1743')
    time.sleep(3)

    os.popen('adb shell input tap 191 1743')
    time.sleep(1)

    os.popen('adb shell input tap 2127 1149')
    time.sleep(1)

    os.popen('adb shell input tap 1674 1149')
    time.sleep(1)

    os.popen('adb shell input tap 2310 673')
    time.sleep(1)

    os.popen('adb shell input tap 404 1741')
    time.sleep(1)

    os.popen('adb shell input tap 1596 1047')
    time.sleep(5)

    os.popen('adb shell input tap 90 2089')
    time.sleep(1)



