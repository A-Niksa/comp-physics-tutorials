# physical parameters:
plate_width = 0.1
plate_height = 0.1
hole_width = 0.04  # the hole is assumed to be rectangular
hole_height = 0.04  # the hole is assumed to be rectangular

# boundary conditions:
plate_left_temperature = 323.0
plate_right_temperature = 283.0
plate_top_temperature = 303.0
plate_bottom_temperature = 303.0
hole_left_temperature = 303.0
hole_right_temperature = 303.0
hole_top_temperature = 303.0
hole_bottom_temperature = 303.0
initial_plate_temperature = 303.0
room_temperature = 303.0

# solver parameters:
rows = 100
columns = 100
tolerance = 1E-1
# NOTE that hx and hy should be determined in a way that hx = hy
hx = plate_width / rows
hy = plate_height / columns

# graphical config:
default_hole_temperature = 283.0  # a temperature for the hole so that it'd appear "different" from the rest of the plate
