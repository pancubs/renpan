import sys

def pyversion():
    return '%s.%s.%s' % (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)
