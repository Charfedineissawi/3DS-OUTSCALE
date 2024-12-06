from django.shortcuts import render
import os
import json
import requests  
from django.conf import settings
from django.http import JsonResponse
import random

# Replace with your actual Hugging Face API token
HUGGING_FACE_API_TOKEN = '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'  

def home(request):
    return render(request, 'index.html') 

def is_monkey_island_question(text):
    json_file_path = os.path.join(settings.BASE_DIR, 'ai_features', 'Monkey_Island.json')
    try:
        with open(json_file_path, 'r') as file:
            keywords = json.load(file)['keywords']
        return any(keyword in text.lower() for keyword in keywords)
    except FileNotFoundError:
        print(f"File not found: {json_file_path}")
        return False

def pirate_translate(text):
    translations = {
        "hello": "ahoy",
        "hi": "ahoy",
        # Add more translations as needed
    }
    
    for word, pirate_word in translations.items():
        text = text.replace(word, pirate_word)
    
    return text

def is_greeting(text):
    greetings = ["ahoy", "hello", "hi", "greetings", "hey"]
    return any(greeting in text.lower() for greeting in greetings)

def random_greeting_response():
    responses = [
        "Ahoy! I be at yer service to answer questions about Monkey Island!",
        "Ahoy there! Ye've found the right pirate for Monkey Island queries!",
        # Add more responses as needed
    ]
    return random.choice(responses)

def chat_with_ai(request):
    user_message = request.GET.get('message', '').strip()  
    
    if not user_message:  # Handle empty input
        return JsonResponse({'response': "Please provide a message."})

    if user_message.lower() == 'bye':
        return JsonResponse({'response': 'Fare thee well!'})

    if is_greeting(user_message):
        response_text = random_greeting_response()
    elif is_monkey_island_question(user_message):
        response_text = get_hugging_face_response(user_message) 
        response_text = pirate_translate(response_text)  
    else:
        response_text = "Arrr, I only be answerin' questions about Monkey Island, matey!"

    return JsonResponse({'response': response_text})

def get_hugging_face_response(user_message):
    url = "https://api-inference.huggingface.co/models/gpt2"  # Model endpoint
    headers = {
        "Authorization": f"Bearer {HUGGING_FACE_API_TOKEN}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": user_message,
        "options": {"use_cache": False}
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            # Check if result is a list and handle accordingly
            if isinstance(result, list) and len(result) > 0:
                return result[0]['generated_text']  # Extract generated text from the first result
            else:
                return result.get('generated_text', "Sorry, I couldn't process that request.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return "Sorry, I couldn't process that request."
    
    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return "Sorry, I couldn't process that request."