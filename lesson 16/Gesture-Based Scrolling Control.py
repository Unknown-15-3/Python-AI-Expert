import cv2, time, pyautogui
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence = 0.7, min_tracking_confidence = 0.7)
mp_drawing = mp.solutions.drawing_utils

SCROLL_SPEED = 300
SCROLL_DELAY = 1
CAM_WIDTH, CAM_HEIGHT = 640, 480

def detect_gesture(landmarks, handedness):
    fingers = []
    tips = [mp_hands.HandLandmark.INDEX_FINGER_TIP, mp_hands.HandLandmark.MIDDLE_FINGER_TIP, mp_hands.   HandLandmark.RING_FINGER_TIP, mp_hands.HandLandmark.PINKY_TIP]

    for tip in tips:
        if landmarks.landmark[tip].y < landmarks.landmark[tip-2].y:
            fingers.append(1)
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    if (handedness == "right" and thumb_tip.x > thumb_ip.x) or (handedness == "left" and thumb_tip.x < thumb_ip.x):
        fingers.append(1)
    return "scroll_up" if sum(fingers) == 5 else "scroll_down" if len(fingers) == 0 else "none"

cap = cv2.VideoCapture(0)
cap.set(3, CAM_WIDTH)
cap.set(4, CAM_HEIGHT)
last_scroll = p_time = 0
print("Gesture Scroll Active \n Open palm: scroll up \n fist: scroll down \n press 'q' to exit")

while cap.isOpened():
    success, image = cap.read()
    if not success: break

    img = cv2.flip(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 1)
    result = hands.process(img)
    gesture, handedness = "none", "unknown"

    if result.multi_hand_landmarks:
        for hand, handedness_info in zip(result.multi_hand_landmarks, result.multi_handedness):
            handedness = handedness_info.classification[0].label
            gesture = detect_gesture(hand, handedness)
            mp_drawing.draw_landmarks(img, hand, mp_hands.HAND_CONNECTIONS)

            if (time.time()- last_scroll)> SCROLL_DELAY:
                if gesture == "scroll_up": pyautogui.scroll(SCROLL_SPEED);
                elif gesture == "scroll_down": pyautogui.scroll(-SCROLL_SPEED);
                last_scroll = time.time()

    fps = 1/(time.time()- p_time) if (time.time() - p_time) > 0 else 0
    p_time = time.time()
    cv2.putText(img, f"FPS: {int(fps)} | Hand: {handedness} / gesture: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("gesture based control", cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    if cv2.waitKey(1) & 0xff == ord('q'): break

cap.release()
cv2.destroyAllWindows()