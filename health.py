# Python Healthcare Management System

patients = []
appointments = []

# Function: Register Patient
def register_patient():

    print("\n===== PATIENT REGISTRATION =====")

    patient_id = len(patients) + 1

    name = input("Enter Patient Name: ")
    age = input("Enter Patient Age: ")
    gender = input("Enter Gender: ")
    phone = input("Enter Phone Number: ")
    disease = input("Enter Health Problem: ")

    patient = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Phone": phone,
        "Disease": disease
    }

    patients.append(patient)

    print("\nPatient Registered Successfully!")
    print("Patient ID:", patient_id)


# Function: View All Patients
def view_patients():

    print("\n===== PATIENT LIST =====")

    if len(patients) == 0:
        print("No Patients Found.")

    else:
        for patient in patients:

            print("--------------------------")
            print("Patient ID:", patient["ID"])
            print("Name:", patient["Name"])
            print("Age:", patient["Age"])
            print("Gender:", patient["Gender"])
            print("Phone:", patient["Phone"])
            print("Disease:", patient["Disease"])


# Function: Search Patient
def search_patient():

    search_id = int(input("Enter Patient ID: "))

    found = False

    for patient in patients:

        if patient["ID"] == search_id:

            print("\nPatient Found!")
            print("Name:", patient["Name"])
            print("Age:", patient["Age"])
            print("Gender:", patient["Gender"])
            print("Phone:", patient["Phone"])
            print("Disease:", patient["Disease"])

            found = True
            break

    if found == False:
        print("Patient Not Found!")


# Function: Book Appointment
def book_appointment():

    print("\n===== BOOK APPOINTMENT =====")

    patient_id = int(input("Enter Patient ID: "))

    found = False

    for patient in patients:

        if patient["ID"] == patient_id:

            doctor = input("Enter Doctor Name: ")
            date = input("Enter Appointment Date: ")

            appointment = {
                "Patient ID": patient_id,
                "Patient Name": patient["Name"],
                "Doctor": doctor,
                "Date": date
            }

            appointments.append(appointment)

            print("\nAppointment Booked Successfully!")
            found = True
            break

    if found == False:
        print("Patient ID Not Found!")


# Function: View Appointments
def view_appointments():

    print("\n===== APPOINTMENT LIST =====")

    if len(appointments) == 0:
        print("No Appointments Found.")

    else:
        for appointment in appointments:

            print("--------------------------")
            print("Patient ID:", appointment["Patient ID"])
            print("Patient Name:", appointment["Patient Name"])
            print("Doctor:", appointment["Doctor"])
            print("Date:", appointment["Date"])


# Main Program
while True:

    print("\n================================")
    print("   HEALTHCARE MANAGEMENT SYSTEM")
    print("================================")

    print("1. Register Patient")
    print("2. View All Patients")
    print("3. Search Patient")
    print("4. Book Appointment")
    print("5. View Appointments")
    print("6. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        register_patient()

    elif choice == "2":
        view_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        book_appointment()

    elif choice == "5":
        view_appointments()

    elif choice == "6":
        print("Thank You for Using Healthcare System!")
        break

    else:
        print("Invalid Choice! Please Try Again.")