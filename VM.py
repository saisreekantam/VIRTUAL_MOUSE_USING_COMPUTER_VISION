import cv2
import mediapipe as mp
import pyautogui
import numpy as np

# Initialize Mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Screen resolution
screen_width, screen_height = pyautogui.size()

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Virtual drawing canvas
canvas = np.zeros((720, 1280, 3), np.uint8)

# Set previous position for drawing
prev_x, prev_y = 0, 0

while True:
    # Read a frame from the webcam
    success, frame = cap.read()
    if not success:
        break

    # Flip the frame horizontally for natural hand movement
    frame = cv2.flip(frame, 1)
    frame_height, frame_width, _ = frame.shape

    # Convert the frame to RGB as Mediapipe expects RGB input
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect hands
    result = hands.process(rgb_frame)

    # Get the hand landmarks
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Extract landmarks for the index finger and thumb
            landmarks = hand_landmarks.landmark

            # Get coordinates of the index finger (landmark 8) and thumb (landmark 4)
            index_finger_tip = landmarks[8]
            thumb_tip = landmarks[4]

            # Convert normalized landmark coordinates to pixel coordinates
            index_finger_x = int(index_finger_tip.x * frame_width)
            index_finger_y = int(index_finger_tip.y * frame_height)
            thumb_x = int(thumb_tip.x * frame_width)
            thumb_y = int(thumb_tip.y * frame_height)

            # Convert hand coordinates to screen coordinates for mouse control
            screen_x = int(index_finger_tip.x * screen_width)
            screen_y = int(index_finger_tip.y * screen_height)

            # Move mouse cursor using the index finger
            pyautogui.moveTo(screen_x, screen_y)

            # Check if thumb and index finger are close enough (pinching gesture) for a click
            if abs(index_finger_x - thumb_x) < 30 and abs(index_finger_y - thumb_y) < 30:
                pyautogui.click()

            # Virtual Drawing
            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = index_finger_x, index_finger_y

            # Draw on the canvas if index finger is up (landmark 8 higher than landmark 6)
            if landmarks[8].y < landmarks[6].y:
                cv2.line(canvas, (prev_x, prev_y), (index_finger_x, index_finger_y), (0, 255, 0), 5)
                prev_x, prev_y = index_finger_x, index_finger_y
            else:
                prev_x, prev_y = 0, 0

            # Draw the hand landmarks on the original frame
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Combine canvas and camera frame for drawing visualization
    frame = cv2.add(frame, canvas)

    # Display the frame
    cv2.imshow("Virtual Mouse and Drawing", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

