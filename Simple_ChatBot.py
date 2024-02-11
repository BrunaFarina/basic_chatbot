from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"what is your name?",
        ["My name is Romeu",]
    ],
    [
        r"how are you ?",
        ["Not bad. How about you?",]
    ],
    [
        r"i'm (.*) good|good",
        ["Great!",]
    ],
    [
        r"what (.*) like to do?",
        ["I'm a chatbot, I like to talk",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", "Hi!!",]

    ],
    [
        r"quit|bye",
        ["Bye. See you soon"]
    ]
]

chat = Chat(pairs, reflections)

if __name__ == '__main__':
    chat.converse()