from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
import json
from main.translatorr import translate
from rest_framework.views import APIView
class TranslatorAPI(APIView):
    def get(self, request):
        text = request.GET.get('text')
        lang_to = request.GET.get('lang_to')
        lang_from = request.GET.get('lang_from')

        with open('C:/Users/atikc/PycharmProjects/kktranslator/translator/language_data.json') as file:
            languages_dict = json.load(file)
        context = {'lang_from':lang_from, 'lang_to':lang_to, 'text':text, 'languages_dict':languages_dict.items()}

        if text and len(text) <= 5000:
            translated_text = translate(lang_from, lang_to, text)
            context['translated_text'] = translated_text
            print(context['translated_text'])
        return Response(context)
class TranslatorHtmlAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'main.html'
    def get(self, request):
        text = request.GET.get('text')
        lang_to = request.GET.get('lang_to')
        lang_from = request.GET.get('lang_from')

        with open('C:/Users/atikc/PycharmProjects/kktranslator/translator/language_data.json') as file:
            languages_dict = json.load(file)
        context = {'lang_from':lang_from, 'lang_to':lang_to, 'text':text, 'languages_dict':languages_dict.items()}

        if text and len(text) <= 5000:
            translated_text = translate(lang_from, lang_to, text)
            context['translated_text'] = translated_text
            print(context['translated_text'])
        return Response(context)





# Create your views here.
