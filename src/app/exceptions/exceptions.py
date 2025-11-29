class GeneralException(Exception):
    ''' Общее исключение '''

class OperatorNotFound(GeneralException):
    ''' Исключение, когда оператор не найден '''