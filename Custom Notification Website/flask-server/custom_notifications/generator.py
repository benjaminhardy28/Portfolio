import openai

API_KEY = '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'
openai.api_key = API_KEY

class NotificationGenerator():
    def __init__(self, user_input):
        self.user_query = user_input
        openai.api_key = API_KEY
        self.model_id = 'gpt-3.5-turbo'
        self.conversation = []
        #self.startupPrompt = 'I have a task for you. I am going to provide you with two different versions of all of the text from a website the next time I write to you. This is all of the text from an HTML website, so some of the information could be irrelevant and I am asking you to filter through that. The two different versions of text are from two different times, before and after when the website was updated. I would like you to analyze both groups of text, and create a summary of the differences in the text. I want this information to be in the form of at most a 30 word notification. This notification does not say what the differences are specifically, but provides an update to what has changed in the text. So in the notification, do not mention anything regarding myself or you and the role of analyzing the website itself, or even the website as a whole. Only provide the notification as if it was given to a user. And also, do not provide any information that is not new to the websites update. Can you do this?. Here is an example: Original text: "Connor McDavid has 10 goals". New Text: "Connor McDavid has 20 goals''. Your output: "NHL player Connor McDavid has scored 10 more goals, bringing his total to 20 goals. Extra information can be added if it describes in better detail the context of the update, like how the output in the example I provided mentions the fact that Connor McDavid is an NHL player.'
        self. startupPrompt = 'I have a task for you. I am going to provide you with two different versions of all of the text from a website the next time I write to you. This is all of the text from an HTML website, so some of the information could be irrelevant and I am asking you to filter through that. The two different versions of text are from two different times, before and after when the website was updated. I would like you to analyze both groups of text, and create a summary of the differences in the text. I want this information to be in the form of at most a 30 word notification. This notification does not say what the differences are specifically, but provides an update to what has changed in the text. So in the notification, do not mention anything regarding myself or you and the role of analyzing the website itself, or even the website as a whole. Only provide the notification as if it was given to a user. And also, do not provide any information that is not new to the website\'s update. Can you do this?. Here is an example: Original text: "Connor McDavid has 10 goals". New Text: "Connor McDavid has 20 goals''. Your output: "NHL player Connor McDavid has scored 10 more goals, bringing his total to 20 goals. Extra information can be added if it describes in better detail the context of the update, like how the output in the example I provided mentions the fact that Connor McDavid is an NHL player. Pretend this notification is going straight to a user who is wanting to know updated information about the web page. They don’t want the notification to include any text that includes words like “the website update mentions” since the notification should purely include the new information.'
        self.conversation.append({'role': 'system', 'content': self.startupPrompt})
        self.ChatGPT_conversation(self.conversation)


    def getNotif(self, newText, previousText):
        getNotificationPrompt = 'Here is the origonal text from before the website was updated:"' + previousText + '". ' + 'Here is the new text from after the website was updated: "' + newText
        self.conversation.append({'role': 'user', 'content': getNotificationPrompt})
        notif = self.ChatGPT_conversation(self.conversation)
        return notif #IK this is super ugly but will fix lol

    def ChatGPT_conversation(self, conversation):
        response = openai.ChatCompletion.create(
            model=self.model_id,
            messages=conversation
        )
        print(response.choices[0].message.content)
        return (response.choices[0].message.content)
        #self.conversation.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})


# if __name__ == "__main__":
#     NotificationGenerator("test")
#     while True:
#         pass