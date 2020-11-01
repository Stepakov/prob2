import sys
import platform

info = "OS info is \n{}\nPython version is {} {}".format(
    platform.uname(), sys.version, platform.architecture()
)

info2 = "Windows: {}\nArchitecture: {}\nSystem: {}\nPython version: {}".format(
    platform.uname(), platform.architecture(), platform.version(),
    sys.version
)

print( info )
print( '\n\n' )
print( info2 )

with open( 'os_info.txt', 'w' ) as ff:
    ff.write( info2 )