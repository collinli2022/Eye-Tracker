from PIL import Image, ImageDraw
import face_recognition
import cv2


cap = cv2.VideoCapture(0)

face_landmarks_list = ""
count = 0

while True:
	_, frame = cap.read()

	if(count % 1 == 0):
		# Find all facial features in all the faces in the image
		face_landmarks_list = face_recognition.face_landmarks(frame)
		#print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

		# 5 = left
		# 6 = right
		if len(face_landmarks_list) >= 1:
			temp = face_landmarks_list[0]
			cv2.line(frame, max(temp['right_eye']), min(temp['right_eye']), (0, 255, 0), 5)
			cv2.line(frame, min(temp['left_eye']), max(temp['left_eye']), (0, 255, 0), 5)
			cv2.imshow('image', frame)

	
	count += 1
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
# Load the jpg file into a numpy array
