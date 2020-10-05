import  pandas as pd

labels_dict = {
    'station_id': 'Station Id',
    'stime': 'Date',
    'air_data_value': 'Air Quality Value',
    'RH': 'RH',
    'UGRD': 'UGRD',
    'VGRD': 'VGRD',
    'HPBL	': 'HPBL	',
    'TMP': 'TMP',
    'goes_measurement': 'Goes Measurement',
    'PM High': 'PM High',
}

def get_dataset():
    dataset = pd.read_csv(
        'https://github.com/KorKux1/Automated-Detection-of-Hazards/raw/develop/Datasets/Air%20Quality%20Data/PM2.5_dataset.csv')

    dataset['stime'] = pd.to_datetime(dataset['stime'])
    dataset = dataset.drop(['Unnamed: 0'], axis=1)
    dummy = [1 if i >= 2.5 else 0 for i in dataset['goes_measurement']]
    dataset['PM High'] = dummy
    dataset['PM High'] = dataset['PM High'].astype(str)

    return dataset
