import sys

print("There are " + str(len(sys.argv) - 1) + " arguements.")
for ar in sys.argv[1:]:
    print(str(ar))