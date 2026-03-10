from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
from database import Base, engine

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


groceries = [
    {"name": "Rice", "tamil": "அரிசி", "price": 60},
    {"name": "Milk", "tamil": "பால்", "price": 40},
    {"name": "Eggs", "tamil": "முட்டை", "price": 6},
    {"name": "Bread", "tamil": "ரொட்டி", "price": 35},
    {"name": "Sugar", "tamil": "சர்க்கரை", "price": 50},
    {"name": "Oil", "tamil": "எண்ணெய்", "price": 120},
]


translations = {
    "rice": "அரிசி",
    "milk": "பால்",
    "eggs": "முட்டை",
    "bread": "ரொட்டி",
    "sugar": "சர்க்கரை",
    "oil": "எண்ணெய்",
    "அரிசி": "Rice",
    "பால்": "Milk",
    "முட்டை": "Eggs",
    "ரொட்டி": "Bread",
    "சர்க்கரை": "Sugar",
    "எண்ணெய்": "Oil",
}


class Item(BaseModel):
    price: int
    quantity: int


class Cart(BaseModel):
    items: List[Item]


class Budget(BaseModel):
    total: int
    budget: int


class Translate(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "groceries": groceries},
    )


@app.get("/groceries")
def get_groceries():
    return groceries


@app.post("/calculate-total")
def calculate_total(cart: Cart):
    total = sum(item.price * item.quantity for item in cart.items)
    return {"total": total}


@app.post("/compare-budget")
def compare_budget(data: Budget):
    if data.total > data.budget:
        return {"status": "Budget exceeded"}
    return {"status": "Within budget"}


@app.post("/translate")
def translate(data: Translate):
    text = data.text.lower()
    return {"translation": translations.get(text, "Translation not found")}