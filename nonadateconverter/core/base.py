from abc import ABC, abstractmethod


class Abstract(ABC):
    @abstractmethod
    def now(self):
        ...

    @abstractmethod
    def weekday(self):
        ...

    @abstractmethod
    def elapsedtime(self):
        ...


class HijriAbstract(Abstract):
    @abstractmethod
    def hijri_to_gregorian(self):
        pass

    @abstractmethod
    def hijri_to_jalali(self):
        pass


class GregorianAbstract(Abstract):
    @abstractmethod
    def gregorian_to_hijri(self):
        pass

    @abstractmethod
    def gregorian_to_jalali(self):
        pass


class JalaliAbstract(Abstract):
    @abstractmethod
    def jalali_to_hijri(self):
        pass

    @abstractmethod
    def jalali_to_gregorian(self):
        pass
