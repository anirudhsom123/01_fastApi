# patient management api
from fastapi import FastAPI , Path , HTTPException
import json

app = FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
        
    return data
    

@app.get("/")
def hello():
    return {
        'message' : 'Patient Management system API'
    }
@app.get("/about")
def about():
    return {
        'message' : 'about page for Patient Management system API'
    }

@app.get('/view')
def view():
    data=load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(...,description="return patient details from DB",example='P001')):
    # load patients
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")
    # return {"error" : "Patient not found"}