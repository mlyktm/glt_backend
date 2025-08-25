# models.py
from sqlalchemy import Column, Integer, String, Boolean, Date, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    firstName = Column(String)
    lastName = Column(String)
    phone = Column(String)
    email = Column(String)
    dob = Column(String)

    city = Column(String)
    state = Column(String)
    streetAddress = Column(String)
    zipcode = Column(String)

    startDate = Column(Date)
    endDate = Column(Date)

    clearanceLevel = Column(String)
    authenticated = Column(Boolean)

    # We'll store these as JSON arrays (simpler than foreign key relationships for now)
    chargeline_ids = Column(String)  # We'll store as comma-separated string
    timesheet_ids = Column(String)
