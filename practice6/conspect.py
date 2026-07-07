# open() - main function which takes 2 arguments - filename and mode
# there are 4 modes: "r" read - error if file doesn't exist
#                     "w" write - creates if doesn't exist
#                     "a" append - creates if doesn't exist
#                     "x" create - error if file exists

#                     "t" - Text - Default value. Text mode
#                     "b" - Binary - Binary mode (e.g. images)

print((open("testfile.txt").read()))