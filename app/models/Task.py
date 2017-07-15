"""
.. module:: Task
    :synopsis: A todo / task item

.. moduleauthor:: Aaron Scheu
"""

from .database import db


class Task(db.Model):
    """Task Model for SQLAlchemy
        :ivar id: table primary key
        :ivar title: Title of the todo item
        :ivar description: Detail about the item
        :ivar due: date until todo should be done
        :ivar state: set to True if task is finished // False if new
    """
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(40), nullable=False)
    description = db.Column(db.Text())
    due = db.Column(db.Date(), nullable=False)
    state = db.Column(db.Boolean(), nullable=False)

    def __init__(self, due, title, description):
        self.title = title
        self.description = description
        self.due = due
        self.state = False

    def __repr__(self):
        """The representation of this entry.

        :returns: The tasks's details.
        :rtype: str
        """
        return '<Due: {},Title: {}, State: {}>'.format(self.due, self.title, self.state)

    def as_dict(self):
        """Get item as dictionary
            - needed for serialization / jsonify
            :returns entry as dict object
            :rtype dictionary
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
