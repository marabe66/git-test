import os, glob
with open ("file_size.txt", "w") as outfile:
    files= glob.glob ("/Volumes/Video/*/*/*.avi")
    for file in files:
        size = os.path.getsize(file)
        if size < 2500000000:
            msize = str (round ((size/(1024*1024)),1)) + "M"
        out_name = os.path.basename(file)
        outfile.write(out_name + " , " + str(msize) + "\n")

# THIS IS A TEST COMMENT TO CHECK CONFLICT 2
