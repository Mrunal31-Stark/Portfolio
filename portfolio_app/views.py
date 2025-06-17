from django.shortcuts import render, redirect
from django.http import FileResponse
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
client = MongoClient(os.getenv('mongodb://localhost:27017'))
db = client['portfolio_db']
contact_collection = db['contact_data']

def home(request):
    return render(request, 'index.html')

def download_resume(request):
    return FileResponse(open('portfolio_app/static/mrunal_resume124 (2).pdf', 'rb'), as_attachment=True)

def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact_collection.insert_one({
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        })
        return redirect('home')
