import uuid
import random
import string


def generate_random_string(length: int):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for _ in range(length))


def generate_random_id():
    return str(uuid.uuid4())


def generate_random_integer(min_value, max_value):
    return random.randint(min_value, max_value)


def dummy_answer():
    id = generate_random_id()
    file_name = generate_random_string(5)
    desciption = f", {generate_random_string(5)} : {generate_random_string(5)} $$% {generate_random_string(5)}"
    uploadTime = generate_random_integer(1700260000000, 9900260617547)
    is_procesed = False
    size = generate_random_integer(20, 1000)

    payload = {
        "logId": id,
        "fileName": f"{file_name}.log",
        "description": desciption,
        "uploadTime": uploadTime,
        "isProcessed": is_procesed,
        "size": size
    }
