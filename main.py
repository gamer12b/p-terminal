import random
import datetime
from re import sub
import time
import json
import encodings
from tkinter.tix import InputOnly
import uuid
import pkg_resources
import screeninfo
import pip
import secrets
import shutil
import sys
import os
import subprocess
import socket
import speedtest_cli
import sysconfig
import platform
import pytube
import psutil
import pkg_resources
from os import name
print("="*40, " Commands ","="*40)
list_of_cmds = """
          [1] help
          [2] shutdown
          [3] restart
          [4] ip
          [5] speedtest
          [6] custom command
          [7] clear
          [8] manage files
          [9] manage folder/s
          [10] kill proccess
          [11] Python modules
          [12] ls
          [13] chdir
          """
print(list_of_cmds)
while True:
    command = input(os.getcwd()+": SlowPC4@root> ")
    if command == "help":
        print("="*40, " Commands ","="*40)
        print(list_of_cmds)
    if command == "shutdown":
        exit()
    if command == "restart":
        os.execv(sys.executable, ["python"] + sys.argv)
    if command == "ip":
        print("Host: "+socket.gethostname())
        ip = socket.gethostbyname(socket.gethostname())
        print("Local IP: "+str(ip))
    if command == "speedtest":
        subprocess.check_call("speedtest")
    if command == "custom command":
        o = input("Enter type/other> ")
        if o == "python":
            e = input("Enter pip/python)> ")
            if e == "python":
                subprocess.check_call("python")
            if e == "pip":
                e = input("Enter install/upgrade/uninstall/upgrade all ")
                if e == "upgrade":
                    subprocess.check_call(f"python -m pip install --upgrade pip")
                if e == "uninstall":
                    e = input("Enter package ")
                    subprocess.check_call(f"python -m pip uninstall {e}")
                if e == "install":
                    e = input("Enter package ")
                    subprocess.check_call(f"python -m pip install {e}")
                if e == "upgrade all":
                    pck = [dist.project_name for dist in pkg_resources.working_set]
                    subprocess.call("pip install --upgrade " + " ".join(pck),shell=True)
    if command == "clear":
        if name == "nt":
            os.system("cls")
        else:
            os.system("clear")
    if command == "ls":
        print("="*40,"Files","="*40)
        print(os.listdir(os.getcwd()))
    if command == "chdir":
        e = input("Enter new dir: ")
        os.chdir(e)
    if command == "manage files":
        print("""
              [1] Create file
              [2] Delete file
              [3] Overwrite file
              [4] Overwrite multiple files
              [5] Delete multiple files
              
              """)
        e = input("Enter: ")
        if e == "1":
            i = input("File name: ")
            a = open(i, "a")
            a.close()
        if e == :