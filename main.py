import os
import time
import pyautogui

# =========================
# SAFETY
# =========================
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.05

# =========================
# PATHS
# =========================
INPUT_DIR = r"C:\Users\pc\Desktop\asdf"
OUTPUT_DIR = r"C:\Users\pc\Desktop\dfsd"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# TIMINGS (seconds)
# =========================
WAIT_AFTER_OPEN = 40
WAIT_AFTER_POLYMESH = 30
WAIT_AFTER_PROCESS = 30
WAIT_AFTER_DECIMATE = 20

CLICK_DELAY = 3
SAVE_DIALOG_WAIT = 3
CLEAR_HOLD_SECONDS = 1.2
AFTER_SAVE_WAIT = 5
AFTER_CLOSE_WAIT = 3

SLOW_DRAG_DURATION = 1.5

# After waits of 30 seconds or more, click the keep-alive location once.
WAIT_THRESHOLD_FOR_CLICK = 30
KEEP_ALIVE_CLICK = (2267, 176)

# =========================
# COORDINATES
# =========================
COORD = {
    # Pre-lightbox slow move
    "slow_move_start": (785, 195),
    "slow_move_end": (1594, 1204),

    # Lightbox close
    "close_lightbox": (405, 325),

    # Canvas drag
    "canvas_drag_start": (1594, 1204),
    "canvas_drag_end": (1663, 2090),

    # Tool actions
    "edit_btn": (853, 310),

    # SubTools preparation
    "subtools": (3387, 1138),
    "after_subtools": (3357, 285),
    "scroll_start": (3799, 285),
    "scroll_end": (3799, 800),

    # PolyMesh3D
    "polymesh3d": (3554, 480),

    # Decimation Master
    "zplugin_btn": (82, 153),
    "decimation_master": (249, 674),
    "process_current": (314, 1149),
    "decimate_current": (302, 1586),

    # Save As
    "saveas_btn": (3614, 168),
    "address_bar": (401, 142),
    "filename_box": (412, 932),

    # Close ZBrush and "No" prompt
    "zbrush_close_x": (3801, 31),
    "no_prompt": (2026, 1282),
}


def click(name: str):
    """Click a named coordinate and wait for the standard click delay."""
    pyautogui.click(*COORD[name])
    time.sleep(CLICK_DELAY)


def click_xy(x: int, y: int):
    """Click an explicit screen coordinate."""
    pyautogui.click(x, y)
    time.sleep(CLICK_DELAY)


def drag(name_start: str, name_end: str, duration: float = 0.5):
    """Drag between two named coordinates."""
    pyautogui.moveTo(*COORD[name_start])
    pyautogui.dragTo(
        *COORD[name_end],
        duration=duration,
        button="left"
    )
    time.sleep(CLICK_DELAY)


def slow_move(name_start: str, name_end: str):
    """Move the cursor slowly between two coordinates."""
    pyautogui.moveTo(*COORD[name_start])
    pyautogui.moveTo(
        *COORD[name_end],
        duration=SLOW_DRAG_DURATION
    )
    time.sleep(CLICK_DELAY)


def scroll_from_to():
    """
    Scroll in the SubTools area.
    The cursor is moved from the recorded start position to the
    recorded end position, with the actual scroll performed while
    positioned over the SubTools panel.
    """
    pyautogui.moveTo(*COORD["scroll_start"])
    pyautogui.scroll(-5)
    pyautogui.moveTo(*COORD["scroll_end"])
    time.sleep(CLICK_DELAY)


def wait_and_keep_alive(seconds: float):
    """Wait and perform one keep-alive click when the wait is >= 30s."""
    time.sleep(seconds)

    if seconds >= WAIT_THRESHOLD_FOR_CLICK:
        click_xy(*KEEP_ALIVE_CLICK)


def clear_with_backspace(hold_seconds: float = CLEAR_HOLD_SECONDS):
    """Clear the currently focused text field."""
    pyautogui.keyDown("backspace")
    time.sleep(hold_seconds)
    pyautogui.keyUp("backspace")


