



import cv2
import time
import math
import argparse
from typing import List, Tuple, Optional

import mediapipe as mp

# ---------- Helpers ----------
def draw_bbox(img, pts: List[Tuple[int, int]], color=(0, 255, 0), thickness=2):
    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]
    x1, y1, x2, y2 = min(xs), min(ys), max(xs), max(ys)
    cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)
    return (x1, y1, x2, y2)

def put_text(img, text, org, scale=0.7, color=(255, 255, 255), thick=2, bg=True):
    if bg:
        (w, h), base = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, scale, thick)
        cv2.rectangle(img, (org[0]-4, org[1]-h-6), (org[0]+w+4, org[1]+6), (0,0,0), -1)
    cv2.putText(img, text, org, cv2.FONT_HERSHEY_SIMPLEX, scale, color, thick, cv2.LINE_AA)

def landmarks_to_pixels(landmarks, w, h) -> List[Tuple[int,int]]:
    return [(int(lm.x * w), int(lm.y * h)) for lm in landmarks]

# ---------- Gesture logic (simple & robust for common poses) ----------
# MediaPipe indices: https://google.github.io/mediapipe/solutions/hands#hand-landmark-model
FINGER_TIPS   = [4, 8, 12, 16, 20]
FINGER_PIPS   = [3, 6, 10, 14, 18]  # for thumb uses 3, others PIP joints
INDEX_TIP, MIDDLE_TIP, RING_TIP, PINKY_TIP = 8, 12, 16, 20

def fingers_up(pts: List[Tuple[int,int]], handedness_label: str) -> List[int]:
    """
    Return list of 5 values (0 or 1) for [Thumb, Index, Middle, Ring, Pinky]
    based on vertical (y) for fingers and horizontal (x) for thumb.
    handedness_label: "Left" or "Right" (as seen by the person, not mirrored)
    """
    up = [0,0,0,0,0]

    # Thumb: compare tip and IP joint along x-axis depending on hand
    # For Right hand: thumb tip x < IP x => extended (tip more to the left on the image)
    # For Left  hand: thumb tip x > IP x => extended
    thumb_tip = pts[4]
    thumb_ip  = pts[3]
    if handedness_label == "Right":
        up[0] = 1 if thumb_tip[0] < thumb_ip[0] else 0
    else:
        up[0] = 1 if thumb_tip[0] > thumb_ip[0] else 0

    # Other fingers: tip is above (smaller y) than PIP -> extended
    for i, (tip_idx, pip_idx) in enumerate(zip([8,12,16,20], [6,10,14,18]), start=1):
        up[i] = 1 if pts[tip_idx][1] < pts[pip_idx][1] else 0

    return up

def classify_gesture(up: List[int]) -> str:
    count = sum(up)
    # quick named gestures
    if count == 0:
        return "Fist"
    if count == 5:
        return "Open Palm"
    if up == [1,0,0,0,0]:
        return "Thumbs Up/Side"
    if up == [0,1,0,0,0]:
        return "Pointing (Index)"
    if up == [0,1,1,0,0]:
        return "Two Fingers"
    if up == [0,1,1,1,1]:
        return "Four (No Thumb)"
    return f"{count} Fingers"

# ---------- Main Detector ----------
def run(video_source: Optional[str] = None):
    mp_hands = mp.solutions.hands
    mp_draw  = mp.solutions.drawing_utils
    mp_styles = mp.solutions.drawing_styles

    if video_source is None:
        cap = cv2.VideoCapture(0)  # webcam
    else:
        cap = cv2.VideoCapture(video_source)

    if not cap.isOpened():
        print("Error: Could not open video source.")
        return

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        model_complexity=1,
        min_detection_confidence=0.6,
        min_tracking_confidence=0.5
    )

    prev_time = time.time()
    fps = 0.0

    # Some cameras produce mirrored preview. For natural interaction you may want to flip horizontally.
    mirror = video_source is None  # flip only for webcam by default

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            if mirror:
                frame = cv2.flip(frame, 1)

            h, w = frame.shape[:2]
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            res = hands.process(rgb)

            # FPS
            now = time.time()
            dt = now - prev_time
            prev_time = now
            fps = 0.9*fps + 0.1*(1.0/dt) if dt > 0 else fps

            if res.multi_hand_landmarks:
                for lm, handed in zip(res.multi_hand_landmarks, res.multi_handedness):
                    label = handed.classification[0].label  # "Left" or "Right"
                    pts = landmarks_to_pixels(lm.landmark, w, h)

                    # bounding box
                    bbox = draw_bbox(frame, pts, color=(0, 255, 0), thickness=2)

                    # landmarks
                    mp_draw.draw_landmarks(
                        frame, lm, mp_hands.HAND_CONNECTIONS,
                        mp_styles.get_default_hand_landmarks_style(),
                        mp_styles.get_default_hand_connections_style()
                    )

                    # gesture
                    up = fingers_up(pts, label)
                    gesture = classify_gesture(up)
                    put_text(frame, f"{label} | {gesture} | {sum(up)} up",
                             (bbox[0], max(25, bbox[1]-10)), scale=0.7)

                    # (Optional) show tip coordinates of index finger
                    ix, iy = pts[8]
                    put_text(frame, f"({ix},{iy})", (ix+8, iy-8), scale=0.5, bg=False)

            put_text(frame, f"FPS: {fps:.1f}", (10, 30), scale=0.7)
            put_text(frame, "Press 'q' to quit", (10, h-10), scale=0.6)

            cv2.imshow("Hand Detection - MediaPipe + OpenCV", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
        hands.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real-time hand detection with MediaPipe.")
    parser.add_argument("--video", type=str, default=None, help="Path to a video file. Omit to use webcam.")
    args = parser.parse_args()
    run(args.video)

