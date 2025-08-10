import csv
import os

class EmployeeManager:
    def __init__(self):
        self.employees = {}  # id: {"Name": "", "Position": "", "Salary": "", "Email": ""}
        self.file_name = "employees.csv"
        self.load_data()

    def load_data(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.employees[row["ID"]] = {
                        "Name": row["Name"],
                        "Position": row["Position"],
                        "Salary": row["Salary"],
                        "Email": row["Email"]
                    }

    def save_data(self):
        with open(self.file_name, mode="w", newline="") as file:
            fieldnames = ["ID", "Name", "Position", "Salary", "Email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for emp_id, data in self.employees.items():
                row = {"ID": emp_id}
                row.update(data)
                writer.writerow(row)

    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        if emp_id in self.employees:
            print("Employee with this ID already exists.")
            return
        name = input("Enter Name: ")
        position = input("Enter Position: ")
        salary = input("Enter Salary: ")
        if not salary.isdigit():
            print("Salary must be a number.")
            return
        email = input("Enter Email: ")

        self.employees[emp_id] = {
            "Name": name,
            "Position": position,
            "Salary": salary,
            "Email": email
        }
        self.save_data()
        print("Employee added successfully.")

    def view_all(self):
        if not self.employees:
            print("No employees found.")
            return
        for emp_id, data in self.employees.items():
            print(f"{emp_id} - {data['Name']} - {data['Position']} - {data['Salary']} - {data['Email']}")

    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        if emp_id not in self.employees:
            print("Employee not found.")
            return
        current = self.employees[emp_id]

        name = input(f"Enter new Name (leave blank to keep '{current['Name']}'): ")
        position = input(f"Enter new Position (leave blank to keep '{current['Position']}'): ")
        salary = input(f"Enter new Salary (leave blank to keep '{current['Salary']}'): ")
        email = input(f"Enter new Email (leave blank to keep '{current['Email']}'): ")

        if name.strip():
            current["Name"] = name
        if position.strip():
            current["Position"] = position
        if salary.strip():
            if salary.isdigit():
                current["Salary"] = salary
            else:
                print("Invalid salary. Keeping old value.")
        if email.strip():
            current["Email"] = email

        self.employees[emp_id] = current
        self.save_data()
        print("Employee updated successfully.")

    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            self.save_data()
            print("Employee deleted.")
        else:
            print("Employee not found.")

    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in self.employees:
            data = self.employees[emp_id]
            print(f"ID: {emp_id}")
            print(f"Name: {data['Name']}")
            print(f"Position: {data['Position']}")
            print(f"Salary: {data['Salary']}")
            print(f"Email: {data['Email']}")
        else:
            print("Employee not found.")


def main():
    manager = EmployeeManager()

    while True:
        print("\n--- Employee Manager ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employee")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            manager.update_employee()
        elif choice == "4":
            manager.delete_employee()
        elif choice == "5":
            manager.search_employee()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
