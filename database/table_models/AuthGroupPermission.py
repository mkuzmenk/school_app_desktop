from database.DB import *


class AuthGroupPermission(Base):
    __tablename__ = 'auth_group_permissions'

    id = Column(mysql.BIGINT, primary_key=True, autoincrement=True)
    group_id = Column(mysql.INTEGER, ForeignKey('auth_group.id'), nullable=False, unique=True)
    permission_id = Column(mysql.INTEGER, ForeignKey('auth_permission.id'), nullable=False, unique=True)

    auth_group = relationship('AuthGroup', back_populates='auth_group_permissions',
                              foreign_keys='AuthGroupPermission.group_id')

    auth_permission = relationship('AuthPermission', back_populates='auth_permissions_group',
                                   foreign_keys='AuthGroupPermission.permission_id')

    def __init__(self, id, group_id, permission_id):
        self.id = id
        self.group_id = group_id
        self.permission_id = permission_id

    def __str__(self):
        return f'{self.id} - Group: {self.group_id} - Permission: {self.permission_id}'

from .AuthGroup import AuthGroup # noqa: E402
from .AuthPermission import AuthPermission # noqa: E402
