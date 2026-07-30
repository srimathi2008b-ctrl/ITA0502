import cv2
import numpy as np

image = cv2.imread("image10.png")

rows, cols = image.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

matrix = cv2.getAffineTransform(pts1, pts2)

result = cv2.warpAffine(image, matrix, (cols, rows))

cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", result)

cv2.imwrite("Affine_Output.png", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
