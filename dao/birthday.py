from dao.models.birthday import Birthday
from typing import Any


class BirthdayDAO:
    def __init__(self, session: Any):
        self.session = session

    def get_one(self, bid: int):
        return self.session.query(Birthday).get(bid)

    def get_all(self):
        return self.session.query(Birthday).all()

    def create(self, birthday_data: dict) -> Birthday:
        birthday: Birthday = Birthday(**birthday_data)
        self.session.add(birthday)
        self.session.commit()
        return birthday

    def delete(self, bid: int) -> None:
        birthday = self.get_one(bid)

        self.session.delete(birthday)
        self.session.commit()

    def update(self, birthday_data: dict) -> None:
        birthday = self.get_one(birthday_data["id"])
        birthday.surname = birthday_data["surname"]
        birthday.birthday = birthday_data["birthday"]
        birthday.wishlist = birthday_data["wishlist"]

        self.session.add(birthday)
        self.session.commit()