def save_as_ztl(folder_path: str, file_base_name: str):
    """
    Save the optimized ZTL.

    Workflow:
    1. Open Save As dialog.
    2. Click address bar and clear it.
    3. Enter output folder and press Enter.
    4. Click filename field and clear it.
    5. Enter the original base filename and press Enter.
    """
    time.sleep(SAVE_DIALOG_WAIT)

    # Address bar
    pyautogui.click(*COORD["address_bar"])
    time.sleep(0.3)
    clear_with_backspace()
    time.sleep(0.2)
    pyautogui.write(folder_path, interval=0.01)
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(1.5)

    # Filename box
    pyautogui.click(*COORD["filename_box"])
    time.sleep(0.3)
    clear_with_backspace()
    time.sleep(0.2)
    pyautogui.write(file_base_name, interval=0.01)
    time.sleep(0.2)
    pyautogui.press("enter")
    time.sleep(AFTER_SAVE_WAIT)


def list_ztl_files(folder: str):
    """Return all ZTL files in alphabetical order."""
    files = [
        file for file in os.listdir(folder)
        if file.lower().endswith(".ztl")
    ]
    files.sort()
    return files


def take_screenshot(base_name: str):
    """
    Take a full-screen screenshot and save it as:
    <base_name>.png
    """
    screenshot_path = os.path.join(
        OUTPUT_DIR,
        f"{base_name}.png"
    )
    pyautogui.screenshot(screenshot_path)
    time.sleep(CLICK_DELAY)


def process_one_file(base_name: str):
    """Run the complete ZBrush workflow for one ZTL file."""

    # Prepare viewport
    slow_move("slow_move_start", "slow_move_end")
    click("close_lightbox")

    # Place/frame model
    drag(
        "canvas_drag_start",
        "canvas_drag_end",
        duration=0.5
    )

    # Enter Edit mode and frame model
    click("edit_btn")
    pyautogui.press("f")
    time.sleep(CLICK_DELAY)

    # SubTools preparation BEFORE PolyMesh3D
    click("subtools")
    click_xy(*COORD["after_subtools"])

    pyautogui.moveTo(*COORD["scroll_start"])
    pyautogui.scroll(-5)
    time.sleep(CLICK_DELAY)

    # Make PolyMesh3D
    click("polymesh3d")
    wait_and_keep_alive(WAIT_AFTER_POLYMESH)

    # Screenshot AFTER Make PolyMesh3D
    take_screenshot(base_name)

    # ZPlugin -> Decimation Master -> Process Current
    click("zplugin_btn")
    click("decimation_master")
    click("process_current")
    wait_and_keep_alive(WAIT_AFTER_PROCESS)

    # ZPlugin -> Decimate Current
    click("zplugin_btn")
    click("decimate_current")
    wait_and_keep_alive(WAIT_AFTER_DECIMATE)

    # Save optimized ZTL
    click("saveas_btn")
    save_as_ztl(OUTPUT_DIR, base_name)

    # Close ZBrush without saving changes to the original
    pyautogui.click(*COORD["zbrush_close_x"])
    time.sleep(AFTER_CLOSE_WAIT)
    pyautogui.click(*COORD["no_prompt"])
    time.sleep(5)


def main():
    """Find and batch-process all ZTL files."""
    files = list_ztl_files(INPUT_DIR)

    if not files:
        print("No .ztl files found.")
        return

    print("Files found:")
    for index, file_name in enumerate(files, 1):
        print(f"  {index}. {file_name}")

    print("\nStarting in 5 seconds...")
    print("FAILSAFE: move mouse to TOP-LEFT corner to abort.")
    time.sleep(5)

    for file_name in files:
        full_path = os.path.join(INPUT_DIR, file_name)
        base_name = os.path.splitext(file_name)[0]

        print(f"\nOpening: {full_path}")
        os.startfile(full_path)

        wait_and_keep_alive(WAIT_AFTER_OPEN)

        print(f"Processing: {base_name}")
        process_one_file(base_name)

    print("\nAll files processed.")


if __name__ == "__main__":
    main()
