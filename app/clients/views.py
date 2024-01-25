from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from datetime import datetime
from .utils import commandeAnonyme, data_cookie, panier_cookie

