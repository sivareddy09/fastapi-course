from fastapi import FastAPI, Depends
import model
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session


app = FastAPI()

model.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/create-details')
def create(request: schemas.Student, db: Session = Depends((get_db()))):

    new_d = model.Student(id=request.id, name=request.name, branch=request.branch)
    db.add(new_d)
    db.commit()
    db.refresh(new_d)

    return new_d


@app.get('/get-details')
def get_details(db: Session = Depends(get_db())):
    det = db.query(model.Student).all()
    return det


