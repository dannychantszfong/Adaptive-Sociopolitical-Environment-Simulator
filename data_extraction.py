import os
import json
from collections import defaultdict, OrderedDict

def count_social_identifier(directory):
    """
    Counts occurrences of each unique value in the 'social_identifier' property
    across all JSON files in the specified directory.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    dict: A dictionary with each unique social identifier as keys and their counts as values.
    """
    social_identifier_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                social_identifiers = data.get('social_identifier', [])
                
                # Process each social identifier
                for identifier in social_identifiers:
                    if identifier in social_identifier_counts:
                        social_identifier_counts[identifier] += 1
                    else:
                        social_identifier_counts[identifier] = 1

    return social_identifier_counts

def count_gender(directory):
    """
    Counts occurrences of each unique value in the 'gender' property
    across all JSON files in the specified directory.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    dict: A dictionary with each unique gender as keys and their counts as values.
    """
    gender_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                gender = data.get('gender', None)
                
                # Process gender
                if gender:
                    if gender in gender_counts:
                        gender_counts[gender] += 1
                    else:
                        gender_counts[gender] = 1

    return gender_counts

def count_age(directory):
    """
    Counts occurrences of each unique age in the 'age' property
    across all JSON files in the specified directory, returning them in sorted order.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    OrderedDict: A dictionary with each unique age as keys and their counts as values, sorted by age.
    """
    age_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                age = data.get('age', None)
                
                # Process age
                if age is not None:
                    if age in age_counts:
                        age_counts[age] += 1
                    else:
                        age_counts[age] = 1

    # Sort the dictionary by age keys
    sorted_age_counts = OrderedDict(sorted(age_counts.items()))

    return sorted_age_counts


def count_education_level(directory):
    """
    Counts occurrences of each unique value in the 'education_level' property
    across all JSON files in the specified directory, specifically for predefined
    education levels.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    dict: A dictionary with each unique education level as keys and their counts as values.
    """
    # Predefined list of education levels
    education_levels = [
        "Primary Education", "Secondary Education", "High School Diploma",
        "Vocational Training", "Associate Degree", "Bachelor's Degree",
        "Master's Degree", "Doctorate or Professional Degree"
    ]
    
    # Initialize the dictionary with predefined education levels set to zero
    education_level_counts = {level: 0 for level in education_levels}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                education_level = data.get('education_level', None)
                
                # Process education level if it is in the predefined list
                if education_level in education_level_counts:
                    education_level_counts[education_level] += 1

    return education_level_counts


def count_occupation(directory):
    """
    Counts occurrences of each unique value in the 'occupation' property
    across all JSON files in the specified directory.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    dict: A dictionary with each unique occupation as keys and their counts as values.
    """
    occupation_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                occupation = data.get('occupation', None)
                
                # Process occupation
                if occupation:
                    if occupation in occupation_counts:
                        occupation_counts[occupation] += 1
                    else:
                        occupation_counts[occupation] = 1

    return occupation_counts


def count_industry(directory):
    """
    Counts occurrences of each unique value in the 'industry' property
    across all JSON files in the specified directory.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    dict: A dictionary with each unique industry as keys and their counts as values.
    """
    industry_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                industry = data.get('industry', None)
                
                # Process industry
                if industry:
                    if industry in industry_counts:
                        industry_counts[industry] += 1
                    else:
                        industry_counts[industry] = 1

    return industry_counts


def count_industry(directory):
    """
    Counts occurrences of each unique value in the 'industry' property
    across all JSON files in the specified directory, returning them in alphabetical order.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    OrderedDict: A dictionary with each unique industry as keys and their counts as values, sorted alphabetically.
    """
    industry_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                industry = data.get('industry', None)
                
                # Process industry
                if industry:
                    if industry in industry_counts:
                        industry_counts[industry] += 1
                    else:
                        industry_counts[industry] = 1

    # Sort the dictionary by industry names
    sorted_industry_counts = OrderedDict(sorted(industry_counts.items()))

    return sorted_industry_counts

def count_income(directory):
    """
    Counts occurrences of each unique value in the 'income' property
    across all JSON files in the specified directory, returning them in numerical order.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    OrderedDict: A dictionary with each unique income as keys and their counts as values, sorted numerically.
    """
    income_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                income = data.get('income', None)
                
                # Process income
                if income is not None:
                    if income in income_counts:
                        income_counts[income] += 1
                    else:
                        income_counts[income] = 1

    # Sort the dictionary by income keys numerically
    sorted_income_counts = OrderedDict(sorted(income_counts.items(), key=lambda x: x[0]))

    return sorted_income_counts

def count_marital_status(directory):
    """
    Counts occurrences of each unique value in the 'marital_status' property
    across all JSON files in the specified directory, returning them in alphabetical order.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    OrderedDict: A dictionary with each unique marital status as keys and their counts as values, sorted alphabetically.
    """
    marital_status_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                marital_status = data.get('marital_status', None)
                
                # Process marital status
                if marital_status:
                    if marital_status in marital_status_counts:
                        marital_status_counts[marital_status] += 1
                    else:
                        marital_status_counts[marital_status] = 1

    # Sort the dictionary by marital status keys alphabetically
    sorted_marital_status_counts = OrderedDict(sorted(marital_status_counts.items()))

    return sorted_marital_status_counts

