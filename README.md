# Screenshot Tool

## How to Use

### 1. Start the Hotkey
- Run `command.exe`.  
- This enables the **Ctrl + Q** shortcut for taking screenshots.

### 2. Take a Screenshot
- Press **Ctrl + Q**.  
- A “Select Area” window appears.  
- Click and drag to select the area you want.  
- You can select multiple areas consecutively if needed.

### 3. Finish and Copy
- Press **Esc** or **Enter** when done.  
- The screenshot is automatically **copied to the clipboard**.  
- **No files are saved**, making it ideal for quick pasting.

---

## Installation / Usage

1. Download the latest release zip from the [Releases section](../../releases).  
2. Extract the zip anywhere on your computer.  
3. Run `command.exe` to enable the hotkey.  
4. Press **Ctrl + Q** to start a screenshot, select the area, then press **Esc** or **Enter** to copy it to the clipboard.  

**Note:** Screenshots are copied to the clipboard and **not saved to disk**.

---

## Notes
- Keep both `command.exe` and `ss.exe` in the **same folder**.  
- Close `command.exe` when not in use to free system resources.

---

## Source Code
The source code is available in the [`src`](src) folder for transparency and modification.

---

## License

Licensed under the Apache License, Version 2.0.  
See the [LICENSE](LICENSE) file for details.

---

## Dependencies
This project uses the following libraries:
- OpenCV (Apache-2.0)
- NumPy (BSD)
- MSS (MIT)
- Pillow (PIL) (PIL license)
- pywin32 (MIT)

---

## Troubleshooting
- If Ctrl + Q does not open the selection window, ensure both `.exe` files are in the same folder.  
- Some antivirus programs may block new executables. Temporarily allow them if needed.
