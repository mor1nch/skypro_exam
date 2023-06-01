from flask import request
from flask_restx import Resource, Namespace

from dao.models.birthday import BirthdaySchema
from implemented import birthday_service

birthdays_schema = BirthdaySchema(many=True)
birthday_schema = BirthdaySchema()
birthday_ns = Namespace('birthday')


@birthday_ns.route('/')
class BirthdaysView(Resource):
    def get(self):
        notes = birthday_service.get_all()
        return birthdays_schema.dump(notes), 200

    def post(self):
        req_json = request.json
        birthday = birthday_service.create(req_json)
        return "Birthday has created", 201, {"location": f"/birthday/{birthday.id}"}


@birthday_ns.route('/<int:bid>')
class BirthdayView(Resource):
    def get(self, bid):
        birthday = birthday_service.get_one(bid)
        return birthday_schema.dump(birthday), 200

    def put(self, bid):
        req_json = request.json
        req_json["id"] = bid
        birthday_service.update(req_json)
        return "Birthday has updated", 204

    def patch(self, bid):
        req_json = request.json
        req_json["id"] = bid
        birthday_service.partially_update(req_json)
        return "Birthday has updated", 204

    def delete(self, bid):
        birthday_service.delete(bid)
        return "Birthday has deleted", 204
