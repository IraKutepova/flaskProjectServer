
from flask import Flask, request

app = Flask(__name__)
ListOfMessages = []

@app.route('/')
def hello_world():
    return 'Messanger Flask server is running!' \
           '<br> <a href="/status"> Check status</a>'

#
@app.route('/status')
def status():
    return {
        'message_count': len(ListOfMessages)
    }
# отправка сообщений
@app.route('/api/Messanger', methods=['POST'])
def SendMessage():
    msg = request.json #
    print(msg)
    # messages.append({"UserName": "Irina", "MessageText": "Welcome"})
    ListOfMessages.append(msg)
    #print(msg)
    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)}. Посланное сообщение: {msgtext}")

    return f"Сообщение отослано успешно. Всего сообщений: {len(ListOfMessages)}", 200

# Получение сообщений
@app.route('/api/Messanger/<int:id>')
def GetMessage(id):
    print(id)
    if id >= 0 and id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "Not found", 400

if __name__ == "__main__":
    app.run()
