import spacy
from data import patient_notes

def extract_entities_spacy(text: str) -> dict:
    #Load the pre-trained spaCy model
    nlp = spacy.load("en_core_web_sm")
    # Process the text with spaCy
    doc = nlp(text)

    #--RESULT COMPILATION--#
    # Create a dictionary to hold the extracted entities
    entities = {}

    # doc.ents contains all the named entities found by the model
    for ent in doc.ents: 
        # ent.label is the type of the entity 
        # ent.text is the actual text 

        # group the entity by label
        if ent.label_ not in entities:
            entities[ent.label_] = []
        entities[ent.label_].append(ent.text.strip())

    return entities

#-- TESTING THE EXTRACTOR --# 
if __name__ == "__main__":
    print("---Running spaCy NLP Extractor ---")

    note_to_text = patient_notes[1]

    extracted_entities = extract_entities_spacy(note_to_text)

    print("\nOriginal Note Snippet:")
    print(note_to_text[:200] + "...")

    print("\Extracted Entities:")
    import json 
    print(json.dumps(extracted_entities, indent=2))

