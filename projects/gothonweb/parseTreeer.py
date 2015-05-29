level = 1
def parse(item, end = "root"):
    global level
    if isinstance(item, (list, tuple)):
        print "["
        for e in item:
            level += 1
            printSpaces(level)
            parse(e, end)
            level -= 1
        printSpaces(level)
        print "] end(%s)" % (end)
    elif type(item) is dict:
        print "{"
        for key in item:
            level += 1
            printSpaces(level)
            print key, ":",
            parse(item[key], key)
            level -= 1
        printSpaces(level)
        print "} end(%s)" % (end)
    else:
        print item
    
def printSpaces(level):
    for i in range(1, level):
        print "   ",
