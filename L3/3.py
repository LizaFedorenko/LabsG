import numpy as np
from PIL import Image, ImageDraw


with open('DS3.txt', 'r') as file:
    lines = file.readlines()
points = [tuple(map(int, line.strip().split())) for line in lines]
alpha = 40

width = 2222
height = 2222

canvas = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(canvas)

rotation_center = (480, 480)
alpha_rad = np.radians(alpha)
rotation_matrix = np.array([[np.cos(alpha_rad), -np.sin(alpha_rad)],
                            [np.sin(alpha_rad), np.cos(alpha_rad)]])

transformed_points = []
for point in points:
    point_vector = np.array(point) - np.array(rotation_center)
    transformed_point_vector = np.dot(rotation_matrix, point_vector)
    transformed_point = tuple(np.round(transformed_point_vector + np.array(rotation_center)).astype(int))
    transformed_points.append(transformed_point)

point_color = (0, 0, 255)  # Синій колір
for point in transformed_points:
    draw.point(point, fill=point_color)

new_size = (960, 960)
canvas = canvas.resize(new_size)
canvas.save("result.png")
canvas.show()
file.close()