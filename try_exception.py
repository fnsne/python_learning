import sys
try:
    file = open("file.txt")
    s=f.readlin()
    i = int(s.strip())
except  OSError as err:
    print("OS error: {0}".format(err))
except  ValueError:
    print("Value Error( Could not convert data to integer)")
except:
    print("Other error", sys.exc_info()[0])
