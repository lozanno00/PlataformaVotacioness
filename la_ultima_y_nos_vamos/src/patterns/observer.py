# Patrón Observer
class Observer:
    def update(self, evento, data):
        pass

class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, evento, data=None):
        for obs in self._observers:
            obs.update(evento, data)
