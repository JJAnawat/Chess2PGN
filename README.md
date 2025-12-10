# Chess2PGN

This repository contains the final project for **Introduction to Digital Imaging (2110431)**, which focuses on detecting and tracking chess moves from video footage. The project aims to convert chessboard states from video frames into Portable Game Notation (PGN) format using advanced computer vision and machine learning techniques.

---

## Table of Contents
- [Overview](#overview)
- [Approach](#approach)
- [Model](#models)
  - [Chess Piece Recognition](#chess-piece-recognition)
- [Data](#data)
- [Pipeline](#pipeline)
- [Evaluation](#evaluation)
- [Team Roles](#team-roles)
- [Challenges and Improvements](#challenges-and-improvements)

---

## Overview
The Chess Move Tracking system extracts each frame from a video, identifies chessboard positions, detects the pieces, and tracks their movements. It ultimately converts the detected changes into FEN (Forsyth-Edwards Notation) and then into PGN (Portable Game Notation). The key objective is to automate the tracking of chess moves from video footage with high accuracy.

---

## Approach
1. **Extract Frames**: Each frame of the input video is extracted for analysis.
2. **Model Inference**: Each frame is processed through object detection models to detect chessboard corners and recognize the chess pieces.
3. **FEN to PGN Conversion**: The detected chessboard positions are converted from FEN to PGN.

---

## Model

### Chess Piece Recognition
- **Model Used**: YOLOv11m
- **Training**:
  - Epochs: 100
  - Batch Size: 16
- **Data**: **additional datasets** provided by the course instructor.
- **Weight Link**: https://drive.google.com/uc?id=1J2o2LK97blBXXD7mg_RuP6w1LQLvrNbA
---

## Data
**Chessboard Corner Detection Data**: Manually labeled data for chessboard corner detetcion using Roboflow.

**Chess Piece Recognition Data**: A combination of datasets from RoboFlow and additional custom datasets provided by the course instructor.

---

## Pipeline
![Screenshot 2024-12-12 155353](https://github.com/user-attachments/assets/167563e9-5e03-4154-baba-6493fb8754e9)
![Screenshot 2024-12-12 155501](https://github.com/user-attachments/assets/7bd7c043-dcc1-4d7c-9d72-9c6843bdded5)

1. **Chessboard Corner Detection**
   - Identify the four corners of the chessboard in each frame using YOLOv8.
   - Crop and align the board area for further processing.
2. **Chess Piece Recognition**
   - Detect chess pieces in the cropped chessboard image using YOLOv11m.
   - Map the detected positions to chessboard slots.
3. **FEN to PGN Conversion**
   - Convert the detected chessboard positions from FEN to PGN.
   - Aggregate PGN data into a CSV file.

---

## Evaluation
### Chess Detection Metrics
- **F1 Curve**
- **Recall Curve**
- **Confusion Matrix**

### Corner Detection Metrics
- **F1 Curve**
- **Recall Curve**
- **Confusion Matrix**

---

## Team Roles
| **Team Member**      | **Role**                                         |
|---------------------|-------------------------------------------------|
| Thiraput Khongmuak  | Model, Pipeline Design, FEN to PGN Conversion    |
| Chanotai Krajeam    | Chess Model Detection (Fast-RCNN), Corner Image Processing (Canny + Houghline) |
| Chayapon Arpayatam  | Chess Detection Model, Corner Detection Data & Model, Evaluation Check |
| Chatdanai Porncharoensub | Chess Model Detection (YOLO11m), PGN Algorithm Improvement, Evaluation |

---

## Challenges and Improvements
- **Insufficient Accuracy**: Initial models were not accurate enough.
- **Model Comparisons**: YOLO significantly outperformed Fast-RCNN and DETR models, even after fine-tuning with RoboFlow and in-class datasets.
- **Model Upgrades**: Upgrading from YOLOv8 to YOLOv11m significantly improved accuracy. Future work could explore larger and more advanced models.
- **PGN Transformation**: The algorithm for converting FEN to PGN is not generalized for all cases.
---

