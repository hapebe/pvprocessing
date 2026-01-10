import pickle
import uuid
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os

app = FastAPI(title="Todo System",description="(Kopie) Beispiel vom HelloCoding.de Blog für eine API mit FastAPI.",version="1",contact={"name":"Felix Schürmeyer"})

def load_data():
    if(os.path.isfile('todos.pickle')):
        with open('todos.pickle', 'rb') as handle:
            return pickle.load(handle)

    return []

class Todo(BaseModel):
    name: str
    description: str
    done: bool | None = None
    id: str | None = None

# Todos Anzeigen
@app.get("/", tags=["Read"])
async def list_item():
    return load_data()

# Spezifische Todo Erhalten
@app.get("/todo/{item_id}",tags=["Read"])
async def read_item(item_id: str):
    data = load_data()

    for item in data:
        if str(item.id) == str(item_id):
            return item

    raise HTTPException(status_code=404, detail="Item not found")

# Todo Punkt Status setzen
@app.get("/done/{item_id}", tags=["Change"])
async def done_item(item_id: str,done: bool):
    data = load_data()

    for index,item in enumerate(data):
        if str(item.id) == str(item_id):
            data[index].done = done;

            pickle.dump(data, open('todos.pickle', 'wb'))

            return data

    raise HTTPException(status_code=404, detail="Item not found")

# Todo Punkt löschen
@app.delete("/todo/{item_id}", tags=["Change"])
async def delete_item(item_id: str):
    data = load_data()

    for index,item in enumerate(data):
        if str(item.id) == str(item_id):
            del data[index]

            pickle.dump(data, open('todos.pickle', 'wb'))

            return data

    raise HTTPException(status_code=404, detail="Item not found")

# Todo Punkt anlegen
@app.post("/todo", tags=["Change"])
async def set_item(item: Todo):
    item.id = uuid.uuid1()
    item.done = False

    data = load_data()

    data.append(item)

    pickle.dump(data, open('todos.pickle', 'wb'))

    return data
