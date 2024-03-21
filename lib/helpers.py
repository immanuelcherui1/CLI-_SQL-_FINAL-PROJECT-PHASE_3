# lib/helpers.py

from models.profile import Profile
from models.model import Model
from models.tea_profile import TeaProfile
from models.milk_profile import MilkProfile
from models.tenant_profile import TenantProfile


def helper_1():
    print("Performing useful function#1.")
    
def exit_program():
    print("Goodbye!")
    exit()

def list_tenant_profiles():
    tenant_profiles = TenantProfile.get_all()
    for tenant_profile in tenant_profiles:
        print(tea_profile) 

# def list_tea_profiles():
#     CURSOR.execute("""
#         SELECT tea_profile.id, tea_profile.date, profiles.name, tea_profile.kilos 
#         FROM tea_profile 
#         JOIN profiles ON tea_profile.pluckers_national_id = profiles.national_id
#     """)
#     return CURSOR.fetchall()

# def list_milk_profiles():
#     CURSOR.execute("""
#         SELECT milk_profile.id, milk_profile.date, profiles.name, milk_profile.litres 
#         FROM milk_profile 
#         JOIN profiles ON milk_profile.dairy_farmer_national_id = profiles.national_id
#     """)
#     return CURSOR.fetchall()


