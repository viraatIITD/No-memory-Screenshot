import cv2
import numpy as np
import mss
from PIL import Image
import win32clipboard
import io

# Globals
refPt = []
cropping = False
clone = None
screen = None

def send_to_clipboard(img_np):
    """Copy numpy image (BGR) to Windows clipboard as a bitmap."""
    img = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)  # Convert BGR -> RGB for PIL
    image = Image.fromarray(img)

    # Save to a bytes buffer in BMP format (required by Windows clipboard)
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # BMP file header is 14 bytes, skip it
    output.close()

    # Set clipboard data
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()


def click_and_crop(event, x, y, flags, param):
    global refPt, cropping, clone, screen

    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE and cropping:
        img = clone.copy()
        cv2.rectangle(img, refPt[0], (x, y), (0, 255, 0), 2)
        cv2.imshow("Select Area", img)

    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        img = clone.copy()
        cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("Select Area", img)


def main():
    global clone, screen, refPt

    # Capture screen with mss
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # primary monitor
        screen = np.array(sct.grab(monitor))
        screen = cv2.cvtColor(screen, cv2.COLOR_BGRA2BGR)

    clone = screen.copy()

    # Fullscreen OpenCV window
    cv2.namedWindow("Select Area", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Select Area", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.setMouseCallback("Select Area", click_and_crop)
    cv2.imshow("Select Area", screen)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Crop selected area
    if len(refPt) == 2:
        x1, y1 = refPt[0]
        x2, y2 = refPt[1]
        cropped = screen[min(y1, y2):max(y1, y2), min(x1, x2):max(x1, x2)]

        # Save file
        # cv2.imwrite("screenshot.png", cropped)
        # print("Screenshot saved as screenshot.png")

        # Copy to clipboard
        send_to_clipboard(cropped)
        print("Screenshot also copied to clipboard (Ctrl+V to paste).")
    else:
        print("No area selected!")


if __name__ == "__main__":
    main()
