In this work, we present a full-stack web application incorporating predictive analytics to improve healthcare services- Smart Healthcare Solutions. Users can book doctor appointments using this Platform, Schedule diagnostic tests online, read medical reports of all patients, and order their medicines. Doctors can also predict the onset of a disease and proactively manage healthcare using machine learning algorithms
## Functions
### Admin
- Signup their account. Then Login (No Approval Required).
- Can register/view/approve/reject/delete doctors (approve those doctors who applied for job in their hospital).
- Can admit/view/approve/reject/discharge patient (discharge patient when treatment is done).
- Can Generate/Download Invoice pdf (Generate Invoice according to medicine cost, room charge, doctor charge, and other charge).
- Can view/book/approve Appointment (approve those appointments which is requested by patient).

### Doctor
- Apply for job in the hospital. Then Login (Approval required by hospital admin, Then only the doctor can login).
- They can only view the patient details (symptoms, name, mobile ) assigned to that doctor by the admin.
- Can view their discharged(by admin) patient list.
- Can view their Appointments, booked by admin.
- Can delete their Appointment, when the doctor attended their appointment.
-  predictive analysis

### Patient
- Create an account for admit in the hospital. Then Login (Approval required by hospital admin, only patient can login).
- Can view assigned doctor's details like ( specialization, mobile, address).
- Can view their booked appointment status (pending/confirmed by admin).
- Can book appointments. (approval required by admin)
- Can view/download Invoice pdf (Only when that patient is discharged by admin).

### Medicine store
- Patient buy medicine as per doctor's prescription.
- Admin add various types of medicine, number of stock, and edit. 
---

## HOW TO RUN THIS PROJECT
- Install Python(3.7.6) (Don't Forget to Tick Add to Path while installing Python)
- Open the Terminal and Execute the Following Commands :
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf
```
- Download This Project Zip Folder and Extract it
- Move to the project folder in Terminal. Then run the following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter the following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/
```

## Drawbacks/LoopHoles
- Anyone can be an Admin. No approval is required for the admin account. So you can disable the admin signup process and use any logic like creating a superuser.
- There should be at least one doctor in the hospital before admitting a patient. So first add doctor.
- On the update page of the doctor/patient you must update the password.

## Disclaimer
This project is developed for demo purposes and it's not supposed to be used in real applications.

##Screenshots
Homepage
![Homepage](https://github.com/user-attachments/assets/530d3c56-4913-45ae-8ca7-78db08f89ec7)

Admin Portal
![Admin Portal](https://github.com/user-attachments/assets/36d781df-4f71-4a6a-9dd8-dcd92cfbb1e2)

Doctor Portal
![Doctor](https://github.com/user-attachments/assets/6c2872aa-0f8d-4fc5-aea1-63a80cfd4b4f)

Patient Portal
![Patient Portal](https://github.com/user-attachments/assets/56ff5db6-66fc-4145-830a-99e729f253ef)


