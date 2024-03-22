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
    national_id_ = input("Enter the national id: ")
    person_profile = Profile.find_by_national_id(national_id_)
    if person_profile:
        print("No:", person_profile.name)
        print("Name:", person_profile.national_id)
        print("National_ID:", person_profile.id)     
    else:
        print(f'Profile with {national_id_} not found')
        
        
def list_specific_dairy_farmers_records():
    dairy_farmer_national_id = input("Enter the national id: ")
    dairy_farmer_profile = Profile.find_by_national_id(dairy_farmer_national_id)
    if dairy_farmer_profile:
        print("Dairy Farmer's Name:", dairy_farmer_profile.national_id)
        milk_records = MilkProfile.find_by_national_id(dairy_farmer_national_id)
        if milk_records:
            print("Milk Records:")
            for record in milk_records:
                print(f"  Date: {record.date}, Litres: {record.litres}")
        else:
            print(f'No milk records found for profile with {dairy_farmer_national_id}')
    else:
        print(f'Profile with national ID {dairy_farmer_national_id} not found')

        
def list_specific_pluckers_records():
    plucker_national_id = input("Enter the national id: ")
    plucker_profile = Profile.find_by_national_id(plucker_national_id)
    if plucker_profile:
        print("Plucker's Name:", plucker_profile.national_id)
        tea_records = TeaProfile.find_by_national_id(plucker_national_id)
        if tea_records:
            print("Tea Records:")
            for record in tea_records:
                print(f"  Date: {record.date}, Kilograms: {record.kilos}")
        else:
            print(f'No tea records found for profile with {plucker_national_id}')
    else:
        print(f'Profile with national ID {plucker_national_id} not found')

   
   
        
    
def update_profile():
    # use a trailing underscore not to override the built-in id function
    profile_id = input("Enter the profile id: ")
    profile = Profile.find_by_id(profile_id)  # Call the method without passing profile_id
    if profile:
        try:
            new_name = input("Enter the profile's new Name: ")
            new_national_id = input("Enter the profile's new National_id: ")
            
            Profile.update(profile_id, new_name, new_national_id)  # Pass the profile_id, new_name, and new_national_id to the update method
            print(f'Success: {profile}')
        except Exception as exc:
            print("Error updating profile: ", exc)
    else:
        print(f'profile {profile_id} not found')
