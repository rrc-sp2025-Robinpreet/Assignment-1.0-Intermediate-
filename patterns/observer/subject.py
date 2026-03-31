from patterns.observer.observer import Observer 

class Subject:
    """Subject superclass for the Observer Pattern."""

    def __init__(self):
        self._observers = []  # List of objects.

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)