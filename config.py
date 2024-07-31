import os
from data_extraction import *
from people_generation import *

def search_pop_poli_attr(pop_data, attribute):
    counter = 0
    
    for i in pop_data:
        for e in pop_data[i]:
            if attribute in e[0]:
                counter += e[1]
            
    return counter

def search_pop_attr(pop_data, attribute):
    return pop_data[attribute]

# Country properties inital
currency = "£"
population = 66970000
name  = "uk"
default = 1

people_path = r"final_year_project\people"
items = os.listdir(people_path)

file_count = sum(1 for item in items if os.path.isfile(os.path.join(people_path, item)))
if round((population/10000),2) < file_count:
    ungerrated_population = round((population/10000),2) - file_count
    generation(ungerrated_population)

file_count = sum(1 for item in items if os.path.isfile(os.path.join(people_path, item)))
population_total = file_count

# Voters Group
Capitalism = search_pop_poli_attr(political_counts,"Capitalism")
Capitalism_perc = round(Capitalism/population_total,2)

Liberalism = search_pop_poli_attr(political_counts,"Liberalism")
Liberalism_perc = round(Liberalism/population_total,2)

Religious_Fundamentalism = search_pop_poli_attr(political_counts,"Religious Fundamentalism")
Religious_Fundamentalism_perc = round(Religious_Fundamentalism/population_total,2)

Environmentalism = search_pop_poli_attr(political_counts,"Environmentalism")
Environmentalism_perc = round(Environmentalism/population_total,2)

Socialism = search_pop_poli_attr(political_counts,"Socialism")
Socialism_freq = round(Socialism/population_total,2)

Farmers = search_pop_attr(occupations_identifier_counts,"Farmers")
Farmers_freq = round(Farmers/population_total,2)

Patriot = search_pop_attr(social_identifier_counts,"Patriot")
Patriot_freq = round(Patriot/population_total,2)
Poor_perc = Patriot_freq

Poor = search_pop_attr(economic_identifier_counts,"Poor")
Poor_freq = round(Poor/population_total,2)

Young = search_pop_attr(social_identifier_counts,"Young")
Young_freq = round(Young/population_total,2)

Parents = search_pop_attr(social_identifier_counts,"Parents")
Parents_freq = round(Parents/population_total,2)

SelfEmployed = search_pop_attr(occupations_identifier_counts,"Self-Employed")
SelfEmployed_freq = round(SelfEmployed/population_total,2)

Retired = search_pop_attr(occupation_counts,"Retired")
Retired_freq = round(Retired/population_total,2)

Motorist = search_pop_attr(commute_identifier_counts,"Motorist")
Motorist_freq = round(Motorist/population_total,2)

Commuter =  search_pop_attr(commute_identifier_counts,"Commuter")
Commuter_freq = round(Commuter/population_total,2)

Retired = search_pop_attr(occupation_counts,"Retired")
Retired_perc = Retired_freq = round(Retired/file_count,2)

Anarchism = search_pop_poli_attr(political_counts,"Anarchism")
Anarchism_perc = Retired_freq = round(Anarchism/file_count,2)

Postmodernism = search_pop_poli_attr(political_counts,"Postmodernism")
Postmodernism_freq = round(Postmodernism/population_total,2)

Modernism = search_pop_poli_attr(political_counts,"Modernism")
Modernism_freq = round(Modernism/population_total,2)

ScientificProgressivism = search_pop_poli_attr(political_counts,"ScientificProgressivism")
ScientificProgressivism_freq = round(ScientificProgressivism/population_total,2)

CulturalTraditionalism = search_pop_poli_attr(political_counts,"CulturalTraditionalism")
CulturalTraditionalism_freq = round(CulturalTraditionalism/population_total,2)

Traditionalism = search_pop_poli_attr(political_counts,"Traditionalism")
Traditionalism_freq = round(Traditionalism/population_total,2)

FreeTradeAdvocates = search_pop_poli_attr(political_counts,"FreeTradeAdvocates")
FreeTradeAdvocates_freq = round(FreeTradeAdvocates/population_total,2)

Liberalism = search_pop_poli_attr(political_counts,"Liberalism")
Liberalism_freq = round(Liberalism/population_total,2)

Protectionism = search_pop_poli_attr(political_counts,"Protectionism")
Protectionism_freq = round(Protectionism/population_total,2)

EconomicNationalism = search_pop_poli_attr(political_counts,"EconomicNationalism")
EconomicNationalism_freq = round(EconomicNationalism/population_total,2)

Altruism = search_pop_poli_attr(political_counts,"Altruism")
Altruism_freq = round(Altruism/population_total,2)

Collectivism = search_pop_poli_attr(political_counts,"Collectivism")
Collectivism_freq = round(Collectivism/population_total,2)

Centrism = search_pop_poli_attr(political_counts,"Centrism")
Centrism_freq = round(Centrism/population_total,2)

