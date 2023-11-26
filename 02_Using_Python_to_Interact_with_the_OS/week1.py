import requests
import psutil
import shutil


requests.ConnectionError
print("Hello World")
print(psutil.cpu_stats())

du = shutil.disk_usage("/")

discUsagePerc = du.used / du.total
print("The current disc utilization is: {:3.2f}%".format(discUsagePerc * 100))
