
import csv

from dataclasses import dataclass
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import select

from typing import Optional

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

Base = declarative_base()

@dataclass
class Org(Base):
    __tablename__ = "orgs"
    pk: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))


    def __repr__(self) -> str:
        return f"User(pk={self.pk}, name={self.name}"


    def org_pk(session, name):
        stmt = select(Org).where(Org.name == name)
        try:
            org = session.scalars(stmt).one()
        except:
            org = None

        if org:
            return org.pk

        stmt = select(Org.pk)
        pks = session.scalars(stmt).all()

        if len(pks) == 0:
            pk = 1
        else:
            pk = max(pks) + 1

        org = Org(pk=pk, name=name)
        session.add(org)
        return pk


@dataclass
class Breach(Base):
    __tablename__ = 'breaches'
    pk: Mapped[int] = mapped_column(primary_key=True)
    org_pk: Mapped[int] = mapped_column(Integer)
    breach_date: Mapped[Optional[str]] = mapped_column(String(20))
    reported_date: Mapped[str] = mapped_column(String(20))


    def __repr__(self) -> str:
        return f"User(pk={self.pk}, breach_date={self.breach_date}, date_reported={self.reported_date}"


    def max_pk(session):
        stmt = select(Breach.pk)
        pks = session.scalars(stmt).all()
        if len(pks) == 0:
            return 0
        else:
            return max(pks)


    def add_one(session, org_pk, dates, reported_date):
        pk = Breach.max_pk(session) + 1
        if dates == '':
            b = Breach(pk=pk, org_pk=org_pk, breach_date=None, reported_date=reported_date)
            session.add(b)
            return
        elif ', ' not in dates:
            b = Breach(pk=pk, org_pk=org_pk, breach_date=dates, reported_date=reported_date)
            session.add(b)
            return
        else:
            for bdate in dates.split(', '):
                b = Breach(pk=pk, org_pk=org_pk, breach_date=bdate, reported_date=reported_date)
                session.add(b)
                pk += 1

