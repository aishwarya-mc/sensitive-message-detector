import pandas as pd

def preprocess_dataset(file_path, output_path):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['Message', 'Message_Type', 'Timestamp'])

    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce', utc=True)
    df = df.dropna(subset=['Timestamp'])
    
    df['Message'] = df['Message'].str.lower()
    
    df.to_csv(output_path, index=False)
    return df

if __name__ == "__main__":
    dataset_path = r"data/chat_messages_dataset-new.csv"
    output_path = r"data/processed_chat_messages_dataset.csv"
    
    processed_df = preprocess_dataset(dataset_path, output_path)
    
    print("Processed dataset written to:", output_path)
    print(processed_df.head())