Individualism = search_pop_poli_attr(political_counts,"Individualism")
Individualism_freq = round(Individualism/population_total,2)

Egoism = search_pop_poli_attr(political_counts,"Egoism")
Egoism_freq = round(Egoism/population_total,2)

Environmentalism = search_pop_poli_attr(political_counts,"Environmentalism")
Environmentalism_freq = round(Environmentalism/population_total,2)

TechnologicalOptimism = search_pop_poli_attr(political_counts,"TechnologicalOptimism")
TechnologicalOptimism_freq = round(TechnologicalOptimism/population_total,2)

Industrialism = search_pop_poli_attr(political_counts,"Industrialism")
Industrialism_freq = round(Industrialism/population_total,2)

Totalitarianism = search_pop_poli_attr(political_counts,"Totalitarianism")
Totalitarianism_freq = round(Totalitarianism/population_total,2)

ReligiousFundamentalism = search_pop_poli_attr(political_counts,"ReligiousFundamentalism")
ReligiousFundamentalism_freq = round(ReligiousFundamentalism/population_total,2)

Nationalism = search_pop_poli_attr(political_counts,"Nationalism")
Nationalism_freq = round(Nationalism/population_total,2)

Conservatism = search_pop_poli_attr(political_counts,"Conservatism")
Conservatism_freq = round(Conservatism/population_total,2)

Liberalism = search_pop_poli_attr(political_counts,"Liberalism")
Liberalism_freq = round(Liberalism/population_total,2)

Progressivism = search_pop_poli_attr(political_counts,"Progressivism")
Progressivism_freq = round(Progressivism/population_total,2)

Libertarianism = search_pop_poli_attr(political_counts,"Libertarianism")
Libertarianism_freq = round(Libertarianism/population_total,2)

Anarchism = search_pop_poli_attr(political_counts,"Anarchism")
Anarchism_freq = round(Anarchism/population_total,2)

Communism = search_pop_poli_attr(political_counts,"Communism")
Communism_freq = round(Communism/population_total,2)

Socialism = search_pop_poli_attr(political_counts,"Socialism")
Socialism_freq = round(Socialism/population_total,2)

DemocraticSocialism = search_pop_poli_attr(political_counts,"DemocraticSocialism")
DemocraticSocialism_freq = round(DemocraticSocialism/population_total,2)

SocialDemocracy = search_pop_poli_attr(political_counts,"SocialDemocracy")
SocialDemocracy_freq = round(SocialDemocracy/population_total,2)

Progressive = search_pop_poli_attr(political_counts,"Progressive")
Progressive_freq = round(Progressive/population_total,2)

Liberalism = search_pop_poli_attr(political_counts,"Liberalism")
Liberalism_freq = round(Liberalism/population_total,2)

FiscalConservatism = search_pop_poli_attr(political_counts,"FiscalConservatism")
FiscalConservatism_freq = round(FiscalConservatism/population_total,2)

Conservatism = search_pop_poli_attr(political_counts,"Conservatism")
Conservatism_freq = round(Conservatism/population_total,2)

Conservatism = search_pop_poli_attr(political_counts,"Conservatism")
Conservatism_freq = round(Conservatism/population_total,2)

LibertarianCapitalism = search_pop_poli_attr(political_counts,"LibertarianCapitalism")
LibertarianCapitalism_freq = round(LibertarianCapitalism/population_total,2)

Laissez_faireCapitalism = search_pop_poli_attr(political_counts,"Laissez_faireCapitalism")
Laissez_faireCapitalism_freq = round(Laissez_faireCapitalism/population_total,2)

MaleSupremacyAdvocates = search_pop_poli_attr(political_counts,"MaleSupremacyAdvocates")
MaleSupremacyAdvocates_freq = round(MaleSupremacyAdvocates/population_total,2)

TraditionalLawandOrderadvocates = search_pop_poli_attr(political_counts,"TraditionalLawandOrderadvocates")
TraditionalLawandOrderadvocates_freq = round(TraditionalLawandOrderadvocates/population_total,2)

Centrism = search_pop_poli_attr(political_counts,"Centrism")
Centrism_freq = round(Centrism/population_total,2)

Feminism = search_pop_poli_attr(political_counts,"Feminism")
Feminism_freq = round(Feminism/population_total,2)

Isolationism = search_pop_poli_attr(political_counts,"Isolationism")
Isolationism_freq = round(Isolationism/population_total,2)

Nationalism = search_pop_poli_attr(political_counts,"Nationalism")
Nationalism_freq = round(Nationalism/population_total,2)

Centrism = search_pop_poli_attr(political_counts,"Centrism")
Centrism_freq = round(Centrism/population_total,2)

Liberalism = search_pop_poli_attr(political_counts,"Liberalism")
Liberalism_freq = round(Liberalism/population_total,2)

Internationalism = search_pop_poli_attr(political_counts,"Internationalism")
Internationalism_freq = round(Internationalism/population_total,2)




