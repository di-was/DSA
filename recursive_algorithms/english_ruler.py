MAJOR_LENGTH = 10
NUM_OF_CM = 1


def draw_line(tick_length, tick_label='', up=True):
    line = "-" * tick_length

    line += ' ' + str(tick_label)
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')

    for j in range(1, 1+num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))



draw_ruler(NUM_OF_CM, MAJOR_LENGTH)
