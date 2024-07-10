import queue
import threading
import time
import random

# Черга для заявок
request_queue = queue.Queue()
# Список для зберігання оброблених заявок
processed_requests = []

# Функція для генерації заявок
def generate_requests(stop_event):
    while not stop_event.is_set():
        request_id = random.randint(1, 1000)  # Генеруємо унікальний ID заявки
        request_queue.put(request_id)  # Додаємо заявку до черги
        print(f"Заявка {request_id} створена та додана до черги.")
        time.sleep(1)

# Функція для обробки заявок
def process_requests(stop_event):
    while not stop_event.is_set() or not request_queue.empty():
        try:
            request_id = request_queue.get(timeout=1)  # Отримуємо заявку з черги
            print(f"Заявка {request_id} обробляється...")
            # Імітуємо обробку заявки
            time.sleep(random.uniform(0.5, 1.5))
            print(f"Заявка {request_id} оброблена.")
            processed_requests.append(request_id)  # Додаємо ID обробленої заявки до списку
        except queue.Empty:
            continue

# Функція для введення Enter для завершення програми
def wait_for_enter(stop_event):
    input("Натисніть Enter для завершення програми...\n")
    stop_event.set()  # Встановлюємо флаг завершення для інших потоків

# Запускаємо головний код програми
if __name__ == "__main__":
    # Подія для сигналу завершення
    stop_event = threading.Event()

    # Створюємо поток для генерації заявок
    generator_thread = threading.Thread(target=generate_requests, args=(stop_event,))
    generator_thread.start()

    # Створюємо поток для обробки заявок
    processor_thread = threading.Thread(target=process_requests, args=(stop_event,))
    processor_thread.start()

    # Очікуємо введення Enter для завершення програми
    wait_for_enter(stop_event)

    # Чекаємо завершення потоків
    generator_thread.join()
    processor_thread.join()

    # Виводимо оброблені заявки
    print("Оброблені заявки:", processed_requests)
















