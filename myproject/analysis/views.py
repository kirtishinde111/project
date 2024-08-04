
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend.
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import UploadFileForm
from .models import UploadFile
from django.urls import reverse

def file_list(request):
    files = UploadFile.objects.all()
    print(f"Files: {files}")  # Debugging line

    return render(request, 'file_list.html', {'files': files})

def delete_file(request, pk):
    upload = get_object_or_404(UploadFile, pk=pk)
    file_path = upload.file.path

    if os.path.exists(file_path):
        os.remove(file_path)
    upload.delete()
    return redirect('analysis:file_list')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save()
            print(f"File uploaded and saved at: {upload.file.path}")  # Debugging line

            return redirect('analysis:process_file', pk=upload.pk)

    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def process_file(request, pk):
    try:
        upload = get_object_or_404(UploadFile, pk=pk)
        print(f"Processing file with PK: {upload.pk}")  # Debugging line
    
    #df = pd.read_csv(upload.file.path)
        file_path = upload.file.path
        if not os.path.exists(file_path):
            return render(request, 'error.html', {'message': 'The requested file does not exist.'})

    
        df = pd.read_csv(file_path)

        first_rows = df.head()
        summary_statistics = df.describe().transpose()
        missing_values = df.isnull().sum()

        plots = []
        for column in df.select_dtypes(include=[float, int]).columns:
            plt.figure(figsize=(6, 5))
            sns.histplot(df[column].dropna(), kde=True)
            plt.title(f'Histogram of {column}')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            plt.close()
            buf.seek(0)
            image_base64 = base64.b64encode(buf.read()).decode('utf-8')
            plots.append({'column': column, 'image': f'data:image/png;base64,{image_base64}'})

        context = {
            'first_rows': first_rows.to_html(),
            'summary_statistics': summary_statistics.to_html(),
            'missing_values': missing_values.to_dict(),
            'plots': plots,
            'pk':pk,
       }
       #return redirect('analysis:visualize_data', pk=upload.pk)

        return render(request, 'process.html', context)
    except Http404:
        return render(request, 'error.html', {'message': 'No file uploaded.'})
 

def generate_histogram(data):
    num_cols = data.select_dtypes(include=['number']).columns
    histograms = {}
    
    for col_name in num_cols:
        plt.figure(figsize=(6, 5))
        data[col_name].hist(bins=30)
        plt.title(f'Histogram of {col_name}')
        plt.xlabel(col_name)
        plt.ylabel('Frequency')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        img_str = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()
        plt.close()
        
        histograms[col_name] = img_str

    return histograms

def visualize_data(request, pk):
    try:

        #upload_file = UploadFile.objects.first()
        upload_file = get_object_or_404(UploadFile, pk=pk)

        print(f"Visualize data for file with PK: {pk}")
        file_path = upload_file.file.path

        if not os.path.exists(file_path):
            return render(request, 'error.html', {'message': 'No file uploaded.'})
    
    
        data = pd.read_csv(file_path)
        histograms = generate_histogram(data)
        context = {
            'histograms': histograms,
            'pk': pk,
        }
        return render(request, 'visualization.html', context)
    except Http404:
       return render(request, 'error.html', {'message': 'No file uploaded.'})