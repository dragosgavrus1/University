import spacy
from spacy import displacy
from tabulate import tabulate

nlp_models = {
    "english": spacy.load("en_core_web_sm"),
    "romanian": spacy.load("ro_core_news_sm")
}

texts = {
    "romanian": [
        "Inteligența artificială transformă industriile prin automatizarea sarcinilor și îmbunătățirea eficienței. Permite mașinilor să învețe din date și să ia decizii inteligente.",
        "Tehnologia avansează într-un ritm fără precedent, modelând modul în care lucrăm, comunicăm și trăim. AI joacă un rol crucial în această evoluție.",
        "Algoritmii de învățare automată analizează cantități uriașe de date pentru a detecta modele și a prezice rezultate. Acest lucru ajută companiile să își optimizeze procesele și să ia decizii bazate pe date.",
        "Roboții alimentați de AI revoluționează producția, sănătatea și serviciile pentru clienți. Aceștia îmbunătățesc productivitatea și oferă soluții inovatoare.",
        "Viitorul AI oferă posibilități infinite, de la mașini autonome la asistenți virtuali personalizați. Considerațiile etice rămân esențiale în dezvoltarea sa."
    ],
    "english": [
        "Artificial Intelligence is transforming industries by automating tasks and improving efficiency. It enables machines to learn from data and make intelligent decisions.",
        "Technology is advancing at an unprecedented pace, shaping the way we work, communicate, and live. AI plays a crucial role in this evolution.",
        "Machine learning algorithms analyze vast amounts of data to detect patterns and predict outcomes. This helps businesses optimize processes and make data-driven decisions.",
        "AI-powered robots are revolutionizing manufacturing, healthcare, and customer service. They enhance productivity and provide innovative solutions.",
        "The future of AI holds endless possibilities, from self-driving cars to personalized virtual assistants. Ethical considerations remain crucial in its development."
    ]    
}

def preprocess_text(text, nlp):
    doc = nlp(text.lower())

    displacy.serve(doc, style='dep')

    entity_dict = {token.text: ent.label_ for ent in doc.ents for token in ent}

    processed_tokens = [
        (token.text, token.lemma_, token.pos_, token.tag_, entity_dict.get(token.text, "") )
        for token in doc
        if not token.is_stop and not token.is_punct and not token.is_space
    ]
    headers = ["Token", "Lemma", "POS", "Tag", "NER"]
    print(tabulate(processed_tokens, headers=headers, tablefmt="grid"))

    return processed_tokens

processed_texts = {
    lang: [preprocess_text(text, nlp_models[lang]) for text in texts_list]
    for lang, texts_list in texts.items()
}

for lang, processed_list in processed_texts.items():
    print(f"--- Processed {lang} texts ---")
    for original, processed in zip(texts[lang], processed_list):
        print(f"Original: {original}")
        print(f"Processed: {processed}")
        print()
