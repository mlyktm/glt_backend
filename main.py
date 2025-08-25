from fastapi import FastAPI, Depends
from pydantic import BaseModel
from datetime import date

from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

from typing import List

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

class EmployeeCreate(BaseModel):
    id: int
    firstName: str
    lastName: str
    phone: str
    email: str
    dob: str

    city: str
    state: str
    streetAddress: str
    zipcode: str

    startDate: date
    endDate: date

    clearanceLevel: str
    authenticated: bool
    chargeline_ids: list[int]
    timesheet_ids: list[int]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API endpoint
@app.post("/employees/")
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    db_employee = models.Employee(
        id=employee.id,
        firstName=employee.firstName,
        lastName=employee.lastName,
        phone=employee.phone,
        email=employee.email,
        dob=employee.dob,
        city=employee.city,
        state=employee.state,
        streetAddress=employee.streetAddress,
        zipcode=employee.zipcode,
        startDate=employee.startDate,
        endDate=employee.endDate,
        clearanceLevel=employee.clearanceLevel,
        authenticated=employee.authenticated,
        chargeline_ids=",".join(map(str, employee.chargeline_ids)),
        timesheet_ids=",".join(map(str, employee.timesheet_ids)),
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return {"message": "Employee added", "id": db_employee.id}

"""
@app.get("/employees/", response_model=List[EmployeeCreate])
def get_employees(db: Session = Depends(get_db)):
    employees = db.query(models.Employee).all()
    return [
        EmployeeCreate(
            **e.__dict__,
            chargeline_ids=[int(x) for x in e.chargeline_ids.split(",") if x],
            timesheet_ids=[int(x) for x in e.timesheet_ids.split(",") if x]
        )
        for e in employees
    ]
    """
    