from dao.models.birthday import Birthday
from dao.birthday import BirthdayDAO


class BirthdayService:
    def __init__(self, dao: BirthdayDAO):
        self.dao = dao

    def get_one(self, bid: int):
        return self.dao.get_one(bid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, birthday_data: dict) -> Birthday:
        return self.dao.create(birthday_data)

    def update(self, birthday_data: dict) -> None:
        return self.dao.update(birthday_data)

    def partially_update(self, birthday_data: dict) -> None:
        birthday = self.get_one(birthday_data["id"])

        if "surname" in birthday_data:
            birthday.surname = birthday_data.get("surname")
        if "birthday" in birthday_data:
            birthday.birthday = birthday_data.get("birthday")
        if "wishlist" in birthday_data:
            birthday.wishlist = birthday_data.get("wishlist")

        self.dao.update(birthday)

    def delete(self, bid: int) -> None:
        self.dao.delete(bid)
