"""
Calculate angle b/w given hour and minute value
"""


def find_angle(h, m):
    if h == 12:
        h = 0
    if m == 60:
        m = 0
    angle = abs((5.5 * m) - (30 * h))
    return angle


angle = find_angle(12, 0)
if angle == 0:
    print("Hour and min hand overlapped")
else:
    print(f"Angle is - {angle}")
