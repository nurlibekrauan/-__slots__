from abc import ABC, abstractmethod


class AccesControl(ABC):
    @abstractmethod
    def can_read(self):
        pass

    @abstractmethod
    def can_write(self):
        pass

    @abstractmethod
    def can_delete(self):
        pass

    def log_message(self, message):
        print(f"{message}")

    def log_error(self, error):
        print(f"Error: {error}")

    def log_warning(self, warning):
        print(f"Warning: {warning}")

    def log_info(self, info):
        print(f"Info: {info}")


class AdminAccess(AccesControl):
    def can_read(self):
        return True

    def can_write(self):
        return True

    def can_delete(self):
        return True


class ModeratorAccess(AccesControl):
    def can_read(self):
        return True

    def can_write(self):
        return False

    def can_delete(self):
        return True


class UserAccess(AccesControl):
    def can_read(self):
        return True

    def can_write(self):
        return False

    def can_delete(self):
        return False


class RegularUser:
    __slots__ = ("name", "age", "email", "role")

    def __init__(self, name='user', age=20, email=None):
        self.name = name
        self.age = age
        self.email = email
        self.role = "user"

    def change_role(self, new_role_class, *args, **kwargs):
        self.__class__ = new_role_class
        self.__init__(self.name, self.age, self.email, *args, **kwargs)

    def update_email(self, new_email):
        self.email = new_email

    def show_info(self):
        print(
            f"Имя: {self.name}, Возраст: {self.age}, Email: {self.email}, Роль: {self.role}"
        )

    def display_info(self):
        return f"Имя: {self.name}, Возраст: {self.age}, Email: {self.email}, Роль: {self.role}"


class User(RegularUser, UserAccess):
    pass


class ModeratorUser(User, ModeratorAccess):
    __slots__ = ("name", "age", "email", "role", "permissions", "is_banned")

    def __init__(self, name, age, email):
        super().__init__(name, age, email)
        self.role = "moderator"
        self.is_banned = False

    def ban_user(self, user: User):
        print(f"Пользователь {user.name} был забанен.")


class AdminUser(ModeratorUser, AdminAccess):
    __slots__ = ("name", "age", "email", "role", "permissions")

    def __init__(self, name, age, email):
        super().__init__(name, age, email)
        self.role = "admin"

    def delete_user(self, user: User):
        print(f"Пользователь {user.name} удален.")


admin = AdminUser(name="Alice", age=30, email="alice@example.com")
moderator = ModeratorUser(name="Bob", age=25, email="bob@example.com")
user = RegularUser(name="Charlie", age=20, email="charlie@example.com")

admin.delete_user(user)  # Админ удаляет пользователя
moderator.ban_user(user)  # Модератор блокирует пользователя
user.update_email("new_email@example.com")  # Пользователь обновляет свой email

print(admin.display_info())  # Отображение информации об администраторе
print(moderator.display_info())  # Отображение информации о модераторе
