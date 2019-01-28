import threading
import time

m_thread = {}

def execute(number):
    while True:
        print(threading.current_thread().getName(), number)
        time.sleep(0.01)

# if __name__ == "__main__":
#     for i in range(1,8):
#         m_thread = threading.Thread(target=execute, args=(i,))
#         m_thread.start()


if __name__ == "__main__":
    m_thread = threading.Thread(target=execute, args=(1,))
    m_thread.start()