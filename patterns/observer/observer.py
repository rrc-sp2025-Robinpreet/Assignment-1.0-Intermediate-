from abc import ABC, abstractmethod

class Observer(ABC):
    """Observer superclass for the Observer Pattern."""

    @abstractmethod
    def update(self, message: str):
        """Called when the subject wants to notify the observer."""
        pass