"""
Line Follower Simulator  (2D, one file)
Needs:  pip install opencv-python numpy
Run:    python line_follower_sim.py        (press  q  to quit,  r  to restart)

The closed loop:   SEE  ->  DECIDE  ->  MOVE  ->  (repeat)
"""

import math
import cv2
import numpy as np

# =====================================================
# SETTINGS 
# =====================================================
WORLD_W, WORLD_H = 800, 600   # size of the track picture (pixels)
VIEW_W, VIEW_H = 120, 80      # size of the robot's camera picture
SPEED = 3                     # how many pixels the robot moves each step
KP = 0.01                     # steering strength (bigger = turns harder)
MAX_TURN = 0.15               # the robot cannot turn more than this per step (radians)
BAND_TOP, BAND_BOTTOM = 30, 50  # which rows of the camera we look at (row 0 = far ahead, row 80 = at the robot)


# =====================================================
# 1. THE WORLD: draw a track
# =====================================================
def make_track():
    track = np.full((WORLD_H, WORLD_W), 255, dtype=np.uint8)  # white paper
    # black oval line: center, (half-width, half-height), angle, start, end, color, thickness
    cv2.ellipse(track, (400, 300), (300, 200), 0, 0, 360, 0, 12)
    return track


# =====================================================
# 2. SEE: build the camera picture
# =====================================================
def get_camera_view(track, x, y, heading):
    # Rotate the world around the robot so the robot always faces UP in the picture.
    angle = 90 + math.degrees(heading)
    M = cv2.getRotationMatrix2D((x, y), angle, 1.0)
    # Then slide the picture so the robot sits at the bottom-middle of the view.
    M[0, 2] += VIEW_W / 2 - x
    M[1, 2] += VIEW_H - y
    # Cut out only VIEW_W x VIEW_H pixels. Outside the track counts as white.
    view = cv2.warpAffine(track, M, (VIEW_W, VIEW_H), borderValue=255)
    return view


# =====================================================
# 3. DECIDE: where is the line? how much should we steer?
# =====================================================
def find_line_error(view):
    band = view[BAND_TOP:BAND_BOTTOM, :]   # a strip of rows ahead of the robot
    dark = band < 100                      # True where the pixel is black (the line)
    columns = np.where(dark)[1]            # x-positions of all the black pixels
    if len(columns) == 0:
        return None                        # no line seen
    line_x = columns.mean()                # average x = middle of the line
    error = line_x - VIEW_W / 2            # negative = line on left, positive = on right
    return error


def steer(error):
    turn = KP * error                      # the further the line, the harder we turn
    return max(-MAX_TURN, min(MAX_TURN, turn))  # clamp to the allowed range


# =====================================================
# 4. MOVE: update the robot's position and heading
# =====================================================
def move_robot(x, y, heading, turn):
    heading += turn                        # turn first
    x += SPEED * math.cos(heading)         # then step forward in the new direction
    y += SPEED * math.sin(heading)
    return x, y, heading


# =====================================================
# 5. DRAWING (only for showing things on screen)
# =====================================================
def draw_world(track, trail, x, y, heading):
    img = cv2.cvtColor(track, cv2.COLOR_GRAY2BGR)
    img = cv2.addWeighted(img, 1.0, trail, 1.0, 0)  # add the green trail
    nose = (int(x + 20 * math.cos(heading)), int(y + 20 * math.sin(heading)))
    cv2.circle(img, (int(x), int(y)), 8, (0, 0, 255), -1)       # red robot
    cv2.line(img, (int(x), int(y)), nose, (255, 0, 0), 2)       # blue nose = heading
    return img


def draw_camera(view, error):
    img = cv2.cvtColor(view, cv2.COLOR_GRAY2BGR)
    cv2.line(img, (0, BAND_TOP), (VIEW_W, BAND_TOP), (0, 200, 0), 1)       # band edges
    cv2.line(img, (0, BAND_BOTTOM), (VIEW_W, BAND_BOTTOM), (0, 200, 0), 1)
    cv2.line(img, (VIEW_W // 2, 0), (VIEW_W // 2, VIEW_H), (0, 0, 255), 1)  # center
    if error is not None:
        line_x = int(VIEW_W / 2 + error)
        cv2.circle(img, (line_x, (BAND_TOP + BAND_BOTTOM) // 2), 3, (255, 0, 0), -1)
    return cv2.resize(img, None, fx=4, fy=4, interpolation=cv2.INTER_NEAREST)


# =====================================================
# 6. MAIN LOOP
# =====================================================
def main():
    track = make_track()

    def reset():
        # start on top of the oval, facing right (heading 0)
        return 400.0, 100.0, 0.0, np.zeros((WORLD_H, WORLD_W, 3), np.uint8), 0.0

    x, y, heading, trail, last_turn = reset()

    while True:
        view = get_camera_view(track, x, y, heading)   # SEE
        error = find_line_error(view)                  # DECIDE (part 1)
        if error is None:
            turn = last_turn                           # lost the line: keep doing what we did
        else:
            turn = steer(error)                        # DECIDE (part 2)
        last_turn = turn
        x, y, heading = move_robot(x, y, heading, turn)  # MOVE

        cv2.circle(trail, (int(x), int(y)), 1, (0, 180, 0), -1)
        cv2.imshow("World", draw_world(track, trail, x, y, heading))
        cv2.imshow("Robot camera", draw_camera(view, error))

        key = cv2.waitKey(15) & 0xFF
        if key == ord("q"):
            break
        if key == ord("r"):
            x, y, heading, trail, last_turn = reset()

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
