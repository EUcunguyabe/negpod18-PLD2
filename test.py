import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QVBoxLayout, QFormLayout

class HealthTestApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Health Test App")
        self.setGeometry(100, 100, 400, 200)

        # Separate symptom questions and counts for each health test
        self.symptoms = {
            "Cold": ["Any headaches?", "Are you having a fever?", "Are you having a dry cough?", "Are you having a dry sneezing?", "Are you experiencing pain and fatigue?"],
            "Allergy": ["Hives or skin rashes?", "Are you having some eye irritations?", "Are you having a stuffy or runny nose?", "Are you having puffy and watery eyes?", "Are you experiencing a sore throat?", "Are you experiencing either one of the following: diarrhea, nausea, vomiting, excess gas, indigestion?", "Any Tingling or swelling of the lips, face, or tongue?"],
            "Stomach Flu": ["Are you experiencing Diarrhea?", "Are you experiencing nausea or vomiting?", "Are you having abdominal cramps?", "Are you having a fever?"],
            "UTI": ["Are you experiencing Pain or burning during urination?", "Are you experiencing frequent urination?", "Are you having cloudy or strong-smelling urine?", "Any lower abdominal pain?"]
        }

        self.admin_authenticated = False

        self.init_admin_login()

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
        self.label.setText("User Information")

        self.admin_layout.removeWidget(self.login_button)
        self.login_button.setParent(None)

        user_name_label = QLabel("User Name:", self)
        self.user_name_entry = QLineEdit(self)

        age_label = QLabel("Age:", self)
        self.age_entry = QLineEdit(self)

        form_layout = QFormLayout()
        form_layout.addRow(user_name_label, self.user_name_entry)
        form_layout.addRow(age_label, self.age_entry)

        self.admin_layout.addLayout(form_layout)

        self.init_health_test_options()

    def init_health_test_options(self):
        self.health_test_options = QWidget(self)
        self.health_test_options.setGeometry(10, 50, 380, 120)

        layout = QVBoxLayout(self.health_test_options)

        # Create buttons dynamically based on health tests
        for test_type in self.symptoms:
            button = QPushButton(f"{test_type} Test", self.health_test_options)
            button.clicked.connect(lambda _, test_type=test_type: self.run_health_test(test_type))
            layout.addWidget(button)

        self.admin_layout.addWidget(self.health_test_options)

    def run_health_test(self, test_type):
        if not self.admin_authenticated:
            QMessageBox.warning(self, "Unauthorized", "Please log in as an admin first.")
            return

        QMessageBox.information(self, "Health Test", f"Welcome {self.user_name_entry.text()}! Let's start the {test_type} test.")

        # Initialize positive count for the specific health test
        positive_symptoms_count = 0

        # Ask symptom questions specific to the selected health test
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HealthTestApp()
    window.show()
    sys.exit(app.exec_())
