import mathf

def handle_response(message) -> str:
  msg = message.lower()

  if msg == 'hello':
    return "Hello!\nHow can I help you!"

  elif msg == 'hi':
    return "Hi\nHow can i help you!"

  elif msg == 'help':
    return "You enter help\n\nThis bot is for basic mathematical operation like\nAddition\nSubtraction\nMultiplication\nDivision\n\nEnter your Expression "

  elif '+' or '-' or '*' or '/' in msg:
    return mathf.math_function(msg)
  
  
  else:
    return "Don't understand what you said!"
