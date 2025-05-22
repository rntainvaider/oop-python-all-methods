from abc import abstractmethod


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
