"""AirQuality Views."""

from django.shortcuts import render
import pandas as pd

def dashboard(request, *args, **kwargs):
    return render(request, 'index.html')


def air_quality(request, *args, **kwargs):
    year = kwargs.get('year', None)
    df = pd.read_csv(
        'https://github.com/KorKux1/Automated-Detection-of-Hazards/raw/develop/Datasets/Air%20Quality%20Data/PM2.5_dataset.csv')

    context = {
        'year': year,
        'records': df.shape[0],
        'air_quality_average': df['air_data_value'].mean(),
        'RH_average': df['RH'].mean(),
        'UGRD_average': df['UGRD'].mean(),
        'VGRD_average': df['VGRD'].mean(),
        'HPBL_average': df['HPBL'].mean(),
        'TMP_average': df['TMP'].mean,
        'GOES_average': df['goes_measurement'].mean(),
    }
    
    return render(request, 'graph.html', context)
