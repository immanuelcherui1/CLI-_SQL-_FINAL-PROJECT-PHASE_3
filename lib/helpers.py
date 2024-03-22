# lib/helpers.py

from models.profile import Profile
from models.tea_profile import TeaProfile
from models.milk_profile import MilkProfile
from models.tenant_profile import TenantProfile


    
def exit_program():
    print("See You Again!")
    exit()
    
  
def list_profiles():
    profile_records = Profile.get_all()
    for profile in profile_records:
        print(profile) 


def list_milk_records():
    milk_records = MilkProfile.get_all()
    for milk_profile in milk_records:
        print(milk_profile)
        

def list_tea_records():
    tea_records = TeaProfile.get_all()
    for tea_profile in tea_records:
        print(tea_profile)
        
        
def list_tenant_records():
    tenant_records = TenantProfile.get_all()
    for tenant_profile in tenant_records:
        print(tenant_profile) 


def find_person_profile_by_national_id():
    # use a trailing underscore not to override the built-in id function
    national_id_ = input("Enter the national id: ")
    person_profile = Profile.find_by_national_id(national_id_)
    if person_profile:
        print("No:", person_profile.name)
        print("Name:", person_profile.national_id)
        print("National_ID:", person_profile.id)
        
         
    else:
        print(f'Profile with {national_id_} not found')

