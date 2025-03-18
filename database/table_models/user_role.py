from database.db import *


class UserRole(Base):
    __tablename__ = 'user_roles'

    user_role_id = Column(mysql.INTEGER, autoincrement=True, primary_key=True)
    user_role_name = Column(mysql.VARCHAR(50), nullable=False, unique=True)

    user_userrole = relationship('User', back_populates='userrole_user',
                                 foreign_keys='User.user_role')

    def __init__(self, user_role_id, user_role_name):
        self.user_role_id = user_role_id
        self.user_role_name = user_role_name

    def __str__(self):
        return f'{self.user_role_name} - {self.user_role_id}'

from .user import User # noqa: E402
