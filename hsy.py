import core

while True:
    text = input('hsy > ')
    result, error = core.run(text)
    
    if error : print(error.as_string())
    else: print(result)