from django.forms import ModelForm

from Emploee.models import Employee


class EmployeeCreate(ModelForm):
    class Meta:
        model=Employee
        fields=["User_name","Password","Name","Age","Profile_img"]


    def clean(self):
        print("inside clean")



class EmployeeUpdate(ModelForm):
    class Meta:
        model=Employee
        fields="__all__"



# class EmployLogin(ModelForm):
#     class Meta:
#         model=Employee
#         fields=["User_name","Password"]
#
#     def clean(self):
#             # print("inside clean")
#         pass