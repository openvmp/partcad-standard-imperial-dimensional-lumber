import cadquery as cq

width = 4
height = 2
length = 120

if width == 1:
    real_width = (width - 0.25)*25.4
elif width >= 8:
    real_width = (width - 0.75)*25.4
else:
    real_width = (width - 0.5)*25.4

if height == 1:
    real_height = (height - 0.25)*25.4
elif height >= 8:
    real_height = (height - 0.75)*25.4
else:
    real_height = (height - 0.5)*25.4

real_length = length*25.4

result = (
    cq.Workplane("XY")
    .box(real_width, real_length, real_height)
    .translate((real_width/2.0, real_length/2.0, real_height/2.0))
    .edges("|Y").fillet(3.2)
)

show_object(result)
