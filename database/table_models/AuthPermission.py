from database.DB import *


class AuthPermission(Base):
    __tablename__ = 'auth_permission'

    id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    name = Column(mysql.VARCHAR(255), nullable=False)
    content_type_id = Column(mysql.INTEGER, nullable=False, unique=True)
    codename = Column(mysql.VARCHAR(100), nullable=False, unique=True)

    auth_permissions_group = relationship('AuthGroupPermission', back_populates='auth_permission',
                                          foreign_keys='AuthGroupPermission.permission_id')

    def __init__(self, id, name, content_type_id, codename):
        self.id = id
        self.name = name
        self.content_type_id = content_type_id
        self.codename = codename

    def __str__(self):
        return f'{self.id} - {self.name} - {self.codename}'

from .AuthGroupPermission import AuthGroupPermission # noqa: E402
