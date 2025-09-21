import torch
from torch.utils.data import DataLoader
from sklearn.metrics import f1_score, confusion_matrix, classification_report
from transformers import AutoTokenizer
import pandas as pd
import numpy as np
from BERT_EmotionClassifier import EmotionsClassifier
from torch_dataset_creator import CustomDataset
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

PRE_TRAINED_MODEL_NAME = "xlm-roberta-base"
MAX_LEN = 160
BATCH_SIZE = 16
MODEL_PATH = 'best_model_v2.bin'
class_names = ["Bucurie", "Furie", "Frica", "Tristete", "Neutru"]

tokenizer = AutoTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME)
df_test = pd.read_csv("data/val.csv")

label_encoder = joblib.load('label_encoder.pkl')

texts = df_test.Tweet.to_numpy()
labels = label_encoder.transform(df_test.Emotion)

test_dataset = CustomDataset(
    texts=texts,
    emotions=labels,
    tokenizer=tokenizer,
    max_len=MAX_LEN
)
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = EmotionsClassifier(len(class_names), PRE_TRAINED_MODEL_NAME)
model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model = model.to(device)
model.eval()

all_preds = []
all_labels = []

with torch.no_grad():
    for batch in test_loader:
        input_ids = batch['input_ids'].to(device)
        attention_mask = batch['attention_mask'].to(device)
        labels = batch['emotions'].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        _, preds = torch.max(outputs, dim=1)

        all_preds.extend(preds.cpu().numpy())
        all_labels.extend(labels.cpu().numpy())

f1 = f1_score(all_labels, all_preds, average='weighted')
conf_matrix = confusion_matrix(all_labels, all_preds)

print("Classification Report:\n", classification_report(all_labels, all_preds, target_names=class_names))
print(f"Weighted F1 Score: {f1:.4f}")

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()
