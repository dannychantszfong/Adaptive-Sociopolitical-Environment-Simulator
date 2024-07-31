
def generated_globalco2(_year, _globaleconomy_):
    zone = "NOICON"
    default = 0.01
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(0.01*_year), 2), round(0+(0.08*_globaleconomy_), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__highincome(CarUsage, AirTravel):
    zone = "ECONOMY"
    default = 0.0
    min_value = -1
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.18*CarUsage), 2), round(0+(0.26*AirTravel), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__lowincome(CarUsage, AirTravel, BusUsage):
    zone = "ECONOMY"
    default = 0.0
    min_value = -1
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.06*CarUsage), 2), round(0+(0.06*AirTravel), 2), round(0-(0.05*BusUsage), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__middleincome(CarUsage, AirTravel):
    zone = "ECONOMY"
    default = 0.0
    min_value = -1
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.16*CarUsage), 2), round(0+(0.16*AirTravel), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__terrorism(_year):
    zone = "HIDDEN"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(0.01*_year), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_airtravel(CO2Emissions, OilDemand, Environment, RailUsage, Pollution):
    zone = "TRANSPORT"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0.32*(CO2Emissions**2), 2), round(0+(0.1*OilDemand), 2), round(-0.14*(Environment**3), 2), round(0-(0.04*RailUsage), 2), round(0+(0.09*Pollution), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_alcoholconsumption(GDP, PovertyRate, Unemployment, Health, WorkerProductivity, CrimeRate, ViolentCrimeRate, HealthcareDemand):
    zone = "WELFARE"
    default = 0.3
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(0.1*GDP)**0.5, 2), round(0.2*(PovertyRate**2), 2), round(0.2*(Unemployment**2), 2), round(0-(0.05*Health), 2), round(0-(0.15*WorkerProductivity), 2), round(0.0+(0.09*CrimeRate), 2), round(0.15*(ViolentCrimeRate**1.2), 2), round(0+(0.12*HealthcareDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_averagetemperature(CO2Emissions, GlobalCO2, ImmigrationDemand, ViolentCrimeRate):
    zone = "PUBLICSERVICES"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(0.25*CO2Emissions), 2), round(0+(0.8*GlobalCO2), 2), round(0.09*(ImmigrationDemand**4), 2), round(0.07*(ViolentCrimeRate**4), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_businessconfidence(Stability, _effectivedebt_, GDP):
    zone = "ECONOMY"
    default = 0.375
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.25*Stability), 2), round(-0.22*(_effectivedebt_**2)+0.06, 2), round(-0.09+(0.18*GDP), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_bususage(GDP, CarUsage, RailUsage, OilDemand):
    zone = "TRANSPORT"
    default = 0.15
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0+(0.1*GDP), 2), round(0-(0.35*CarUsage), 2), round(0-(0.22*RailUsage), 2), round(0+(0.13*OilDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_carusage(GDP, Environment, Motorist_freq, CO2Emissions, OilDemand, Obesity, Pollution, ElectricCarTransition):
    zone = "TRANSPORT"
    default = 0.8
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0.55*(GDP**1.59), 2), round(0-(0.22*Environment), 2), round(-0.4+(0.8*Motorist_freq), 2), round(0.5*(1.0-ElectricCarTransition)*CO2Emissions, 2), round(0.3*(1.0-ElectricCarTransition)*OilDemand, 2), round(0+(0.2*Obesity), 2), round(0.28*(1.0-ElectricCarTransition)*Pollution, 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_charity(_HighIncome, _LowIncome, Religious_perc, IncomeTax, LuxuryGoodsTax, Punitivewealthtax, PovertyRate, UniversalBasicIncome, Education, Health, ForeignRelations):
    zone = "WELFARE"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0.62*(_HighIncome**3), 2), round(0.22*(_LowIncome**3), 2), round(0+(0.12*Religious_perc), 2), round(-0.28*(IncomeTax**8), 2), round(-0.12*(LuxuryGoodsTax**8), 2), round(0-(0.25*Punitivewealthtax), 2), round(0-(0.04*PovertyRate), 2), round(-0.02-(0.12*UniversalBasicIncome), 2), round(0+(0.12*Education), 2), round(0+(0.09*Health), 2), round(0+(0.05*ForeignRelations), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_co2emissions(ForeignRelations, Environmentalist):
    zone = "ECONOMY"
    default = 0.1
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0-(0.1*ForeignRelations), 2), round(0.1+(Environmentalist**2)*-0.7, 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_corruption(_security_, GDP, InternationalTrade, OilPrice, Democracy, _All_, _percept_trust, TaxEvasion):
    zone = "LAWANDORDER"
    default = 0.4
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0-(_security_**2)*0.2, 2), round(-0.5*(GDP**4)*GDP, 2), round(-0.5*(InternationalTrade**2)*InternationalTrade, 2), round(0.15*(OilPrice**2), 2), round(0-(Democracy**1.5)*0.5, 2), round(0-(_All_**2)*0.1, 2), round(0.1-(0.2*_percept_trust), 2), round(0.06*(TaxEvasion**2), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_crimerate(_All_, GDP):
    zone = "LAWANDORDER"
    default = 0.7
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0.05-(0.18*_All_), 2), round(0-(0.08*GDP), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_currencystrength(GDP, InternationalTrade, Tourism, FoodPrice, OilPrice):
    zone = "ECONOMY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(22*(GDP**1.24)-0.52, 2), round(0.2+(InternationalTrade**2.9)*-0.66, 2), round(0.12-(Tourism**3)*0.42, 2), round(0.4-(0.8*FoodPrice)**2, 2), round(0.4-(0.8*OilPrice), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_democracy():
    zone = "WELFARE"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [50]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_education(WorkerProductivity, RacialTension, CrimeRate, ViolentCrimeRate):
    zone = "PUBLICSERVICES"
    default = 0.18
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.2+(WorkerProductivity*0.4), 2), round(0-(0.08*RacialTension), 2), round(-0.12*(CrimeRate**6), 2), round(-0.12*(ViolentCrimeRate**4), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_electriccartransition(Technology, Environmentalist_perc, OilPrice, CarEmmissionsLimits, HybridCarsInitiative, PetrolTax, Newcarsubsidies, Banlowmpgcars, CO2Emissions, OilDemand):
    zone = "TRANSPORT"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.4*Technology), 2), round(0+(0.15*Environmentalist_perc), 2), round(0.29*(OilPrice**3), 2), round(0.10+(0.18*CarEmmissionsLimits), 2), round(0.08+(0.07*HybridCarsInitiative), 2), round(0+(0.2*PetrolTax), 2), round(0.1+(0.1*Newcarsubsidies), 2), round(0.07+(0.12*Banlowmpgcars), 2), round(0-(0.17*CO2Emissions), 2), round(0-(0.08*OilDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_emigration(Stability, Unemployment, ForeignRelations, Population):
    zone = "FOREIGNPOLICY"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0.4-(0.4*Stability), 2), round(0.25*(Unemployment**2), 2), round(0+(0.1*ForeignRelations), 2), round(0-(0.10*Population), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_energyefficiency(GDP, CO2Emissions, OilDemand):
    zone = "ECONOMY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.05*GDP), 2), round(0-(0.11*CO2Emissions), 2), round(0-(0.1*OilDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_environment(Environmentalist):
    zone = "PUBLICSERVICES"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.4+(0.8*Environmentalist), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_equality(Socialist, CrimeRate, _global_socialism, ViolentCrimeRate):
    zone = "WELFARE"
    default = 0.4
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.2+(0.4*Socialist), 2), round(0-(CrimeRate*0.22), 2), round(0.1-(_global_socialism*0.2), 2), round(0.2*(1-ViolentCrimeRate)**4, 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_foodprice(AverageTemperature, InternationalTrade, OilPrice, AgricultureSubsidies, FoodStandards, BiofuelSubsidies, _LowIncome_fixed, _MiddleIncome_fixed, Health, Obesity):
    zone = "PUBLICSERVICES"
    default = 0.2
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0.6*(AverageTemperature**2), 2), round(0-(0.48*InternationalTrade), 2), round(0.0+(0.2*OilPrice), 2), round(0.0-(0.25*AgricultureSubsidies), 2), round(0.05+(0.04*FoodStandards), 2), round(0.0+(0.125*BiofuelSubsidies), 2), round(-3000*(_LowIncome_fixed**1.2), 2), round(-4500*(_MiddleIncome_fixed**1.2), 2), round(0.0-(0.07*Health), 2), round(0-(Obesity**2), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_foreignaidreceived(GDP, PovertyRate, HumanDevelopment, Corruption, ForeignRelations, Health, Education, Environment, Socialist, Poor, Farmers, Patriot):
    zone = "FOREIGNPOLICY"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0.6-(GDP**0.3), 2), round(0-(0.2*PovertyRate), 2), round(0.12-(HumanDevelopment*0.24), 2), round(0-(Corruption**2)*0.3, 2), round(-0.3+(0.6*ForeignRelations), 2), round(0+(0.2*Health), 2), round(0+(0.18*Education), 2), round(0+(0.2*Environment), 2), round(0+(0.1*Socialist), 2), round(0+(0.2*Poor), 2), round(0+(0.07*Farmers), 2), round(0-(0.1*Patriot), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_foreigninvestment(Stability, Democracy, WorkerProductivity, WorkingWeek, Wages, ForeignRelations, GDP, Capitalism):
    zone = "FOREIGNPOLICY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.2+(0.4*Stability), 2), round(-0.1+(0.2*Democracy), 2), round(-0.2+(0.4*WorkerProductivity), 2), round(-0.15+(0.3*WorkingWeek), 2), round(0.15-(0.3*Wages), 2), round(-0.2+(ForeignRelations**3)*0.4, 2), round(0.2*(GDP**0.6), 2), round(-0.1+(0.2*Capitalism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_foreignrelations(RacialTension, _Terrorism, Patriot_freq, ImmigrationDemand):
    zone = "FOREIGNPOLICY"
    default = 0.14
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0.3-(0.6*RacialTension), 2), round(0.24-(_Terrorism*1), 2), round(0.2-(0.4*Patriot_freq), 2), round(-0.1+(0.16*ImmigrationDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_gdp(_globaleconomy_, Capitalism, CO2Emissions, ImmigrationDemand, Unemployment, Environment, Equality, OilDemand, _HighIncome, Pollution, Wages):
    zone = "ECONOMY"
    default = 0.57
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0.25*(_globaleconomy_**0.8), 2), round(-0.2+(0.65*Capitalism), 2), round(0.7*(CO2Emissions**1.4), 2), round(0.41*(ImmigrationDemand**4), 2), round(0.45-(0.5*Unemployment)**0.75, 2), round(-0.84*(Environment**2), 2), round(-0.28*(Equality**6), 2), round(0+(0.4*OilDemand), 2), round(0.28*(_HighIncome**2), 2), round(0.32*(Pollution**2.85), 2), round(0.3*(Wages**3.2), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_genderequality(Liberal):
    zone = "WELFARE"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.14+(0.28*Liberal), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_generationalwealthgap(StatePensions, FreeBusPasses, PropertyTax, GraduateTax, RentControls, UniversityGrants, Young, Equality):
    zone = "ECONOMY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0.25*(StatePensions**4), 2), round(0+(0.08*FreeBusPasses), 2), round(0-(0.27*PropertyTax), 2), round(0.05+(0.15*GraduateTax), 2), round(-0.08-(0.08*RentControls), 2), round(-0.06-(0.12*UniversityGrants), 2), round(-0.23*(Young**3), 2), round(-0.15*(Equality**3), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_health(Retired_freq, WorkerProductivity, ImmigrationDemand):
    zone = "PUBLICSERVICES"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.2+(0.4*Retired_freq), 2), round(-0.15+(0.15*WorkerProductivity), 2), round(0.07*(ImmigrationDemand**6), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_healthcaredemand(Immigration, IllegalImmigration, Health, Technology, Alcoholism, DrugAddiction, Obesity, ContagiousDisease, ViolentCrimeRate, TobaccoUse, AsthmaEpidemic, HospitalOvercrowding):
    zone = "PUBLICSERVICES"
    default = 0.22
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(0.12*Immigration), 2), round(0+(0.12*IllegalImmigration), 2), round(0-(0.26*Health), 2), round(0.28*(Technology**1.44), 2), round(0+(0.12*Alcoholism), 2), round(0+(0.12*DrugAddiction), 2), round(0+(0.1*Obesity), 2), round(0+(0.1*ContagiousDisease), 2), round(0.08*(ViolentCrimeRate**2), 2), round(0+(0.08*TobaccoUse), 2), round(0.07*(AsthmaEpidemic**1.2), 2), round(0+(0.6*HospitalOvercrowding), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_humandevelopment(Wages, Health, Education, Religious_freq, ImmigrationDemand, Tourism, _All_):
    zone = "WELFARE"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.3334*Wages), 2), round(0+(0.3334*Health), 2), round(0+(0.3334*Education), 2), round(-4*(Religious_freq-0.68)**32, 2), round(-0.1+(0.16*ImmigrationDemand), 2), round(-0.2+(0.4*Tourism), 2), round(-0.2+(0.4*_All_), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_immigration(Unemployment,  Wages, Population):
    zone = "FOREIGNPOLICY"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0.24*(Unemployment**3), 2),  round(-0-(0.22*Wages), 2), round(0+(0.10*Population), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_immigrationdemand(_globaleconomy_):
    zone = "FOREIGNPOLICY"
    default = 0.8
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0.1+(_globaleconomy_+1)*-0.1, 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_illegalimmigration(ImmigrationDemand, Immigration, ImmigrationRules):
    zone = "FOREIGNPOLICY"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(1-ImmigrationRules)*ImmigrationDemand, 2), round(0+(0.2*Immigration), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_industrialautomation(_year, RoboticsResearch, Technology, DriverlessCarLaws, Unemployment, TradeUnionist, WorkerProductivity, WorkingWeek):
    zone = "ECONOMY"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.008*_year), 2), round(0.34*(RoboticsResearch**1.2), 2), round(0.45*(Technology**0.8), 2), round(0.2*(DriverlessCarLaws**0.2), 2), round(0.0+(0.4*Unemployment), 2), round(0.0-(0.17*TradeUnionist), 2), round(0.02+(0.15*WorkerProductivity), 2), round(0.1-(0.25*WorkingWeek), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_inflation(Hyperinflation, CurrencyStrength, Wealthy, _HighIncome, BusinessConfidence, Stability):
    zone = "ECONOMY"
    default = 0.2
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0.78*(Hyperinflation**4), 2), round(0.05-(0.45*CurrencyStrength), 2), round(-0.29*(Wealthy**3), 2), round(-0.25*(_HighIncome**4), 2), round(0.05-(0.65*BusinessConfidence)**3, 2), round(-0.06*(Stability**4), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_internationaltrade(ForeignRelations, GDP, AirTravel, CO2Emissions, Pollution, Farmers_freq):
    zone = "FOREIGNPOLICY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.2+(0.2*ForeignRelations), 2), round(0.12*(GDP**0.6), 2), round(0+(0.2*AirTravel), 2), round(0+(0.2*CO2Emissions), 2), round(0+(0.05*Pollution), 2), round(0-(0.04*Farmers_freq), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_internetcurrencyadoption(_year, Technology, _MiddleIncome, Young, InternetCurrencyTaxation, InternetTax, IncomeTax, SalesTax, Inflation, FlatTax, CO2Emissions, TaxEvasion):
    zone = "ECONOMY"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0+(0.001*_year), 2), round(0.0+(0.42*Technology), 2), round(0+(0.18*_MiddleIncome), 2), round(0.0+(0.16*Young), 2), round(0.0-(0.2*InternetCurrencyTaxation), 2), round(0.0-(0.05*InternetTax), 2), round(0+(0.02*IncomeTax), 2), round(0+(0.07*SalesTax), 2), round(0.12*(Inflation**4), 2), round(0+(0.02*FlatTax), 2), round(0+(0.025*CO2Emissions), 2), round(0.08*(TaxEvasion**4), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_internetspeed(Technology, Young, SelfEmployed, SelfEmployed_freq, CarUsage):
    zone = "ECONOMY"
    default = 0.25
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0+(0.2*Technology), 2), round(-0.1+(0.2*Young), 2), round(-0.1+(0.25*SelfEmployed), 2), round(0+(0.09*SelfEmployed_freq), 2), round(-0.06*(CarUsage**4), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_legaldrugconsumption(_global_liberalism, Health, WorkerProductivity, AlcoholConsumption, HealthcareDemand,Narcotics):
    zone = "WELFARE"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0.25*(_global_liberalism**5)*Narcotics, 2), round(-0.22*(Health**2), 2), round(0.00-(0.04*WorkerProductivity), 2), round(0-(0.3*AlcoholConsumption), 2), round(0+(0.06*HealthcareDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_lifespan(_year, Health, Environment, Technology, ViolentCrimeRate, Retired_freq, Population, HealthcareDemand):
    zone = "PUBLICSERVICES"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.1+(0.02*_year), 2), round(0+(0.65*Health), 2), round(-0.2+(0.4*Environment), 2), round(0.0+(0.15*Technology), 2), round(0.0-(0.2*ViolentCrimeRate), 2), round(0.0+(0.12*Retired_freq), 2), round(-0.1+(0.2*Population), 2), round(0.13*(HealthcareDemand**3), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_oildemand(_globaleconomy_, OilPrice):
    zone = "TRANSPORT"
    default = 0.1
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-0.1+(_globaleconomy_+1)*0.1, 2), round(0.+(0.5*OilPrice), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_oilprice(GDP, Motorist, Motorist_freq,ElectricCarTransition):
    zone = "TRANSPORT"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-0.4*(1.0-ElectricCarTransition)*GDP, 2), round(0.3-(0.6*Motorist), 2), round(0.2-(0.4*Motorist_freq), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_oilsupply(_year, OilPrice):
    zone = "TRANSPORT"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0-(0.015*_year), 2), round(0-(0.5*OilPrice), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_population(TrafficCongestion, FoodPrice, Pollution, Homelessness, HealthcareDemand):
    zone = "PUBLICSERVICES"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-0.10+(0.2*TrafficCongestion), 2), round(-0.04+(0.08*FoodPrice), 2), round(0+(0.10*Pollution), 2), round(-0.5+(0.1*Homelessness), 2), round(0+(0.08*HealthcareDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_povertyrate(Poor, CrimeRate, RacialTension, _global_socialism, Socialist, ViolentCrimeRate, Education):
    zone = "WELFARE"
    default = 0.65
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0.3-(Poor**2), 2), round(0.61*(CrimeRate**2), 2), round(0+(0.22*RacialTension), 2), round(0.2*(_global_socialism**5), 2), round(-0.35*(Socialist**2), 2), round(0.17*(ViolentCrimeRate**3), 2), round(-0.13*(Education**2), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_privateenergy(GDP, CleanEnergySubsidies, MicrogenerationGrants, OilDrillingSubsidy, Mandatorymicrogeneration, SmartMeterProgram, EcoHomeRegulations, Unemployment, TradeUnionist, TradeUnionist_freq, _global_socialism):
    zone = "ECONOMY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-0.2+(0.3*GDP), 2), round(0.05+(0.05*CleanEnergySubsidies), 2), round(-0.05-(0.1*MicrogenerationGrants), 2), round(0+(0.12*OilDrillingSubsidy), 2), round(-0.1-(0.25*Mandatorymicrogeneration), 2), round(-0.03-(0.05*SmartMeterProgram), 2), round(-0.03-(0.04*EcoHomeRegulations), 2), round(0-(0.09*Unemployment), 2), round(0-(0.06*TradeUnionist), 2), round(0-(0.04*TradeUnionist_freq), 2), round(-0.02-(0.06*_global_socialism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_privatehealthcare(StateHealthService, GDP, Health, Equality, _LowIncome_fixed, _MiddleIncome_fixed, _HighIncome_fixed, Retired, Unemployment, TradeUnionist, _global_socialism, HospitalOvercrowding):
    zone = "PUBLICSERVICES"
    default = 0.55
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-1.25*(StateHealthService**1.3), 2), round(0+(0.45*GDP), 2), round(0.3*(Health**0.6), 2), round(0-(0.1*Equality), 2), round(0-(1100*_LowIncome_fixed), 2), round(0-(2200*_MiddleIncome_fixed), 2), round(0-(3600*_HighIncome_fixed), 2), round(0.00+(0.16*Retired), 2), round(0-(0.07*Unemployment), 2), round(0-(0.1*TradeUnionist), 2), round(-0.02-(0.06*_global_socialism), 2), round(0-(0.47*HospitalOvercrowding), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_privatehousing(StateHousing, GDP, _LowIncome, _MiddleIncome, Equality, _global_socialism):
    zone = "WELFARE"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-1.25*(StateHousing**1.3), 2), round(0+(0.5*GDP), 2), round(0-(0.17*_LowIncome), 2), round(0-(0.08*_MiddleIncome), 2), round(0-(0.1*Equality), 2), round(-0.02-(0.06*_global_socialism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_privatepensions(StatePensions, GDP, _MiddleIncome, Equality, Retired, Retired_income, _global_socialism):
    zone = "WELFARE"
    default = 0.45
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0-(0.85*StatePensions), 2), round(0+(0.55*GDP), 2), round(0-(0.10*_MiddleIncome), 2), round(0-(0.2*Equality), 2), round(0.1+(0.5*Retired), 2), round(0.05+(0.1*Retired_income), 2), round(-0.02-(0.06*_global_socialism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_privaterail(GDP, RailUsage, Unemployment, TradeUnionist, TradeUnionist_freq, _global_socialism):
    zone = "TRANSPORT"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-0.2+(0.3*GDP), 2), round(0.00+(0.35*RailUsage), 2), round(0-(0.09*Unemployment), 2), round(0-(0.06*TradeUnionist), 2), round(0-(0.04*TradeUnionist_freq), 2), round(-0.02-(0.06*_global_socialism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_privateschools(StateSchools, GDP, _LowIncome_fixed, _MiddleIncome_fixed, _HighIncome_fixed, Equality, Education, Unemployment, TradeUnionist, _global_socialism):
    zone = "PUBLICSERVICES"
    default = 0.45
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-1.25*(StateSchools**1.3), 2), round(0+(0.55*GDP), 2), round(-1000-(_LowIncome_fixed**1.2)*3000, 2), round(-4000-(_MiddleIncome_fixed**1.5)*6000, 2), round(-8000-(_HighIncome_fixed**1.8)*5000, 2), round(0-(0.1*Equality), 2), round(0.29*(Education**0.6)+0.06, 2), round(0-(0.13*Unemployment), 2), round(0-(0.1*TradeUnionist), 2), round(-0.02-(0.06*_global_socialism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_privatetelecoms(GDP, Technology, InternetTax, TelecommutingInitiative, Unemployment, TradeUnionist, TradeUnionist_freq, _global_socialism):
    zone = "ECONOMY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-0.2+(0.3*GDP), 2), round(0+(0.2*Technology), 2), round(-0.06-(0.12*InternetTax), 2), round(0.05+(0.05*TelecommutingInitiative), 2), round(0-(0.09*Unemployment), 2), round(0-(0.06*TradeUnionist), 2), round(0-(0.04*TradeUnionist_freq), 2), round(-0.02-(0.06*_global_socialism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_privatewater(GDP, Unemployment, TradeUnionist, TradeUnionist_freq, _global_socialism):
    zone = "PUBLICSERVICES"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-0.2+(0.3*GDP), 2), round(0-(0.09*Unemployment), 2), round(0-(0.06*TradeUnionist), 2), round(0-(0.04*TradeUnionist_freq), 2), round(-0.02-(0.06*_global_socialism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_racialtension(_Terrorism, Patriot_freq, _global_liberalism,  ImmigrationDemand):
    zone = "FOREIGNPOLICY"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(-0.2+(_Terrorism**4), 2), round(-0.12+(0.24*Patriot_freq), 2), round(0.1-(0.2*_global_liberalism), 2), round(0-(0.1*ImmigrationDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_railusage(GDP, CarUsage, BusUsage, OilDem1and):
    zone = "TRANSPORT"
    default = 0.25
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0+(0.2*GDP), 2), round(0-(0.35*CarUsage), 2), round(0-(0.25*BusUsage), 2), round(0+(0.12*OilDem1and), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_stability(PovertyRate, Environment, Health, Education, CrimeRate, ViolentCrimeRate, Democracy, Equality, RacialTension, GDP, _Terrorism, Corruption, _effectivedebt_, Tourism, ImmigrationDemand, _global_liberalism):
    zone = "PUBLICSERVICES"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0.1-(PovertyRate*0.2), 2), round(0.8*(Environment-0.5)**3, 2), round(0.8*(Health-0.5)**3, 2), round(0.8*(Education-0.5)**3, 2), round(0.1-(CrimeRate*0.2), 2), round(0.1-(ViolentCrimeRate*0.2), 2), round(0.8*(Democracy-0.5)**3, 2), round(0.8*(Equality-0.5)**3, 2), round(0.1-(RacialTension*0.2), 2), round(0.8*(GDP-0.5)**3, 2), round(0.1-(_Terrorism*0.2), 2), round(0-(Corruption**2)*0.2, 2), round(-0.32*(_effectivedebt_**2)+0.06, 2), round(-0.3+(0.6*Tourism), 2), round(-0.10+(0.20*ImmigrationDemand), 2), round(0.08-(_global_liberalism+1)**-6, 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_technology(WorkerProductivity, Education, Unemployment):
    zone = "ECONOMY"
    default = 0.4
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0.15*(WorkerProductivity**4), 2), round(-0.1+(0.16*Education), 2), round(0.12*(Unemployment**4), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_tobaccouse(GDP, Health):
    zone = "WELFARE"
    default = 0.54
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(0.4*GDP), 2), round(0-(0.11*Health), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_tourism(AirlineTax, AntisocialBehaviour, CrimeRate, StreetGangs, ViolentCrimeRate, ForeignRelations, BorderControls, SalesTax, _globaleconomy_, ClassWarfare, Environment, Pollution, GDP, HealthcareDemand):
    zone = "ECONOMY"
    default = 0.35
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0-(0.3*AirlineTax), 2), round(0-(0.1*AntisocialBehaviour), 2), round(0-(0.1*CrimeRate), 2), round(0-(0.3*StreetGangs), 2), round(0-(0.2*ViolentCrimeRate), 2), round(0+(0.4*ForeignRelations), 2), round(0.0-(0.22*BorderControls), 2), round(0-(0.05*SalesTax), 2), round(0+(0.25*_globaleconomy_), 2), round(0-(0.4*ClassWarfare), 2), round(-0.1+(0.1*Environment), 2), round(-0.03-(0.03*Pollution), 2), round(0+(0.10*GDP), 2), round(0+(0.06*HealthcareDemand), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_trafficcongestion(CarUsage, Commuter, Motorist, Motorist_freq, GDP, CO2Emissions):
    zone = "TRANSPORT"
    default = 0.25
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(CarUsage**1.4), 2), round(0.4-(0.80*Commuter), 2), round(0.3-(0.6*Motorist), 2), round(0.2-(0.2*Motorist_freq), 2), round(-0.10*(GDP**2), 2), round(0+(0.1*CO2Emissions), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_unemployment(WorkingWeek, TradeUnionist, Commuter_freq, RacialTension, PovertyRate, CrimeRate, WorkerProductivity, Wages, Poor, ImmigrationDemand, Socialist, Obesity, _global_socialism, ViolentCrimeRate):
    zone = "ECONOMY"
    default = 1.0
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0+(0.2*WorkingWeek), 2), round(-0.25*(TradeUnionist**1.28), 2), round(0-(0.28*Commuter_freq), 2), round(0.7*(RacialTension**3), 2), round(0.24*(PovertyRate**8), 2), round(0.26*(CrimeRate**4), 2), round(-0.215+(WorkerProductivity*0.3), 2), round(0.2-(0.4*Wages), 2), round(-0.10*(Poor**2), 2), round(-0.22*(ImmigrationDemand**2)+0.05, 2), round(-0.2*(Socialist**4), 2), round(0+(0.07*Obesity), 2), round(-0.04+(0.08*_global_socialism), 2), round(0.05*(ViolentCrimeRate**1.1), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_veganism(FoodPrice, Environmentalist_perc, JunkFoodTax, HealthFoodSubsidies, FoodStandards, HealthyEatingCampaign, CompulsoryFoodLabelling, Farmers_freq, CO2Emissions):
    zone = "WELFARE"
    default = 0.1
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0.25*(FoodPrice**3), 2), round(0+(0.12*Environmentalist_perc), 2), round(0.05+(0.1*JunkFoodTax), 2), round(0.07+(0.11*HealthFoodSubsidies), 2), round(0+(0.12*FoodStandards), 2), round(0+(0.06*HealthyEatingCampaign), 2), round(0.05+(0.16*CompulsoryFoodLabelling), 2), round(0-(0.15*Farmers_freq), 2), round(0-(0.08*CO2Emissions), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_violentcrimerate(Health, _All_, Retired, _global_liberalism):
    zone = "LAWANDORDER"
    default = 0.63
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0.05*(1.0-Health)**4, 2), round(0.05-(0.21*_All_), 2), round(0-(0.18*Retired), 2), round(0-(0.1*_global_liberalism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_wages(_LowIncome, _MiddleIncome, WorkerProductivity, Inflation, _global_socialism):
    zone = "ECONOMY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(-0.25+(0.5*_LowIncome), 2), round(-0.13+(0.26*_MiddleIncome), 2), round(0-(0.4*WorkerProductivity), 2), round(0.21*(Inflation**3), 2), round(0.04-(0.08*_global_socialism), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_workerproductivity(GDP, InternationalTrade, Unemployment):
    zone = "ECONOMY"
    default = 0.45
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(0.35*(GDP**0.76), 2), round(-0.2+(0.4*InternationalTrade), 2), round(-0.08+(0.16*Unemployment), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_workingweek(TradeUnionist, Health, WorkerProductivity):
    zone = "ECONOMY"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = [round(0.1-(0.1*TradeUnionist), 2), round(-0.24*(Health**8), 2), round(-0.06+(0.12*WorkerProductivity), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_rareearthprice(_default_, _year, RareEarthRefinement, Technology, ForeignRelations, GreenElectronicsInitiative, _globaleconomy_, CurrencyStrength, Rareearthcrisis):
    zone = "ECONOMY"
    default = 0.0
    min_value = 0
    max_value = 1
    emotion = "HIGHBAD"

    effects = [round(0.1, 2), round(0+(0.02*_year), 2), round(-0.1-(0.2*RareEarthRefinement), 2), round(0.8*(Technology**3.7), 2), round(-0.2*(ForeignRelations**0.4), 2), round(-0.1-(0.17*GreenElectronicsInitiative), 2), round(-0.07+(_globaleconomy_+1)*0.07, 2), round(0.08-(0.16*CurrencyStrength), 2), round(0+(1.0*Rareearthcrisis), 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated_mentalhealth(WorkingWeek, LegalDrugConsumption, FakeNews, Pollution, UniversalBasicIncome, Alcoholism, PovertyRate, ViolentCrimeRate, HealthcareDemand, Homelessness, Unemployment, DrugAddiction):
    zone = "PUBLICSERVICES"
    default = 0.5
    min_value = 0
    max_value = 1
    emotion = "HIGHGOOD"

    effects = [round(-0.07*(WorkingWeek*2)-1**5, 2), round(-0.11*(LegalDrugConsumption**3), 2), round(-0.04-(0.05*FakeNews), 2), round(-0.11*(Pollution**4), 2), round(0.02+(0.06*UniversalBasicIncome), 2), round(0.07*(1-Alcoholism)**5, 2), round(-0.08*(PovertyRate**5), 2), round(-0.08*(ViolentCrimeRate**6), 2), round(0.04-(0.08*HealthcareDemand), 2), round(0.12*(1-Homelessness)**5, 2), round(0.05*(1-Unemployment)**5, 2), round(0.08*(1-DrugAddiction)**5, 2), ]
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__turnout_retired():
    zone = "NOCLICK"
    default = 0.0
    min_value = -1
    max_value = 1
    emotion = "UNKNOWN"

    effects = []
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__turnout_youth():
    zone = "NOCLICK"
    default = 0.0
    min_value = -1
    max_value = 1
    emotion = "UNKNOWN"

    effects = []
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__turnout_ethnic():
    zone = "NOCLICK"
    default = 0.0
    min_value = -1
    max_value = 1
    emotion = "UNKNOWN"

    effects = []
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__turnout():
    zone = "NOCLICK"
    default = 0.0
    min_value = -1
    max_value = 1
    emotion = "UNKNOWN"

    effects = []
    effects = [value for value in effects if value > 0]
    return sum(effects)

def generated__campaigneffectiveness():
    zone = "NOCLICK"
    default = 1.0
    min_value = 0
    max_value = 1
    emotion = "UNKNOWN"

    effects = []
    effects = [value for value in effects if value > 0]
    return sum(effects)













