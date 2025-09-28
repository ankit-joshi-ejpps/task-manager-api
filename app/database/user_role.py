import enum

class UserRole(str, enum.Enum):
    ADMINISTRATOR = "administrator"
    USER = "user"
