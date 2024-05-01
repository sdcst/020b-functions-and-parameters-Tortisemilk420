
def area_rectangle(length,width):
# determine the area of a rectangle
# parameters:
#   length: float value
#   width : float value
# return:
#   float value : area if it can be calculated
#   str : "could not calculate area" if an exception occurs
    #print(length)
    #print(width)

    try:
        length = float(length)
        width = float(width)    
        area = length * width
        return area
    except:
        return "could not calculate area"

x = area_rectangle(4,"hello")
print(x)
