from django.http import JsonResponse
from django.shortcuts import render
from django.utils.crypto import get_random_string
import json
import string
import string_utils

# Create your views here.

def home(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        lowercase = body['lowercase']
        uppercase = body['uppercase']
        numbers = body['numbers']
        special_characters = body['special']
        password_length = body['length']
        print(lowercase,uppercase,numbers,special_characters,password_length)
        allowed_chars = ''
        count=0
        if lowercase :
            count+=1
        if uppercase :
            count+=1
        if numbers :
            count+=1
        if special_characters :
            count+=1
        if count == 0:
            allowed_chars=string.printable
            unique_id = get_random_string(length=int(password_length),allowed_chars=allowed_chars)
        else:
            set_len = int(password_length)//count
            if lowercase :
                allowed_chars = allowed_chars.join(get_random_string(length=int(set_len),allowed_chars=string.ascii_lowercase))
            if uppercase :
                allowed_chars = allowed_chars.join(get_random_string(length=int(set_len),allowed_chars=string.ascii_uppercase))
            if numbers :
                allowed_chars = allowed_chars.join(get_random_string(length=int(set_len),allowed_chars=string.digits))
            if special_characters :
                allowed_chars = allowed_chars.join(get_random_string(length=int(set_len),allowed_chars='!#$%&*=@\^_{|}~'))
            if len(allowed_chars)<int(password_length):
                needed = int(password_length)-len(allowed_chars)
                allowed_chars = allowed_chars.join(get_random_string(length=needed,allowed_chars=allowed_chars))
            unique_id = string_utils.shuffle(allowed_chars)[:int(password_length)]
        print(unique_id)
        data = {'password':unique_id}
        return JsonResponse(data)
    else:
        return render(request,'index.html')
