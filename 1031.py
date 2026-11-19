from fastapi import FastAPI , Depends,HTTPException
from sqlmodel import Session, select
app = FastAPI()
@app.patch("/heroes/{hero_id}")

def update_hero(hero_id : int, new_age:int, session: Session = Depends(get_sssieon)):
    db_hero = session.get(Hero , hero_id)
    if not db_hero:
        raise HTTPException(status_code=404 , detail ="Hero not found")

    db_hero = session.get(Hero , hero_id)

    if not db_hero:
        raise HTTPException(status_code = 404 , detail = "Hero not found")
    db_hero.age = new_age
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return {"message": "Hero updated" , "hero" : db_hero}

@app.delete("/heroes/{hero_id}")
def delete_hero(hero_id: int, session : Session = Depends(get_session)):
    db_hero = session.get(Hero, hero_id)

    if not db_hero:
        raise HTTPException (status_code = 404 , detail = "Herb not found")

    session.delete(db_hero)
    session.commit()
    return {"message" : "Hero deleted successfully"}