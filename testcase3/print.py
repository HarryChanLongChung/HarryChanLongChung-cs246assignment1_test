import sys

print("There are " + str(len(sys.argv) - 1) + " arguements.")
if len(sys.argv) == 1:
    for ar in sys.argv[1:]:
        print(str(ar))
print("No arguments")