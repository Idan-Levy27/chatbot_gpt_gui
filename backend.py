import openai

API_KEY = "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"


class Chatbot:
    def __init__(self):
        openai.api_key = API_KEY

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke abut birds.")
    print(response)