def count_political_identifier(directory):
    """
    Counts occurrences of each unique value in the 'political_identifier' property
    across all JSON files in the specified directory, organized by axis, and sorts results where applicable.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    dict: A nested dictionary with each political axis as keys and another dictionary
          of terms and their counts as values.
    """
    # Initialize a nested dictionary to store counts
    political_counts = defaultdict(lambda: defaultdict(int))

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                political_identifier = data.get('political_identifier', {})

                # Ensure political_identifier is a dictionary before proceeding
                if isinstance(political_identifier, dict):
                    # Iterate through each axis in the political identifier
                    for axis, values in political_identifier.items():
                        if isinstance(values, list):  # List of terms
                            for term in values:
                                if isinstance(term, str):  # Ensure term is string
                                    political_counts[axis][term] += 1
                        elif isinstance(values, dict):  # Key-value pairs
                            for term, count in values.items():
                                if isinstance(term, str) and isinstance(count, int):
                                    political_counts[axis][term] += count  # Aggregate counts

    # Convert defaultdict to regular dict for return and sort where applicable
    final_counts = {}
    for axis, terms in political_counts.items():
        # Sort terms if the axis is 'political_sensitivity' or any other needing sorting
        if axis == 'political_sensitivity':
            sorted_terms = OrderedDict(sorted(terms.items(), key=lambda x: int(x[0])))
        else:
            sorted_terms = sorted(terms.items(), key=lambda x: x[0])
        final_counts[axis] = sorted_terms

    return final_counts


def count_economic_identifier(directory):
    """
    Counts occurrences of each unique value in the 'economic_identifier' property
    across all JSON files in the specified directory, returning them in alphabetical order.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    OrderedDict: A dictionary with each unique economic identifier as keys and their counts as values, sorted alphabetically.
    """
    economic_identifier_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                economic_identifier = data.get('economic_identifier', None)
                
                # Process economic identifier
                if economic_identifier:
                    if economic_identifier in economic_identifier_counts:
                        economic_identifier_counts[economic_identifier] += 1
                    else:
                        economic_identifier_counts[economic_identifier] = 1

    # Sort the dictionary by economic identifier keys alphabetically
    sorted_economic_identifier_counts = OrderedDict(sorted(economic_identifier_counts.items()))

    return sorted_economic_identifier_counts

def count_occupations_identifier(directory):
    """
    Counts occurrences of each unique value in the 'occupations_identifier' property
    across all JSON files in the specified directory, returning them in alphabetical order.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    OrderedDict: A dictionary with each unique occupations identifier as keys and their counts as values, sorted alphabetically.
    """
    occupations_identifier_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                occupations_identifier = data.get('occupations_identifier', None)
                
                # Process occupations identifier
                if occupations_identifier:
                    if occupations_identifier in occupations_identifier_counts:
                        occupations_identifier_counts[occupations_identifier] += 1
                    else:
                        occupations_identifier_counts[occupations_identifier] = 1

    # Sort the dictionary by occupations identifier keys alphabetically
    sorted_occupations_identifier_counts = OrderedDict(sorted(occupations_identifier_counts.items()))

    return sorted_occupations_identifier_counts

def count_living_status(directory):
    """
    Counts occurrences of each unique value in the 'living_status' property
    across all JSON files in the specified directory, returning them in alphabetical order.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    OrderedDict: A dictionary with each unique living status as keys and their counts as values, sorted alphabetically.
    """
    living_status_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                living_status = data.get('living_status', None)
                
                # Process living status
                if living_status:
                    if living_status in living_status_counts:
                        living_status_counts[living_status] += 1
                    else:
                        living_status_counts[living_status] = 1

    # Sort the dictionary by living status keys alphabetically
    sorted_living_status_counts = OrderedDict(sorted(living_status_counts.items()))

    return sorted_living_status_counts

def count_commute_identifier(directory):
    """
    Counts occurrences of each unique value in the 'commute_identifier' property
    across all JSON files in the specified directory, returning them in alphabetical order.

    Args:
    directory (str): Path to the directory containing JSON files.

    Returns:
    OrderedDict: A dictionary with each unique commute identifier as keys and their counts as values, sorted alphabetically.
    """
    commute_identifier_counts = {}

    # Iterate over each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data = json.load(file)
                commute_identifier = data.get('commute_identifier', None)
                
                # Process commute identifier
                if commute_identifier:
                    if commute_identifier in commute_identifier_counts:
                        commute_identifier_counts[commute_identifier] += 1
                    else:
                        commute_identifier_counts[commute_identifier] = 1

    # Sort the dictionary by commute identifier keys alphabetically
    sorted_commute_identifier_counts = OrderedDict(sorted(commute_identifier_counts.items()))

    return sorted_commute_identifier_counts

directory = 'final_year_project\people'

social_identifier_counts = count_social_identifier(directory)
#print(social_identifier_counts)

gender_counts = count_gender(directory)
#print(gender_counts)

age_counts = count_age(directory)
#print(age_counts)

education_counts = count_education_level(directory)
#print(education_counts)

occupation_counts = count_occupation(directory)
#print(occupation_counts)

industry_counts = count_industry(directory)
#print(industry_counts)

industry_counts = count_industry(directory)
#print(industry_counts)

income_counts = count_income(directory)
#print(income_counts)

marital_status_counts = count_marital_status(directory)
#print(marital_status_counts)

political_counts = count_political_identifier(directory)
#print(political_counts)

economic_identifier_counts = count_economic_identifier(directory)
#print(economic_identifier_counts)

occupations_identifier_counts = count_occupations_identifier(directory)
#print(occupations_identifier_counts)

living_status_counts = count_living_status(directory)
#print(living_status_counts)

commute_identifier_counts = count_commute_identifier(directory)
#print(commute_identifier_counts)
