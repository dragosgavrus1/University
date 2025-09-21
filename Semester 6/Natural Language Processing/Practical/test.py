import torch
from transformers import AutoTokenizer, AutoModel
from BERT_EmotionClassifier import EmotionsClassifier
import torch.nn.functional as F
import joblib

MODEL_NAME = "xlm-roberta-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

class_names = ["Bucurie", "Furie", "Frica", "Tristete", "Neutru"]

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = EmotionsClassifier(len(class_names), MODEL_NAME)
model.load_state_dict(torch.load("best_model.bin", map_location=device))
model = model.to(device)
model.eval()

label_encoder = joblib.load('label_encoder.pkl')

def predict_emotion(text):
    encoding = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=100,
        truncation=True,
        return_attention_mask=True,
        return_token_type_ids=False,
        padding='max_length',
        return_tensors='pt',
    )

    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids, attention_mask=attention_mask)
        probabilities = F.softmax(outputs, dim=1)
        predicted_class = torch.argmax(probabilities, dim=1)
    
    predicted_emotion = label_encoder.inverse_transform([predicted_class.cpu().item()])[0]
    confidence = probabilities.max().cpu().item()
    return predicted_emotion, confidence

if __name__ == "__main__":
    test_sentences = [
        "Ma simt foarte bine astazi! Sper sa nu se strice vremea.",
        "Sunt foarte furios pentru ca am pierdut autobuzul.",
        "Imi este frica sa vorbesc in public.",
        "Ma simt trist pentru ca am pierdut ceva important.",
        "Astazi este o zi obisnuita, nimic special.",
        "Ma simt ingrijorat in legatura cu examenul de maine.",
        "Sunt dezamagit de rezultatele obtinute. Dar incerc sa raman optimist.",
        "Ma simt calm si relaxat dupa o zi lunga.",
        "Desi sunt fericit, nu pot sa nu ma gandesc la problemele de la munca.",
        "Am castigat un premiu, dar ma simt ciudat pentru ca prietenul meu nu a castigat.",
        "Ma simt linistit, dar in acelasi timp putin ingrijorat pentru ziua de maine.",
        "Astazi a fost o zi plina de surprize, unele bune, altele mai putin placute.",
        "Ma simt trist pentru ca am pierdut ceva important, dar incerc sa raman optimist.",
        "Sunt ingrijorat pentru ca nu stiu ce se va intampla, dar incerc sa raman calm.",
        "Ma simt fericit ca am terminat proiectul, dar sunt si putin stresat pentru prezentare.",
        "Sunt fericit ca am primit o promovare, dar ma simt si stresat de noile responsabilitati."
    ]

    for sentence in test_sentences:
        emotion, confidence = predict_emotion(sentence)
        print(f"Input Text: {sentence}")
        print(f"Predicted Emotion: {emotion} (Confidence: {confidence:.2f})\n")
