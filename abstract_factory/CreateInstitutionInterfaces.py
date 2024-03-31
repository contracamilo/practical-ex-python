from abc import abstractmethod, ABC  # abc (Abstract Base Classes).

from abstract_factory.Institution import PublicInstitution, PrivateInstitution


class InstitutionFactory(ABC):
    @abstractmethod
    def create_institution(self, name):
        pass


class PublicInstitutionFactory(InstitutionFactory):
    def create_institution(self, name):
        return PublicInstitution(name)


class PrivateInstitutionFactory(InstitutionFactory):
    def create_institution(self, name):
        return PrivateInstitution(name)
