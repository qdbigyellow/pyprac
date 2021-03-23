from typing import List
import uvicorn
import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

DATABASE_URL = "sqlite:///./fastapi.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

# 也可以用 declarative_base 用类来实现一个表
notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)

# Engine实现了对各种不同的数据库客户端的封装和调度，是所有SQLAlchemy应用程序的入口点，
# 要使用SQLAlchemy库来操作一个数据库，首先需要获得一个Engine对象，
# engine = create_engine('sqlite://:memory:')  -- 是使用sqlite提供的内存数据库，用于测试使用
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# 是一个容器，其中包含了和DDL相关的所有信息，包括Table、Column等对象。
# 当SQLAlchemy根据数据表映射类生成SQL语句时，它会查询metadata中的信息，然后根据信息生成SQL语句。
metadata.create_all(engine)

# pydantic
class NoteIn(BaseModel):
    text: str
    completed: bool
    
class Note(BaseModel):
    id: int
    text: str
    completed: bool   

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.on_event("startup")
async def startup():
    await database.connect()
    

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()        
    

@app.get("/notes/", response_model=List[Note])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)

@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}


if __name__ == '__main__':
    uvicorn.run(app='fastapi_sql:app', host="127.0.0.1", port=8000, reload=True, debug=True)