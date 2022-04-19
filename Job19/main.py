def draw_rectangle(width, height):
    w = "-" * width
    s = " " * width
    for i in range(height+1):
        if i == 0 or i == height:
            print("|" + w + "|")
        else:
            print("|" + s + "|")

draw_rectangle(5, 6)