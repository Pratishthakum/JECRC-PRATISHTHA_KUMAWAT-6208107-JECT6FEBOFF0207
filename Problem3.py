#Hospital Patient Visit Counter



class Solution:

    def department_patient_count(self, visits):
        dept_count = {}
        
        for i in visits:
            department = i["department"]
            if department in dept_count:
                dept_count[department] += 1
            else:
                dept_count[department] = 1

        max_department = max(dept_count, key=dept_count.get)

        return dept_count, max_department
