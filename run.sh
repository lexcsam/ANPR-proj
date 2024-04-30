#!/bin/bash

# Build Docker image
docker build -t ANPR-Proj .

# Run Docker container
docker run -d --name ANPR_cont ANPR-Proj

# Run detect_video.py script in the container
docker exec -it ANPR_cont python detect_video.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --video ./data/video/licence_plate.mp4 --output ./detections/results.avi --crop

# Run licence_plate_recognizer.py script in the container
docker exec -it ANPR_cont python licence_plate_recognizer.py

# Remove the container once finished
docker stop ANPR_cont
docker rm ANPR_cont
