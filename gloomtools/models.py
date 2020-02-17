from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, Text, create_engine, Table, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
import os
from typing import Type
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

def get_sqlalchemy_uri() -> str:

    if 'RDS_HOSTNAME' in os.environ:
        print('Using RDS database...')
        host = os.environ['RDS_HOSTNAME']
        port = os.environ['RDS_PORT']
        name = os.environ['RDS_DB_NAME']
        username = os.environ['RDS_USERNAME']
        password = os.environ['RDS_PASSWORD']
        # postgresql://scott:tiger@localhost:5432/mydatabase
        uri = f'postgresql://{username}:{password}@{host}:{port}/{name}'
    else:
        print('No RDS database found, set RDS_ environment variables before running')
        uri = None

    return uri


Base = declarative_base()

# Create user model.

def make_secondary_table(a: str, b: str) -> Table:
    table_name = f'{a}_{b}_secondary'
    association_table = Table(table_name, Base.metadata,
        Column(f'{a}_id', Integer, ForeignKey(f'{a}.id')),
        Column(f'{b}_id', Integer, ForeignKey(f'{b}.id'))
    )
    return association_table

user_role_table = make_secondary_table('user', 'role')

class User(UserMixin, Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    email = Column(String(120), index=True, unique=True)
    password_hash = Column(String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def __str__(self):
        return self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    roles = relationship(
        'Role',
        secondary=user_role_table,
        back_populates='users',
        lazy='subquery'
    )

class Role(Base):
    __tablename__ = 'role'
    id = Column(Integer, primary_key=True)
    name = Column(Text)

    users = relationship(
        'User',
        secondary=user_role_table,
        back_populates='roles',
        lazy='subquery'
    )

    def __str__(self):
        return self.name


class AbilityCard(Base):
    __tablename__ = 'abilitycard'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    initiative = Column(Integer)
    level = Column(Integer)
    toptext = Column(Text)
    toploss = Column(Boolean)
    topduration = Column(Text)
    topaoe = Column(JSONB)
    topquest = Column(JSONB)
    bottomtext = Column(Text)
    bottomloss = Column(Boolean)
    bottomduration = Column(Text)
    bottomaoe = Column(JSONB)
    bottomquest = Column(JSONB)

