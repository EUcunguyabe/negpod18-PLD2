import tkinter as tk
from tkinter import messagebox

class HealthTestApp:
    def __init__(self, master):
        self.master = master
        master.title("Health Test App")

        self.label = tk.Label(master, text="Welcome to the Health Test App! Choose a test to proceed:")
        self.label.pack()

        self.cold_button = tk.Button(master, text="Cold Test", command=lambda: self.run_health_test("Cold"))
        self.cold_button.pack()

        self.allergy_button = tk.Button(master, text="Allergy Test", command=lambda: self.run_health_test("Allergy"))
        self.allergy_button.pack()

        self.flu_button = tk.Button(master, text="Stomach Flu Test", command=lambda: self.run_health_test("Stomach Flu"))
        self.flu_button.pack()

        self.uti_button = tk.Button(master, text="UTI Test", command=lambda: self.run_health_test("UTI"))
        self.uti_button.pack()

    def run_health_test(self, test_type):
        messagebox.showinfo("Health Test", f"Welcome! Let's start the {test_type} test.")

        # Rest of your code for the specific health test goes here...
          # Initialize positive count
        positive_symptoms_count = 0

        symp = messagebox.askquestion("Symptom", "Any headaches?")
        if symp == 'yes':
            positive_symptoms_count += 1

        symp1 = messagebox.askquestion("Symptom", "Are you having a fever?")
        if symp1 == 'yes':
            positive_symptoms_count += 1

        symp2 = messagebox.askquestion("Symptom", "Are you having a dry cough?")
        if symp2 == 'yes':
            positive_symptoms_count += 1

        symp3 = messagebox.askquestion("Symptom", "Are you having a dry sneezing?")
        if symp3 == 'yes':
            positive_symptoms_count += 1

        symp4 = messagebox.askquestion("Symptom", "Are you experiencing pain and fatigue?")
        if symp4 == 'yes':
            positive_symptoms_count += 1

        # Determine results for cold based on symptoms
        if positive_symptoms_count >= 3:
            message = """
            It's possible you have a cold. Here are some general tips:

            - Rest more than usual and avoid exercise until symptoms are gone.
            - Drink lots of clear fluids (e.g., water, tea).
            - Stay away from cigarette smoke.
            - Do not take antibiotics unless specifically prescribed for you.
            - Avoid drinking alcohol because it weakens your immune system.
            - Avoid caffeine, which can increase congestion and dehydration.
            - Eat a well-balanced diet, including fruits, vegetables, and grains.
            """
            messagebox.showinfo("Health Test Result", message)
        else:
            messagebox.showinfo("Health Test Result", "Based on your symptoms, it seems you may not have a cold.")

        # Ask if the user wants to continue the test using a messagebox
        continue_test = messagebox.askquestion("Continue Test", "Do you want to continue the test?")
        if continue_test.lower() == 'yes':
            # Initialize positive count for the second part of the test
            positive_symptoms_count2 = 0

            sympNam1 = messagebox.askquestion("Symptom", "Hives or skin rashes?")
            if sympNam1 == 'yes':
                positive_symptoms_count2 += 1

            sympNam2 = messagebox.askquestion("Symptom", "Are you having some eye irritations?")
            if sympNam2 == 'yes':
                positive_symptoms_count2 += 1

            sympNam3 = messagebox.askquestion("Symptom", "Are you having a stuffy or runny nose?")
            if sympNam3 == 'yes':
                positive_symptoms_count2 += 1

            sympNam4 = messagebox.askquestion("Symptom", "Are you having puffy and watery eyes?")
            if sympNam4 == 'yes':
                positive_symptoms_count2 += 1

            sympNam5 = messagebox.askquestion("Symptom", "Are you experiencing a sore throat?")
            if sympNam5 == 'yes':
                positive_symptoms_count2 += 1

            sympNam6 = messagebox.askquestion("Symptom", "Are you experiencing either one of the following: diarrhea, nausea, vomiting, excessing gas, indigestion?")
            if sympNam6 == 'yes':
                positive_symptoms_count2 += 1

            sympNam7 = messagebox.askquestion("Symptom", "Any Tingling or swelling of the lips, face, or tongue?")
            if sympNam7 == 'yes':
                positive_symptoms_count2 += 1
        
            # Determine results for the second part of the test based on symptoms
            if positive_symptoms_count2 >= 5:
                message = """
                The most effective way to manage allergies is to eliminate or avoid the allergen. 
                Lifestyle changes, such as keeping living spaces clean for dust mite allergies or
                staying indoors during high pollen counts, can help. Medications like antihistamines, 
                decongestants, and anti-inflammatory agents are used to relieve symptoms caused by 
                unavoidable allergens. Antihistamines alleviate sneezing and itching, decongestants 
                reduce nasal congestion, and anti-inflammatory agents, usually in nasal spray form, 
                address swelling and sneezing. In severe cases, allergy shots, containing small amounts
                of allergens, are administered to build the immune system's defenses. While some 
                allergies may diminish with age, others persist throughout life.
                """
                messagebox.showinfo("Health Test Result", "It's likely you are experiencing allergies.\n\n" + message)
            else:
                messagebox.showinfo("Health Test Result", "Based on your symptoms, it seems you may not have the allergies.")

                 # Ask if the user wants to continue the test using a messagebox
        continue_test = messagebox.askquestion("Continue Test", "Do you still want to continue the test?, we would test for Stomach flu")
        if continue_test.lower() == 'yes':
            # Initialize positive count for the thirdd part of the test
            positive_symptoms_count3 = 0

            sympName1 = messagebox.askquestion("Symptom", "Are you experiencing Diarrhea?")
            if sympName1 == 'yes':
                positive_symptoms_count3 += 1

            sympName2 = messagebox.askquestion("Symptom", "Are you experiencing nausea or vomiting?")
            if sympName2 == 'yes':
                positive_symptoms_count3 += 1

            sympName3 = messagebox.askquestion("Symptom", "Are you having a abdominal cramps?")
            if sympName3 == 'yes':
                positive_symptoms_count3 += 1

            sympName4 = messagebox.askquestion("Symptom", "Are you having a fever.?")
            if sympName4 == 'yes':
                positive_symptoms_count3 += 1
           
        
            # Determine results for the second part of the test based on symptoms
            if positive_symptoms_count3 >= 3:
                message = """
               What to do: Stay hydrated by drinking fluids, 
               eat bland foods, get plenty of rest. If symptoms 
               are severe, persist, or if dehydration is a concern, 
               seek medical attention.
                """
                messagebox.showinfo("Health Test Result", "It's likely you are experiencing Stomach Flu.\n\n" + message)
            else:
                messagebox.showinfo("Health Test Result", "Based on your symptoms, it seems you may not have stomach flu.")

               # Ask if the user wants to continue the test using a messagebox
        continue_test = messagebox.askquestion("Continue Test", "Do you still want to continue the test?, we would test for UTIs (Urinary track infection)")
        if continue_test.lower() == 'yes':
            # Initialize positive count for the thirdd part of the test
            positive_symptoms_count3 = 0

            sympName12 = messagebox.askquestion("Symptom", "Are you experiencing  Pain or burning during urination?")
            if sympName12 == 'yes':
                positive_symptoms_count3 += 1

            sympName22 = messagebox.askquestion("Symptom", "Are you experiencing  frequent urination?")
            if sympName22 == 'yes':
                positive_symptoms_count3 += 1

            sympName33 = messagebox.askquestion("Symptom", "Are you having cloudy or strong-smelling urine?")
            if sympName33 == 'yes':
                positive_symptoms_count3 += 1

            sympName44 = messagebox.askquestion("Symptom", "Any lower abdominal pain?")
            if sympName44 == 'yes':
                positive_symptoms_count3 += 1
           
        
            # Determine results for the second part of the test based on symptoms
            if positive_symptoms_count3 >= 3:
                message = """
            What to do: Drink plenty of water, urinate frequently,
            and consult a healthcare professional for proper diagnosis 
            and treatment, which often involves antibiotics.
                """
                messagebox.showinfo("Health Test Result", "It's likely you are experiencing Stomach Flu.\n\n" + message)
            else:
                messagebox.showinfo("Health Test Result", "Based on your symptoms, it seems you may not have stomach flu.")
        else:
            messagebox.showinfo("Health Test Result", "Thanks for taking the test. Goodbye!")

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthTestApp(root)
    root.mainloop()
