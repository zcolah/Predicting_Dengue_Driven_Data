import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def features_train(features_train, labels_train, city):
    features_train = features_train[features_train.city==city].reset_index(drop = True)
    labels_train = labels_train[labels_train.city==city].reset_index(drop = True)
    features_labels = pd.merge(features_train, labels_train)

    features_labels = features_new(features_labels)
    return features_labels

def features_test(features_test, features_train, city):
    features_train_last50week = features_train[features_train.city==city].reset_index(drop = True).tail(50)
    features_test = features_test[features_test.city==city].reset_index(drop = True)
    frames = [features_train_last50week, features_test]
    features_test = pd.concat(frames).reset_index(drop = True)

    features_test = features_new(features_test)

    return features_test

def normalize(features):
    
    features_n = MinMaxScaler().fit_transform(features[features.columns[4:45]])
    features_n = pd.DataFrame(features_n, columns = features.columns[4:45], index=features.index)
    if 'total_cases' in features_n.columns:
        features_n = features_n.drop(columns=['total_cases'])
    features_n['month'] = features['month']
    features_n['weekofyear'] = features['weekofyear']
    features_n['odd_year'] = features['odd_year']
    
    return features_n


def features_new(features):
    # These two columns completely correlate as discussed in A3
    features = features.drop(columns=['reanalysis_sat_precip_amt_mm', 'reanalysis_specific_humidity_g_per_kg'])
    features = features.fillna(method = 'ffill')
    features['month'] = pd.to_datetime(features['week_start_date']).dt.month
    features['odd_year'] = features.year.astype('int64') % 2 == 1
    features['ndvi_mean'] = (features['ndvi_ne'] + features['ndvi_nw'] + features['ndvi_se'] + features['ndvi_sw']) / 4.0

    features['ndvi_mean_rolling_avg'] = features['ndvi_mean'].rolling(window = 50).mean()
    features['ndvi_ne_rolling_avg'] = features['ndvi_ne'].rolling(window = 50).mean()
    features['ndvi_nw_rolling_avg'] = features['ndvi_nw'].rolling(window = 50).mean()
    features['ndvi_se_rolling_avg'] = features['ndvi_se'].rolling(window = 50).mean()
    features['ndvi_sw_rolling_avg'] = features['ndvi_sw'].rolling(window = 50).mean()
    features['precipitation_amt_mm_rolling_avg'] = features['precipitation_amt_mm'].rolling(window = 50).mean()
    features['reanalysis_air_temp_k_rolling_avg'] = features['reanalysis_air_temp_k'].rolling(window = 50).mean()
    features['reanalysis_avg_temp_k_rolling_avg'] = features['reanalysis_avg_temp_k'].rolling(window = 50).mean()
    features['reanalysis_dew_point_temp_k_rolling_avg'] = features['reanalysis_dew_point_temp_k'].rolling(window = 50).mean()
    features['reanalysis_max_air_temp_k_rolling_avg'] = features['reanalysis_max_air_temp_k'].rolling(window = 50).mean()
    features['reanalysis_min_air_temp_k_rolling_avg'] = features['reanalysis_min_air_temp_k'].rolling(window = 50).mean()
    features['reanalysis_precip_amt_kg_per_m2_rolling_avg'] = features['reanalysis_precip_amt_kg_per_m2'].rolling(window = 50).mean()
    features['reanalysis_relative_humidity_percent_rolling_avg'] = features['reanalysis_relative_humidity_percent'].rolling(window = 50).mean()
    features['reanalysis_tdtr_k_rolling_avg'] = features['reanalysis_tdtr_k'].rolling(window = 50).mean()
    features['station_avg_temp_c_rolling_avg'] = features['station_avg_temp_c'].rolling(window = 50).mean()
    features['station_diur_temp_rng_c_rolling_avg'] = features['station_diur_temp_rng_c'].rolling(window = 50).mean()
    features['station_max_temp_c_rolling_avg'] = features['station_max_temp_c'].rolling(window = 50).mean()
    features['station_min_temp_c_rolling_avg'] = features['station_min_temp_c'].rolling(window = 50).mean()
    features['station_precip_mm_rolling_avg'] = features['station_precip_mm'].rolling(window = 50).mean()

    features.drop(features.head(50).index, inplace=True)

    return features

def calculate_outliers(features):
    data = features['total_cases']
    # calculate summary statistics
    data_mean, data_std = mean(data), std(data)
    # identify outliers
    cut_off = data_std * 3
    lower, upper = data_mean - cut_off, data_mean + cut_off
    # identify outliers
    outliers = [x for x in data if x < lower or x > upper]
    print('Identified outliers: %d' % len(outliers))
    # remove outliers
    outliers_removed = [x for x in data if x >= lower and x <= upper]
    print('Non-outlier observations: %d' % len(outliers_removed))
        

def remove_outliers(features):
    return (features[np.abs(features.total_cases-features.total_cases.mean())< (3*features.total_cases.std())])