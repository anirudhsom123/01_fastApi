# patient management api
from fastapi import FastAPI , Path , HTTPException ,Query
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

# path param
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(...,description="return patient details from DB",example='P001')):
    # load patients
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404,detail="Patient not found")
    # return {"error" : "Patient not found"}

# query Parameter
@app.get('/sort')
def sorted_patient(sort_by: str =Query(...,description="select out of height , weight and bmi to sort") ,
                   order: str =Query('asc',description="select from asc for ascending desc for descending")):
    valid_fields=['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=404,detail="select from field height , weight and bmi")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code=404,detail="select from field asc for ascending and desc for descending")
    
    data=load_data()
    sort_order=True if order=='desc' else False

    sorted_data= sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data
