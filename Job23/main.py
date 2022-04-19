def draw_triangle(height):
    x = height
    for i in range(height):
        if i == height-1:
            print(" /" + "_"*((height*2)-2) + "\\")
        else:
            print(" "*(x) + "/" + " "*(i*2) + "\\")
            x -= 1

draw_triangle(7)