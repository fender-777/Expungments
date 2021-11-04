import os
import time
import shutil


def scan_and_move():
    path = '.'
    files = os.listdir(path)
    for pdf_file in files:
        if pdf_file.endswith('pdf'):
            #        print("PDF name is {}".format(pdf_file))
            # this gives modified time in seconds since the Epoch
            mod_time_epoch = os.path.getmtime(pdf_file)

            # this formats the seconds into a yyyymm format
            mod_time = time.strftime('%Y%m', time.localtime(mod_time_epoch))
            # print("ModTime is {}".format(modTime))

            # our directory is CWD/modTime
            dirPath = os.path.join(path, mod_time)
            #            print(dirPath)

            if not os.path.exists(dirPath):
                #                print("Directory {} not present, making it".format(dirPath))
                os.mkdir(dirPath)
            #            print("Moving pdf {} to {}".format(pdf_file, dirPath))
            shutil.move(pdf_file, dirPath)

scan_and_move()
