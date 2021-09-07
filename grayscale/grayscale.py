import cv2
inp = input("""Please type below your image's path.
If your image and python file in same directory, 
you can just type image's name with its extension.
Type here : """)

image = cv2.imread(inp)
print("Now we are preparing your grayscale image. Just wait and have fun!")


def grayscale(image):
    for i in range(len(image)):
        for j in range(len(image[0])):
            b = image[i][j][0] / 3
            g = image[i][j][1] / 3
            r = image[i][j][2] / 3
            gr = b + g + r
            image[i][j][0], image[i][j][1], image[i][j][2] = gr, gr, gr
        print("Wait a little...")
    return image
grayscale(image)
cv2.imshow("Grayscale Image", image)
cv2.imwrite("grayscale.jpg",image)
print("Your grayscale image was saved under the directory of python file.")
cv2.waitKey(0)
cv2.destroyAllWindows()
