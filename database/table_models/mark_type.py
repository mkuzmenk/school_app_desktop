from database.db import *


class MarkType(Base):
    __tablename__ = 'mark_types'

    mark_type_id = Column(mysql.INTEGER, primary_key=True, autoincrement=True)
    mark_type_name = Column(mysql.VARCHAR(255), nullable=False)

    #mark_marktype = relationship('Mark', back_populates='marktype_mark', foreign_keys='Mark.mark_type')

    def __init__(self, mark_type_id, mark_type_name):
        self.mark_type_id = mark_type_id
        self.mark_type_name = mark_type_name

    def __str__(self):
        return f'{self.mark_type_id} - {self.mark_type_name}'

from .mark import Mark # noqa: E402