

def validate_gender(gen:str):
    if gen.lower() not in ["male","female"]:
        raise ValueError(f"gender must be male or female")  