import json
import random
from datetime import datetime
import string
import numpy as np
import hashlib
import os

class PersonalIdentifiers:
    def __init__(self, is_child = False, parent_last_name = None, parent_age = None,  parent_address = None, parent_nationality = None, parent_language = None):
        #Inital
        environment_instance = Environment()
        self.social_identifier = []
        self.is_child = is_child
        self.parent_last_name = parent_last_name
        self.parent_age = parent_age
        self.parent_address = parent_address
        self.parent_nationality = parent_nationality
        self.parent_language = parent_language
        self.children_list = []
        self.industry_list = ['Games', 'Culture and Media', 'Internet Services', 'Communication Equipment', 'Communication Services', 'Semiconductors', 'Software Development', 'Electronic Chemicals', 'Insurance', 'Optical and Photoelectronic', 'Electronic Components', 'Home Appliances', 'Transportation Equipment', 'Computer Equipment', 'Consumer Electronics', 'Construction Engineering', 'Shipbuilding', 'Railways and Highways', 'Education', 'Packaging Materials', 'Banking', 'Brokerage', 'Cement and Building Materials', 'Beauty and Care', 'Shipping and Ports', 'Engineering Consulting Services', 'Decoration and Renovation', 'Aviation and Airports', 'Trade Industry', 'Electricity', 'Instruments and Meters', 'Mining Industry', 'Jewelry', 'Precious Metals', 'General Equipment', 'Gas', 'Rubber Products', 'Non-metallic Materials', 'Logistics Industry', 'Petroleum', 'Wind Power Equipment', 'Chemical Raw Materials', 'Photovoltaic Equipment', 'Energy Metals', 'Batteries', 'Tourism and Hotels', 'Specialized Equipment', 'Agriculture, Livestock, and Fisheries', 'Auto Services', 'Diversified Financials', 'Paper and Printing', 'Utilities', 'Steel', 'Coal', 'Commercial Retail', 'Renovation and Building Materials', 'Food and Beverage', 'Textiles and Apparel', 'Fertilizers', 'Pesticides and Veterinary Drugs', 'Conglomerates', 'Power Equipment', 'Environmental Industry', 'Real Estate Development', 'Medical Devices', 'Alcoholic Beverages', 'Plastic Products', 'Household Light Industry', 'Professional Services', 'Aerospace', 'Chemical Fibers', 'Construction Machinery', 'Real Estate Services', 'Auto Parts', 'Chemical Products', 'Bioproducts', 'Chemical Pharmaceuticals', 'Traditional Chinese Medicine', 'Complete Automobiles', 'Motors', 'Power Grid Equipment']

        #Personal Identifiers
        self.id = self.generate_id()
        self.gender = random.choice(["Male", "Female"])
        self.first_name,self.middle_name,self.last_name = self.generate_name(self.gender)

        #self.nickname = ''
        #self.aliases = ''

        self.date_of_birth = self.generate_dob(is_child)
        dob_datetime = datetime.strptime(self.date_of_birth, "%Y-%m-%d")  # Convert string to datetime
        self.age = self.calculate_age(dob_datetime,environment_instance.date)

        self.nationality = "British"
        #self.identification_number = self.generate_id_number()
        
        #self.birth_weight = self.generate_birth_weight()
        #self.birth_length = self.generate_birth_length()

        #Physical Characteristics
        #self.height = self.generate_height(self.gender)
        #self.weight = self.generate_weight(self.gender)
        #self.eye_color = self.generate_eye_color()
        #self.hair_color = self.generate_hair_color()
        #self.blood_type = self.generate_blood_type()
        #self.fingerprint = self.generate_fignerprint()
        #self.dna = self.generate_dna()

        
        self.address = self.generate_address()
        self.phone = self.generate_phone()
        self.email = self.generate_email()
        
        #Socioeconomic Indicators
        self.education_level = self.generate_education_level(self.age)
        self.occupation, self.industry = self.generate_occupation(self.age, self.industry_list)
        self.work_experience = self.generate_work_experience(self.age,self.occupation)
        self.income = self.generate_income(self.work_experience,self.education_level,self.occupation,self.industry_list, self.industry)

        #Health and Medical Information
        #self.medical_history = self.generate_medical_history(self.age)
        #self.allergies = self.generate_allergies()
        #self.medications = self.generate_medications()
        #self.immunizations = self.generate_immunizations()

        #Cultural or Social Identifiers
        self.religion  = self.generate_religion()
        self.ethnicity = self.generate_ethnicity()
        self.languages = self.generate_languages()

        #Legal Identifiers
        #self.criminal_record = self.generate_criminal_record()
        self.marital_status = self.generate_marital_status()
        self.parental_status = self.generate_parental_status()
        
        #Other properties
        self.political_identifier = self.generate_political_identifier(self.age)
        self.economic_identifier = self.generate_economic_status(self.income)
        self.occupations_identifier = self.occupation

        self.car_num, self.car_value = self.generate_car_properties(self.economic_identifier)
        self.house_num, self.house_value = self.generate_house_properties(self.economic_identifier)
        self.living_status = self.generate_living_status(self.economic_identifier,self.car_num)
        self.commute_identifier = self.generate_commute_identifier(self.car_num)
        self.is_patriot()
        
        #Correction variable
        #self.height_growth_rate = self.generate_growth_rate()

    def generate_id(self):
        hash_object = hashlib.sha256()
        length = 16
        characters = string.ascii_letters + string.digits + string.punctuation

        random_string = ''.join(random.choice(characters) for _ in range(length))
        hash_object.update(random_string.encode('utf-8'))
        id = hash_object.hexdigest()
        return id

    def load_names(self):
        with open(r'final_year_project\config\name.json', 'r') as file:
            names_data = json.load(file)
        return names_data
    
    def load_surnames(self):
        with open('final_year_project\config\surname.json', 'r') as file:
            surnames_data = json.load(file)
        return surnames_data


    def load_json(self,filename):
        with open(filename) as f:
            return json.load(f)

    def generate_name(self, gender):
        names = self.load_names()  
        surnames = self.load_surnames()

        # Filter names by gender
        filtered_names = [name_item["Name"] for name_item in names if name_item["Genre"] == gender.lower()]

        first_name = random.choice(filtered_names)
        middle_name = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=1)) + '.'  # Initial for middle name
        if self.is_child:
            last_name = self.parent_last_name.capitalize()
        else:
            last_name = random.choice(surnames).capitalize()
        return first_name, middle_name, last_name

    def generate_dob(self, is_child):
        if is_child:
            parent_age = self.parent_age

            year = random.randint(2000 - int(parent_age) + 16, 1998)
            month = random.randint(1, 12)
            day = self.get_random_day(month, year)
            return datetime(year, month, day).strftime("%Y-%m-%d")
        else:
            year = random.randint(1950, 1980)
            month = random.randint(1, 12)
            day = self.get_random_day(month, year)
            return datetime(year, month, day).strftime("%Y-%m-%d")
        
    def calculate_age(self, birthdate, on_date):
        # Calculate the difference between the two dates
        difference = on_date - birthdate

        # Calculate age logic remains the same
        age = difference.days // 365
        if (on_date.month, on_date.day) < (birthdate.month, birthdate.day):
            age -= 1
        
        if age < 18:
            self.social_identifier.append("Young")

        return age

    @staticmethod
    def get_random_day(month, year):
        # February
        if month == 2:
            if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
                # Leap year
                return random.randint(1, 29)
            else:
                return random.randint(1, 28)
        # April, June, September, November
        elif month in [4, 6, 9, 11]:
            return random.randint(1, 30)
        # January, March, May, July, August, October, December
        else:
            return random.randint(1, 31)
    
    def generate_birth_weight(self):
        weight_kg = random.uniform(2.5, 4.5)
        return round(weight_kg, 2)  

    def generate_birth_length(self):
        length_cm = random.uniform(48, 53)
        return round(length_cm, 1)

    def generate_height(self, gender):
        if gender.lower() == 'male':
            height_cm = random.uniform(165, 190)

        elif gender.lower() == 'female':
            height_cm = random.uniform(150, 175)

        return round(height_cm, 1)  # Rounded to 1 decimal place for realism

    def generate_weight(self, gender):
        if gender.lower() == 'male':
            weight_kg = random.uniform(70, 90)
        elif gender.lower() == 'female':
            weight_kg = random.uniform(50, 70)

        return round(weight_kg, 1)  # Rounded to 1 decimal place for realism

    def generate_eye_color(self):
        eye_colors = ["Brown", "Blue", "Green", "Hazel", "Gray", "Amber"]
        return random.choice(eye_colors)

    def generate_hair_color(self):
        hair_colors = ["Black", "Brown", "Blonde", "Red", "Gray", "White"]
        return random.choice(hair_colors)

    def generate_blood_type(self):
        blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        return random.choice(blood_types)
    
    # Function to generate a random address
    def generate_address(self):
        local_types = self.load_json(r'final_year_project\config\address_entity\local_type.json')
        name1 = self.load_json(r"final_year_project\config\address_entity\name1.json")
        name2 = self.load_json(r'final_year_project\config\address_entity\name2.json')
        populated_places = self.load_json(r'final_year_project\config\address_entity\populated_place.json')
        postcode_districts = self.load_json(r'final_year_project\config\address_entity\postcode_district.json')
        regions = self.load_json(r'final_year_project\config\address_entity\region.json')
        types = self.load_json(r'final_year_project\config\address_entity\type.json')
        countries = self.load_json(r'final_year_project\config\address_entity\country.json')
        counties = self.load_json(r'final_year_project\config\address_entity\county_unitary.json')
        districts = self.load_json(r'final_year_project\config\address_entity\district_borough.json')

        house_number = str(random.randint(1, 100))
        street_name = random.choice(name2)
        city = random.choice(populated_places)
        region = random.choice(regions)
        postal_code = random.choice(postcode_districts)
        country = random.choice(countries)
        main_category = random.choice(list(types.keys()))
        sub_categories = random.choice(list(types[main_category]))

        if region in country:
            country == region

        return house_number,street_name,city,region,postal_code,country,main_category,sub_categories

    def generate_phone(self):
        prefix = '07'
        number = ''.join(random.choice('0123456789') for _ in range(9))
        phone_number = prefix + number
        
        return phone_number
    
    def generate_email(self):
        domains = random.choice("abcdefghijklmnopqrstuvwxyz")
        letters = string.ascii_lowercase
        length = int(random.choice("0123456789"))
        first_name = self.first_name
        last_name = self.last_name
        number = random.randint(1, 99)
        domain = random.choice(domains)
        random_string = ''.join(random.choice(letters) for i in range(length))
        
        email_pattern = random.choice([
            f"{first_name}.{last_name}{number}@{domain}mail.com",
            f"{first_name}{last_name}.{number}@{domain}mail.com",
            f"{first_name}.{last_name}.{random_string}@{domain}mail.com"
        ])
        
        return email_pattern
    
    def generate_occupation(self, age, industry_list):
        occupations = ["Retired", "Self-Employed", "State Employees", "Farmers", "Academic", "Blue-Collar Worker", "White-Collar Worker", "Grey-Collar Worker","Unemployed", "Student"]
        
        employed_list = ["Self-Employed", "Blue-Collar Worker", "White-Collar Worker","Grey-Collar Worker"]


        if age <= 6:
            return None,""
        elif 7 <= age <= 18:
            prob_student = min(max(-(0.46 * age - 3) ** 2 + 99, 0), 100) / 100
        elif 19 <= age <= 23:
            # Adjusted formula for ages 18-23 to decrease student probability
            prob_student = min(max(-(0.1 * age - 1.9) ** 2 + 80, 0), 100) / 100
        else:
            # Adjusted formula for ages >23 to further decrease student probability
            prob_student = max(1 / (0.1 * (age - 23) ** 2 + 2), 0)
        
        prob_unemployed = 0.01  # Constant probability for being unemployed
        
        # Calculate the remaining probability for other occupations
        prob_other = max(1 - prob_student - prob_unemployed, 0)
        prob_per_other_occupation = prob_other / (len(occupations) - 3)
        
        # Creating a weighted list for occupation selection
        weights = [prob_per_other_occupation if occupation not in ["Unemployed", "Student", None] else prob_unemployed if occupation == "Unemployed" else prob_student for occupation in occupations]
        
        chosen_occupation = random.choices(occupations, weights=weights, k=1)[0]

        if chosen_occupation in employed_list:
            return chosen_occupation, random.choice(industry_list)
        else:
            return chosen_occupation, ""

    def generate_education_level(self, age):
        education_levels = [
            "None",
            "Primary Education",
            "Secondary Education",
            "High School Diploma",
            "Vocational Training",
            "Associate Degree",
            "Bachelor's Degree",
            "Master's Degree",
            "Doctorate / Professional Degree"
        ]
        
        # Define probabilities based on age
        if age < 6:
            return None
        
        if 6 <= age <= 12:
            probabilities = [
                0,    # None
                1,    # Primary Education
                0,    # Secondary Education
                0,    # High School Diploma
                0,    # Vocational Training
                0,    # Associate Degree
                0,    # Bachelor's Degree
                0,    # Master's Degree
                0     # Doctorate or Professional Degree
            ]
        elif 13 <= age <= 15:
            probabilities = [
                0,    # None
                0,    # Primary Education
                1,    # Secondary Education
                0,    # High School Diploma
                0,    # Vocational Training
                0,    # Associate Degree
                0,    # Bachelor's Degree
                0,    # Master's Degree
                0     # Doctorate or Professional Degree
            ]
        elif 16 <= age <= 18:
            probabilities = [
                0,    # None
                0,    # Primary Education
                0,    # Secondary Education
                1,    # High School Diploma
                0,    # Vocational Training
                0,    # Associate Degree
                0,    # Bachelor's Degree
                0,    # Master's Degree
                0     # Doctorate or Professional Degree
            ]
        else:  # age 19+
            probabilities = [
                0,    # None
                0,    # Primary Education
                0,    # Secondary Education
                0,    # High School Diploma
                0.25, # Vocational Training
                0.25, # Associate Degree
                0.25, # Bachelor's Degree
                0.15, # Master's Degree
                0.10  # Doctorate or Professional Degree
            ]
        
        # Use numpy's choice method to select an education level based on the defined probabilities
        education_level = np.random.choice(education_levels, p=probabilities)
        return education_level

    def generate_work_experience(self, age,current_occupation):
        occupations = ["Self-Employed", "State Employees", "Farmers", "Academic", "Blue-Collar Worker", "White-Collar Worker", "Unemployed", "Student"]
        if age < 14:
            return None

        max_experience_years = age - 14
        # 直接为当前职业保留一年经验
        experience_distribution = {current_occupation: 1}
        remaining_years = max_experience_years - 1

        # 如果当前职业不在预定义职业列表中，添加它
        if current_occupation not in occupations:
            occupations.append(current_occupation)

        num_occupations = random.randint(1, len(occupations)) - 1  # 减去已分配给当前职业的1年
        selected_occupations = random.sample([occ for occ in occupations if occ != current_occupation], num_occupations)

        for i, occupation in enumerate(selected_occupations):
            if i == len(selected_occupations) - 1:
                # 为最后一个职业分配剩余的所有年份
                experience_distribution[occupation] = remaining_years
            else:
                # 保证有足够的年份可以分配给剩余的职业
                if remaining_years > len(selected_occupations) - i:
                    years = random.randint(1, remaining_years - (len(selected_occupations) - i - 1))
                else:
                    years = 1  # 如果剩余年份不足，为每个职业分配1年
                experience_distribution[occupation] = years
                remaining_years -= years

        return experience_distribution

    def generate_income(self,work_experience,education_level,occupation, industry_list, industry):
        industry_dict = {}

        #Create random industral weight
        for i in industry_list:
            ran = random.randint(1,500)/100
            p_n = random.randint(0,1)
            if p_n == 0:
                ran = ran
            else:
                ran = -ran

            industry_dict[i] = ran

        education_levels = {
            "None": 0,
            "Primary Education": 1,
            "Secondary Education": 2,
            "High School Diploma": 3,
            "Vocational Training": 4,
            "Associate Degree": 5,
            "Bachelor's Degree": 6,
            "Master's Degree": 7,
            "Doctorate / Professional Degree": 8
        }
        occupation_base_income = {
            "Self-Employed": 30000,
            "State Employees": 25000,
            "Farmers": 15000,
            "Academic": 35000,
            "Blue-Collar Worker": 20000,
            "White-Collar Worker": 40000,
            "Grey-Collar Worker": 50000,
            "Unemployed": 0,
            "Student": 5000,
            "Retired":0,
            None:0,
        }
        occupation_education_limit = {
            "Farmers": "High School Diploma",
            "Self-Employed": "Bachelor's Degree",
            "State Employees": "Master's Degree",
            "Academic": "Doctorate / Professional Degree",
            "Blue-Collar Worker": "Vocational Training",
            "Grey-Collar Worker": "Vocational Training",
            "White-Collar Worker": "Master's Degree",
            "Unemployed": "None",
            "Student": "None",
        }

        if occupation in ["Unemployed", "Student", "Retired", None]:
            return occupation_base_income[occupation]

        # 计算工作经验对收入的影响，这里简单假设每年增加一个随机数%
        if work_experience == None:
            experience_bonus = 0
        else:
            experience_bonus = sum(work_experience.values()) * (random.randint(1,5)/100)
        
        # 计算教育水平的基础值，如果超过某职业的教育上限，则使用上限的教育水平
        education_value = education_levels[education_level]
        education_limit = education_levels[occupation_education_limit[occupation]]
        if education_value > education_limit:
            education_value = education_limit
        
        # 简化的假设：每提升一个教育水平，基础收入增加5%
        education_bonus = education_value * 0.05

        # 计算最终收入
        base_income = occupation_base_income[occupation]
        if industry == "":
            industry_corr = 1
        else:
            industry_corr =  + industry_dict[industry]

        final_income = base_income * (1 + experience_bonus + education_bonus)

        return final_income

    def generate_medical_history(self, age):
        # Adjusting likelihood for number of diseases
        weights = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]  # Higher weight for lower numbers
        num_of_disease = random.choices(range(0, 10), weights=weights, k=1)[0]

        data = self.load_json(r"final_year_project\config\diseases.json")
        diseases = []

        # Age-based disease categorization (simplified example)
        if age <= 6 or age >= 60:
            age_group = 'extremes'
        else:
            age_group = 'middle'

        # Flatten and categorize diseases based on age group
        all_diseases = []
        for category, diseases_list in data.items():
            for disease in diseases_list:
                # Here, you can define how to categorize diseases based on age. This is a placeholder.
                if age_group == 'extremes':
                    all_diseases.append(disease.capitalize())  # Assuming all diseases are relevant for demonstration
                else:
                    # Adjust this logic based on the actual relevance of diseases to age groups
                    all_diseases.append(disease.capitalize())

        for i in range(num_of_disease):
            disease = random.choice(all_diseases)
            if disease not in diseases:  # To avoid repeating the same disease
                diseases.append(disease.capitalize())
        
        return diseases

    def generate_allergies(self):
        data = self.load_json(r"final_year_project\config\allergies.json")

        num_of_allergies = random.randint(0,3)
        allergies = []
        for i in range(num_of_allergies):
            if i not in allergies:
                allergies.append(random.choice(data))

        return allergies
    
    def generate_medications(self):
        data = self.load_json(r"final_year_project\config\medicines.json")

        num_of_medications = random.randint(0,3)
        medications = []
        for i in range(num_of_medications):
            medications.append(random.choice(data))

        return medications
    
    def generate_immunizations(self):
        data = self.load_json(r"final_year_project\config\immunisation.json")

        num_of_immunizations = random.randint(0,3)
        immunizations = []
        for i in range(num_of_immunizations):
            immunizations.append(random.choice(data))

        return immunizations

    def generate_religion(self):
        if random.randint(0,1) == 0:
            return None #no religion
        else:
            self.social_identifier.append("Religious")
            data = self.load_json(r"final_year_project\config\religions.json")
            # Convert the dictionary into a list of tuples for easier processing
            religions = list(data.items())
            # Generate a random number between 0 and 1
            rand_num = random.random()
            # Accumulate probabilities until the random number is less than the accumulated probability
            acc_prob = 0
            for religion, prob in religions:
                acc_prob += prob
                if rand_num < acc_prob:
                    return religion
            # In case the probabilities do not sum to 1 due to rounding,
            # return the last religion
            return religions[-1][0]

    def generate_ethnicity(self):
        data = self.load_json(r"final_year_project\config\ethnicity.json")

        for item in data:
            item["%"] = float(item["%"]) / 100
        
        rand_num = random.random()
        acc_prob = 0
        for item in data:
            acc_prob += item["%"]
            if rand_num < acc_prob:
                return item["Ethnicity"]
        # In case the probabilities do not sum to 1 due to rounding,
        # return the last ethnicity
        
        if data[-1]["%"] < 50:
            self.social_identifier.append("Ethnic Minorities")

        return data[-1]["Ethnicity"]

    def generate_languages(self):
        data = self.load_json(r"final_year_project\config\language.json")
        rand_prob = random.uniform(0, sum(data.values()))
        current = 0
        
        # Iterate through the languages and their probabilities
        for language, prob in data.items():
            current += prob
            # Check if the random number falls within the current range
            if rand_prob <= current:
                return language

    def generate_criminal_record(self):
        return None

    def generate_marital_status(self):
        stage = ["Single", "Married", "Divorced", "Widowed",  "Separated"]
        if self.age < 16:
            return "Single"
        else:
            return random.choice(stage)
    
    def generate_parental_status(self):
        # Decide if the object is a parent, let's say there's a 50% chance
        if self.age > 18:
            is_parent = random.choice([True, False])
            
            if is_parent:
                # If a parent, randomly decide the number of kids, e.g., between 1 and 4
                num_kids = random.randint(1, 4)
                self.social_identifier.append("Parents")
                self.generate_children(num_kids)
                return "Parent", num_kids
            else:
                # If not a parent, return 0 for the number of kids
                return "Not a Parent", 0
        else:
            return "Not a Parent", 0
    
    def generate_children(self,num_kids):
        #Parent information
        for _ in range(num_kids):
            child = PersonalIdentifiers(is_child=True, parent_last_name=self.last_name, parent_age = self.age, parent_address=self.address, parent_nationality = self.nationality, parent_language = self.languages)  # Modify this call based on child-specific logic

            # Set child-specific attributes here
            self.children_list.append(child.id)

            pop_list = ["parent_last_name","parent_age","parent_address","parent_nationality","parent_language","industry_list"]

            for i in pop_list:
                del child.__dict__[i]

            child_data_json = json.dumps(child.__dict__, indent=4)

            with open(f"final_year_project\people\{child.id}.json", "w") as file:
                file.write(child_data_json)

            print(f"Child Data saved to {child.id}.json")

    def generate_political_identifier(self, age):
        if age >= 14:
            international_service_axis = [
                "Isolationism",
                "Nationalism",
                "Centrism",
                "Liberalism",
                "Internationalism"
                ]

            gender_axis = [
                "Male Supremacy Advocates",
                "Traditional Law and Order advocates",
                "Centrism",
                "Feminism"
            ]
            
            economic_axis = [
                "Communism",
                "Socialism",
                "Democratic Socialism",
                "Social Democracy",
                "Progressive",
                "Liberalism",
                "Fiscal Conservatism",
                "Conservatism",
                "Conservatism",
                "Libertarian Capitalism",
                "Laissez-faire Capitalism"
            ]

            political_authority_axis = [
                "Totalitarianism",
                "Religious Fundamentalism",
                "Nationalism",
                "Conservatism",
                "Liberalism",
                "Progressivism",
                "Libertarianism",
                "Anarchism"
            ]

            environmental_engagement_axis = [
                "Environmentalism",
                "Technological Optimism", #Sustainable Agriculture Advocates
                "Industrialism"
            ]

            altruism_egoism_axis = [
                "Altruism",
                "Collectivism",
                "Centrism",
                "Individualism",
                "Egoism"
            ]

            globalization_protectionism_axis = [
                "Globalization supporters",
                "Free Trade Advocates",
                "Liberalism",
                "Protectionism",
                "Economic Nationalism"
            ]

            modernity_tradition_axis = [
                "Postmodernism",
                "Modernism", #Urban Progressivism
                "Scientific Progressivism",#Secularism
                "Cultural Traditionalism",
                "Traditionalism"#Religious Fundamentalism
            ]

            axials = [
                international_service_axis,
                gender_axis,
                economic_axis,
                political_authority_axis,
                environmental_engagement_axis,
                altruism_egoism_axis,
                globalization_protectionism_axis,
                modernity_tradition_axis
            ]

            political_identifier = {
                "international_service_axis" :[],
                "gender_axis":[],
                "economic_axis":[],
                "political_authority_axis":[],
                "environmental_engagement_axis":[],
                "altruism_egoism_axis":[],
                "globalization_protectionism_axis":[],
                "modernity_tradition_axis":[],
                "advocacy":[],
                "political_sensitivity":0
            }

            axis_names = [
                "international_service_axis",
                "gender_axis",
                "economic_axis",
                "political_authority_axis",
                "environmental_engagement_axis",
                "altruism_egoism_axis",
                "globalization_protectionism_axis",
                "modernity_tradition_axis",
            ]
            political_identifier_dict = {}

            #Generate all political standpoint
            for axis_name, axis_list in zip(axis_names, axials):
                choice = random.choice(axis_list)  
                score = random.randint(0, 100)
                political_identifier[axis_name] = [choice, score]
                political_identifier_dict[axis_name] = [choice, score]

            identity_list = []
            for axis_name in axis_names:
                identity_list.append(political_identifier[axis_name])

            #Generate political sensitivity
            political_identifier["political_sensitivity"] = random.choices([i for i in range(1,10)], weights = [1 / number for number in [i for i in range(1,10)]], k = 1)

            #Generate all possible support event
            advocacy = self.load_json(r"final_year_project\config\advocacy.json")

            advocacy_num = random.choices([i for i in range(1,political_identifier["political_sensitivity"][0]+1)], weights = [1 / number for number in range(1,political_identifier["political_sensitivity"][0]+1)], k=1)

            possible_advocacy = []

            individual_standpoints = [v[0] for v in political_identifier_dict.values()]

            matching_advocacies = {}
            for advocacy, required_standpoints in advocacy.items():
                if any(standpoint in individual_standpoints for standpoint in required_standpoints):
                    matching_advocacies[advocacy] = required_standpoints
                    possible_advocacy.append(advocacy)

            advocacies = []
            for i in range(advocacy_num[0]):
                if len(possible_advocacy) > 0:
                    advocacy = random.choice(possible_advocacy)
                    possible_advocacy.pop(possible_advocacy.index(advocacy))
                    advocacies.append(advocacy)

            political_identifier["advocacy"] = advocacies

            return political_identifier
        else:
            return 
    
    def generate_economic_status(self,income):
        # Assuming these are your thresholds for simplicity
        wealthy_threshold = 125140
        middle_class_threshold = 12570

        # Determine socioeconomic status based on income
        if income >= wealthy_threshold:
            status = "Wealthy"
        elif income >= middle_class_threshold:
            status = "Middle Class"
        else:
            status = "Poor"

        return status

    def generate_car_properties(self,economic_status):
        if economic_status == 'Poor':
            # Assuming poor individuals have a 50% chance to own a car, and if they do, it's of low value.
            num_cars = 0 if random.random() > 0.5 else 1
            total_value = 5000 if num_cars > 0 else 0  # Assuming a low-value car
        elif economic_status == 'Middle Class':
            # Assuming middle-class individuals likely own 1 or 2 cars, of moderate value.
            num_cars = random.randint(1, 2)
            total_value = num_cars * random.randint(10000, 20000)  # Assuming moderate-value cars
        elif economic_status == 'Wealthy':
            # Assuming higher-class individuals own 2 or more cars, with high total value.
            num_cars = random.randint(2, 4)
            total_value = num_cars * random.randint(30000, 50000)  # Assuming high-value cars

        return num_cars, total_value

    def generate_house_properties(self, economic_status):
        # Initialize default properties
        house_properties = {'number_of_houses': 0, 'value_of_house': 0}
        
        # Define economic status properties
        if economic_status == 'Poor':
            # Poor are less likely to own a house
            house_properties['number_of_houses'] = random.choices([0, 1], weights=[9, 1], k=1)[0]
            house_properties['value_of_house'] = 0 if house_properties['number_of_houses'] == 0 else random.randint(5000, 50000)
        
        elif economic_status == 'Middle Class':
            # Middle class has a higher chance of owning a house
            house_properties['number_of_houses'] = random.choices([0, 1], weights=[3, 7], k=1)[0]
            house_properties['value_of_house'] = 0 if house_properties['number_of_houses'] == 0 else random.randint(50000, 300000)
        
        elif economic_status == 'Wealthy':
            # Wealthy are more likely to own one or more houses
            house_properties['number_of_houses'] = random.choices([1, 2], weights=[7, 3], k=1)[0]
            house_properties['value_of_house'] = random.randint(300000, 2000000) if house_properties['number_of_houses'] >= 1 else 0

        return house_properties['number_of_houses'], house_properties['value_of_house']

    def generate_living_status(self, economic_status, car_num):
        # Define possible living statuses
        living_statuses = {
            'Poor': ["Renting", "Homeless", "Squatting", "Government-Subsidized Housing", "Sharing with others"],
            'Middle Class': ["Renting", "Homeownership", "Sharing with others"],
            'Wealthy': ["Homeownership"]
        }
        
        # Adjust available options based on car ownership for mobile living
        if car_num > 0:
            living_statuses['Poor'].append("Mobile Living")
            living_statuses['Middle Class'].append("Mobile Living")
            # Assuming higher class can also choose Mobile Living if they wish to
            living_statuses['Wealthy'].append("Mobile Living")

        possible_statuses = living_statuses[economic_status]
        
        return random.choice(possible_statuses)

    def generate_commute_identifier(self, car_num):
        # Individuals with no cars can only be Commuters.
        if car_num == 0:
            return "Commuter"
        else:
            return random.choice(["Commuter", "Motorist"])
        
    def is_patriot(self):
        if random.randint(0, 1) == 0:
            self.social_identifier.append("Patriot")
    
 
