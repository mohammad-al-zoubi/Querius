from .password_helper import PasswordHelper
from server.helpers import token_helper

password_helper = PasswordHelper()


def create_token(payload):
    return token_helper.create_token(payload)


def get_current_user(token):
    return token_helper.get_current_user(token)


def compare_to_hash(password, pw_hash):
    return password_helper.compare_to_hash(password, pw_hash)
