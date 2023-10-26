from PIL import Image, ImageDraw

with open('DS3.txt', 'r') as file:
    lines = file.readlines()

points = []

for line in lines:
    x, y = map(int, line.strip().split())
    points.append((x, y))
width = 960
height = 540
canvas = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(canvas)

point_size = 3
point_color = (255, 0, 0)

for x, y in points:
    draw.ellipse(
        [(x - point_size, y - point_size), (x + point_size, y + point_size)],
        fill=point_color,
        outline=point_color,
    )

canvas.save("result.png")
canvas.show()
file.close()