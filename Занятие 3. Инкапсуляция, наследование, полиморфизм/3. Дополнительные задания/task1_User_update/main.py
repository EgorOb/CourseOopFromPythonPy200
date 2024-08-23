class PermissionError(Exception):
    """Кастомное исключение для ошибок доступа."""
    pass


class Role:
    """Класс, представляющий роль пользователя."""

    def __init__(self, role_name: str):
        self.role_name = role_name

    def __repr__(self):
        return f"Role({self.role_name})"


class User:
    """Класс, представляющий пользователя."""

    def __init__(self, username: str, password: str, address: str, role: Role):
        self.username = username
        self.__password = password
        self.__address = address
        self.role = role

    def get_password(self) -> str:
        return self.__password

    def get_address(self) -> str:
        return self.__address


class AccessControl:
    """Класс для управления доступом к данным пользователя."""

    def __init__(self, user: User):
        self.user = user

    def has_permission(self, role_name: str) -> bool:
        """Проверяет, имеет ли текущий пользователь необходимые права."""
        return self.user.role.role_name == role_name

    def get_sensitive_data(self, data_type: str, role_name: str) -> str:
        """Возвращает конфиденциальные данные, если есть необходимые права."""
        if not self.has_permission(role_name):
            raise PermissionError("Access denied")

        if data_type == "password":
            return self.user.get_password()
        elif data_type == "address":
            return self.user.get_address()
        else:
            raise ValueError("Unknown data type")


if __name__ == "__main__":
    admin_role = Role("admin")
    user_role = Role("user")

    admin_user = User("admin_user", "admin_secret", "123 Admin St", admin_role)
    normal_user = User("normal_user", "user_secret", "456 User St", user_role)

    admin_access = AccessControl(admin_user)
    user_access = AccessControl(normal_user)

    try:
        print(admin_access.get_sensitive_data("password", "admin"))  # Должно вернуться "admin_secret"
        print(user_access.get_sensitive_data("password", "admin"))  # Должна возникнуть ошибка
    except PermissionError as e:
        print(e)
