# math-bot.github.io
This bot can evaluate the mathematical expression and returns results according to the expression, it only handles +,-,*, and / symbols.
 
 Discord bot


The provided Python code comprises a Discord bot utilizing Flask for keeping the bot alive and responding to user messages.
The bot, triggered by messages beginning with '?', interprets and processes user inputs.
It supports basic mathematical operations through the math_function function, which evaluates expressions using the eval function. 
The handle_response function further refines the bot's behavior by responding to greetings, providing help information, 
and executing mathematical operations based on user input.
Notably, there's an error in the code that checks for mathematical operators, 
and it's advisable to handle potential security concerns associated with using eval for expression evaluation.
