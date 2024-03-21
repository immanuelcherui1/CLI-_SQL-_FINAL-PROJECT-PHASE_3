#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.profile import Profile
from models.model import Model
from models.tea_profile import TeaProfile
from models.milk_profile import MilkProfile
from models.tenant_profile import TenantProfile
import ipdb


def reset_database():
    
    Profile.drop_table()
    Model.drop_table()
    TeaProfile.drop_table()
    MilkProfile.drop_table()
    TenantProfile.drop_table()
    
    
    Profile.create_table()
    Model.create_table()
    TeaProfile.create_table()
    MilkProfile.create_table()
    TenantProfile.create_table()

    # Seed Profiles
    Profile.create("George Okumu", 31875378),
    Profile.create("Naomi Mogi", 37654341),
    Profile.create("Immanuel Ronoh", 18795402),
    Profile.create("Sarah Wanjiku", 42345878),
    Profile.create("Ian Chesire", 37650321),
    Profile.create("Adriano Suprine", 28769430),
    Profile.create("Lamech Omwega", 22845878),
    Profile.create("Samuel Omoding", 18654620),
    Profile.create("Mary Watiri", 33765032),
    Profile.create("Sydney Mukisira", 42305070),
    Profile.create("Hillary Maina", 27600021),
    Profile.create("Philiph Wekullo", 15876543)
    

    # Seed Models
    Model.create("Tea")
    Model.create("Milk")
    Model.create("Tenant")

    # Seed Tea Profiles
    TeaProfile.create("2024-03-10", 31875378, 23.3)
    TeaProfile.create("2024-03-10", 33765032, 41.2)
    TeaProfile.create("2024-03-10", 42345878, 27.5)
    TeaProfile.create("2024-03-10", 37654341, 22.6)
    
    TeaProfile.create("2024-03-11", 33765032, 23.5)
    TeaProfile.create("2024-03-11", 42345878, 26.7)
    TeaProfile.create("2024-03-11", 31875378, 12.6)
    
    TeaProfile.create("2024-03-12", 33765032, 15.7)
    TeaProfile.create("2024-03-12", 42345878, 9.3)
    
    TeaProfile.create("2024-03-13", 31875378, 57.9)
    
    TeaProfile.create("2024-03-14", 33765032, 34.6)
    TeaProfile.create("2024-03-14", 42345878, 19.6)
    
    TeaProfile.create("2024-03-15", 31875378, 20.5)
    
    TeaProfile.create("2024-03-16", 33765032, 45.1)
    TeaProfile.create("2024-03-16", 42345878, 26.8)
    TeaProfile.create("2024-03-16", 18654620, 58.2)
    
    
    # Seed Milk Profiles
    MilkProfile.create("2024-03-10", 18795402, 13.5)
    MilkProfile.create("2024-03-10", 31875378, 11.2)
    MilkProfile.create("2024-03-10", 28769430, 37.9)
    MilkProfile.create("2024-03-10", 37650321, 23.6)
    
    MilkProfile.create("2024-03-11", 28769430, 33.9)
    MilkProfile.create("2024-03-11", 42345878, 26.0)
    MilkProfile.create("2024-03-11", 31875378, 18.8)
    
    MilkProfile.create("2024-03-12", 31875378, 15.0)
    MilkProfile.create("2024-03-12", 42345878, 31.6)
    
    MilkProfile.create("2024-03-13", 18795402, 36.3)
    MilkProfile.create("2024-03-13", 31875378, 37.8)
    
    MilkProfile.create("2024-03-14", 42345878, 59.7)
    MilkProfile.create("2024-03-14", 28769430, 27.5)
    MilkProfile.create("2024-03-14", 37650321, 45.6)
    
    MilkProfile.create("2024-03-15", 18795402, 27.8)
    MilkProfile.create("2024-03-15", 28769430, 14.2)
    
    MilkProfile.create("2024-03-16", 18795402, 63.9)
    MilkProfile.create("2024-03-16", 27600021, 30.7)
    MilkProfile.create("2024-03-16", 31875378, 22.5)
    MilkProfile.create("2024-03-16", 37650321, 39.0)
    

    # Seed Tenant Profiles
    TenantProfile.create(31875378, "2023-12-01", 101, 5000)
    TenantProfile.create(22845878, "2024-01-05", 102, 5500)
    TenantProfile.create(18795402, "2024-01-17", 103, 6000)
    TenantProfile.create(27600021, "2024-02-05", 104, 5000)
    TenantProfile.create(18654620, "2024-02-11", 105, 5500)
    TenantProfile.create(42305070, "2024-02-11", 106, 6000)
    TenantProfile.create(42345878, "2024-03-01", 107, 5000)


reset_database()
ipdb.set_trace()
