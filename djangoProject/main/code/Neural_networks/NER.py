import os

def ner(text):
    command = 'curl -X POST "https://3beb-109-202-60-123.eu.ngrok.io/model" -H "accept: application/json" -H "Content-Type: application/json" -d {"x": [ ' + text + ']}'
    pipe = os.popen(command)
    output = str(pipe.read())
    return output