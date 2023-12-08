import sys
import random
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QVBoxLayout, QFormLayout, QTextBrowser


class HealthTestApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Health Test App")
        self.setGeometry(100, 100, 400, 400)

        # Separating symptom questions and counts for all health tests
        self.symptoms = {
            "Cold": ["Any headaches?", "Are you having a fever?", "Are you having dry coughs?", "Are you experiencing dry sneezes?", "Are you experiencing pain and/or fatigue?"],
            "Allergy": ["Hives or skin rashes?", "Are you having any eye irritations?", "Are you having a stuffy or runny nose?", "Are you having puffy and watery eyes?", "Are you experiencing a sore throat?", "Are you experiencing either one of the following: diarrhea, nausea, vomiting, excess gas, indigestion?", "Any Tingling or swelling of the lips, face, or tongue?"],
            "Stomach Flu": ["Are you experiencing Diarrhea?", "Are you experiencing nausea or vomiting?", "Are you having abdominal cramps?", "Are you having a fever?"],
            "UTI": ["Are you experiencing a painful or burning sensation during urination?", "Are you experiencing frequent urination?", "Are you having cloudy or strong-smelling urine?", "Any lower abdominal pain?"]
        }
        
        self.admin_authenticated = False

        self.init_admin_login()
        
        # initializaton of login 

    def init_admin_login(self):
        self.label = QLabel("Admin Login", self)
        self.username_label = QLabel("Username:", self)
        self.username_entry = QLineEdit(self)
        self.password_label = QLabel("Password:", self)
        self.password_entry = QLineEdit(self)
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.login_button = QPushButton("Login", self)
        self.login_button.clicked.connect(self.admin_login)

        self.admin_layout = QVBoxLayout(self)
        self.admin_layout.addWidget(self.label)

        form_layout = QFormLayout()
        form_layout.addRow(self.username_label, self.username_entry)
        form_layout.addRow(self.password_label, self.password_entry)
        self.admin_layout.addLayout(form_layout)

        self.admin_layout.addWidget(self.login_button)

        self.setLayout(self.admin_layout)

    def admin_login(self):
        # Add your authentication logic here
        username = self.username_entry.text()
        password = self.password_entry.text()

        # For simplicity, let's assume a hardcoded admin username and password
        if username == "admin" and password == "adminpassword":
            self.admin_authenticated = True
            self.init_user_info()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password. Please try again.")

    def init_user_info(self):
        self.label.setText("Patient Information")

        self.admin_layout.removeWidget(self.login_button)
        self.login_button.setParent(None)

        patient_name_label = QLabel("Patient Name:", self)
        self.patient_name_entry = QLineEdit(self)

        age_label = QLabel("Patient Age:", self)
        self.patient_age_entry = QLineEdit(self)

        # Simplified ID generation: current timestamp + random number
        patient_id_label = QLabel("Patient ID:", self)
        timestamp = int(time.time())
        random_number = random.randint(1000, 9999)
        simplified_patient_id = f"{timestamp}-{random_number}"
        self.patient_id_entry = QLineEdit(simplified_patient_id)
        self.patient_id_entry.setReadOnly(True)

        form_layout = QFormLayout()
        form_layout.addRow(patient_name_label, self.patient_name_entry)
        form_layout.addRow(age_label, self.patient_age_entry)
        form_layout.addRow(patient_id_label, self.patient_id_entry)

        self.admin_layout.addLayout(form_layout)

        save_data_button = QPushButton("Save Data", self)
        save_data_button.clicked.connect(self.save_data)
        self.admin_layout.addWidget(save_data_button)

        self.init_health_test_options()

    def init_health_test_options(self):
        self.health_test_options = QWidget(self)
        self.health_test_options.setGeometry(10, 150, 380, 120)

        layout = QVBoxLayout(self.health_test_options)

        # Create buttons dynamically based on health tests
        for test_type in self.symptoms:
            button = QPushButton(f"{test_type} Test", self.health_test_options)
            button.clicked.connect(lambda _, test_type=test_type: self.run_health_test(test_type))
            layout.addWidget(button)

        self.admin_layout.addWidget(self.health_test_options)

        self.view_results_button = QPushButton("View Results", self)
        self.view_results_button.clicked.connect(self.view_results)
        self.clear_page_button = QPushButton("Clear Page", self)
        self.clear_page_button.clicked.connect(self.clear_page)

        self.admin_layout.addWidget(self.view_results_button)
        self.admin_layout.addWidget(self.clear_page_button)

    def run_health_test(self, test_type):
        if not self.admin_authenticated:
            QMessageBox.warning(self, "Unauthorized", "Please log in as an admin first.")
            return

        QMessageBox.information(self, "Health Test", f"Welcome {self.patient_name_entry.text()}! Let's start the {test_type} test.")

        # Initialize positive count for the specific health test
        positive_symptoms_count = 0

        # Ask different assumption question 
        for symptom_question in self.symptoms[test_type]:
            response = QMessageBox.information(self, "Symptom", symptom_question, QMessageBox.Yes | QMessageBox.No)
            if response == QMessageBox.Yes:
                positive_symptoms_count += 1

        # Determine results based on symptoms for the specific health test
        if positive_symptoms_count >= 3:
            message = f"Based on your symptoms, it's possible you have {test_type}. We advise you to seek medical attention as soon as possible."
            QMessageBox.information(self, "Health Test Result", message)
        else:
            QMessageBox.information(self, "Health Test Result", f"Based on your symptoms, it seems you may not have {test_type}.")

    def view_results(self):
        if not self.admin_authenticated:
            QMessageBox.warning(self, "Unauthorized", "Please log in as an admin first.")
            return

        results_summary = "Health Test Results:\n\n"
        # Include logic here to fetch and display results from the database or any other storage
        # For now, let's display a placeholder message
        results_summary += "No results available yet. Run some health tests!"

        results_dialog = QTextBrowser()
        results_dialog.setText(results_summary)
        results_dialog.setWindowTitle("View Results")
        results_dialog.exec_()

    def save_data(self):
        if not self.admin_authenticated:
            QMessageBox.warning(self, "Unauthorized", "Please log in as an admin first.")
            return

        patient_name = self.patient_name_entry.text()
        patient_age = self.patient_age_entry.text()
        patient_id = self.patient_id_entry.text()
        print(f"Patient ID: {patient_id}, Patient Name: {patient_name}, Age: {patient_age} - Data saved to the database.")

    def clear_page(self):
        self.admin_authenticated = False
        self.health_test_options.setParent(None)
        self.label.setText("Admin Login")
        self.username_entry.clear()
        self.password_entry.clear()
        self.init_admin_login()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HealthTestApp()
    window.show()
    sys.exit(app.exec_())
