import telebot

# Replace with your own token
TOKEN = '5574372357:AAEE__wHSt8v7Gfw53hrx_Vr6bO-IuL6U4I'

# Create a bot instance
bot = telebot.TeleBot(TOKEN)

# Create a dictionary to store user information
users = {}

# Define a function to handle "/start" command
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Welcome to the registration bot! Please enter your name:")

# Define a function to handle user input
@bot.message_handler(func=lambda message: True)
def handle_input(message):
    chat_id = message.chat.id
    user_input = message.text

    # If the user has not provided their name yet
    if chat_id not in users:
        # Store the user's name
        users[chat_id] = {'name': user_input}
        bot.send_message(chat_id, "Please enter your surname:")
    # If the user has provided their name but not their surname
    elif 'surname' not in users[chat_id]:
        # Store the user's surname
        users[chat_id]['surname'] = user_input
        bot.send_message(chat_id, "Please enter your phone number (with country code):")
    # If the user has provided their name and surname but not their phone number
    elif 'phone_number' not in users[chat_id]:
        # Store the user's phone number
        users[chat_id]['phone_number'] = user_input
        bot.send_message(chat_id, "Please enter any other information you'd like to provide:")
    # If the user has provided all the necessary information
    else:
        # Store any additional information the user has provided
        users[chat_id]['additional_info'] = user_input
        # Send a confirmation message to the user
        confirmation_message = "Thank you for registering! Here's the information you provided:\n\n" \
                               f"Name: {users[chat_id]['name']}\n" \
                               f"Surname: {users[chat_id]['surname']}\n" \
                               f"Phone Number: {users[chat_id]['phone_number']}\n" \
                               f"Additional Information: {users[chat_id].get('additional_info', 'N/A')}"
        bot.send_message(chat_id, confirmation_message)
        # Remove the user's information from the dictionary to allow for new registrations
        del users[chat_id]

# Start the bot
bot.polling()
