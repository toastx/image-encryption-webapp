from flask import Flask,render_template, redirect, url_for
import requests

server = Flask(__name__, template_folder='templates')

database = {}



@server.route("/encryption")
def encrypt_image():
    None

@server.route("/decryption")
def decrypt_image():
    None
