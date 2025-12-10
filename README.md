# Chess2PGN

This repository contains the final project for **Introduction to Digital Imaging (2110431)**, which focuses on detecting and tracking chess moves from video footage. The project aims to convert chessboard states from video frames into Portable Game Notation (PGN) format using advanced computer vision and machine learning techniques.

---

## Table of Contents
- [Overview](#overview)
- [Approach](#approach)
- [Model](#models)
  - [Chess Piece Recognition](#chess-piece-recognition)
- [Limitations](#limitations)

---

## Overview
The Chess Move Tracking system first calibrate the whole video by using first frame to identify board layout and its orientation. After that it heuristically stream through the whole video and extract from those frames. It then map from chess states into PGN format by comparing result with chess engine. The key objective is to automate the tracking of chess moves from video footage with high accuracy.

---

## Approach
1. **Calibration**: Extract first frame of each video to calibration board layout and orientation.
2. **Video Stream**: Extract chess states from video using pixel different
3. **PGN Conversion**: Map 1-1 between 2 chess states and asking chess engine if there's a valid one, and use that.

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

## Limitations
- **Heavily Rely on the Calibration Phase**: If program failed to find the board layout or board orientation first, the whole program will surely predict wrong PGN output.
- **Rely on Multiple Assumptions**: 
   - Assume the whole video is static
   - Assume the video rotation fall into 90, 180, 270, 360 degrees
   - Assume the game is starting/middle game (not end game)
---

