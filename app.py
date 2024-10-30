from numpy import linalg, ndarray
from notifypy import Notify
import sounddevice as sd
import time

TOXIC_THRESHOLD = 30
NOTIFICATION_INTERVAL = 20

last_notification_time = time.time() - NOTIFICATION_INTERVAL


def monitor_toxic(indata: ndarray, _frames, _time, _status):
    global last_notification_time
    current_time = time.time()

    volume_norm = linalg.norm(indata) * 10
    print(volume_norm)

    if (
        current_time - last_notification_time > NOTIFICATION_INTERVAL
        and volume_norm > TOXIC_THRESHOLD
    ):
        last_notification_time = current_time
        notification = Notify()
        notification.title = "注意"
        notification.message = "声を小さくしてください"
        notification.send()


def main():
    while True:
        with sd.InputStream(callback=monitor_toxic):
            sd.sleep(1000)


if __name__ == "__main__":
    main()
