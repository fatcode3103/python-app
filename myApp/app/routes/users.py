from flask import Blueprint, jsonify, request

users_bp = Blueprint("users", __name__,  url_prefix="/users")

users_bp.route("", methods=["GET"])
def get_all_users():
  all_users = [{"id": 1, "name": "abc"}, {"id": 2, "name": "xyz"}]
  return jsonify(all_users)