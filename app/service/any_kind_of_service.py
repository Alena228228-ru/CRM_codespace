from abc import ABC, abstractmethod

from repository.any_kind_of_repo import TeacherRepository


class StudentABC(ABC):
    @abstractmethod
    async def add_teacher(self, name: str): pass

    @abstractmethod
    async def get_teacher(self, name: str) -> bool: pass

    @abstractmethod
    async def update_teacher(self, name: str): pass

    @abstractmethod
    async def del_teacher(self, name: str): pass

class Teacher(StudentABC):
    @classmethod
    def add_teacher(self, tg_id: int, name: str) -> bool:
        return TeacherRepository().add_teacher(tg_id=tg_id, name = name)

    @classmethod
    def get_teacher(self, tg_id: int) -> bool:
        return TeacherRepository().get_teacher(tg_id=tg_id)

    @classmethod
    def update_teacher(self, tg_id: int) -> bool:
        return TeacherRepository().update_teacher(tg_id=tg_id)

    @classmethod
    def del_teacher(self, tg_id: int) -> bool:
        return TeacherRepository().del_teacher(tg_id=tg_id)

