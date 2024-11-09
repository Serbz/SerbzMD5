try:
    import traceback
except:
    try:
        import os

        os.system("python -m pip install traceback")
    except:
        pass
    pass
try:
    import asyncio, datetime, fnmatch, math, os, random, re, string, sys, time, colorama, ahk, optparse, hashlib
    from string import ascii_lowercase
    from colorama import init, Fore, Back, Style
    from dotenv import load_dotenv
    from os import system, name
    import psutil, numpy
    from os.path import join, getsize
except ModuleNotFoundError:
    print(ModuleNotFoundError)
    import os
    try:
        import re
    except:
        os.system("python3.9 -m pip install re")
        os.execv(sys.executable, ['python'] + sys.argv)
        SystemExit()
        sys.exit()
    def find_between(s, first, last):
        try:
            start = s.index(first) + len(first)
            end = s.index(last, start)
            return s[start:end]
        except ValueError:
            return ""
    strStr = ModuleNotFoundError
    stringy = find_between(traceback.format_exc(), "\'", "\'")
    ##IF STRINGY IS MISSING IMPORT THAT DOES NOT MATCH PIP INSTALL PACKAGE NAME PUT TRY EXCEPTS HERE WHERE Stringy=
    try:
        os.system("python -m pip install " + stringy + " --compile --no-cache-dir")
    except:
        os.system("python3.9 -m pip install " + stringy + " --compile --no-cache-dir")
        pass
    try:
        os.system("python -m pip install python-" + stringy + " --compile --no-cache-dir")
    except:
        os.system("python3.9 -m pip install python-" + stringy + " --compile --no-cache-dir")
        pass
    try:
        os.system("python -m pip install " + stringy + "-python --compile --no-cache-dir")
    except:
        os.system("python3.9 -m pip install " + stringy + "-python --compile --no-cache-dir")
        pass
    try:
        os.system("python -m pip install py" + stringy + " --compile --no-cache-dir")
    except:
        os.system("python3.9 -m pip install py" + stringy + " --compile --no-cache-dir")
        pass
    import sys
    os.execv(sys.executable, ['python'] + sys.argv)
    SystemExit()
    sys.exit()
    pass
    

Md5HashList = []
Md5HashFile = input(r"Name for MD5 npy file to use/create: ")
Generate_Compare = ""
while (Generate_Compare == ""):
    Generate_Compare = str(input(r"[G]enerate or [C]ompare?: ")).lower()
    print(Generate_Compare)
    if Generate_Compare != "g" and Generate_Compare != "c":
        print("You must input G or C")
        Generate_Compare = ""


async def Init():
    global Md5HashList, Generate_Compare
    #add inputs here
    #hash gen is done need inputs for generate or compare
    wdir = r"E:\\GP"
    async def generate_md5_hash(filename, counter, GC=Generate_Compare, block_size=2 ** 20, progress_blocks=128):
        global Md5HashList
        md5 = hashlib.md5()
        blocks = 0
        total_blocks = 1 + (os.path.getsize(filename) / block_size)
        with open(filename, 'rb') as file:
            while True:
                try:
                    data = file.read(block_size)
                except:
                    data = False
                    pass
                if not data:
                    break
                md5.update(data)
                # Display progress in the command line
                #if (blocks % progress_blocks) == 0:
                #    percentage_string = "\n{0}%".format(100 * blocks / total_blocks)
                #    sys.stdout.write(percentage_string)
                #    sys.stdout.flush()
                blocks += 1
        #sys.stdout.buffer.write(str(str(counter)+". "+str(filename)+"\n"+str(md5.hexdigest())+"\n\n").encode('utf8'))
        print(str(str(counter)+". "+str(filename)+"\n"+str(md5.hexdigest())))
        if GC == "g":
            Md5HashList.append([str(filename),md5.hexdigest()])
        #print(Md5HashList)
        return md5.hexdigest()
        
    async def directories(wdir):
        dirs = [x[0] for x in os.walk(wdir)]
        return dirs
    async def files(dirs):
        counter = 0
        filepaths = []
        for dir in dirs:
            for file in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, file)) and str(r"driveupload") not in os.path.join(dir, file) and \
                    str(r"drivedownload") not in os.path.join(dir, file):
                    filepaths.append(os.path.join(dir, file))
        return filepaths
        
    errors = []
     ######################   
    if Generate_Compare == "g":
        dirs = await directories(wdir)
        filepaths = await files(dirs)
        counter = 0
        for each in filepaths:
            counter = counter + 1
            print(str(str(counter)+". "+str(each)+"\n"))
        counter = 0
        for each in filepaths:
            ### DUPE ### CLEAN ###
            counter = counter + 1
            try:
                await generate_md5_hash(filename=each, counter=counter)
            except Exception as e:
                errors.append(e)
                print(e)
                pass
        numpy.save(fr"{wdir}\\md5check\{Md5HashFile}"+".npy", Md5HashList)
        for each in Md5HashList:
            print(each)
     #########################   
    elif Generate_Compare == "c":
        Md5HashList = numpy.load(fr"{wdir}\\md5check\{Md5HashFile}"+".npy")
        counter = 0
        for each in Md5HashList:
            if os.path.exists(each[0]) and os.path.isfile(each[0]):
                ### DUPE ### CLEAN ###
                counter = counter + 1
                md5 = None
                try:
                    md5 = await generate_md5_hash(filename=each[0], counter=counter)
                except Exception as e:
                    errors.append(e)
                    print(e)
                    pass
                if md5 is not None:
                    if md5 == each[1]:
                        #print(fr"File: {each[0]}"+"\n"+fr"Md5:        {md5}"+"\n"+fr"Stored Md5: {each[1]}"+"\n"+fr"MD5 Check Passed!"+"\n\n")
                        print(fr"{each[1]}"+"\n"+fr"MD5 Check Passed!"+"\n\n")
                    else:
                        #print(fr"File: {each[0]}"+"\n"+fr"Md5:        {md5}"+"\n"+fr"Stored Md5: {each[1]}"+"\n"+fr"MD5 Check FAILED!"+"\n\n")
                        print(fr"{each[1]}"+"\n"+fr"MD5 Check FAILED!"+"\n\n")
    print(r"Done!")
    numpy.savetxt(fr"{wdir}\\md5check\Errors"+".txt", errors)
    print("errors saved")
    return
    
  
loop = asyncio.get_event_loop()
loop.create_task(Init())
loop.run_forever()
