import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img,
            "Sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Mercury",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Venus",
            (180,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Earth",
            (240,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Mars",
            (320,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Jupiter",
            (400,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Saturn",
            (480,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Uranus",
            (560,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.putText(img,
            "Neptune",
            (640,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255, 255, 255)
            )

cv2.imshow("Display Image", img)
cv2.waitKey(0)
cv2.imwrite("Solar_SystemWithNames.jpg", img)