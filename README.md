# Virtual Mouse and Drawing with Hand Gestures

This project allows you to control your computer's mouse and draw virtually using hand gestures, leveraging **Mediapipe**, **OpenCV**, and **PyAutoGUI**. The index finger moves the cursor, and pinching the thumb and index finger performs a mouse click. Additionally, you can draw on a virtual canvas using your hand.

## Features

- **Mouse Control**: Move the mouse using the index finger's position.
- **Click Gesture**: Simulate a mouse click when the thumb and index finger are close together.
- **Virtual Drawing**: Draw on the screen using the index finger when it is lifted.

## Requirements

- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI
- NumPy

## How It Works

1. **Initialization**:
   - **Mediapipe Hand Detector**: Initializes the hand tracking model to detect hand landmarks.
   - **PyAutoGUI**: Used for controlling the mouse cursor.
   - **OpenCV**: Captures video from the webcam and displays the output.

2. **Video Capture**:
   - Opens the webcam and reads frames continuously.

3. **Hand Detection**:
   - Converts the frame to RGB and processes it to detect hand landmarks.
   - Extracts the coordinates of the index finger tip and thumb tip.

4. **Mouse Control**:
   - Maps the index finger's position to screen coordinates and moves the mouse cursor accordingly.

5. **Click Detection**:
   - Checks if the index finger and thumb are close together to simulate a mouse click.

6. **Virtual Drawing**:
   - Draws on a virtual canvas if the index finger is lifted, by connecting the previous and current positions with a line.

7. **Display Output**:
   - Combines the camera frame with the virtual drawing canvas and displays the result in a window.

8. **Exit**:
   - Closes the application when the 'q' key is pressed.

## Usage

1. Clone this repository and install the required packages:
   ```bash
   pip install opencv-python mediapipe pyautogui numpy, now use your hand gestures for control and press q to exit
    
