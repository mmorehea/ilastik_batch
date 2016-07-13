import os
import sys
import glob
import ConfigParser
import code
import subprocess

folderpath = sys.argv[1]

config = ConfigParser.ConfigParser()
configlist = config.read("./config.ini")

l = glob.glob(os.path.join(folderpath, "*"))

ilastikpath = config.get("info", "PathToIlastik")
ilastikprojectpath = config.get("info", "IlastikProject")

#code.interact(local=locals())

for each in l:
    s = ilastikpath + " --headless --project=" + ilastikprojectpath + " " + each
    print s
    subprocess.call(s, shell=True)
