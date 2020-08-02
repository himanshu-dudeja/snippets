# Question
# A floppy disk shows f bytes free and
# u bytes used. If you delete a file of size
# o bytes and create a new file of size
# n bytes, how many free bytes will the floppy disk have?
# f, u, o and n are user-entered values.


def floppy():
    f = int(input("Enter floppy disk free(f) bytes - "))
    u = int(input("Enter floppy disk used(u) bytes - "))
    o = int(input("Enter file size to be deleted - "))
    n = int(input("Enter file size for new file to be created - "))

    total_space = f + u
    print("Total Spcae - ", total_space)

    if u >= o:
        u = u - o
        f = f + o

        if f >= n:
            f = f - n
            u = u + n
        else:
            print("Free space should be greater than new file creation size")
            exit()
    else:
        print("Used Space should be greater than the file size mentioned to delete")
        exit()

    print("Free Space left is - ", f)
    print("Used Space is - ", u)
    print("Total space - ", f + u)


floppy()
