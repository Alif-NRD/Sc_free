import os, sys
os.system("git pull")
try:
    __import__("Alif").NRD()
except Exception as e:
    exit(str(e))
