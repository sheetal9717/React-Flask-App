#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 13:07:31 2020

@author: sheetal
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname("__file__"))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(80), unique=True)
    country_code = db.Column(db.String(40), unique=True)
    total_cases = db.Column(db.Integer, unique=False)
    recovered_cases = db.Column(db.Integer, unique=False)
    death_cases = db.Column(db.Integer, unique = False)
    # email = db.Column(db.String(120), unique=True)

    def __init__(self, country, country_code, total_cases, recovered_cases, death_cases):
        self.country = country
        self.country_code = country_code
        self.total_cases = total_cases
        self.recovered_cases = recovered_cases
        self.death_cases = death_cases


class CountrySchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('country', 'country_code', 'total_cases', 'recovered_cases', 'death_cases')


country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)


@app.route("/")
def hello():
    return "Hello World!"

# endpoint to create new user
@app.route("/country", methods=["POST"])
def add_country():
    country = request.json['country']
    country_code = request.json['country_code']
    total_cases = request.json['total_cases']
    recovered_cases = request.json['recovered_cases']
    death_cases = request.json['death_cases']
    
    new_country = Country(country, country_code, total_cases, recovered_cases, death_cases)
    
    db.session.add(new_country)
    db.session.commit()
    print("***************************")
    print(new_country.country)
    print(new_country.country_code)
    print(new_country.total_cases)
   
    print("***************************")
    return "successfully added"


# endpoint to show all users
@app.route("/country", methods=["GET"])
def get_country():
    all_countries = Country.query.all()
    result = countries_schema.dump(all_countries)
    print("++++++++++++++++++++")
    print(type(result))
    print("++++++++++++++++++++")
    return jsonify(result)


#endpoint to get user detail by id
@app.route("/country/<id>", methods=["GET"])
def country_detail(id):
    country_ = Country.query.get(id)
    return country_schema.jsonify(country_)


# # endpoint to update user
# @app.route("/user/<id>", methods=["PUT"])
# def user_update(id):
#     user = User.query.get(id)
#     username = request.json['username']
#     email = request.json['email']

#     user.email = email
#     user.username = username

#     db.session.commit()
#     return user_schema.jsonify(user)


# # endpoint to delete user
# @app.route("/user/<id>", methods=["DELETE"])
# def user_delete(id):
#     user = User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()

#     return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)