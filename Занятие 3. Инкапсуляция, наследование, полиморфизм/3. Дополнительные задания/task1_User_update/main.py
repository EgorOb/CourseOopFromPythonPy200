class PermissionError(Exception):
    """Кастомное исключение для ошибок доступа."""
    pass


class Role:
    """Класс, представляющий роль пользователя и его права."""

    def __init__(self, name: str, permissions: dict):
        """
        :param name: Название роли (например, 'admin', 'user')
        :param permissions: Словарь прав, где ключ — действие (например, 'view_password'), а значение — bool
        """
        self.name = name
        self.permissions = permissions

    def has_permission(self, action: str) -> bool:
        """Проверяет, есть ли у роли разрешение на конкретное действие."""
        return self.permissions.get(action, False)


class User:
    """Класс, представляющий пользователя."""

    def __init__(self, username: str, password: str, address: str, role: Role):
        self.username = username
        self.__password = password
        self.__address = address
        self.role = role

    def get_password(self) -> str:
        """
        Проверяет есть ли у пользователя право на просмотр пароля ('view_password').
        Если такое разрешение есть, то возвращает пароль,
        если нет, то вызывает ошибку PermissionError
        """
        if self.role.has_permission("view_password"):
            return self.__password
        else:
            raise PermissionError("Доступ запрещен к паролю")

    def get_address(self) -> str:
        """
        Проверяет есть ли у пользователя право на просмотр адреса ('view_address').
        Если такое разрешение есть, то возвращает адрес,
        если нет, то вызывает ошибку PermissionError
        """
        if self.role.has_permission("view_address"):
            return self.__address
        else:
            raise PermissionError("Доступ запрещен к адресу")


if __name__ == "__main__":
    # Настройка прав
    admin_permissions = {"view_password": True, "view_address": True}
    user_permissions = {"view_address": True}

    # Создание ролей
    admin_role = Role("admin", admin_permissions)
    user_role = Role("user", user_permissions)

    # Создание пользователей с различными ролями
    admin_user = User("admin", "admin_secret", "123 Admin St", admin_role)
    normal_user = User("user", "user_secret", "456 User St", user_role)

    # Проверка прав для admin
    print(admin_user.get_password())  # Должно вернуться "admin_secret"
    print(admin_user.get_address())  # Должно вернуться "123 Admin St"

    # Проверка прав для user
    try:
        print(normal_user.get_address())  # Должно вернуться "456 User St"
        print(normal_user.get_password())  # Должна возникнуть ошибка, так как у пользователя нет прав
    except PermissionError as e:
        print('Ошибка доступа')

