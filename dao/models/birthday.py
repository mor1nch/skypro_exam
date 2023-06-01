from marshmallow import Schema, fields
from sqlalchemy import Column, Integer, String, Date
from datetime import date

from setup_db import db


class Birthday(db.Model):
    __tablename__ = 'birthday'

    id = Column(Integer, primary_key=True)
    surname = Column(String())
    birthday = Column(Date(), default=date.today())
    wishlist = Column(String())


class BirthdaySchema(Schema):
    id = fields.Int(dump_only=True)
    surname = fields.Str()
    birthday = fields.DateTime()
    wishlist = fields.Str()
