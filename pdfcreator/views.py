from dataclasses import replace
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django import forms

# Project's files imports:
from pdfcreator.utils.pdfcreator import createpdf
from pdfcreator.utils.csvreader import csv_to_html, csv_reader
from pdfcreator.utils.variablereader import variablereader, variable_modifier

# Main project form (text area for the text editor)
class NameForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control main-text-box'}))

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']

            variable_list = variablereader(text) # This function reasd variables within the text input in the text area, variables are reperesented as follows. "$variable$"
            variable_replace = csv_reader()[1]
            texts = variable_modifier(text, variable_list, variable_replace)
            createpdf(texts) # This functions generates a PDF file from the text input into the main text area

            return render(request, 'pdfcreator/index.html', {'form': form})
        else:    
            return render(request, 'pdfcreator/index.html', {'form': form})

    if request.method == 'GET':
        form = NameForm
        table = csv_to_html() # This function reads a CSV file and creates a HTML table from it
        headers = csv_reader()[0]
        return render(request, 'pdfcreator/index.html', {'form': form, 'table' : table, 'headers': headers})