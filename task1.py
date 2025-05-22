from abc import abstractmethod


class Logger:
    def __init__(self, log_count: int) -> None:
        """Инициализирует объект Logger.

        Args:
            log_count: Количество логов.
        """
        self._log_count = log_count  # Количество записей

    @abstractmethod
    def log_event(self) -> None:
        pass

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта с количеством записей логов.

        Returns:
            str: Строка в формате "Количество записей <значение>".
        """
        return f"Количество записей {self._log_count}"


logger = Logger(5)
print(logger)
