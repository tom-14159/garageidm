from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from models import *

engine = create_engine("sqlite://", echo=True)
Base.metadata.create_all(engine)

with Session(engine) as session:
    rc = RoleCategory(uri="garageidm", name="GarageIDM")
    role = Role(uri="garageidm:workgroup_manager", name="Správce pracovních skupin", role_category=rc)
    session.add_all([rc, role])
    session.commit()

session = Session(engine)