from abc import abstractmethod
from datetime import datetime


class Logger:
    def __init__(self) -> None:
        """
        Инициализирует объект Logger с нулевым счетчиком логов.
        """
        self._log_count = 0  # Количество записей

    @abstractmethod
    def log_event(self) -> None:
        """
        Абстрактный метод, для логирования событий.
        Должен быть реализован в дочерних классах.
        """
        pass

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта с количеством записей логов.

        Returns:
            str: Строка в формате "Количество записей <значение>".
        """
        return f"Количество записей {self._log_count}"


class FileLogger(Logger):
    logs = list()  # Список для хранения логов

    def log_event(self, message: str) -> None:
        """
        Добавляет сообщение в список logs и увеличивает счетчик _log_count.

        Args:
            message (str): Сообщение для логирования.
        """
        self._log_count += 1
        self.logs.append(message)


class TimedLogger(FileLogger):
    def log_event(self, message: str) -> None:
        """
        Добавляет сообщение в список logs и временную метку.
        А так же увеличивает счетчик лога _log_count.

        Args:
            message (str): Сообщение для логирования.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Временная метка лога
        timed_message: dict[str, str] = {"message": message, "created_at": timestamp}
        super().log_event(timed_message)

    def __getitem__(self, index: int):
        """
        Возвращает лог по индексу.

        Args:
            index (int): Индекс лога.

        Returns:
            dict[str, str]: Словарь логов.
        """
        return self.logs[index]


loger = TimedLogger()
loger.log_event("Добавил что-то")
loger.log_event("Удалил что-то")
print(loger.logs)
print(loger[0])
