from ultralytics import YOLO
import cv2
import os

# Load YOLOv8 model
model = YOLO("yolov8m.pt")

print("\n===== Object Detection =====")
print("1. Webcam")
print("2. Image")
print("3. Video")

choice = input("Enter your choice (1/2/3): ")

# -----------------------------
# Webcam Detection
# -----------------------------
if choice == "1":

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame, conf=0.5)
        annotated_frame = results[0].plot()

        cv2.imshow("Webcam Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# -----------------------------
# Image Detection
# -----------------------------
elif choice == "2":

    image_path = input("Enter image path: ").strip().strip('"').strip("'")

    if not os.path.exists(image_path):
        print("Image not found!")
        exit()

    results = model(image_path, conf=0.6)

    annotated = results[0].plot()

    h, w = annotated.shape[:2]

    max_width = 900
    scale = min(max_width / w, 1.0)

    display = cv2.resize(
    annotated,
    (int(w * scale), int(h * scale))
)

    cv2.imshow("Image Detection", display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# -----------------------------
# Video Detection
# -----------------------------
# -----------------------------
# Video Detection
# -----------------------------
elif choice == "3":

    video_path = input("Enter video path: ").strip().strip('"').strip("'")

    if not os.path.exists(video_path):
        print("❌ Video not found!")
        exit()

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("❌ Unable to open video!")
        exit()

    while True:

        ret, frame = cap.read()

        if not ret:
            print("✅ Video Finished")
            break

        # Run YOLOv8 object detection
        results = model(frame, conf=0.5)

        # Draw bounding boxes
        annotated_frame = results[0].plot(line_width=2)

        # Resize for display (optional)
        h, w = annotated_frame.shape[:2]
        max_width = 1000
        scale = min(max_width / w, 1.0)

        display = cv2.resize(
            annotated_frame,
            (int(w * scale), int(h * scale))
        )

        cv2.imshow("Video Detection", display)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()