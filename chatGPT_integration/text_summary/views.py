import openai

from django.http import JsonResponse
from rest_framework.views import APIView

from django.conf import settings

openai.api_key = settings.OPEN_AI_SECRET_KEY

class GetSummary(APIView):
    def post(self,request):
        ques = 'can you please summarize the following text in 30 words:'
        data = request.data

        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= ques + "\n\n" + data['text'],
        temperature=0.7,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
        )

        return JsonResponse({'data' : response['choices'][0]['text']})
