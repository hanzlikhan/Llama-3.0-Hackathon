
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from chatbot import Chatbot
from Backend.sentiment_analysis import SentimentAnalyzer
from resources import get_resources
from Backend.crisis_management import send_crisis_alert

app = Flask(__name__)
api = Api(app)

chatbot = Chatbot()
sentiment_analyzer = SentimentAnalyzer()

class ChatbotResource(Resource):
    def post(self):
        user_input = request.json.get('message')
        response = chatbot.generate_response(user_input)
        return jsonify({"response": response})

class SentimentResource(Resource):
    def post(self):
        text = request.json.get('text')
        sentiment = sentiment_analyzer.analyze_sentiment(text)
        return jsonify({"sentiment": sentiment})

class ResourcesResource(Resource):
    def get(self):
        resource_type = request.args.get('type')
        resources = get_resources(resource_type)
        return jsonify(resources)

class CrisisResource(Resource):
    def post(self):
        phone = request.json.get('phone')
        message = request.json.get('message')
        send_crisis_alert(phone, message)
        return jsonify({"status": "alert sent"})

class UserResource(Resource):
    def get(self):
        user_id = request.args.get('user_id')
        # Implement user data retrieval
        user_data = {}  # Fetch user data from database
        return jsonify(user_data)

api.add_resource(ChatbotResource, '/chatbot')
api.add_resource(SentimentResource, '/sentiment')
api.add_resource(ResourcesResource, '/resources')
api.add_resource(CrisisResource, '/crisis')
api.add_resource(UserResource, '/user_data')

if __name__ == '__main__':
    app.run(debug=True)