class Environment:
    def __init__(self):
        date_int = 20000101

        # Convert integer to string and then to datetime
        date_str = str(date_int)
        self.date = datetime.strptime(date_str, "%Y%m%d")

    def get_date(self):
        date_int = 20000101
        date_str = str(date_int)
        return datetime.strptime(date_str, "%Y%m%d")

def generation(number_of_people):
    for i in range(int(number_of_people)):
        people_path = r"final_year_project\people"
        items = os.listdir(people_path)
        file_num = sum(1 for item in items if os.path.isfile(os.path.join(people_path, item)))

        person = PersonalIdentifiers()

        #for debug
        for key, value in person.__dict__.items():
            try:
                json.dumps(value)
            except TypeError as e:
                print(f"Error serializing {key}: {e}")

        pop_list = ["parent_last_name","parent_age","parent_address","parent_nationality","parent_language","industry_list"]

        for i in pop_list:
            del person.__dict__[i]

        # Convert to JSON and save to file
        person_data_json = json.dumps(person.__dict__, indent=4)
        with open(people_path + f"\{person.id}.json", "w") as file:
            file.write(person_data_json)

        print(f"Data saved to {person.id}.json")

        
        items = os.listdir(people_path)
        print(file_num)

        if file_num >= number_of_people:
            break


