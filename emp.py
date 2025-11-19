def get_employee_details(name, emp_id, department, salary):
  formatted_string = (
      f"Employee Name: {name}\n"
      f"Employee ID: {emp_id}\n"
      f"Department: {department}\n"
      f"Salary: ${salary:,.2f}" 
  )
  return formatted_string


employee1_details = get_employee_details("Alice Smith", "EMP001", "Marketing", 65000.75)
print(employee1_details)

print("\n" + "="*30 + "\n") 

employee2_details = get_employee_details("Bob Johnson", "EMP002", "Engineering", 80000)
print(employee2_details)