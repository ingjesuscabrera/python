# -*- coding: utf-8 -*-
import json

# Cargamos a un diccionaio:
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Convertimos un diccionario en  JSON:
y = json.dumps(x)

# Vemos el Json como string:
print(y)
