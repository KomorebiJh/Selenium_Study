import os
import re
import sys
import time

'''
前置：remount
  
1.adb install -r -d apk 

2.再cd data/app/apkName , 使用mv 命令把system/app/appName/目录下的 lib 和 oat文件夹替换掉system/app里的同名文件夹
"com.cvte.maxhub.launcher551-1"

3.再进入system/app下，先删除原有的apk文件，在push新文件，重命名为需要的文件：appName。

4.reboot

'''

ip = input("输入ip地址和端口：")
#ip地址需要加上端口号

appPath = input("粘贴apk路径:")
"""
删掉system和data目录下的文件后需要安装的apk路径。
	注意是写绝对路径，指向该文件
"""
PackageName = input("要删除的应用名:")
"""
用来删除/data/data/目录下的应用。
	注意是要写应用包名
		格式：com.cvet.maxhub.Mark
"""
	
os.system('adb connect %s' % ip)
time.sleep(3)
#等2s
os.system('adb root')
time.sleep(2)
#等2s
os.system('adb connect %s' % ip)
time.sleep(2)
#等2s
os.system('adb remount')
time.sleep(2)
#等2s

'''
Systemapp = input("要删除的system应用名:")

需要删除system的应用的时候，要把包名填进来。
	可以直接在下载的apk文件复制文件名，如批注下载后的文件名是：
		MaxhubMark_master_551_maxhub_sa06_release_R.3.1.88.apk
			直接取：MaxhubMark。
'''


os.system('adb shell rm -rf /data/app/com.cvte.maxhub.%s-1/' %PackageName)
time.sleep(5)
#等2s
os.system('adb install -r -d %s' % appPath)
#强制安装apk应用
time.sleep(30)
#等30s
'''
先删除data/app/里面的文件，重新安装，避免出现-2、-3的情况
'''

def Pattern1(appPath):
	#去掉_之后的字符串
	pattern = re.compile(r"Maxhub.*?_")
	pathname = pattern.findall(appPath)
	StrPath = ''.join(pathname)
	return StrPath

MaxhubAppPath = Pattern1(appPath)

def Pattern2(MaxhubAppPath):
	#只取Maxhub在内的
	pattern_1 = re.compile(r"[^_]")
	testname = pattern_1.findall(MaxhubAppPath)
	StrName = ''.join(testname)
	return StrName

SystemAppName = Pattern2(MaxhubAppPath)

"""
以上两个函数用来获取应用的名字，用于删除system/app文件的
"""
	
os.system('adb shell rm -rf /system/app/%s/%s.apk' %(SystemAppName,SystemAppName))
time.sleep(2)
#等2s

'''
删system的文件
'''

os.system('adb shell mv -f /data/app/com.cvte.maxhub.%s-1/lib/ /system/app/%s/' %(PackageName,SystemAppName))
time.sleep(4)
#等2s
os.system('adb shell mv -f /data/app/com.cvte.maxhub.%s-1/oat/ /system/app/%s/' %(PackageName,SystemAppName))
time.sleep(4)
#等2s

'''
把system/app/appName/目录下的 lib 和 oat文件夹替换掉system/app里的同名文件夹
'''
	
os.system('adb push %s /system/app/%s/%s.apk' %(appPath,SystemAppName,SystemAppName))
time.sleep(30)
#等30s
os.system('adb reboot')
time.sleep(3)
#等2s
os.system('exit')
'''
把文件推到system/app目录下并修改名字
'''

'''
if __name__ == '__main__':
    print "start!"
else:
    print "test'"
'''