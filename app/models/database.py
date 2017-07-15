"""
.. module:: database
    :synopsis: stupid fix, was not able to use db in __init__


.. moduleauthor:: Aaron Scheu <aaron.s@ceyu.de>
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
