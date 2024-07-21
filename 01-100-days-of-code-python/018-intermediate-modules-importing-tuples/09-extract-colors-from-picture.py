# Extract the colors from a photo of the picture we are going to paint

import colorgram

colors = colorgram.extract("damien-horst.jpg", 20)

palette = []
for c in colors:
    r = c.rgb.r
    g = c.rgb.g
    b = c.rgb.b
    palette.append((r, g, b))

print(palette)  # Copy this palette in mOnPicassJofn
