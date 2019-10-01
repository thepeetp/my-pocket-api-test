import uuid
from datetime import date


def generate_username():
    return 'robot_' + str(uuid.uuid4())

def get_date():
    return str(date.today())

def get_monthly():
    return get_date().replace('-', '')[:6]