class Person():
    _name = None
    _phone_number = None

    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number

    def is_phone_number_matching(self, input_phone_number):
        if input_phone_number == self._phone_number:
            return True
        return False

    def get_name(self):
        return self._name

    @staticmethod
    def normalize_phone_number(phone_number):
        result = ""
        for num in range(len(phone_number)):
            if phone_number[num] != "-" or phone_number[num]!= " ":
                result += phone_number[num]
        return result

