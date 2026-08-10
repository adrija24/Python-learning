class employee:
    company = "Google"

    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = employee()
e1.name = "Shivam"
e1.show()
e1.change_company("Tesla")
e1.show()
print(employee.company)
