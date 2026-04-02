def bilinear_resize(image, new_h, new_w):
    """
    Resize a 2D grid using bilinear interpolation.
    """
    # Write code here
    ## Calculate (x, y)
    import math
    #import numpy as np
    new_image = [[0] * new_w for _ in range(new_h)] 
    h = len(image)
    w = len(image[0])
    for i in range(new_h):
        for j in range(new_w):
            if new_h == 1:
                src_y = 0
            else:
                src_y = i*((len(image) - 1) / (new_h - 1))
            src_x = j*((len(image[0]) - 1) / (new_w - 1))

            y0 = math.floor(src_y)
            x0 = math.floor(src_x)

            dy = src_y - y0
            dx = src_x - x0

            x1 = min(x0 + 1, w - 1)
            y1 = min(y0 + 1, h - 1)
            
            v = image[y0][x0]*(1-dx)*(1-dy) + image[y0][x1]*dx*(1-dy) + image[y1][x0]*(1-dx)*dy + image[y1][x1]*dx*dy
            new_image[i][j] = v

    return new_image
            