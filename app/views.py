from flask import Blueprint
from flask import Flask, render_template, url_for, redirect, request, session, jsonify, flash, Blueprint
from .database import Database

view = Blueprint("views", __name__)

@view.route("/")
@view.route("/home")
def home():
    return render_template("index.html", **{"session": session})

@view.route("/get_card")
def get_card(name):
    db = Database()
    cards = db.get_cards_by_name(name, limit=100)
    return cards

@view.route("/get_history")
def get_history(name):
    db = Database()
    history = db.get_price_history(name, limit=15)
    return history
