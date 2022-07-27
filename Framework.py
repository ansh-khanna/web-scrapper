import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
import Login_1_1
import Home_Page

Login_1_1.login_main()

while Login_1_1.t == 1:
    Home_Page.home()
