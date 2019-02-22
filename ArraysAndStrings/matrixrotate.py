def rotate(image):
    layer = len(image) / 2
    length = len(image)
    for i in range(layer):
        #rotate
        last = length - 1 - i
        for j in range(i, last, 1):
            top = image[i][j]
            right = image[j][last]
            bottom = image[last][last-j+i]
            left = image[last-j+i][i]

            temp = right
            image[j][last] = top
            image[i][j] = left
            image[last-j+i][i] = bottom
            image[last][last-j+i] = temp
    return True
