from module_func import *

# основная программа
printRectangle(-1, 5, "output")
PrintSquare(3, "output1")

# Test 1:
module_func.printRectangle(4, 0, "output")
module_func.PrintSquare(3, "output1")
print("test 2")
# Test 2:
module_func.printRectangle(0, 0, "output")
module_func.PrintSquare(0, "output1")
print("test 3")
# Test 3:
module_func.printRectangle(-100, 0, "output")
module_func.PrintSquare(-3, "output1")
print("test 4")
# Test 4:
module_func.printRectangle(4, 5, "output")
module_func.PrintSquare(3, "output1")
print("Complete")
print("test 5")
# Test 5:
module_func.printRectangle(0, 0, "output")
module_func.PrintSquare(0, "output1")
