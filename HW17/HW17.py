#Linux: Домашнее задание 17 (Python)

#Написать скрипт, который будет бесконечно пинговать указанный адрес (переменная или ввод
#пользователя) с интервалом 1 секунда между попытками. Если время пинга превышает 100 мс или
#не удается выполнить пинг в течение 3 последовательных отправок пакетов, скрипт просто выведет сообщения об этом.
#Пришлите скрипт или ссылку на github репо с решением

import subprocess
import time
import re

# Ввод IP-адреса или домена
target = input("Введите адрес для пинга (например, 8.8.8.8): ")

# Счётчик неудачных попыток
fail_count = 0

print(f"Начинаем пинговать {target}... (интервал 1 секунда)")

while True:
    try:
        # subprocess запускает команду ping и возвращает результат
        result = subprocess.run(
            ["ping", "-c", "1", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Успешный пинг
        if result.returncode == 0:
            # Ищем время ответа в миллисекундах
            match = re.search(r'time=(\d+\.\d+)', result.stdout)
            if match:
                ping_time = float(match.group(1))
                print(f"Ответ от {target}: {ping_time} мс")

                if ping_time > 100:
                    print(f"Внимание: Пинг {ping_time} мс превышает 100 мс!")

                fail_count = 0  # сбрасываем счётчик

        else:
            print("Не удалось получить ответ от адреса.")
            fail_count += 1

        # Если подряд 3 неудачных пинга
        if fail_count >= 3:
            print("Три неудачных пинга подряд. Прерывание.")
            break

        time.sleep(1)

    except KeyboardInterrupt:
        print("Остановлено пользователем.")
        break
