from dao.birthday import BirthdayDAO
from services.birthday import BirthdayService
from setup_db import db

birthday_dao = BirthdayDAO(session=db.session)

birthday_service = BirthdayService(dao=birthday_dao)
