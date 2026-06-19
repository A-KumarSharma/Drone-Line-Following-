# 🚁 Autonomous Line Following Drone using PySimVerse

## Overview

This project demonstrates an autonomous line-following drone built using **PySimVerse**, **OpenCV**, **CVZone**, and color-based computer vision techniques.

The drone detects a colored line in the simulation environment and follows it automatically using a simple **Bang-Bang Controller**. The controller continuously adjusts the drone's yaw (rotation) based on the line position relative to the center of the camera frame.

---

## Features

* Real-time drone simulation with PySimVerse
* Autonomous takeoff
* Color-based line detection
* Contour tracking using OpenCV and CVZone
* Bang-Bang control algorithm
* Live visualization of detection results
* Simple and lightweight implementation

---
## DEMO VIDEO

---

## Technologies Used

* Python 3.x
* PySimVerse
* OpenCV
* CVZone
* NumPy

---

## Installation

### Clone the Repository

```bash
[git clone https://github.com/yourusername/drone-line-follower.git](https://github.com/A-KumarSharma/Drone-Line-Following-.git)
cd drone-line-follower
```

### Install Dependencies

```bash
pip install pysimverse
pip install opencv-python
pip install cvzone
pip install numpy
```

---

## Project Structure

```text
project/
│
├── main.py
├── README.md
```

---

## How It Works

### 1. Connect to Drone

The script initializes a connection to the PySimVerse drone:

```python
drone = Drone()
drone.connect()
drone.streamon()
```

---

### 2. Take Off

The drone automatically takes off to a height of 25 units.

```python
drone.take_off(takeoff_height=25)
```

---

### 3. Detect the Line

A specific color range is selected in HSV space:

```python
hsvVals = {
    'hmin': 0,
    'smin': 113,
    'vmin': 73,
    'hmax': 10,
    'smax': 229,
    'vmax': 255
}
```

The detected color mask is used to find contours representing the target line.

---

### 4. Calculate Error

The horizontal distance between:

* Frame center
* Detected line center

is calculated:

```python
error = center_x - cx
```

---

### 5. Bang-Bang Controller

The drone adjusts its yaw based on the line position.

```python
if abs(error) < deadband_px:
    yaw = 0
elif error < 0:
    yaw = yaw_power
else:
    yaw = -yaw_power
```

---

### 6. Move Forward

The drone continuously moves forward while correcting its heading.

```python
drone.send_rc_control(
    0,      # left/right
    20,     # forward
    0,      # up/down
    yaw     # rotation
)
```

---

## Controls

| Key | Action       |
| --- | ------------ |
| Q   | Quit Program |

---

## Parameters

### Detection Settings

```python
hsvVals
```

Adjust these values depending on the line color.

### Control Settings

```python
deadband_px = 2
yaw_power = 0.4
```

| Parameter   | Description                     |
| ----------- | ------------------------------- |
| deadband_px | Allowed error before correction |
| yaw_power   | Turning strength                |

---

## Output Window

The application displays:

1. Original Camera Feed
2. Color Detection Result
3. Binary Mask
4. Contour Detection

These views help visualize the line tracking process in real time.

---

## Future Improvements

* PID Controller
* Dynamic speed adjustment
* Multi-color line tracking
* Object avoidance
* Waypoint navigation
* Deep Learning based path following

---

## Example Workflow

```text
Take Off
    ↓
Detect Line
    ↓
Find Contour Center
    ↓
Calculate Error
    ↓
Adjust Yaw
    ↓
Move Forward
    ↓
Repeat
```

---

## Author

Developed using:

* PySimVerse
* OpenCV
* CVZone

For educational purposes in autonomous drone navigation and computer vision.

---

Feel free to modify, distribute, and use this project for learning and research purposes.
