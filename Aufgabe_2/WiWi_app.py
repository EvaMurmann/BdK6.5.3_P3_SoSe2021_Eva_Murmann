# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 15:00:44 2021

@author: alpha
"""

from flask import Flask, render_template, request

print(__name__)
app = Flask (__name__)

#Decorator 
@app.route("/") #Start page 
@app.route("/home")
def home_page():
    return render_template("WiWi_display.html")

@app.route("/about/<username>") #Information page
def show_about(username):
    return f"<h2>Homepage of {username}</h2>"

@app.route("/info") #Information page
def show_info():
    return "<p>Some information</p>"
    
    
@app.route("/Search/<Institut>") #
def WiWi_display(Institut):
    return render_template ("WiWi_display.html", Institut=Institut)
    
@app.route("/WiWi_form")
def isbn_form():
    return render_template ("WiWi_form.html")

@app.route("/WiWi_form_content", methods=["GET"])
def WiWi_form_display():
    Institut = request.args.get("Institut")
    print(request.args)
    return render_template ("WiWi_display.html", Institut=Institut)

