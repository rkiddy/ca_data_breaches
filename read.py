
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy import select

from tables import Org
from tables import Breach

if __name__ == '__main__':

    cmd = "wget -O list_`date '+%Y%m%d_%H%M'`.csv 'https://www.oag.ca.gov/privacy/databreach/list-export'"

    db = create_engine(f"mysql+pymysql://ray:zome_zekret_zing@localhost/ca_breaches", echo=False)

    Session = sessionmaker(bind=db)
    session = Session()

    with open('list.csv', newline='') as f:
        rdr = csv.reader(f)
        top = next(rdr)
        for row in rdr:
            org_pk = Org.org_pk(session, row[0])
            Breach.add_one(session, org_pk, row[1], row[2])
            session.commit()

