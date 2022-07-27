import cv2
import os

path = "opencv/rouizi/"

video = cv2.VideoCapture(os.path.join(path, "videos/pexels-cottonbro-5532768.mp4"))

frame_width  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps          = int(video.get(cv2.CAP_PROP_FPS))

print("Width  =", frame_width)
print("Height =", frame_height)
print("FPS    =", fps)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("meu_novo_video.avi", fourcc, fps, (frame_width, frame_height))

def open_video():
    while True:
        success, frame = video.read()
        # cv2.imshow("frame", frame)
        output.write(frame)
        if cv2.waitKey(20) == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()


# x = input("Press enter to continue")
open_video()