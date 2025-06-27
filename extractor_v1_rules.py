import re 
from data import patient_notes

def extract_patient_info_rules(text: str) -> dict: 
    # Pattern to find patient ID, which follows "Patient ID:" and consists of digits
    patient_id_pattern = r"Patient ID: (\d+)"    
    # Pattern to find patient name, which follows "Patient Name:" consists of letters and spaces
    patient_name_pattern = r"Patient Name: ([A-Za-z\s]+)"
    # Pattern to find a medication, which follows any character .* and re.DOTALL '.' to match newlines
    medication_pattern = r"Medications: (.*?)(?=\n\n|\Z)"  # Non-greedy match until double newline or end of string
    
    ### Extraction Logic ###
    patient_id_match = re.search(patient_id_pattern, text)
    patient_name_match = re.search(patient_name_pattern, text)
    medication_match = re.search(medication_pattern, text, re.DOTALL | re.IGNORECASE)

    extracted_data = {
        "patient_id": patient_id_match.group(1).strip() if patient_id_match else None,
        "patient_name": patient_name_match.group(1).strip() if patient_name_match else None,
        "medications": medication_match.group(1).strip() if medication_match else None
    } 
    return extracted_data

# --TESTING THE EXTRACTOR --# 
# This block only runs when you excute this script directly 

if __name__ == "__main__": 
    print("--- Running Rule-Based Extractor ---")

    # Check the first note
    note_to_test = patient_notes[0]

    extracted_info = extract_patient_info_rules(note_to_test)

    print("\n Original Note Snippet:")
    print(note_to_test[:200]+ "...") #Print the first 200 characters of the note

    print("\n Extracted Information:")
    import json
    print(json.dumps(extracted_info, indent=2))

