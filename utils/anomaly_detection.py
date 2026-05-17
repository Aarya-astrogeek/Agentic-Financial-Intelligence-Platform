from sklearn.ensemble import IsolationForest

def detect_anomalies(df):

    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    df['anomaly'] = model.fit_predict(df[['Amount']])

    anomalies = df[df['anomaly'] == -1]

    return anomalies