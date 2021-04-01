# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:44:21 2021

@author: Marek
"""
from app import get_app

app = get_app()
with app.test_client() as test_client:
    response = test_client.get('/')
    
assert '200' in str(response)



