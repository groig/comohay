import abc
import logging


class BaseImporter(abc.ABC):

    normalized_data = []

    source:str

    logger = logging.getLogger('console')

    def __init__(self):
        self.get_normalized_data()

    def run(self):
        self.remove_normalized_data_duplicates()
        self.import_data()
        self.remove_old_data()

    @abc.abstractmethod
    def import_data(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_normalized_data(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def remove_old_data(self):
        raise NotImplementedError()

    def remove_normalized_data_duplicates(self):
        e = []
        for element in self.normalized_data:
            duplicated = False
            for checked_element in e:
                if  checked_element['title'] == element['title'] and checked_element['desctiption'] == element['desctiption']:
                    duplicated = True
            if not duplicated:
                e.append(element)
        self.normalized_data = e
