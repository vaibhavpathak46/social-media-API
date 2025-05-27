from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils

router=APIRouter(
    tags=["Authentication"]
)
@router.post("/login")
def login( userCredentials:schemas.UserLogin, db: Session = Depends(database.get_db)):
   user= db.query(models.User).filter(models.User.email==userCredentials.email).first()
   if not user:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
   utils.verify(userCredentials.password, user.password)
   if not user:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")
   return {"message":"Login successful"}