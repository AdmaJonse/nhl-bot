"""
This module contains a generic observable data store that will notify any observers when its
stored data changes.
"""

from typing import Generic, List, Optional, TypeVar

from src.observer.observer import Observer
from src.observer.subject import Subject

T = TypeVar('T')

class DataStore(Generic[T], Subject):
    """
    This class defines a generic observable data store that will notify any observers when its
    stored data changes.
    """

    def __init__(self):
        self._data      : Optional[T]    = None
        self._observers : List[Observer] = []


    def set_data(self, data : T) -> None:
        """
        Update the data in the data store and notify observers if it is different from what
        was already stored.
        """
        if self._data != data:
            self._data = data
            self.notify()


    def get_data(self) -> Optional[T]:
        """
        Return the data from the data store.
        """
        return self._data


    def subscribe(self, observer : Observer) -> None:
        """
        Subscribe to updates to the data.
        """
        if observer not in self._observers:
            self._observers.append(observer)


    def unsubscribe(self, observer: Observer) -> None:
        """
        Unsubscribe from updates to the data.
        """
        if observer in self._observers:
            self._observers.remove(observer)


    def notify(self) -> None:
        """
        Notify observers that a change has occurred to the stored data.
        """
        for observer in self._observers:
            observer.update(self._data)
