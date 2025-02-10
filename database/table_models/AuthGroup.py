from database.DB import *


class AuthGroup(Base):
    __tablename__ = 'auth_group'

    id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    name = Column(mysql.VARCHAR(150), unique=True, nullable=False)

    auth_group_permissions = relationship('AuthGroupPermission', back_populates='auth_group',
                                          foreign_keys='AuthGroupPermission.group_id')

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'{self.id} - {self.name}'

from .AuthGroupPermission import AuthGroupPermission # noqa: E402
