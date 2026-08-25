import cv2
import numpy as np

# 이미지 불러오기
image = cv2.imread("sample.jpg")

# 이미지가 제대로 불러와졌는지 확인
if image is None:
    print("sample.jpg 파일을 찾을 수 없습니다.")
    exit()

# BGR 이미지를 HSV로 변환
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 빨간색 범위 설정
lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

# 빨간색 영역 검출
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# 두 마스크 합치기
mask = mask1 + mask2

# 빨간색 부분만 추출
result = cv2.bitwise_and(image, image, mask=mask)

# 결과 화면에 표시
cv2.imshow("Original", image)
cv2.imshow("Red Filtered", result)

cv2.waitKey(0)
cv2.destroyAllWindows()