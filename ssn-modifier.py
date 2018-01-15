from os import listdir , remove , rename
import shutil
from os.path import join , isdir , isfile , dirname , abspath

basePath = 'SSN-Intranet-Downloader'
realBase = ''
replaceBase = ''
startCode = 'file:///'

def getCurrentDir():
    currentDir = dirname(abspath(__file__))
    return currentDir.replace(basePath , '' , 1)

replaceBase = getCurrentDir()

def gethref(filePath):
    global status
    outfile = filePath.replace('.html' , 't.html' , 1)
    out = open(outfile , 'a')
    with open(filePath , 'r') as openFile:
        for line in openFile:
            if 'href' in line:
                if basePath in line:
                    startIndex = line.rindex('file:///')
                    endIndex = line.rindex(basePath)

                    out.write(line[:startIndex])
                    out.write(startCode + replaceBase + line[endIndex:])
            else:
                out.write(line)        
    remove(filePath)
    rename(outfile , filePath)

def doforallfiles(SsnIntranetPath):
    for content in listdir(SsnIntranetPath):
        if isdir(join(SsnIntranetPath , content)):
            doforallfiles(join(SsnIntranetPath , content))
        elif '.html' in content:
            gethref(join(SsnIntranetPath , content))
                

doforallfiles(join(replaceBase ,basePath))