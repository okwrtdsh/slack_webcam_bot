import datetime
import os

import cv2
import requests


def post_file(filepath):
    filename = os.path.basename(filepath)
    requests.post(
        url="https://slack.com/api/files.upload",
        params={
            'token': os.getenv('TOKEN'),
            'channels': os.getenv('CHANNEL'),
            'filename': filename,
            'initial_comment': '',
            'title': filename},
        files={'file': open(filepath, 'rb')}
    )


def main():
    cap = cv2.VideoCapture(0)
    res, img = cap.read()
    if not res:
        print("Error: Could not capture image")
        return
    cap.release()
    now = datetime.datetime.now()
    cv2.putText(
        img, now.strftime('%Y/%m/%d %H:%M:%S'),
        (img.shape[1] - 19*20, img.shape[0]),
        cv2.FONT_HERSHEY_PLAIN,
        2, (0, 255, 0), 2, cv2.LINE_AA)
    filepath = now.strftime('/img/%Y%m%d_%H%M%S.png')
    cv2.imwrite(filepath, img)
    post_file(filepath)


if __name__ == '__main__':
    main()
