# -*- coding: utf-8 -*-


#import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.response_selection import get_first_response


app = Flask(__name__)

greet=[]
opens=[]
closes=[]
customer_care=[]
new_acc_doc=[]
new_check_book=[]
change_address=[]

def fileopen(fname,lname):
    fn="TrainingData/"+fname
    fh=open(fn,"r")
    fl=fh.readlines()

    for item in fl:
        lname.append(item.rstrip())

    fh.close()
    return lname


BankBot = ChatBot(name = 'BankBot',
                  read_only = True, #later make true to stop learnig
                  logic_adapters = ["chatterbot.logic.BestMatch"],
                  response_selection_method=get_first_response,)


greet=fileopen("greetings",greet)
opens=fileopen("openingtimings",opens)
closes=fileopen("closingtimings",closes)
customer_care=fileopen("customercare",customer_care)
new_acc_doc=fileopen("newaccdoc",new_acc_doc)
new_check_book=fileopen("newcheckbook",new_check_book)
change_address=fileopen("changeaddress",change_address)


#
# greet = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome."
# ]
#
# open_timing= [
#     "bank open",
#     "The Bank opens at 9AM",
# ]
#
# close_timing = [
#     "bank close",
#     "The Bank closes at 5PM",
# ]
#
# customer_care =[
#     "customer care contact number ",
#     "Call us at 122333444 to connect to an executive"
# ]
#
# documents =[
# 'What are the documents required to open a saving bank account?',
# '''Copy of ration card or any other address proof.
# Identification proof (PAN Card/Passport / Driving License / Election Card)etc all the documents to be self attested and to be verified with the Originals.
# 2 Photographs.'''
# ]



#Initializing Trainer Object
trainer = ListTrainer(BankBot)

#Training BankBot
trainer.train(greet)
trainer.train(opens)
trainer.train(closes)
trainer.train(customer_care)
trainer.train(new_acc_doc)
trainer.train(new_check_book)
trainer.train(change_address)



@app.route("/")
def home():
    return render_template("home.html")
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(BankBot.get_response(userText))
if __name__ == "__main__":
    app.run()
