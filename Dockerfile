# Stage 1: Install requirements and save model
FROM python:3.9-slim as builder

WORKDIR /app

COPY requirements.txt .

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy necessary files
COPY save_model.py .
COPY detect_video.py .
COPY licence_plate_recognizer.py .
COPY data ./data
COPY checkpoints ./checkpoints

# Save the model
RUN python save_model.py --weights ./data/custom.weights --output ./checkpoints/custom-416 --input_size 416 --model yolov4

# Stage 2: Runtime
FROM python:3.9-slim

WORKDIR /app

# Copy saved model and scripts from the previous stage
COPY --from=builder /app/checkpoints ./checkpoints
COPY --from=builder /app/detect_video.py .
COPY --from=builder /app/licence_plate_recognizer.py .
COPY --from=builder /app/data ./data

# Set up entrypoint
ENTRYPOINT ["python"]

# Command to run when container starts
CMD ["detect_video.py", "--weights", "./checkpoints/custom-416", "--size", "416", "--model", "yolov4", "--video", "./data/video/licence_plate.mp4", "--output", "./detections/results.avi", "--crop"]
