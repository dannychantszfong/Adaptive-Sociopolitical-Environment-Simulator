from math import *
import popularity
import simulation_config
import simulation_callout
import config

def abortionlaw_function(x):
    popularity.Religious_Fundamentalism_popularity = -0.14*exp(-0.75*x)
    popularity.Traditionalism_popularity = -0.33*x - 0.18
    popularity.Conservatism_popularity = -0.1*exp(-0.68*x)
    popularity.Liberalism_popularity = 0.28*x
    popularity.Feminism_popularity = 0.06*exp(0.16*x)
    popularity.Progressivism_popularity = 0.26*x + 0.17*exp(0.43*x)
    popularity.Secularism_popularity = 0.18*x + 0.14 + 0.06*exp(-0.21*x)
    simulation_callout.Population = 0.05-(0.1*x)
    simulation_config.global_liberalis = 0.20*(x**2)-0.06
    simulation_callout.genderequality = -0.1+(0.2*x)


def adulteducationsubsidies_function(x):
    popularity.Socialism_popularity = 0.17*x
    popularity.Progressivism_popularity = 0.3*x + 0.08
    popularity.Democratic_Socialism_popularity = 0.18 + 0.16*exp(-0.53*x)
    popularity.Libertarian_Capitalism_popularity = -0.21*x
    popularity.Neoliberalism_popularity = -0.06*exp(-0.35*x)
    popularity.Conservatism_popularity = -0.37*x
    simulation_callout.education = 0.03+(0.04*x)
    simulation_config.WorkerProductivity = 0.02+(0.02*x)


def agriculturesubsidies_function(x):
    popularity.Protectionism_popularity = 0.17 + 0.09*exp(-0.77*x)
    popularity.Populism_popularity = 0.29*x + 0.1 + 0.11*exp(-0.13*x)
    popularity.Nationalism_popularity = 0.27*x + 0.1*exp(-0.2*x)
    popularity.Capitalism_popularity = -0.37*x - 0.18*exp(0.39*x)
    popularity.Neoliberalism_popularity = -0.36*x
    popularity.Libertarian_Capitalism_popularity = -0.11*x - 0.1*exp(0.79*x)
    popularity.Unemployed_popularity = 0.00-(0.17*x)
    popularity.Farmers_popularity = 0.075+(0.31*x)
    config.Farmers_freq = 0.01+(0.12*x)

def airlinetax_function(x):
    popularity.Environmentalism_popularity = 0.07 + 0.18*exp(-0.92*x)
    popularity.Industrialism_popularity = -0.34*x - 0.18
    popularity.Libertarianism_popularity = -0.14*x - 0.07*exp(-0.27*x)
    popularity.Neoliberalism_popularity = -0.35*x - 0.16*exp(-0.11*x)
    simulation_config.airtravel = 0-(0.3*x)
    simulation_config.GDP = 0.00-(0.05*x)
    simulation_config.MiddleIncome = 0-(0.02*x)*simulation_config.airtravel
    simulation_config.HighIncome = 0-(0.03*x)*simulation_config.airtravel


def alcoholawarenesscampaign_function(x):
    simulation_config.AlcoholConsumption = 0-(0.15*x)


def alcohollaw_function(x):
    popularity.Conservatism_popularity = 0.16*exp(-0.33*x)
    popularity.Collectivism_popularity = 0.13 + 0.06*exp(-0.1*x)
    popularity.Religious_Fundamentalism_popularity = 0.18*x
    popularity.Liberalism_popularity = -0.3*x - 0.16*exp(-0.01*x)
    popularity.Individualism_popularity = -0.2*x
    popularity.Libertarianism_popularity = -0.12*x - 0.11
    popularity.Young_popularity = -0.2*(x**2)
    simulation_config.AlcoholConsumption = 0.4-(1.0*x)
    simulation_config.global_liberalis = 0.04-(0.12*x)
    simulation_config.Tourism = -0.05*(x**4)

def alcoholtax_function(x):
    popularity.Collectivism_popularity = 0.22*x + 0.18*exp(0.37*x)
    popularity.Environmentalism_popularity = 0.33*x + 0.19*exp(0.31*x)
    popularity.Progressivism_popularity = 0.06*exp(0.5*x) + 0.15
    popularity.Libertarianism_popularity = -0.1*exp(-0.18*x)
    popularity.Neoliberalism_popularity = -0.14*x - 0.09*exp(-0.83*x)
    popularity.Individualism_popularity = -0.39*x - 0.14
    simulation_config.AlcoholConsumption = -0.58*(x**2)
    popularity.Poor_popularity = -0.2*(simulation_config.AlcoholConsumption*x)
    simulation_config.PovertyRate = 0.2*(simulation_config.AlcoholConsumption*x)
    simulation_callout.Equality = -0.1*(simulation_config.AlcoholConsumption*x)


def antibioticsban_function(x):
    popularity.Environmentalism_popularity = 0.37*x
    popularity.Progressivism_popularity = 0.13*exp(0.2*x)
    popularity.Industrialism_popularity = -0.28*x - 0.15*exp(-0.7*x)
    popularity.Neoliberalism_popularity = -0.19*x - 0.06*exp(-0.79*x)
    popularity.Capitalism_popularity = -0.34*x
    popularity.Farmers_popularity = -0.25*(x**1.6)
    popularity.Capitalism_popularity = -0.03-(0.015*x)
    simulation_config.health = 0.02+(0.04*x)
    config.Farmers_freq = -0.03-(0.07*x)
    simulation_callout.FoodPrice = 0.05+(0.10*x)


def anticorruptionagency_function(x):
    simulation_config.Corruption = 0-(0.3*x)
    popularity.Self_Employed_popularity = 0-(0.5*x)*simulation_config.Corruption
    popularity.Liberalism_popularity = 0.14*x + 0.05
    popularity.Collectivism_popularity = 0.32*x
    popularity.Progressivism_popularity = 0.33*x + 0.07*exp(0.58*x) + 0.09
    popularity.Totalitarianism_popularity = -0.31*x - 0.15*exp(-0.76*x)
    Corrupt_regimes = -0.3*x
    Elitism_popularity = -0.23*x - 0.1*exp(0.33*x)


def armedpolice_function(x):
    popularity.Liberalism_popularity = -0.15*x - 0.16
    simulation_callout.crimerate = -0.10*(x**0.68)+0.01
    simulation_config.ViolentCrimeRate = -0.20*(x**0.4)
    simulation_config.security = (0.025+0.035*x)
    popularity.Self_Employed_popularity = 0+(0.18*x)
    config.Self_Employed_freq = 0+(0.03*x)
    popularity.Unemployed_popularity = 0-(0.04*x)
    popularity.Conservatism_popularity = 0.31*x + 0.19*exp(0.6*x)
    popularity.Totalitarianism_popularity = 0.07*exp(-0.85*x)
    popularity.Nationalism_popularity = 0.17*exp(0.1*x) + 0.12
    popularity.Anarchism_popularity = -0.21*x - 0.17
    popularity.Progressivism_popularity = -0.18*exp(0.78*x)


def artssubsidies_function(x):
    popularity.Liberalism_popularity = 0.01+(0.08*x)
    popularity.Capitalism_popularity = -0.01-(0.03*x)
    simulation_config.ForeignRelations = 0+(0.07*x)
    simulation_config.Tourism = 0+(0.10*x)
    simulation_callout.education = 0+(0.03*x)
    simulation_config.global_liberalis = -0.01+(0.06*x)
    popularity.Unemployed_popularity = 0-(0.01*x)
    popularity.Socialism_popularity = 0.06*exp(0.41*x)
    popularity.Collectivism_popularity = 0.08 + 0.13*exp(-0.62*x)
    popularity.Cultural_Relativism_popularity = 0.11*exp(0.13*x) + 0.16
    popularity.Neoliberalism_popularity = -0.09*exp(0.32*x) - 0.2
    popularity.Libertarian_Capitalism_popularity = -0.26*x - 0.1*exp(-0.78*x)
    popularity.Egoism_popularity = -0.39*x


def automationtax_function(x):
    simulation_config.GDP = 0.5+(0.5*x)
    simulation_config.TaxEvasion = 1.0-(0.2*x)
    popularity.Capitalism_popularity = -0.11*exp(0.19*x)
    simulation_config.Technology = -0.033-(0.066*x)

    simulation_config.CorporateExodus = 0.05+(0.1*x)
    simulation_config.BrainDrain = 0.02+(0.08*x)
    popularity.Socialism_popularity = 0.21*x + 0.12
    popularity.Protectionism_popularity = 0.18*exp(0.87*x)
    popularity.Populism_popularity = 0.07*exp(0.34*x) + 0.16
    popularity.Neoliberalism_popularity = -0.27*x
    popularity.Libertarian_Capitalism_popularity = -0.38*x - 0.08*exp(0.03*x)


def bancoal_function(x):

    popularity.Environmentalism_popularity = 0.11*exp(0.76*x)
    popularity.Capitalism_popularity = -0.02-(0.07*x)
    simulation_config.co2emissions = -0.03-(0.08*x)
    simulation_config.GDP = -0.02-(0.06*x)
    simulation_config.OilDemand = 0.01+(0.04*x)
    simulation_config.environment = 0.02+(0.03*x)
    simulation_config.AsthmaEpidemic = -0.02-(0.06*x)
    popularity.Progressivism_popularity = 0.3*x
    popularity.Globalization_supporters_popularity = 0.39*x + 0.16*exp(0.92*x)
    popularity.Industrialism_popularity = -0.14*x - 0.11 - 0.2*exp(-0.24*x)
    popularity.Neoliberalism_popularity = -0.12*x - 0.19*exp(0.4*x)
    popularity.Nationalism_popularity = -0.32*x - 0.12 - 0.14*exp(-0.9*x)


def bandivorce_function(x):
    popularity.Conservatism_popularity = 0.24*x + 0.13*exp(-0.68*x)
    popularity.Religious_Fundamentalism_popularity = 0.14*x + 0.18
    popularity.Liberalism_popularity = -0.33*x - 0.1
    config.Religious_Fundamentalism_freq = -0.01-(x*0.02)
    simulation_config.global_liberalis = -0.16*(x**2)-0.06
    simulation_callout.genderequality  = -0.1-(0.08*x)
    popularity.Traditionalism_popularity = 0.4*x
    popularity.Feminism_popularity = -0.13*x - 0.13*exp(0.4*x)
    popularity.Individualism_popularity = -0.09 - 0.05*exp(-0.64*x)


def banforeignchurchservice_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.19*x + 0.15*exp(0.05*x)
    popularity.Liberalism_popularity = -0.15*x - 0.05*exp(0.18*x)
    popularity.EthnicMinorities_popularity = -0.07-(x*0.43)
    simulation_callout.ImmigrationDemand = -0.03-(x*0.25)
    simulation_callout.RacialTension = 0.05+(x*0.25)
    popularity.Nationalism_popularity = 0.33*x + 0.19*exp(0.89*x)
    popularity.Internationalism_popularity = -0.12*exp(-0.08*x)
    popularity.Secularism_popularity = -0.12*x - 0.16


def banhomosexuality_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.19 + 0.13*exp(-0.35*x)
    popularity.Liberalism_popularity = -0.16*exp(-0.28*x)
    popularity.Conservatism_popularity = 0.04+(x*0.04)
    simulation_callout.crimerate = 0+(x**4)*0.06
    config.Religious_Fundamentalism_freq = -0.02-(x*0.04)
    simulation_config.global_liberalis = -0.16*(x**2)-0.06
    popularity.Traditionalism_popularity = 0.18*x + 0.11
    popularity.Nationalism_popularitys = 0.3*x
    popularity.Progressivism_popularity = -0.11*exp(0.56*x) - 0.12
    popularity.Secularism_popularity = -0.17*x - 0.1*exp(0.03*x)


def banlowmpgcars_function(x):
    simulation_config.OilDemand = simulation_config.inv_ElectricCarTransition*(-0.05*x)-0.025
    simulation_config.carusage = simulation_config.inv_ElectricCarTransition*(x**2)*-0.1-0.05
    popularity.Motorist_popularity = simulation_config.inv_ElectricCarTransition*(x**2)*-0.14-0.05
    popularity.Environmentalism_popularity = 0.06 + 0.16*exp(-0.95*x)
    simulation_config.environment = simulation_config.inv_ElectricCarTransition*(x**2)*0.11+0.03
    simulation_config.co2emissions = simulation_config.inv_ElectricCarTransition*(x**2)*-0.05-0.01
    popularity.Progressivism_popularity = 0.16*x + 0.13*exp(0.07*x)
    popularity.Globalization_supporters_popularity = 0.33*x + 0.05
    popularity.Industrialism_popularity = -0.17*x
    popularity.Libertarian_Capitalism_popularity = -0.12 - 0.18*exp(-0.99*x)
    popularity.Neoliberalism_popularity = -0.08*exp(-0.25*x)


def banprivateeducation_function(x):
    simulation_callout.privateschools = -0.1+(x**0.5)*-1.5
    simulation_callout.Equality = 0.08*(x**0.5)
    popularity.Socialism_popularity = 0.06*(x**0.5)
    simulation_config.global_socialism = 0.06*(x**0.5)
    simulation_config.ClassWarfare = 0-(0.10*x)
    popularity.Capitalism_popularity = -0.05-(0.12*x)
    popularity.Wealthy_popularity = -0.04-(0.11*x)
    popularity.Socialism_popularity = 0.22*x + 0.13 + 0.11*exp(-0.84*x)
    popularity.Collectivism_popularity = 0.08*exp(0.61*x)
    popularity.Democratic_Socialism_popularity = 0.19*x + 0.14
    popularity.Libertarianism_popularity = -0.13*x - 0.11 - 0.08*exp(-0.75*x)
    popularity.Neoliberalism_popularity = -0.07*exp(-0.17*x)
    popularity.Conservatism_popularity = -0.2*x


def banprivatehealthcare_function(x):
    simulation_config.PrivateHealthcare = -0.1+(x**0.5)*-1.5
    simulation_callout.Equality = 0.08*(x**0.5)
    popularity.Socialism_popularity = 0.07*(x**0.5)
    simulation_config.global_socialism = 0.06*(x**0.5)
    popularity.Capitalism_popularity = -0.11*(x**0.5)
    popularity.Wealthy_popularity = -0.05-(0.13*x)
    popularity.Socialism_popularity = 0.23*x
    popularity.Collectivism_popularity = 0.39*x + 0.17*exp(-0.12*x)
    popularity.Democratic_Socialism_popularity = 0.19*x
    popularity.Libertarian_Capitalism_popularity = -0.37*x - 0.15*exp(0.14*x)
    popularity.Neoliberalism_popularity = -0.12 - 0.16*exp(-0.9*x)
    popularity.Conservatism_popularity = -0.26*x


def bansecondhomeownership_function(x):
    popularity.Wealthy_popularity = -0.21*(x**0.5)
    popularity.Capitalism_popularity = -0.11*(x**0.5)
    popularity.Poor_popularity = 0.08*(x**0.9)
    simulation_config.PovertyRate = 0-(x*0.06)
    popularity.Socialism_popularity = 0.07*(x**0.5)
    simulation_config.Homelessness = -0.17*(x**0.5)
    simulation_callout.Equality = 0.08*(x**2)
    simulation_config.global_socialism = 0.05*(x**3)+0.05
    popularity.Socialism_popularity = 0.13*exp(0.49*x)
    popularity.Progressivism_popularity = 0.34*x + 0.05 + 0.15*exp(-0.32*x)
    popularity.Populism_popularity = 0.23*x + 0.09
    popularity.Libertarianism_popularity = -0.31*x - 0.06*exp(0.41*x)
    popularity.Neoliberalism_popularity = -0.14*x - 0.06*exp(-0.35*x)
    popularity.Conservatism_popularity = -0.2*x


def bansundayshopping_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.32*x
    popularity.Liberalism_popularity = -0.14*exp(0.45*x)
    simulation_config.GDP = -0.02+(0*x)
    simulation_config.global_liberalis = -0.06*(x**1.2)
    popularity.Traditionalism_popularity = 0.21*x
    popularity.Nationalism_popularitys = 0.21*x
    popularity.Secularism_popularity = -0.07 - 0.17*exp(-0.36*x)
    popularity.Neoliberalism_popularity = -0.24*x


def bicyclesubsidies_function(x):
    simulation_config.health = 0.02+(0.02*x)
    simulation_config.carusage = 0-(0.03*x)
    simulation_config.railUsage = 0-(0.03*x)
    simulation_config.bususage = 0-(0.03*x)
    simulation_config.Obesity = -0.01-(0.01*x)
    popularity.Environmentalism_popularity = 0.15 + 0.13*exp(-0.73*x)
    popularity.Progressivism_popularity = 0.1 + 0.08*exp(-0.01*x)
    popularity.Globalization_supporters_popularity = 0.29*x
    popularity.Industrialism_popularity = -0.21*x - 0.19
    popularity.Libertarianism_popularity = -0.36*x - 0.11*exp(0.91*x)


def biofuelsubsidies_function(x):
    simulation_config.OilDemand = 0-(0.15*x)*simulation_config.carusage
    popularity.Environmentalism_popularity = 0.18*exp(0.2*x) + 0.17
    popularity.Farmers_popularity = 0.02+(0.07*x)
    popularity.Motorist_popularity = 0.02+(0.02*x)
    config.Farmers_freq = 0.02+(0.05*x)
    simulation_config.co2emissions = 0-(0.06*x)
    popularity.Progressivism_popularity = 0.31*x + 0.13 + 0.14*exp(-0.92*x)
    popularity.Nationalism_popularitys = 0.05 + 0.18*exp(-0.05*x)
    popularity.Neoliberalism_popularity = -0.29*x - 0.06*exp(0.24*x) - 0.09
    popularity.Libertarian_Capitalism_popularity = -0.19*x
    popularity.Industrialism_popularity = -0.06*exp(-0.6*x)


def bodycameras_function(x):
    popularity.Liberalism_popularity = 0.31*x + 0.15
    popularity.Conservatism_popularity = -0.05-(0.03*x)
    popularity.Self_Employed_popularity = -0.02-(0.02*x)
    simulation_callout.RacialTension = -0.14-(0.1*x)
    simulation_config.Corruption = -0.03-(0.07*x)
    popularity.Progressivism_popularity = 0.13*x + 0.16*exp(-0.89*x)
    popularity.Totalitarianism_popularity = -0.32*x
    popularity.Conservatism_popularity = -0.38*x - 0.06 - 0.14*exp(-0.29*x)


def bordercontrols_function(x):
    popularity.Patriot_popularity = 0+(0.30*x)
    popularity.Liberalism_popularity = -0.35*x - 0.17*exp(0.86*x)
    simulation_config.IllegalImmigration = 0-(x**1.5)*0.90
    simulation_config.Terrorism = 0-(0.1*x)
    popularity.EthnicMinorities_popularity = 0.00-(0.42*x)
    popularity.Nationalism_popularity = 0.14*exp(-0.04*x)
    popularity.Conservatism_popularity = 0.16*exp(0.79*x)
    popularity.Totalitarianism_popularity = 0.15*x + 0.09*exp(0.91*x) + 0.07
    popularity.Internationalism_popularity = -0.12*x - 0.2
    popularity.Globalization_supporters_popularity = -0.05 - 0.16*exp(-0.94*x)


def borderwall_function(x):
    popularity.Liberalism_popularity = -0.25*x
    popularity.Patriot_popularity = 0.22+(0.25*x)
    simulation_config.ForeignRelations = -0.09-(0.09*x)
    simulation_config.IllegalImmigration = -0.28-(x**3)*0.42
    popularity.EthnicMinorities_popularity = -0.3-(0.25*x)
    popularity.Nationalism_popularity = 0.15*x
    popularity.Conservatism_popularity = 0.23*x
    popularity.Totalitarianism_popularity = 0.1*x + 0.07*exp(0.23*x) + 0.16
    popularity.Internationalism_popularity = -0.09*exp(0.8*x)
    popularity.Progressivism_popularity = -0.14*exp(-0.47*x)


def businessstartupcampaign_function(x):
    popularity.Self_Employed_popularity = 0.1+(0.03*x)
    config.Self_Employed_freq = 0+(0.12*x)
    simulation_config.global_socialism = 0-(0.05*x)
    popularity.Capitalism_popularity = 0+(0.03*x)
    popularity.Liberalism_popularity = 0.12 + 0.16*exp(-0.21*x)
    popularity.Neoliberalism_popularity = 0.33*x + 0.12 + 0.19*exp(-0.21*x)
    popularity.Libertarian_Capitalism_popularity = 0.33*x + 0.14
    popularity.Socialism_popularity = -0.17 - 0.1*exp(-0.47*x)
    popularity.Protectionism_popularity = -0.37*x - 0.06


def buslanes_function(x):
    popularity.Commuter_popularity = 0.05+(0.17*x)
    popularity.Motorist_popularity = 0.00-(0.25*x)
    simulation_config.bususage = 0.05+(0.2*x)
    popularity.Environmentalism_popularity = 0.23*x + 0.16*exp(0.21*x) + 0.11
    popularity.Collectivism_popularity = 0.17 + 0.09*exp(-0.28*x)
    popularity.Progressivism_popularity = 0.21*x + 0.17*exp(-0.17*x)
    popularity.Neoliberalism_popularity = -0.25*x - 0.07*exp(-0.68*x)
    popularity.Libertarianism_popularity = -0.24*x - 0.1*exp(0.55*x)


def bussubsidies_function(x):
    popularity.Commuter_popularity = 0.10+(0.34*x)
    popularity.Motorist_popularity = 0.00-(0.15*x)
    simulation_config.bususage = 0.00+(0.32*x)
    popularity.Commuter_popularity_income_fixed = 75+(300*x)*simulation_config.bususage
    popularity.Capitalism_popularity = -0-(0.06*x)
    popularity.Unemployed_popularity = 0-(0.01*x)
    popularity.Environmentalism_popularity = 0.14*exp(0.68*x)
    popularity.Socialism_popularity = 0.31*x + 0.05*exp(0.93*x) + 0.15
    popularity.Collectivism_popularity = 0.06*exp(0.93*x)
    popularity.Neoliberalism_popularity = -0.18*x - 0.16
    popularity.Libertarian_Capitalism_popularity = -0.19*x - 0.18*exp(0.09*x)
    popularity.Conservatism_popularity = -0.2 - 0.19*exp(-0.13*x)


def capceopaymultiplier_function(x):
    popularity.Capitalism_popularity = -0.18*(x+0.25)**3
    popularity.Socialism_popularity = 0.15*(x+0.39)**3
    simulation_config.HighIncome = -0.21*(x+0.32)**4
    simulation_config.CorporateExodus = +0.29*(x**3)
    simulation_config.BrainDrain = 0.29*(x+0.1)**3
    simulation_callout.Equality = 0.15*(x+0.2)**4
    popularity.Wealthy_popularity = -0.32*(x**3)
    simulation_config.global_socialism = 0.07*(x**4)+0.05
    popularity.Socialism_popularity = 0.25*x + 0.17*exp(-0.01*x)
    popularity.Progressivism_popularity = 0.3*x
    popularity.Populism_popularity = 0.24*x + 0.11*exp(0.4*x)
    popularity.Libertarian_Capitalism_popularity = -0.28*x - 0.06*exp(0.21*x) - 0.07
    popularity.Neoliberalism_popularity = -0.09 - 0.05*exp(-0.59*x)
    popularity.Conservatism_popularity = -0.3*x - 0.16*exp(0.55*x)


def capitalcontrols_function(x):
    simulation_callout.emigration = -0.05-(0.05*x)
    simulation_callout.BusinessConfidence = -0.1-(0.05*x)
    simulation_callout.foreigninvestment = -0.5-(0.4*x)
    simulation_config.BrainDrain = -0.6-(0.2*x)
    simulation_config.CorporateExodus = -0.2-(0.2*x)
    popularity.Capitalism_popularity = -0.2*x - 0.09*exp(0.04*x)
    popularity.Socialism_popularity = 0.15+(0.1*x)
    popularity.Wealthy_popularity = -0.25-(0.12*x)
    simulation_config.global_socialism = 0.05+(0.03*x)
    popularity.Protectionism_popularity = 0.17 + 0.19*exp(-0.46*x)
    popularity.Nationalism_popularity = 0.07 + 0.08*exp(-1.0*x)
    popularity.Socialism_popularity = 0.18*exp(0.07*x) + 0.14
    popularity.Neoliberalism_popularity = -0.15 - 0.05*exp(-0.13*x)
    popularity.Libertarian_Capitalism_popularity = -0.1*exp(0.72*x) - 0.09


def capitalgainstax_function(x):
    simulation_config.GDP = -0.08*(x**5)
    popularity.Socialism_popularity = 0+(0.1*x)
    popularity.Capitalism_popularity = 0-(0.12*x)
    simulation_callout.Equality = 0+(0.09*x)
    simulation_config.HighIncome = 0-(0.10*x)
    config.Self_Employed_freq = 0-(0.05*x)
    popularity.Self_Employed_popularity = 0-(0.1*x)
    simulation_config.global_socialism = 0.02+(0.04*x)
    popularity.Wealthy_popularity = 0-(0.10*x)
    popularity.Socialism_popularity = 0.37*x + 0.14 + 0.1*exp(-0.78*x)
    popularity.Progressivism_popularity = 0.19 + 0.18*exp(-0.48*x)
    popularity.Democratic_Socialism_popularity = 0.4*x + 0.07
    popularity.Libertarian_Capitalism_popularity = -0.25*x - 0.14*exp(-0.1*x)
    popularity.Neoliberalism_popularity = -0.11 - 0.1*exp(-0.72*x)
    popularity.Conservatism_popularity = -0.36*x - 0.18*exp(0.17*x) - 0.06


def carboncaptureandstorage_function(x):
    simulation_config.co2emissions = -0.02-(0.09*x)
    popularity.Progressivism_popularity = 0.3*x + 0.11 + 0.16*exp(-0.6*x)
    popularity.Industrialism_popularity = 0.28*x + 0.14*exp(-0.81*x)
    popularity.Environmentalism_popularity = -0.37*x - 0.08*exp(-0.34*x)
    popularity.Libertarianism_popularity = -0.37*x - 0.16 - 0.14*exp(-0.38*x)


def carbontax_function(x):
    simulation_config.co2emissions = 0-(0.2*x)
    simulation_config.GDP = -0.25*(x**2)
    popularity.Environmentalism_popularity = 0.11*x
    simulation_callout.energyefficiency = 0+(0.25*x)
    simulation_config.airtravel = 0-(0.28*x)
    popularity.Capitalism_popularity = 0.02-(0.11*x)
    popularity.Motorist_popularity = -0.07*(1.0-simulation_callout.ElectricCarTransition)*x
    popularity.Progressivism_popularity = 0.15*exp(0.18*x) + 0.18
    popularity.Internationalism_popularity = 0.12*exp(0.51*x) + 0.17
    popularity.Industrialism_popularity = -0.26*x - 0.08
    popularity.Libertarianism_popularity = -0.23*x - 0.09*exp(-0.13*x)
    popularity.Neoliberalism_popularity = -0.06*exp(0.57*x)


def caremmissionslimits_function(x):
    popularity.Motorist_popularity = 0-(0.08*x)* simulation_config.inv_ElectricCarTransition
    popularity.Environmentalism_popularity = 0.12*exp(0.42*x) + 0.15
    simulation_config.environment = 0+(0.23*x)
    simulation_config.carusage = -0.01-(0.02*x)
    simulation_config.co2emissions = -0.01-(0.06*x)
    popularity.Progressivism_popularity = 0.22*x + 0.1*exp(0.5*x)
    popularity.Globalization_supporters_popularity = 0.11*x + 0.05*exp(-0.92*x)
    popularity.Industrialism_popularity = -0.09*exp(-0.05*x)
    popularity.Libertarian_Capitalism_popularity = -0.09*exp(0.73*x) - 0.06
    popularity.Nationalism_popularitys = -0.06 - 0.09*exp(-0.51*x)


def carpoolingcampaign_function(x):
    simulation_config.carusage = -0.01-(0.03*x)
    popularity.Environmentalism_popularity = 0.28*x + 0.09
    popularity.Collectivism_popularity = 0.07*exp(0.98*x) + 0.13
    popularity.Progressivism_popularity = 0.17*x + 0.1*exp(0.69*x) + 0.17
    popularity.Individualism_popularity = -0.27*x
    popularity.Libertarianism_popularity = -0.15 - 0.16*exp(-0.42*x)


def cartax_function(x):
    simulation_config.carusage = 0.00-(0.14*x)
    popularity.Motorist_popularity = -0.05-(0.15*x)
    popularity.Environmentalism_popularity = 0.12*exp(0.63*x) + 0.12
    popularity.Farmers_popularity = -0.04-(0.04*x)
    popularity.Progressivism_popularity = 0.23*x
    popularity.Collectivism_popularity = 0.3*x + 0.07*exp(-0.27*x)
    popularity.Libertarianism_popularity = -0.36*x - 0.2*exp(-0.07*x)
    popularity.Neoliberalism_popularity = -0.39*x - 0.19*exp(-0.69*x)
    popularity.Individualism_popularity = -0.18*exp(-0.36*x)


def cctvcameras_function(x):
    popularity.Liberalism_popularity = -0.19*x
    simulation_callout.crimerate = -0.15*(x**0.4)
    simulation_config.ViolentCrimeRate = -0.08*(x**0.8)+0.03
    popularity.Conservatism_popularity = 0.07*exp(-0.11*x)
    simulation_config.security = (0.025+0.038*x)
    simulation_config.global_liberalis = -0.14*(x**2)-0.03
    popularity.Totalitarianism_popularity = 0.21*x + 0.2*exp(0.2*x) + 0.09
    popularity.Nationalism_popularity = 0.27*x
    popularity.Anarchism_popularity = -0.35*x - 0.11*exp(0.94*x) - 0.14


def charitytaxrelief_function(x):
    popularity.Capitalism_popularity = 0.02+(0.02*x)
    popularity.Wealthy_popularity = 0.03+(0.03*x)
    simulation_config.HighIncome = 0.02+(0.02*x)
    simulation_callout.charity = 0.1+(0.1*x)
    popularity.Liberalism_popularity = 0.12*x + 0.18
    popularity.Conservatism_popularity = 0.35*x + 0.1 + 0.09*exp(-0.04*x)
    popularity.Neoliberalism_popularity = -0.2*x
    popularity.Socialism_popularity = -0.13 - 0.18*exp(-0.42*x)


def childbenefit_function(x):
    popularity.Capitalism_popularity = -0.05-(0.02*x)
    popularity.Poor_popularity = 0.05+(0.04*x)
    simulation_callout.Equality = 0.5+(0.15*x)
    popularity.Parents_popularity = 0+(0.23*x)
    popularity.Liberalism_popularity = 0.05+(0.12*x)
    config.Parents_freq = 0.025+(0.05*x)
    simulation_config.LowIncome = 0+(0.11*x)
    simulation_callout.Population = 0+(0.1*x)
    simulation_config.global_socialism = 0.02+(0.04*x)
    simulation_callout.genderequality  = 0.02+(0.07*x)
    popularity.Socialism_popularity = 0.23*x
    popularity.Collectivism_popularity = 0.12*exp(0.53*x) + 0.16
    popularity.Progressivism_popularity = 0.34*x + 0.17
    popularity.Libertarian_Capitalism_popularity = -0.25*x - 0.1*exp(0.71*x)
    popularity.Neoliberalism_popularity = -0.38*x - 0.09 - 0.06*exp(-0.28*x)
    popularity.Conservatism_popularity = -0.06*exp(0.57*x)


def childcareprovision_function(x):
    popularity.Parents_popularity = 0.05+(0.06*x)
    popularity.Capitalism_popularity = -0.03-(0.02*x)
    simulation_config.WorkerProductivity = 0.02+(0.08*x)
    config.Parents_freq = 0.025+(0.045*x)
    popularity.Unemployed_popularity = -0.01-(0.11*x)
    simulation_callout.Population = 0+(0.1*x)
    simulation_config.global_socialism = 0.03+(0.06*x)
    simulation_callout.genderequality  = 0.04+(0.09*x)
    popularity.Socialism_popularity = 0.32*x + 0.1*exp(-0.47*x)
    popularity.Feminism_popularity = 0.35*x + 0.17*exp(-0.44*x)
    popularity.Progressivism_popularity = 0.37*x + 0.11 + 0.06*exp(-0.24*x)
    popularity.Libertarianism_popularity = -0.31*x - 0.17*exp(0.06*x) - 0.15
    popularity.Conservatism_popularity = -0.29*x - 0.13
    popularity.Neoliberalism_popularity = -0.26*x - 0.16


def citizenshiptests_function(x):
    popularity.Patriot_popularity = 0.1+(0.16*x)
    simulation_callout.RacialTension = -0.1-(0.22*x)
    config.Patriot_freq = 0.02+(0.04*x)
    simulation_callout.ImmigrationDemand = -0.05-(0.12*x)
    popularity.Liberalism_popularity = -0.09*exp(0.68*x) - 0.19
    popularity.EthnicMinorities_popularity = -0.02-(0.03*x)
    popularity.Nationalism_popularity = 0.32*x
    popularity.Conservatism_popularity = 0.36*x + 0.09 + 0.18*exp(-0.83*x)
    popularity.Totalitarianism_popularity = 0.07*exp(-0.06*x)
    popularity.Internationalism_popularity = -0.17*exp(-0.68*x)
    popularity.Progressivism_popularity = -0.19*exp(0.12*x)


def cityfarms_function(x):
    popularity.Farmers_popularity = 0.01+(0.02*x)
    config.Farmers_freq = 0+(0.04*x)
    simulation_callout.FoodPrice = -0.01-(0.04*x)
    popularity.Environmentalism_popularity = 0.19*x + 0.14 + 0.18*exp(-0.6*x)
    popularity.Progressivism_popularity = 0.31*x + 0.11
    popularity.Community_movements_popularity = 0.06*exp(-0.41*x)
    popularity.Neoliberalism_popularity = -0.32*x - 0.19*exp(0.96*x) - 0.06


def cleanenergysubsidies_function(x):

    popularity.Environmentalism_popularity = 0.2*x
    popularity.Capitalism_popularity = -0.02-(0.05*x)
    simulation_config.environment = 0.06+(0.12*x)
    simulation_config.OilDemand = -0.01-(0.11*x)
    simulation_config.co2emissions = -0.01-(0.15*x)
    popularity.Progressivism_popularity = 0.16*x + 0.08*exp(0.87*x) + 0.17
    popularity.Socialism_popularity = 0.06 + 0.09*exp(-0.97*x)
    popularity.Neoliberalism_popularity = -0.37*x - 0.15*exp(0.42*x)
    popularity.Capitalism_popularity = -0.16*x - 0.14*exp(-0.3*x)
    popularity.Industrialism_popularity = -0.14*exp(0.86*x)


def cleanfuelsubsidy_function(x):

    simulation_config.environment = 0.00+(0.09*x)*simulation_config.carusage
    popularity.Environmentalism_popularity = 0.17*exp(0.64*x)
    popularity.Motorist_popularity = 0.02+(0.02*x)
    popularity.Progressivism_popularity = 0.36*x + 0.1*exp(0.69*x)
    popularity.Nationalism_popularitys = 0.12*x + 0.12 + 0.13*exp(-0.56*x)
    popularity.Industrialism_popularity = -0.06*exp(-0.2*x)
    popularity.Neoliberalism_popularity = -0.17*x
    popularity.Libertarian = -0.2*x - 0.18 - 0.08*exp(-0.48*x)


def climatechangeadaptionfund_function(x):

    popularity.Environmentalism_popularity = 0.24*x
    config.Environmentalism_freq = 0+(0.04*x)
    popularity.Farmers_popularity = 0.1+(0.06*x)
    popularity.Unemployed_popularity = 0.0-(0.1*x)
    popularity.Internationalism_popularity = 0.34*x + 0.14*exp(-0.58*x)
    popularity.Progressivism_popularity = 0.08*exp(0.97*x)
    popularity.Neoliberalism_popularity = -0.07*exp(0.39*x) - 0.06
    popularity.Nationalism_popularitys = -0.11*x - 0.11*exp(-0.91*x)
    popularity.Libertarianism_popularity = -0.36*x - 0.08


def closeairportscompletely_function(x):
    simulation_config.airtravel = -0.6-(x**2)*0.8
    simulation_config.InternationalTrade = -0.1-(x**2)*0.24
    simulation_config.ForeignRelations = -0.04-(x**2)*0.04
    simulation_config.Tourism = -0.1-(x**2)*0.25
    popularity.Environmentalism_popularity = 0.08+(x**2)*0.2
    simulation_config.environment = 0.02+(x**2)*0.04
    simulation_config.GDP = -0.03-(x**2)*0.06
    simulation_callout.ImmigrationDemand = -0.12-(x**2)*0.26
    simulation_config.IllegalImmigration = -0.12-(x**2)*0.26
    Radical_Environmentalism_popularity = 0.15*exp(0.84*x) + 0.16
    Localism = 0.26*x + 0.16 + 0.1*exp(-0.25*x)
    popularity.Globalization_supporters_popularity = -0.12 - 0.14*exp(-0.63*x)
    popularity.Neoliberalism_popularity = -0.35*x - 0.18
    popularity.Industrialism_popularity = -0.14*exp(0.61*x)


def communitypolicing_function(x):
    popularity.Liberalism_popularity = 0.25*x + 0.13
    simulation_callout.crimerate = -0.035*(x**0.75)-0.02
    simulation_config.ViolentCrimeRate = -0.02*(x**0.8)-0.02
    simulation_callout.RacialTension = 0-(0.08*x)
    simulation_config.global_liberalis = 0+(0.05*x)
    popularity.Unemployed_popularity = 0-(0.02*x)
    popularity.Progressivism_popularity = 0.25*x
    popularity.Collectivism_popularity = 0.18*exp(0.78*x)
    popularity.Totalitarianism_popularity = -0.19*exp(0.05*x)
    popularity.Conservatism_popularity = -0.17*exp(0.18*x) - 0.07


def compulsorychurchattendance_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.28*x + 0.05*exp(-0.03*x)
    popularity.Liberalism_popularity = -0.32*x - 0.09
    popularity.EthnicMinorities_popularity = -0.02-(x*0.18)
    config.Religious_Fundamentalism_freq = 0.04+(x*0.20)
    popularity.Traditionalism_popularity = 0.36*x + 0.17
    popularity.Secularism_popularity = -0.38*x
    popularity.Individualism_popularity = -0.3*x - 0.08


def compulsoryfoodlabelling_function(x):
    simulation_config.Obesity = -0.02-(0.03*x)
    simulation_config.health = 0.02+(0.03*x)
    popularity.Capitalism_popularity = 0-(0.02*x)
    simulation_config.GDP = 0-(0.01*x)
    popularity.Environmentalism_popularity = 0.34*x + 0.06*exp(0.98*x) + 0.12
    Health_movements_popularity = 0.21*x
    popularity.Libertarianism_popularity = -0.38*x - 0.08*exp(0.2*x) - 0.06


def compulsoryforeignlanguageclasses_function(x):
    simulation_config.InternationalTrade = 0.02+(0.08*x)
    simulation_config.ForeignRelations = 0.01+(0.02*x)
    simulation_callout.RacialTension = 0-(0.015*x)
    simulation_callout.education = 0+(0.04*x)
    simulation_callout.foreigninvestment = 0+(0.1*x)
    simulation_config.Tourism = 0+(0.1*x)
    popularity.Young_popularity = 0+(0.1*x)
    popularity.Patriot_popularity = 0-(0.12*x)
    popularity.Capitalism_popularity = 0+(0.05*x)
    popularity.Internationalism_popularity = 0.11 + 0.19*exp(-0.7*x)
    popularity.Liberalism_popularity = 0.27*x + 0.13*exp(0.18*x)
    popularity.Progressivism_popularity = 0.22*x + 0.19 + 0.14*exp(-0.53*x)
    popularity.Nationalism_popularity = -0.38*x
    popularity.Conservatism_popularity = -0.16*exp(-0.21*x)


def compulsorylanguagelessons_function(x):
    simulation_callout.RacialTension = -0.05-(x*0.10)
    simulation_callout.education = 0.02+(x*0.03)
    simulation_config.ForeignRelations = 0.045+(x*0.10)
    simulation_config.InternationalTrade = 0.02+(x*0.08)
    simulation_callout.ImmigrationDemand = 0.01+(x*0.08)
    popularity.Patriot_popularity = -0.08*(x**2)
    popularity.Internationalism_popularity = 0.09*exp(-0.61*x)
    popularity.Liberalism_popularity = 0.15*x + 0.18
    popularity.Progressivism_popularity = 0.17*x + 0.15*exp(0.01*x)
    popularity.Nationalism_popularity = -0.05*exp(0.54*x) - 0.12
    popularity.Conservatism_popularity = -0.19*x - 0.08


def compulsoryschoolsports_function(x):
    simulation_config.health = 0.02+(0.025*x)
    simulation_config.Obesity = 0-(0.05*x)
    popularity.Young_popularity = -0.2-(0.03*x)
    popularity.Collectivism_popularity = 0.17*exp(0.15*x)
    Conservatism_popularity_and_Progressivism_popularity = 0.33*x + 0.09*exp(0.09*x)
    popularity.Individualism_popularity = -0.09 - 0.17*exp(-0.07*x)
    Liberalism_popularitys = -0.11*x - 0.07


def compulsoryworkfortheunemployed_function(x):
    popularity.Poor_popularity = -0.12*(x*popularity.Unemployed_popularity)
    popularity.Socialism_popularity = -0.12*(x**0.5)
    simulation_config.GDP = 0.02*(x**0.5)
    simulation_config.MiddleIncome = 0.02+(x*0.05)
    popularity.Capitalism_popularity = 0.03+(x*0.06)
    popularity.Unemployed_popularity = 0-(0.05*x)
    simulation_config.global_socialism = -0.03-(x*0.07)
    popularity.Conservatism_popularity = 0.22*x + 0.11
    popularity.Neoliberalism_popularity = 0.4*x + 0.06*exp(0.34*x) + 0.13
    popularity.Socialism_popularity = -0.32*x - 0.11
    popularity.Liberalism_popularity = -0.19 - 0.08*exp(-0.75*x)
    popularity.Progressivism_popularity = -0.07 - 0.17*exp(-0.75*x)


def congestioncharging_function(x):
    popularity.Motorist_popularity = -0.05-(0.05*x)
    simulation_config.carusage = -0.02-(0.02*x)
    TrafficCongestion = -0.06-(0.12*x)
    popularity.Environmentalism_popularity = 0.19*x + 0.14
    popularity.Urban_Progressivism_popularity = 0.37*x + 0.14
    popularity.Liberalism_popularity = 0.19*exp(-0.17*x)
    popularity.Libertarianism_popularity = -0.24*x - 0.18
    popularity.Conservatism_popularity = -0.34*x - 0.09 - 0.07*exp(-0.02*x)
    popularity.Neoliberalism_popularity = -0.14*x - 0.16


def consumerrights_function(x):
    popularity.Capitalism_popularity = 0.00-(0.06*x)
    popularity.Self_Employed_popularity = 0.00-(0.10*x)
    popularity.Liberalism_popularity = 0.22*x
    simulation_config.GDP = -0.04*(x**4)
    popularity.Progressivism_popularity = 0.37*x + 0.06
    popularity.Socialism_popularity = 0.12*x + 0.16*exp(0.03*x) + 0.16
    popularity.Neoliberalism_popularity = -0.21*x - 0.07*exp(0.26*x)
    popularity.Conservatism_popularity = -0.16*exp(-0.6*x)


def corporationtax_function(x):
    simulation_config.GDP = -0.27*(x**5)
    popularity.Socialism_popularity = 0+(0.22*x)
    popularity.Capitalism_popularity = -0.03-(0.23*x)
    popularity.Wealthy_popularity = 0-(0.2*x)
    popularity.Self_Employed_popularity = 0-(0.12*x)
    simulation_config.HighIncome = 0-(0.07*x)
    simulation_config.global_socialism = 0+(0.02*x)
    popularity.Socialism_popularity = 0.33*x + 0.1*exp(-0.32*x)
    popularity.Progressivism_popularity = 0.21*x + 0.17
    popularity.Democratic_Socialism_popularity = 0.17*x
    popularity.Neoliberalism_popularity = -0.16*x
    popularity.Libertarian_Capitalism_popularity = -0.14*x - 0.07
    popularity.Conservatism_popularity = -0.12*x - 0.13


def creationism_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.39*x
    popularity.Liberalism_popularity = -0.24*x - 0.06*exp(-0.88*x)
    config.Religious_Fundamentalism_freq = 0.35-(x*0.7)
    simulation_config.global_liberalis = -0.08+(0.16*x)
    Traditionalists = 0.4*x + 0.12*exp(0.14*x) + 0.15
    popularity.Secularism_popularity = -0.05*exp(0.4*x) - 0.14


def curfews_function(x):
    simulation_callout.crimerate = -0.03-(0.13*x)
    simulation_config.ViolentCrimeRate = -0.11*(x**0.8)-0.05
    simulation_callout.privateschools = -0.05-(0.2*x)
    popularity.Liberalism_popularity = -0.15*x - 0.08*exp(0.78*x)
    simulation_config.Terrorism = -0.1-(0.3*x)
    simulation_config.security = 0.12+(0.11*x)
    simulation_config.GDP = -0.08*(x**4)
    simulation_config.global_liberalis = -0.11*(x**3)-0.05
    popularity.Totalitarianism_popularity = 0.29*x + 0.17
    popularity.Conservatism_popularity = 0.27*x
    popularity.Nationalism_popularity = 0.16 + 0.16*exp(-0.73*x)
    popularity.Progressivism_popularity = -0.1*x - 0.2*exp(0.1*x) - 0.14
    popularity.Anarchism_popularity = -0.39*x - 0.13*exp(0.38*x)


def cyberbullyingawarenesscampaign_function(x):
    popularity.Parents_popularity = 0.02+(0.03*x)
    CyberBullying = -0.08-(0.12*x)
    popularity.Young_popularity = 0.05+(0.05*x)
    InternetCrime = -0.01-(0.06*x)
    popularity.Progressivism_popularity = 0.27*x
    popularity.Liberalism_popularity = 0.34*x + 0.06


def cyclingcampaign_function(x):


    simulation_config.health = 0.02+(0.02*x)
    simulation_config.carusage = 0-(0.03*x)
    simulation_config.railUsage = 0-(0.03*x)
    simulation_config.bususage = 0-(0.03*x)
    simulation_config.Obesity = -0.01-(0.02*x)
    popularity.Environmentalism_popularity = 0.21*x
    popularity.Urban_Progressivism_popularity = 0.17*x + 0.1
    popularity.Industrialism_popularity = -0.16*x - 0.1
    popularity.Neoliberalism_popularity = -0.29*x - 0.1


def deathpenalty_function(x):


    popularity.Patriot_popularity = 0.10+(0.02*x)
    popularity.Liberalism_popularity = -0.29*x
    simulation_config.ViolentCrimeRate = -0.06*(x**0.8)-0.03
    simulation_config.global_liberalis = -0.04-(0.04*x)
    popularity.Conservatism_popularity = 0.20+(0.14*x)
    simulation_callout.Population = -0.01-(0.02*x)
    popularity.Totalitarianism_popularity = 0.13*x
    popularity.Traditionalism_popularity = 0.18*x + 0.16
    popularity.Religious_Fundamentalism_popularity = -0.31*x - 0.2


def detentionwithouttrial_function(x):

    popularity.Patriot_popularity = 0.1+(0.1*x)
    popularity.Liberalism_popularity = -0.1 - 0.14*exp(-0.4*x)
    simulation_config.Terrorism = -0.1-(0.1*x)
    simulation_config.security = (0.05+0.05*x)
    simulation_config.ForeignRelations = 0-(0.10*x)
    simulation_config.global_liberalis = -0.11*(x**2)-0.05
    popularity.Totalitarianism_popularity = 0.19*exp(0.49*x) + 0.1
    Extreme_forms_of_Nationalism_popularity = 0.32*x + 0.18
    popularity.Conservatism_popularity = 0.35*x
    popularity.Progressivism_popularity = -0.1*exp(-0.4*x)
    Human_Rights_movements_popularity = -0.24*x - 0.13


def diplomaticservice_function(x):


    simulation_config.ForeignRelations = 0+(0.07*x)
    popularity.Internationalism_popularity = 0.16 + 0.15*exp(-0.61*x)
    popularity.Liberalism_popularity = 0.3*x + 0.19*exp(-0.36*x)
    popularity.Progressivism_popularity = 0.34*x + 0.17*exp(0.98*x)
    popularity.Isolationism_popularity = -0.3*x - 0.06 - 0.09*exp(-0.57*x)
    popularity.Nationalism_popularitys = -0.36*x
    popularity.Conservatism_popularity = -0.2*x - 0.1*exp(0.95*x) - 0.09


def disabilitybenefit_function(x):

    simulation_callout.Equality = 0.04+(0.05*x)
    popularity.Retired_popularity = 0.02+(0.02*x)
    popularity.Retired_popularity_income_fixed = 600+(6500*x)
    popularity.Socialism_popularity = 0.24*x
    popularity.Liberalism_popularity = 0.15*exp(0.09*x) + 0.15
    popularity.Progressivism_popularity = 0.12 + 0.08*exp(-0.46*x)
    popularity.Neoliberalism_popularity = -0.17*exp(0.66*x) - 0.15
    popularity.Libertarian_Capitalism_popularity = -0.16 - 0.05*exp(-0.52*x)
    popularity.Conservatism_popularity = -0.07 - 0.17*exp(-0.51*x)


def diversityquotasforcompanies_function(x):

    popularity.EthnicMinorities_popularity = 0.1+(x*0.15)
    simulation_callout.Equality = 0.05+(x*0.05)
    popularity.Capitalism_popularity = -0.04-(x*0.04)
    popularity.Self_Employed_popularity = -0.06-(x*0.04)
    simulation_callout.RacialTension = -0.075-(x*0.11)
    popularity.Liberalism_popularity = 0.05+(0.08*x)
    simulation_config.global_liberalis = 0.05*(x**2)
    popularity.Progressivism_popularity = 0.15*x + 0.18*exp(0.49*x) + 0.1
    popularity.Feminism_popularity = 0.11*exp(1.0*x) + 0.07
    popularity.Libertarianism_popularity = -0.11*x - 0.15*exp(-0.69*x)
    popularity.Conservatism_popularity = -0.4*x - 0.16 - 0.09*exp(-0.28*x)
    popularity.Neoliberalism_popularity = -0.2*x - 0.14 - 0.15*exp(-0.09*x)


def divertedprofitstax_function(x):
    simulation_config.GDP = 0.5+(0.5*x)
    popularity.Capitalism_popularity = -0.1-(0.1*x)
    popularity.Self_Employed_popularity = 0.08+(0.04*x)
    popularity.Socialism_popularity = 0.04+(0.06*x)
    simulation_config.ForeignRelations = -0.05-(0.05*x)
    popularity.Socialism_popularity = 0.34*x + 0.17*exp(0.9*x) + 0.18
    popularity.Progressivism_popularity = 0.19*x
    popularity.Nationalism_popularitys = 0.13*x
    popularity.Neoliberalism_popularity = -0.34*x
    popularity.Libertarianism_popularity = -0.19 - 0.07*exp(-1.0*x)


def driverlesscarlaws_function(x):
    popularity.Motorist_popularity = 0.02+(0.05*x)
    popularity.Commuter_popularity = 0.1+(0.1*x)
    simulation_config.Technology = 0.01+(0.014*x)
    popularity.Capitalism_popularity = 0.01+(0.01*x)
    popularity.Progressivism_popularity = 0.06 + 0.12*exp(-0.86*x)
    popularity.Technological_Optimism_popularity = 0.37*x
    popularity.Environmentalism_popularity = 0.35*x + 0.05 + 0.18*exp(-0.81*x)
    popularity.Traditionalism_popularity = -0.1*exp(0.37*x)
    popularity.Conservatism_popularity = -0.21*x - 0.06*exp(0.82*x) - 0.1


def dronestrikeact_function(x):
    popularity.Liberalism_popularity = -0.09 - 0.09*exp(-0.82*x)
    popularity.Conservatism_popularity = 0.08+(0.1*x)
    popularity.Patriot_popularity = 0+(0.25*x)
    simulation_config.Terrorism = 0-(0.2*x)
    simulation_config.ForeignRelations = -0.08-(0.12*x)
    popularity.Internationalism_popularity = -0.39*x - 0.14


def drugenforcement_function(x):

    DrugAddiction = -0.01-(0.03*x)
    simulation_config.ViolentCrimeRate = -0.01*(x**0.8)-0.02
    popularity.Conservatism_popularity = 0.08*exp(0.83*x) + 0.2
    popularity.Totalitarianism_popularity = 0.16*exp(0.12*x) + 0.14
    popularity.Traditionalism_popularity = 0.27*x
    popularity.Liberalism_popularity = -0.11*exp(-0.06*x)
    popularity.Progressivism_popularity = -0.22*x
    popularity.Libertarianism_popularity = -0.22*x - 0.07*exp(-0.03*x)


def drugtreatment_function(x):


    DrugAddiction = -0.01-(0.06*x)
    simulation_config.health = 0.02+(0.02*x)
    popularity.Progressivism_popularity = 0.08*exp(-0.66*x)
    popularity.Liberalism_popularity = 0.22*x + 0.05*exp(-0.29*x)
    popularity.Conservatism_popularity = 0.19*exp(-0.42*x)


def ecohomeregulations_function(x):

    popularity.Capitalism_popularity = 0-(0.04*x)
    popularity.Environmentalism_popularity = 0.19*exp(-0.19*x)
    simulation_config.co2emissions = 0-(0.05*x)
    config.Environmentalism_freq = 0+(0.04*x)
    simulation_callout.energyefficiency = 0.05+(0.15*x)
    popularity.Progressivism_popularity = 0.29*x + 0.18*exp(0.76*x) + 0.13
    popularity.Internationalism_popularity = 0.16*x + 0.06*exp(0.58*x) + 0.15
    popularity.Libertarianism_popularity = -0.14*exp(-0.95*x)
    popularity.Industrialism_popularity = -0.14*x
    popularity.Neoliberalism_popularity = -0.17*exp(0.19*x) - 0.16


def electriccarsinitiative_function(x):


    simulation_config.OilDemand = -0.04-(0.2*x)*simulation_config.carusage
    popularity.Motorist_popularity = 0.01+(0.03*x)
    simulation_callout.ElectricCarTransition = 0+(0.15*x)
    simulation_config.environment = 0.03+(0.12*x)*simulation_config.carusage
    config.Environmentalism_freq = 0+(0.05*x)
    popularity.Environmentalism_popularity = 0.22*x
    popularity.Progressivism_popularity = 0.1 + 0.13*exp(-0.56*x)
    popularity.Technological_Optimism_popularity = 0.24*x
    Oil_Industry = -0.19*exp(-0.55*x)
    popularity.Conservatism_popularity = -0.24*x - 0.15
    popularity.Neoliberalism_popularity = -0.16*x - 0.18*exp(0.3*x) - 0.18


def emptyhomestax_function(x):
    simulation_callout.Equality = 1.0-(0.4*x)
    popularity.Socialism_popularity = 0.00+(0.04*x)
    popularity.Young_popularity = 0.00+(0.04*x)
    popularity.Retired_popularity = -0.01-(0.06*x)
    simulation_config.Homelessness = -0.01-(0.08*x)
    popularity.Capitalism_popularity = -0.02-(0.04*x)
    popularity.Farmers_popularity = 0.02+(0.02*x)
    popularity.Wealthy_popularity = 0-(0.04*x)
    simulation_config.global_socialism = 0+(0.07*x)
    Housing_rights_activists_popularity = 0.24*x + 0.14*exp(-0.13*x)
    popularity.Socialism_popularity = 0.34*x + 0.15
    popularity.Progressivism_popularity = 0.31*x + 0.13 + 0.13*exp(-0.97*x)
    popularity.Neoliberalism_popularity = -0.2 - 0.14*exp(-0.96*x)
    popularity.Libertarianism_popularity = -0.4*x - 0.1*exp(-0.09*x)
    popularity.Conservatism_popularity = -0.07 - 0.09*exp(-0.23*x)


def enterpriseinvestmentscheme_function(x):
    popularity.Self_Employed_popularity = 0.10+(0.2*x)
    simulation_config.GDP = 0.01+(0.03*x)
    popularity.Capitalism_popularity = 0+(0.05*x)
    simulation_config.global_socialism = -0.04-(0.06*x)
    config.Self_Employed_freq = 0.02+(0.06*x)
    simulation_config.HighIncome = 0+(0.09*x)
    popularity.Neoliberalism_popularity = 0.31*x + 0.12
    popularity.Capitalism_popularity = 0.23*x + 0.2*exp(0.06*x) + 0.12
    popularity.Conservatism_popularity = 0.18*exp(0.92*x) + 0.17
    popularity.Socialism_popularity = -0.33*x - 0.11 - 0.13*exp(-0.95*x)
    popularity.Progressivism_popularity = -0.25*x


def executivetermlength_function(x):
    simulation_config.Democracy = 0.2-(x**2)*0.4
    popularity.Liberalism_popularity = 0.17 + 0.06*exp(-0.41*x)
    popularity.Progressivism_popularity = 0.23*x
    popularity.Totalitarianism_popularity = -0.29*x - 0.08 - 0.2*exp(-0.58*x)
    popularity.Conservatism_popularity = -0.15*exp(0.87*x) - 0.06


def executivetermlimit_function(x):
    simulation_config.Democracy = 0.1-(x**2)*0.2
    popularity.Liberalism_popularity = 0.1-(x**2)*0.2


def faithschoolsubsidies_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.25*x + 0.17*exp(0.17*x) + 0.05
    simulation_callout.education = 0.03+(0.04*x)
    config.Religious_Fundamentalism_freq = 0.02+(0.35*x)
    simulation_callout.RacialTension = 0.1+(0.17*x)
    Religious_Fundamentalism_popularity_income = 0+(0.06*x)
    simulation_config.global_liberalis = -0.11*(x**3)
    popularity.Conservatism_popularity = 0.24*x + 0.09
    popularity.Traditionalism_popularity = 0.1*x + 0.18
    popularity.Secularism_popularity = -0.16 - 0.16*exp(-0.8*x)
    popularity.Liberalism_popularity = -0.29*x - 0.14
    popularity.Progressivism_popularity = -0.15*x


def familyplanning_function(x):
    simulation_callout.genderequality  = 0.1+(0.15*x)
    simulation_config.health = 0+(0.08*x)
    simulation_callout.education = 0+(0.04*x)
    HIVAIDS = 0-(0.2*x)
    popularity.Liberalism_popularity = 0.1*x
    popularity.Religious_Fundamentalism_popularity = -0.16*x - 0.11*exp(0.02*x) - 0.15
    popularity.Conservatism_popularity = 0-(0.1*x)
    config.Parents_freq = -0.05-(0.15*x)
    simulation_config.global_liberalis = 0.02+(0.04*x)
    simulation_callout.Population = 0-(0.06*x)
    popularity.Feminism_popularity = 0.11*exp(0.76*x) + 0.08
    popularity.Progressivism_popularity = 0.26*x + 0.09
    popularity.Traditionalism_popularity = -0.2*x - 0.14


def femalegenitalmutilationban_function(x):
    popularity.Conservatism_popularity = -0.03-(0.03*x)
    popularity.Liberalism_popularity = 0.23*x + 0.1
    simulation_callout.genderequality  = 0.05+(0.02*x)
    popularity.Religious_Fundamentalism_popularity = -0.12*(x**1.25)
    popularity.Feminism_popularity = 0.15*exp(0.89*x)
    popularity.Human_Rights_Advocacy_popularity = 0.14*x + 0.18*exp(0.51*x) + 0.07
    popularity.Traditionalism_popularity = -0.31*x


def financialtransactionstax_function(x):
    simulation_config.GDP = -0.07*(x**3)
    popularity.Socialism_popularity = 0+(0.05*x)
    popularity.Capitalism_popularity = -0.02-(0.08*x)
    popularity.Wealthy_popularity = 0-(0.23*x)
    simulation_config.HighIncome = 0-(0.02*x)
    simulation_config.global_socialism = 0+(0.01*x)
    popularity.Progressivism_popularity = 0.29*x + 0.2*exp(0.5*x) + 0.07
    popularity.Socialism_popularity = 0.26*x + 0.12*exp(0.57*x)
    popularity.Liberalism_popularity = 0.3*x
    popularity.Neoliberalism_popularity = -0.16*x - 0.17*exp(0.81*x) - 0.11
    popularity.Libertarian_Capitalism_popularity = -0.25*x
    popularity.Free_Market_Advocates_popularity = -0.13*x - 0.18 - 0.06*exp(-0.69*x)


def flagsoneverystreetcorner_function(x):
    popularity.Patriot_popularity = 0.03+(x*0.21)
    simulation_config.ForeignRelations = 0-(x*0.04)**2
    config.Patriot_freq = 0.17*(x**2)+0.1
    simulation_callout.RacialTension = 0.01+(0.03*x)
    popularity.EthnicMinorities_popularity = -0.01-(0.02*x)
    popularity.Nationalism_popularity = 0.36*x
    popularity.Conservatism_popularity = 0.16*x + 0.12*exp(0.14*x) + 0.16
    popularity.Patriot_popularityic_movements_popularity = 0.14*exp(0.32*x) + 0.18
    popularity.Internationalism_popularity = -0.1*x
    popularity.Liberalism_popularity = -0.36*x - 0.05 - 0.09*exp(-0.74*x)
    popularity.Anarchism_popularity = -0.05*exp(0.57*x)


def flattax_function(x):
    simulation_config.GDP = 0.5+(0.5*x)
    popularity.Socialism_popularity = 0-(0.25*x)
    popularity.Capitalism_popularity = 0-(0.12*x)
    simulation_callout.Equality = 0-(0.3*x)
    simulation_config.MiddleIncome = 0-(0.80*x)
    popularity.Wealthy_popularity = -0.2*(x**11)
    simulation_config.LowIncome = 0-(0.16*x)
    simulation_config.MiddleIncome = 0-(0.14*x)
    simulation_config.HighIncome = 0-(0.06*x)
    popularity.Poor_popularity = -0.1-(x**2)*1.2
    popularity.Libertarianism_popularity = 0.2*exp(-0.35*x)
    popularity.Neoliberalism_popularity = 0.07*exp(0.38*x)
    popularity.Conservatism_popularity = 0.15*x + 0.16*exp(-0.21*x)
    popularity.Progressivism_popularity = -0.15 - 0.06*exp(-0.84*x)
    popularity.Socialism_popularity = -0.27*x - 0.1*exp(0.61*x)
    popularity.Democratic_Socialism_popularity = -0.14*x - 0.12


def foodstamps_function(x):
    simulation_config.health = 0.02+(0.08*x)*config.Poor_perc
    simulation_config.LowIncome = 0.03+(0.04*x)
    popularity.Poor_popularity = 0.04+(0.15*x)
    simulation_config.PovertyRate = -0.03-(0.12*x)
    popularity.Socialism_popularity = 0.02+0.08*x
    popularity.Farmers_popularity = 0+(0.03*x)
    simulation_callout.Equality = 0.02+(0.08*x)
    popularity.Socialism_popularity = 0.2*exp(0.49*x) + 0.2
    popularity.Progressivism_popularity = 0.12*x + 0.2 + 0.17*exp(-0.9*x)
    popularity.Liberalism_popularity = 0.34*x + 0.14 + 0.12*exp(-0.27*x)
    popularity.Libertarianism_popularity = -0.36*x
    popularity.Neoliberalism_popularity = -0.18*x - 0.14*exp(0.55*x) - 0.12
    popularity.Conservatism_popularity = -0.3*x


def foodstandards_function(x):
    popularity.Farmers_popularity = -0.02-(0.08*x)
    popularity.Liberalism_popularity = 0.01+(0.04*x)
    simulation_config.health = 0.01+(0.03*x)
    simulation_config.Obesity = -0.04-(0.06*x)
    popularity.Progressivism_popularity = 0.22*x
    popularity.Environmentalism_popularity = 0.06 + 0.11*exp(-0.14*x)
    popularity.Neoliberalism_popularity = -0.36*x - 0.07
    popularity.Libertarianism_popularity = -0.29*x - 0.19*exp(0.58*x) - 0.17


def forcepolitical_military_religiousoath_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.06+(x*0.11)
    simulation_callout.RacialTension = 0.05+(x**2)*0.15
    simulation_config.ForeignRelations = -0.02-(x**2)*0.08
    config.Religious_Fundamentalism_freq = 0.02+(x**2)*0.21
    popularity.Liberalism_popularity = -0.15*exp(0.78*x) - 0.19
    popularity.Totalitarianism_popularity = 0.27*x
    popularity.Nationalism_popularity = 0.38*x + 0.16*exp(-0.8*x)
    popularity.Secularism_popularity = -0.13*exp(0.58*x)
    popularity.Individualism_popularity = -0.31*x - 0.08


def foreignaid_function(x):
    popularity.Socialism_popularity = 0.02+(0.04*x)
    popularity.Patriot_popularity = -0.02-(0.28*x)
    popularity.Liberalism_popularity = 0.15*x + 0.08 + 0.07*exp(-0.43*x)
    simulation_config.ForeignRelations = 0+(0.6*x)
    popularity.EthnicMinorities_popularity = 0.02+(0.20*x)
    popularity.Internationalism_popularity = 0.14*x + 0.12
    popularity.Progressivism_popularity = 0.3*x + 0.19*exp(0.25*x) + 0.13
    popularity.Nationalism_popularity = -0.13*exp(-0.28*x)
    popularity.Conservatism_popularity = -0.27*x - 0.08
    popularity.Isolationism_popularity = -0.16*x - 0.15*exp(0.11*x)


def foreigninvestmentrestrictions_function(x):
    simulation_callout.foreigninvestment = 0-(1*x)
    simulation_config.ForeignRelations = 0-(0.2*x)
    popularity.Capitalism_popularity = 0-(0.2*x)
    popularity.Patriot_popularity = 0+(0.1*x)
    popularity.Protectionism_popularity = 0.37*x + 0.17 + 0.1*exp(-0.13*x)
    popularity.Nationalism_popularity = 0.28*x + 0.1*exp(0.35*x) + 0.05
    popularity.Populism_popularity = 0.11*x + 0.18*exp(0.25*x)
    popularity.Globalization_supporters_popularity = -0.13*x
    popularity.Neoliberalism_popularity = -0.32*x - 0.17*exp(0.92*x) - 0.05
    popularity.Capitalism_popularity_Advocates = -0.28*x - 0.06*exp(0.21*x) - 0.14


def foreigninvestortaxbreaks_function(x):
    popularity.Patriot_popularity = -0.1-(0.14*x)
    simulation_callout.BusinessConfidence = 0.05+(0.05*x)
    simulation_config.HighIncome = 0.12*(x**2)
    simulation_config.ForeignRelations = 0.05+(0.05*x)
    simulation_callout.foreigninvestment = 0.08+(0.13*x)
    popularity.Neoliberalism_popularity = 0.23*x + 0.2
    popularity.Globalization_supporters_popularity = 0.08*exp(-0.72*x)
    popularity.Capitalism_popularity_Advocates = 0.29*x + 0.09*exp(0.07*x)
    popularity.Protectionism_popularity = -0.38*x - 0.09
    popularity.Nationalism_popularity = -0.13*x - 0.14*exp(0.45*x) - 0.07
    popularity.Populism_popularity = -0.35*x - 0.16


def freebuspasses_function(x):
    popularity.Retired_popularity = 0.01+(0.06*x)
    simulation_config.bususage = config.Retired_perc*(0.5*x)
    popularity.Retired_popularity_income_fixed = 250+(2000*x)
    popularity.Socialism_popularity = 0.37*x
    popularity.Environmentalism_popularity = 0.13 + 0.13*exp(-0.39*x)
    popularity.Progressivism_popularity = 0.14*x
    popularity.Neoliberalism_popularity = -0.31*x
    popularity.Libertarianism_popularity = -0.18*exp(-0.56*x)



def freeeyetests_function(x):
    popularity.Poor_popularity = 0.05+(0.05*x)
    popularity.Capitalism_popularity = 0-(0.05*x)
    popularity.Socialism_popularity = 0.01+(0.03*x)
    simulation_config.PovertyRate = -0.03-(0.03*x)
    simulation_config.LowIncome_fixed = 50+(200*x)
    popularity.Retired_popularity = 0.01+(0.03*x)
    simulation_config.health = 0.0+(0.02*x)
    popularity.Socialism_popularity = 0.28*x + 0.06
    popularity.Liberalism_popularity = 0.26*x + 0.05*exp(0.4*x)
    popularity.Progressivism_popularity = 0.16*exp(-0.69*x)
    popularity.Neoliberalism_popularity = -0.22*x
    popularity.Libertarianism_popularity = -0.14*x
    popularity.Conservatism_popularity = -0.36*x - 0.07*exp(0.15*x) - 0.07


def freeparentingclasses_function(x):
    popularity.Parents_popularity = 0.05+(0.04*x)
    config.Parents_freq = 0+(0.03*x)
    simulation_callout.Population = 0.02+(0.04*x)
    simulation_callout.genderequality  = 0.03+(0.06*x)
    popularity.Progressivism_popularity = 0.1*exp(0.21*x)
    popularity.Liberalism_popularity = 0.3*x + 0.14
    popularity.Social_Welfare_Advocates_popularity = 0.36*x + 0.06*exp(0.96*x) + 0.11
    popularity.Libertarianism_popularity = -0.31*x - 0.15*exp(0.43*x) - 0.11
    popularity.Conservatism_popularity = -0.37*x - 0.06
    popularity.Neoliberalism_popularity = -0.17*exp(0.94*x)


def freeschoolmeals_function(x):
    popularity.Poor_popularity = 0.00+(0.05*x)
    simulation_config.health = 0.00+(0.07*x)
    popularity.Socialism_popularity = 0.01+(0.03*x)
    simulation_config.PovertyRate = -0.03-(0.055*x)
    popularity.Parents_popularity = 0.01+(0.03*x)
    config.Parents_freq = 0.01+(0.02*x)
    simulation_config.LowIncome_fixed = 50+(150*x)
    simulation_config.Obesity = 0-(0.06*x)
    popularity.Socialism_popularity = 0.37*x + 0.13*exp(0.32*x)
    popularity.Progressivism_popularity = 0.25*x + 0.11
    Educational_Equity_Advocates_popularity = 0.09*exp(0.06*x) + 0.09
    popularity.Neoliberalism_popularity = -0.26*x - 0.18*exp(0.79*x) - 0.15
    popularity.Libertarianism_popularity = -0.16*x - 0.19
    popularity.Fiscal_Conservatism_popularity = -0.3*x - 0.15


def frequentflyertax_function(x):
    simulation_config.airtravel = 0-(0.2*x)
    popularity.Socialism_popularity = 0.00+(0.04*x)
    popularity.Environmentalism_popularity = 0.26*x + 0.1*exp(-0.25*x)
    simulation_config.GDP = 0.00-(0.02*x)
    popularity.Wealthy_popularity = 0-(0.04*x)
    popularity.Progressivism_popularity = 0.28
    popularity.Global_Climate_Change_Advocates_popularity = 0.2*exp(0.36*x)
    popularity.Neoliberalism_popularity = -0.17*exp(0.89*x) - 0.14
    popularity.Libertarianism_popularity = -0.22*x - 0.16*exp(0.6*x) - 0.16


def fuelefficiency_function(x):
    simulation_config.OilDemand = -0.05-(0.13*x)*simulation_config.carusage
    simulation_config.carusage = 0.02+(0.06*x)
    popularity.Environmentalism_popularity = 0.22*x
    popularity.Capitalism_popularity = -0.01-(0.02*x)
    simulation_config.co2emissions = 0-(0.07*x)
    popularity.Progressivism_popularity = 0.24*x
    popularity.Liberalism_popularity = 0.06 + 0.05*exp(-0.49*x)
    popularity.Conservatism_popularity = -0.1*x
    popularity.Libertarianism_popularity = -0.19*exp(0.9*x)


def gambling_function(x):
    popularity.Liberalism_popularity = 0.00+(0.08*x)
    popularity.Religious_Fundamentalism_popularity = 0.00-(0.15*x)
    simulation_config.GDP = 0.00+(0.04*x)
    popularity.Unemployed_popularity = 0.00-(0.03*x)
    popularity.Capitalism_popularity = 0.01+(0.04*x)
    simulation_config.Tourism = 0.04*(x**0.8)
    popularity.Libertarianism_popularity = 0.34*x + 0.11*exp(0.18*x)
    popularity.Free_Market_Advocates_popularity = 0.17*exp(-0.91*x)
    popularity.Conservatism_popularity = -0.11 - 0.18*exp(-0.14*x)
    popularity.Progressivism_popularity = -0.15*exp(0.92*x)


def gamehunting_function(x):
    EndangeredSpecies = 0+(1.0*x)
    simulation_config.environment = 0+(0.05*x)
    popularity.Environmentalism_popularity = -0.13*x - 0.17*exp(0.68*x)
    popularity.Poor_popularity = 0-(0.1*x)
    popularity.Farmers_popularity = 0-(0.12*x)
    simulation_config.Tourism = 0-(0.05*x)
    popularity.Libertarianism_popularity = 0.26*x + 0.16*exp(0.16*x) + 0.11
    popularity.Conservatism_popularity = 0.13*x + 0.2
    popularity.Traditionalism_popularity = 0.15*exp(0.06*x) + 0.19
    popularity.Progressivism_popularity = -0.14*x


def gatedcommunities_function(x):
    simulation_callout.crimerate = -0.04*(x**0.75)
    popularity.Conservatism_popularity = 0.00+(0.40*x)
    simulation_callout.Equality = 0.00-(0.11*x)
    simulation_config.global_liberalis = -0.02-(0.11*x)
    popularity.Wealthy_popularity = 0.00+(0.42*x)
    popularity.Neoliberalism_popularity = 0.08*exp(0.42*x)
    popularity.Individualism_popularity = 0.12*exp(-0.02*x)
    popularity.Socialism_popularity = -0.13*exp(-0.16*x)
    popularity.Community_movements_popularity = -0.3*x
    popularity.Liberalism_popularity = -0.09*exp(0.04*x)


def gaymarriage_function(x):
    popularity.Religious_Fundamentalism_popularity = -0.23*x
    popularity.Liberalism_popularity = 0.18*x + 0.15 + 0.17*exp(-0.9*x)
    popularity.Young_popularity = 0.05+(0.05*x)
    simulation_config.global_liberalis = 0+(0.04*x)
    MarriedTaxAllowance_cost = 0.07*(x**1.5)
    popularity.Progressivism_popularity = 0.17*exp(-0.76*x)
    popularity.Human_Rights_Advocacy_popularity = 0.3*x + 0.08*exp(0.53*x)
    popularity.Conservatism_popularity = -0.19*x - 0.17*exp(-0.18*x)
    popularity.Traditionalism_popularity = -0.15*exp(0.02*x) - 0.19


def genderdiscriminationact_function(x):
    simulation_config.Democracy = 0.1+(0.1*x)
    simulation_callout.genderequality  = 0+(0.3*x)
    popularity.Liberalism_popularity = 0.15*exp(0.76*x)
    popularity.Conservatism_popularity = -0.1-(0.1*x)
    simulation_config.global_liberalis = 0.08*(x**3)+0.02
    popularity.Feminism_popularity = 0.31*x + 0.17*exp(0.79*x)
    popularity.Progressivism_popularity = 0.23*x + 0.12*exp(-0.91*x)
    popularity.Traditionalism_popularity = -0.16*x - 0.12*exp(-0.05*x)
    Male_Supremacy_Advocates_popularity_Advocates_popularity = -0.11 - 0.15*exp(-0.62*x)


def gendertransition_function(x):
    popularity.Religious_Fundamentalism_popularity = -0.11*x
    popularity.Conservatism_popularity = -0.15*exp(-0.68*x)
    popularity.Liberalism_popularity = 0.28*x + 0.15
    simulation_config.HealthcareDemand = 0.02*(x**4)
    simulation_config.global_liberalis = 0.1*(x**2)+0.02
    popularity.Feminism_popularity = 0.19*x + 0.06 + 0.14*exp(-0.59*x)
    popularity.Progressivism_popularity = 0.3*x + 0.15 + 0.14*exp(-0.17*x)
    popularity.Traditionalism_popularity = -0.19 - 0.07*exp(-0.39*x)


def generalmediacensorship_function(x):
    popularity.Liberalism_popularity = -0.33*x - 0.17
    simulation_config.Terrorism = 0-(x*0.07)
    simulation_config.Corruption = 0.1+(0.17*x)
    simulation_config.global_liberalis = 0-(0.07*x)
    popularity.Totalitarianism_popularity = 0.22*x + 0.19*exp(0.18*x)
    popularity.Conservatism_popularity = 0.2*x + 0.11
    simulation_config.Democracy_Advocates = -0.18*x - 0.1
    simulation_config.Free_Speech_Advocates_popularity = -0.11*exp(-0.52*x)


def governmentsubsidiesforunions_function(x):
    popularity.Capitalism_popularity = 0-(0.12*x)
    simulation_config.global_socialism = 0.024+(0.058*x)
    simulation_config.Wages = 0+(0.04*x)
    popularity.Socialism_popularity = 0.12*x + 0.11 + 0.13*exp(-0.82*x)
    popularity.Progressivism_popularity = 0.1*exp(-0.18*x)
    popularity.Labor_Movements_popularity = 0.12*x + 0.1 + 0.15*exp(-0.18*x)
    popularity.Neoliberalism_popularity = -0.11*x - 0.2
    popularity.Libertarianism_popularity = -0.2 - 0.15*exp(-0.81*x)
    popularity.Conservatism_popularity = -0.18*exp(0.32*x)


def graduatetax_function(x):
    simulation_callout.education = -0.06*(x**2)
    popularity.Young_popularity = -0.2-(0.1*x)
    popularity.Capitalism_popularity = 0.02+(0.01*x)
    popularity.Socialism_popularity = -0.05-(0.02*x)
    simulation_config.MiddleIncome = 0-(0.04*x)
    popularity.Progressivism_popularity = 0.08*exp(0.97*x)
    popularity.Socialism_popularity = 0.06 + 0.15*exp(-0.62*x)
    popularity.Neoliberalism_popularity = -0.32*x - 0.13 - 0.08*exp(-0.37*x)
    popularity.Libertarianism_popularity = -0.11 - 0.19*exp(-0.96*x)
    popularity.Conservatism_popularity = -0.19*exp(0.92*x)


def greenelectronicsinitiative_function(x):
    popularity.Environmentalism_popularity = 0.15*x + 0.05*exp(0.58*x)
    simulation_config.co2emissions = -0.06*(x**0.6)
    simulation_callout.energyefficiency = 0.+(0.08*x)
    simulation_config.Pollution = 0-(0.05*x)
    popularity.Capitalism_popularity = 0-(0.05*x)
    popularity.Progressivism_popularity = 0.22*x
    simulation_config.Technology_Optimists = 0.25*x + 0.06
    popularity.Neoliberalism_popularity = -0.18*x - 0.2*exp(0.96*x) - 0.11


def handgunlaws_function(x):
    simulation_config.ViolentCrimeRate = 0.16-(0.32*x)
    simulation_callout.crimerate = -0.1+(0.2*x)
    popularity.Liberalism_popularity = 0.05 + 0.17*exp(-0.38*x)
    popularity.Patriot_popularity = 0.20-(0.40*x)
    popularity.Parents_popularity = -0.15+(0.30*x)
    simulation_config.global_liberalis = 0-(0.05*x)
    simulation_config.security = 0.08*(x**4)
    popularity.Progressivism_popularity = 0.17*x + 0.13*exp(-0.8*x)
    popularity.Conservatism_popularity = 0.3*x
    popularity.Libertarianism_popularity = -0.18*exp(0.25*x) - 0.1
    popularity.Gun_Rights_Advocates_popularity = -0.17*exp(-0.82*x)


def healthcarevouchers_function(x):
    simulation_callout.Equality = 0.1*(x**3)
    simulation_config.PovertyRate = -0.1*(x*3)
    simulation_config.global_socialism = -0.01-(0.12*x)
    simulation_config.PrivateHealthcare = 0+(0.6*x)
    simulation_config.privateschools_income_fixed = 150+(1550*x)
    popularity.Capitalism_popularity = 0.02+(0.05*x)
    popularity.Neoliberalism_popularity = 0.09*exp(-0.36*x)
    popularity.Conservatism_popularity = 0.36*x + 0.12 + 0.2*exp(-0.04*x)
    popularity.Market_Reform_Advocates_popularity = 0.19*x + 0.13*exp(-0.78*x)
    popularity.Socialism_popularity = -0.2*x
    popularity.Progressivism_popularity = -0.37*x - 0.2*exp(-0.43*x)
    popularity.Universal_Healthcare_Advocates_popularity = -0.28*x - 0.12*exp(-0.84*x)


def healthfoodsubsidies_function(x):
    simulation_config.health = 0.03+(0.06*x)
    simulation_callout.FoodPrice = -0.03-(0.05*x)
    popularity.Environmentalism_popularity = 0.27*x + 0.2*exp(0.95*x) + 0.05
    popularity.Progressivism_popularity = 0.1*exp(0.92*x)
    popularity.Public_Health_Advocacy = 0.18*x
    popularity.Neoliberalism_popularity = -0.08*exp(0.26*x)


def healthtaxcredits_function(x):
    simulation_config.PrivateHealthcare = 0+(0.3*x)
    simulation_config.MiddleIncome = 0+(0.08*x)
    simulation_config.HighIncome = 0+(0.06*x)
    popularity.Wealthy_popularity = 0.02+(0.06*x)
    simulation_config.MiddleIncome = 0.04+(0.06*x)
    popularity.Socialism_popularity = -0.01-(0.05*x)
    popularity.Poor_popularity = -0.01-(0.05*x)
    popularity.Capitalism_popularity = 0.02+(0.04*x)
    popularity.Neoliberalism_popularity = 0.12*x + 0.09*exp(-0.26*x)
    popularity.Conservatism_popularity = 0.3*x + 0.17
    popularity.Market_Reform_Advocates_popularity = 0.33*x + 0.2*exp(0.89*x)
    popularity.Progressivism_popularity = -0.15*x - 0.17 - 0.12*exp(-0.98*x)
    popularity.Socialism_popularity = -0.25*x
    popularity.Universal_Healthcare_Advocates_popularity = -0.18*exp(0.85*x) - 0.14


def healthyeatingcampaign_function(x):
    simulation_config.health = 0.01+(0.04*x)
    simulation_config.Obesity = -0.03-(0.05*x)
    popularity.Public_Health_Advocacy = 0.3*x + 0.16
    popularity.Progressivism_popularity = 0.28*x + 0.19
    popularity.Environmentalism_popularity = 0.15*x + 0.13 + 0.06*exp(-0.76*x)
    popularity.Libertarianism_popularity = -0.07*exp(-0.3*x)


def helicoptermoney_function(x):
    simulation_callout.Inflation = 0.78*(x**4)
    popularity.Socialism_popularity = 0.08+(0.08*x)
    simulation_config.PovertyRate = -0.08-(0.08*x)
    simulation_config.GDP = 0.05+(0.06*x)
    popularity.Poor_popularity = 0.12+(0.08*x)
    simulation_config.LowIncome = 0.1+(0.05*x)
    simulation_callout.currencystrength = -0.08*(x**2)
    popularity.Social_Welfare_Advocates_popularity = 0.27*x + 0.11
    popularity.Populism_popularity = 0.11*exp(0.03*x) + 0.18
    popularity.Neoliberalism_popularity = -0.4*x - 0.15*exp(0.27*x)
    popularity.Fiscal_Conservatism_popularity = -0.13*x - 0.19
    popularity.Libertarianism_popularity = -0.15 - 0.15*exp(-0.84*x)


def humancloningresearchgrants_function(x):
    popularity.Religious_Fundamentalism_popularity = -0.28*x - 0.14
    popularity.Conservatism_popularity = -0.12-(0.14*x)
    popularity.Wealthy_popularity = 0.1+(0.13*x)
    simulation_config.health = -0.01-(0.02*x)
    simulation_config.Technology = 0.02+(0.03*x)
    popularity.Scientific_Progressivism_popularity = 0.17 + 0.18*exp(-0.25*x)
    popularity.Liberalism_popularity = 0.39*x + 0.07*exp(0.11*x)
    popularity.Technological_Optimism_popularity = 0.32*x + 0.17*exp(-0.58*x)
    popularity.Ethical_Conservatism_popularity = -0.14*x - 0.11
    popularity.Progressivism_popularity = -0.24*x


def hybridcarsinitiative_function(x):
    simulation_config.OilDemand = -0.02-(0.12*x)*simulation_config.carusage
    popularity.Environmentalism_popularity = 0.26*x + 0.19
    popularity.Motorist_popularity = 0.02+(0.02*x)
    simulation_config.carusage = 0.01+(0.02*x)
    simulation_config.environment = 0.02+(0.12*x)*simulation_config.carusage
    config.Environmentalism_freq = 0+(0.05*x)
    simulation_config.HighIncome = 0+(0.02*x)
    popularity.Progressivism_popularity = 0.07*exp(0.81*x)
    simulation_config.Technology_Optimists = 0.17*exp(-0.17*x)
    Oil_Industry = -0.39*x - 0.11 - 0.12*exp(-0.91*x)
    popularity.Conservatism_popularity = -0.34*x
    popularity.Neoliberalism_popularity = -0.39*x - 0.09*exp(0.13*x) - 0.08


def idcards_function(x):
    popularity.Liberalism_popularity = -0.2*x - 0.13*exp(0.53*x) - 0.06
    simulation_callout.crimerate = -0.065*(x**0.75)
    simulation_config.ViolentCrimeRate = -0.04*(x**0.7)
    popularity.Conservatism_popularity = 0.10+(0.14*x)
    simulation_config.security = 0+(0.15*x)
    popularity.Patriot_popularity = 0.11+(0.07*x)
    simulation_config.global_liberalis = -0.09*(x**2)-0.04
    popularity.Privacy_advocates_popularity = -0.19*exp(-0.57*x)
    popularity.Libertarianism_popularity = -0.17*x


def importtarrifs_function(x):
    simulation_config.GDP = 0.25+(0.75*x)
    popularity.Capitalism_popularity = 0.10-(0.10*x)
    popularity.Unemployed_popularity = 0.00-(0.10*x)
    popularity.Patriot_popularity = 0.10+(0.10*x)
    simulation_config.ForeignRelations = 0-(0.16*x)
    simulation_config.InternationalTrade = -0.05-(0.28*x)
    popularity.Protectionism_popularity = 0.13*x + 0.17
    popularity.Nationalism_popularity = 0.11*x + 0.14*exp(-0.43*x)
    popularity.Populism_popularity = 0.36*x + 0.15
    popularity.Capitalism_popularity_Advocates = -0.32*x - 0.13 - 0.19*exp(-0.39*x)
    popularity.Globalization_supporters_popularity = -0.08*exp(0.79*x) - 0.1
    popularity.Neoliberalism_popularity = -0.25*x - 0.07 - 0.1*exp(-0.26*x)


def incometax_function(x):
    simulation_config.GDP = -0.16*(x**5)
    popularity.Socialism_popularity = 0.112*(x**3)
    popularity.Capitalism_popularity = 0-(0.27*x)
    simulation_callout.Equality = 0+(0.3*x)
    simulation_config.MiddleIncome = -1.33*(x**1.37)
    popularity.Wealthy_popularity = 0-(x**11)
    simulation_config.LowIncome = -0.03-(x**2)*0.1
    simulation_config.MiddleIncome = 0-(0.14*x)
    simulation_config.HighIncome = 0-(0.15*x)
    popularity.Progressivism_popularity = 0.34*x + 0.09
    popularity.Socialism_popularity = 0.12*x + 0.08*exp(-0.21*x)
    popularity.Democratic_Socialism_popularity = 0.3*x
    popularity.Libertarianism_popularity = -0.38*x - 0.18*exp(0.46*x)
    popularity.Neoliberalism_popularity = -0.34*x - 0.08*exp(0.45*x) - 0.09


def inheritancetax_function(x):
    popularity.Wealthy_popularity = -0.1-(0.25*x)
    popularity.Socialism_popularity = 0+(0.16*x)
    simulation_callout.Equality = 0.1+(0.3*x)
    popularity.Conservatism_popularity = -0.19*exp(0.01*x) - 0.1
    simulation_config.MiddleIncome = 0-(0.18*x)
    simulation_config.HighIncome = 0-(0.07*x)
    popularity.Retired_popularity = 0-(0.22*x)
    simulation_config.global_socialism = 0+(0.1*x)
    popularity.Progressivism_popularity = 0.35*x
    popularity.Socialism_popularity = 0.22*x + 0.1*exp(0.95*x)
    Redistribution_Advocates_popularity = 0.2*x + 0.1
    popularity.Neoliberalism_popularity = -0.19*x - 0.17*exp(0.32*x) - 0.14
    Wealth_Preservation_Advocates = -0.31*x - 0.15


def intellectualpropertyrights_function(x):
    simulation_config.ForeignRelations = 0+(0.05*x)
    simulation_callout.foreigninvestment = 0+(0.1*x)
    simulation_config.Technology = 0+(0.18*x)
    popularity.Poor_popularity = 0-(0.05*x)
    popularity.Capitalism_popularity = 0+(0.05*x)
    popularity.Young_popularity = -0.10*(x**4)
    simulation_config.global_socialism = 0.04-(0.05*x)
    Creators = 0.12 + 0.11*exp(-0.92*x)
    popularity.Capitalism_popularity = 0.16*x + 0.16*exp(0.71*x) + 0.2
    popularity.Neoliberalism_popularity = 0.36*x + 0.1 + 0.15*exp(-0.66*x)
    Open_Source_Advocates_popularity = -0.06*exp(0.17*x)
    popularity.Progressivism_popularity = -0.12*x - 0.13*exp(0.4*x) - 0.17
    Digital_Rights_Activists = -0.34*x


def intelligenceservices_function(x):
    popularity.Liberalism_popularity = 0-(0.18*x)
    simulation_callout.crimerate = -0.051*(x**0.75)
    popularity.Patriot_popularity = 0+(0.05*x)
    simulation_config.Terrorism = 0.2-(0.3*x)
    simulation_config.security = 0+(0.4*x)
    popularity.Conservatism_popularity = 0.21*x + 0.08 + 0.06*exp(-0.94*x)
    popularity.Privacy_advocates_popularity = -0.14*x - 0.12*exp(0.98*x)
    popularity.Civil_Liberties_Advocates_popularity = -0.09*exp(-0.27*x)


def internationalfusionresearchproject_function(x):
    popularity.Environmentalism_popularity = -0.12-(0.1*x)
    simulation_callout.energyefficiency = 0.0+(0.04*x)
    simulation_config.ForeignRelations = 0.05+(0.1*x)
    simulation_config.Technology = 0.03+(0.05*x)
    simulation_config.OilDemand = -0.24*(x**2)
    popularity.Unemployed_popularity = -0.02-(0.10*x)
    simulation_callout.privateenergy = 0.02+(0.06*x)
    popularity.Environmentalism_popularitys = 0.14*exp(-0.71*x)
    popularity.International_Cooperation_Advocates_popularity = 0.08*exp(0.52*x)
    popularity.Nationalists_popularity = -0.25*x - 0.1*exp(0.01*x) - 0.14
    popularity.Fiscal_Conservatism_popularity = -0.11*exp(0.51*x)


def internetcensorship_function(x):
    popularity.Conservatism_popularity = 0.10+(0.15*x)
    simulation_config.Technology = 0.00-(0.13*x)
    popularity.Liberalism_popularity = -0.18*x - 0.11*exp(0.62*x)
    popularity.Young_popularity = -0.08-(0.25*x)
    simulation_config.global_liberalis = -0.05*(x**2)-0.02
    simulation_config.security = 0+(0.05*x)
    simulation_config.Free_Speech_Advocates_popularity = -0.28*x - 0.05
    Digital_Rights_Activists = -0.12*exp(0.11*x)


def internetcurrencytaxation_function(x):
    simulation_config.GDP = 0.5+(0.5*x)
    simulation_config.TaxEvasion = 1.0-(0.2*x)
    popularity.Capitalism_popularity = 0-(0.05*x)
    simulation_callout.internetcurrencyadoption = 0.0+(1.0*x)
    popularity.Liberalism_popularity = -0.1*(x**5)-0.02
    popularity.Self_Employed_popularity = -0.03-(0.04*x)
    popularity.Fiscal_Conservatism_popularity = 0.05*exp(-0.42*x)
    popularity.Regulation_Advocates_popularity = 0.27*x + 0.36
    popularity.Cryptocurrency_Advocates_popularity = -0.36*x - 0.13*exp(-0.85*x)
    popularity.Libertarianism_popularity = -0.18*exp(0.56*x) - 0.16
    popularity.Digital_Freedom_Advocates_popularity = -0.25*x - 0.18


def internettax_function(x):
    simulation_config.GDP = 0.00-(0.07*x)
    simulation_config.Technology = -0.11-(0.25*x)
    simulation_config.MiddleIncome = 0-(0.02*x)
    popularity.Conservatism_popularity = 0.05*exp(0.97*x)
    popularity.Digital_Economy_Advocates_popularity = -0.35*x - 0.09*exp(-0.51*x)
    popularity.Free_Internet_Advocates_popularity = -0.17*exp(-0.95*x)
    popularity.Liberalism_popularity = -0.31*x - 0.19


def judiciaryindependence_function(x):
    simulation_config.Democracy = 0.25-(x+1.25)**-3
    simulation_config.Corruption = 0.05-(x**6)*0.15
    popularity.Liberalism_popularity = 0.27*x + 0.15
    simulation_config.global_liberalis = 0.06*(x**2)-0.02
    simulation_config.Democracy_Advocates = 0.14*x
    popularity.Totalitarianism_popularity = -0.4*x - 0.2 - 0.08*exp(-0.55*x)
    popularity.Conservatism_popularity = -0.16*x - 0.2


def junkfoodtax_function(x):
    simulation_config.health = 0.02+(0.06*x)
    popularity.Young_popularity = -0.02-(0.04*x)
    simulation_config.privateschools_income_fixed = -5-(25*x)
    simulation_config.PovertyRate = 0.02+(0.02*x)
    popularity.Public_Health_Advocacy = 0.39*x + 0.06*exp(0.47*x)
    popularity.Environmentalism_popularity = 0.11*exp(-0.16*x)
    popularity.Progressivism_popularity = 0.14*x

    popularity.Libertarianism_popularity = -0.4*x - 0.14*exp(0.03*x) - 0.1
    popularity.Conservatism_popularity = -0.16*exp(0.54*x) - 0.06


def jurytrial_function(x):
    popularity.Liberalism_popularity = 0.34*x + 0.19*exp(0.84*x) + 0.07
    simulation_config.Corruption = -0.02-(0.06*x)
    simulation_config.global_liberalis = 0.01+(0.03*x)
    simulation_config.Democracy_Advocates = 0.14*x + 0.15*exp(-0.56*x)



def keepthecountrytidycampaign_function(x):
    simulation_config.environment = 0+(0.04*x)
    popularity.Environmentalism_popularity = 0.01+(0.02*x)
    config.Environmentalism_freq = 0+(0.05*x)
    popularity.Environmentalism_popularitys = 0.12*exp(0.13*x)
    popularity.Community_movements_popularity = 0.29*x
    popularity.Public_Health_Advocacy = 0.25*x



def labordaybankholiday_function(x):
    simulation_config.GDP = -0-(0.02*x)
    simulation_config.global_socialism = 0.02+(0.02*x)
    popularity.Socialism_popularity = 0.02+(0.03*x)
    popularity.Socialism_popularity = 0.34*x + 0.12*exp(0.91*x)
    popularity.Progressivism_popularity = 0.18*x
    popularity.Neoliberalism_popularity = -0.18*exp(0.93*x)


def labourlaws_function(x):
    popularity.Socialism_popularity = -0.05+(0.1*x)
    popularity.Capitalism_popularity = 0.05-(0.1*x)
    simulation_config.WorkerProductivity = 0.05-(0.10*x)
    simulation_config.global_socialism = -0.10+(0.20*x)
    simulation_config.Wages = -0.12+0.24*x
    popularity.Socialism_popularity = 0.39*x + 0.19 + 0.12*exp(-0.02*x)
    popularity.Progressivism_popularity = 0.29*x + 0.1 + 0.19*exp(-0.24*x)
    popularity.Neoliberalism_popularity = -0.39*x - 0.14*exp(0.58*x)
    popularity.Libertarian_Capitalism_popularity = -0.14*exp(-0.81*x)


def legalaid_function(x):
    popularity.Liberalism_popularity = 0.09 + 0.17*exp(-0.41*x)
    popularity.Poor_popularity = 0.01+(0.02*x)
    popularity.Socialism_popularity = 0.01+(0.02*x)
    simulation_callout.Equality = 0.02+(0.04*x)
    simulation_config.LowIncome = 0+(0.04*x)
    popularity.Progressivism_popularity = 0.05*exp(0.15*x) + 0.12
    popularity.Social_Justice_Advocates_popularity = 0.26*x + 0.14*exp(-0.76*x)
    popularity.Fiscal_Conservatism_popularity = -0.15*x
    popularity.Neoliberalism_popularity = -0.19 - 0.07*exp(-0.7*x)


def legaliseprostitution_function(x):
    popularity.Conservatism_popularity = -0.27*x - 0.19 - 0.13*exp(-0.33*x)
    simulation_config.GDP = 0.02+(0.01*x)
    popularity.Liberalism_popularity = 0.15*x + 0.13 + 0.07*exp(-0.08*x)
    popularity.Parents_popularity = -0.08-(0.02*x)
    popularity.Religious_Fundamentalism_popularity = -0.28*x - 0.08
    simulation_config.global_liberalis = 0.05*(x**2)+0.03
    simulation_callout.crimerate = -0.01-(0.01*x)
    popularity.Capitalism_popularity = 0.01+(0.01*x)
    config.Self_Employed_freq = 0.01+(0.01*x)
    simulation_callout.genderequality  = 0.05+(0.05*x)
    simulation_config.Tourism = 0.01*(x**2)
    popularity.Feminism_popularity = 0.11*exp(-0.84*x)
    popularity.Libertarianism_popularity = 0.16*exp(0.06*x) + 0.1
    popularity.Traditionalism_popularity = -0.09*exp(0.94*x) - 0.16


def limitautomatedtrading_function(x):
    popularity.Capitalism_popularity = -0.23*(x**1.22)
    popularity.Wealthy_popularity = -0.02-(0.08*x)
    simulation_config.HighIncome = -0.07*(x**0.67)
    popularity.Liberalism_popularity = -0.01-(0.04*x)
    simulation_config.GDP = -0.01-(0.03*x)
    popularity.Progressivists_popularity = 0.11*exp(0.13*x)
    popularity.Populism_popularity = 0.13*exp(0.82*x)
    popularity.Neoliberalism_popularity = -0.18*x - 0.18
    popularity.Free_Market_Advocates_popularity = -0.07*exp(0.33*x)


def limitorbancarsincities_function(x):

    simulation_config.carusage = -0.05-(x**2)*0.2
    popularity.Motorist_popularity = -0.1-(x**2)*0.25
    popularity.Environmentalism_popularity = 0.07*exp(0.43*x) + 0.11
    Motorist_freq = -0.04-(x**2)*0.22
    simulation_config.environment = 0.05+(x**2)*0.15*simulation_config.carusage
    simulation_config.bususage = 0.05+(x**2)*0.31
    popularity.Urban_Progressivism_popularity = 0.1*exp(0.21*x)
    popularity.Public_Health_Advocacy = 0.37*x + 0.06*exp(-0.54*x)
    popularity.Libertarianism_popularity = -0.35*x - 0.18*exp(-0.99*x)
    popularity.Neoliberalism_popularity = -0.25*x - 0.06 - 0.12*exp(-0.09*x)


def luxurygoodstax_function(x):
    Wealthy_perc = 0+(1.0*x)
    popularity.Wealthy_popularity = -0.29*(x**1.5)
    popularity.Socialism_popularity = 0+(0.18*x)
    popularity.Capitalism_popularity = 0-(0.08*x)
    simulation_callout.Equality = 0.05+(0.2*x)
    simulation_config.HighIncome = 0-(0.18*x)
    popularity.Progressivism_popularity = 0.23*x + 0.12*exp(0.51*x) + 0.12
    popularity.Socialism_popularity = 0.18*x + 0.17*exp(-0.11*x)
    popularity.Economic_Equality_Advocates_popularity = 0.18*x + 0.06*exp(-0.11*x)
    popularity.Neoliberalism_popularity = -0.1*exp(-0.66*x)
    Luxury_Industry = -0.3*x - 0.08 - 0.17*exp(-0.39*x)
    popularity.Conservatism_popularity = -0.17


def mandatorymicrochipimplant_function(x):
    popularity.Liberalism_popularity = -0.14*exp(0.37*x) - 0.18
    simulation_callout.crimerate = 0.00-(0.15*x)
    simulation_config.ViolentCrimeRate = -0.36*(x**0.8)
    popularity.Conservatism_popularity = 0.15+(0.07*x)
    popularity.Patriot_popularity = 0.11+(0.07*x)
    popularity.Religious_Fundamentalism_popularity = -0.05-(0.03*x)
    simulation_config.global_liberalis = -0.18*(x**2)-0.10
    simulation_config.security = 0+(0.22*x)
    popularity.Privacy_advocates_popularity_popularity = -0.3*x - 0.19*exp(0.3*x)
    popularity.Human_Rights_Advocacy_popularity = -0.11*x - 0.19


def mandatorymicrogeneration_function(x):
    popularity.Environmentalism_popularity = 0.21*x
    simulation_config.OilDemand = -0.02-(x*0.08)
    simulation_config.co2emissions = -0.01-(x*0.06)
    config.Environmentalism_freq = 0.08+(x*0.12)
    popularity.Capitalism_popularity = -0.05-(0.09*x)
    simulation_config.environment = 0.02+(0.04*x)
    popularity.Progressivism_popularity = 0.29*x + 0.12
    popularity.Energy_Independence_Advocates_popularity = 0.1*exp(0.41*x)
    popularity.Libertarianism_popularity = -0.38*x - 0.18*exp(0.57*x) - 0.05
    popularity.Neoliberalism_popularity = -0.3*x - 0.11*exp(-0.16*x)


def mansiontax_function(x):
    Wealthy_perc = 0.75+(0.5*x)
    popularity.Wealthy_popularity = -0.1-(0.15*x)
    popularity.Retired_popularity = -0.8*(x**8)
    simulation_callout.Equality = 0.28*(x**5)
    popularity.Socialism_popularity = 0.06+(0.08*x)
    simulation_config.HighIncome = -0.05-(0.1*x)
    popularity.Progressivism_popularity = 0.25*x + 0.06 + 0.12*exp(-0.63*x)
    popularity.Socialism_popularity = 0.11*x
    popularity.Housing_Equity_Advocates_popularity = 0.15*x + 0.15*exp(-0.53*x)
    popularity.Wealth_Preservation_Advocates_popularity = -0.19*exp(0.73*x) - 0.14
    popularity.Neoliberalism_popularity = -0.37*x - 0.15*exp(0.3*x)
    popularity.Conservatism_popularity = -0.16*exp(0.39*x) - 0.1


def marriedtaxallowance_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.1+(0.2*x)
    popularity.Conservatism_popularity = 0.35*x
    popularity.Parents_popularity = 0.02+(0.03*x)
    simulation_config.global_liberalis = -0.04-(0.04*x)
    Religious_Fundamentalism_popularity_income = 0.05+(0.05*x)
    popularity.Traditionalism_popularity = 0.38*x + 0.13*exp(0.82*x) + 0.14
    popularity.Fiscal_Conservatism_popularity = 0.36*x + 0.2
    popularity.Progressivism_popularity = -0.23*x - 0.06*exp(-0.01*x)
    popularity.Liberalism_popularity = -0.21*x - 0.12*exp(0.21*x) - 0.15
    popularity.Social_Equality_Advocates_popularity = -0.12*exp(0.03*x) - 0.16


def marsprogram_function(x):
    popularity.Patriot_popularity = 0.05+(0.20*x)
    config.Patriot_freq = 0.05+(0.15*x)
    popularity.Unemployed_popularity = -0.04-(0.12*x)
    popularity.Self_Employed_popularity = 0.035+(0.075*x)
    simulation_config.Technology = 0+(0.14*x)
    config.Religious_Fundamentalism_freq = -0.02-(0.06*x)
    popularity.Technological_Optimism_popularity = 0.26*x + 0.06 + 0.1*exp(-0.06*x)
    popularity.International_Cooperation_Advocates_popularity = 0.32*x + 0.08
    popularity.Scientific_Progressivism_popularity = 0.26*x + 0.09 + 0.13*exp(-0.16*x)
    popularity.Fiscal_Conservatism_popularity = -0.14*x - 0.14 - 0.1*exp(-0.99*x)
    popularity.Environmentalism_popularitys = -0.23*x


def maternityleave_function(x):
    popularity.Parents_popularity = 0.07+(0.15*x)
    simulation_config.WorkerProductivity = -0.05-(0.07*x)
    config.Parents_freq = 0.025+(0.04*x)
    simulation_callout.Population = 0.03+(0.03*x)
    simulation_callout.genderequality  = 0.1+(0.32*x)
    popularity.Feminism_popularity = 0.17*exp(0.41*x)
    popularity.Progressivism_popularity = 0.19*exp(0.09*x)
    popularity.Social_Welfare_Advocates_popularity = 0.19*x + 0.17
    popularity.Neoliberalism_popularity = -0.14*x - 0.18
    popularity.Fiscal_Conservatism_popularity = -0.32*x


def microgenerationgrants_function(x):
    popularity.Environmentalism_popularity = 0.32*x + 0.16*exp(-0.13*x)
    simulation_callout.energyefficiency = 0.01+(0.11*x)
    config.Environmentalism_freq = 0.02+(0.06*x)
    simulation_config.co2emissions = -0.01-(0.04*x)
    simulation_config.environment = 0.02+(0.04*x)
    popularity.Progressivism_popularity = 0.09 + 0.15*exp(-0.83*x)
    popularity.Energy_Independence_Advocates_popularity = 0.4*x
    popularity.Neoliberalism_popularity = -0.23*x - 0.17*exp(-0.77*x)
    popularity.Fiscal_Conservatism_popularity = -0.21*x - 0.17*exp(0.42*x)


def militaryspending_function(x):
    popularity.Patriot_popularity = -0.35+(0.62*x)
    popularity.Unemployed_popularity = 0.00-(0.08*x)
    popularity.Self_Employed_popularity = 0.00+(0.23*x)
    simulation_config.Terrorism = 0-(0.2*x)
    config.Self_Employed_freq = -0.02+(0.04*x)
    popularity.Liberalism_popularity = -0.10*(x**4)
    simulation_config.Technology = 0.09*(x**6.2)
    popularity.Nationalism_popularity = 0.17 + 0.15*exp(-0.48*x)
    popularity.Conservatism_popularity = 0.28*x
    popularity.Progressivism_popularity = -0.12 - 0.2*exp(-0.37*x)
    popularity.Peace_movements_popularity = -0.26*x - 0.13
    popularity.Social_Welfare_Advocates_popularity = -0.32*x - 0.11*exp(0.93*x) - 0.11


def minimumwage_function(x):
    simulation_config.LowIncome_fixed = 3000+(4000*x)
    simulation_config.PovertyRate = -0.05-(0.05*x)
    popularity.Unemployed_popularity = 0.04*(x**2)
    popularity.Capitalism_popularity = -0.13*(x**2)
    simulation_callout.Equality = 0.06*(x**4)
    popularity.Socialism_popularity = 0.08+(0.10*x)
    simulation_config.CorporateExodus = 0.10*(x**2)
    simulation_config.global_socialism = 0.02+(0.04*x)
    simulation_config.Wages = 0.04+(0.12*x)
    Labor_movements = 0.11 + 0.07*exp(-0.99*x)
    popularity.Socialism_popularity = 0.32*x + 0.1*exp(0.39*x) + 0.05
    popularity.Progressivism_popularity = 0.35*x + 0.06*exp(0.03*x) + 0.07
    popularity.Libertarian_Capitalism_popularity = -0.39*x - 0.11
    popularity.Neoliberalism_popularity = -0.16*x - 0.09


def monorail_function(x):
    simulation_config.carusage = -0.06-(0.10*x)
    popularity.Commuter_popularity = 0.12+(0.15*x)
    popularity.Unemployed_popularity = 0-(0.05*x)
    simulation_config.airtravel = -0.05*(x**5)
    simulation_config.InternationalTrade = 0.04*(x**5)
    simulation_config.WorkerProductivity = 0.06*(x**3)
    simulation_config.railUsage = 0.12*(x**6)
    popularity.Urban_Development_Advocates = 0.38*x + 0.15
    popularity.Environmentalism_popularity = 0.2 + 0.19*exp(-0.8*x)
    popularity.Public_Transport_Advocates_popularity = 0.2*exp(0.04*x)
    popularity.Fiscal_Conservatism_popularity = -0.09 - 0.19*exp(-0.38*x)
    popularity.Neoliberalism_popularity = -0.28*x - 0.16
    Car_Industry_Lobby = -0.18*x


def mortgagetaxrelief_function(x):
    simulation_config.MiddleIncome = 0.1+(0.18*x)
    popularity.Socialism_popularity = -0.06-(0.07*x)
    popularity.Poor_popularity = -0.07-(0.06*x)
    simulation_config.MiddleIncome = 0+(0.09*x)
    simulation_callout.generationalwealthgap = 0.05+(0.10*x)
    popularity.Homeownership_Advocates_popularity = 0.08*exp(0.1*x)
    popularity.Middle_Class_popularity = 0.31*x + 0.2*exp(0.04*x)
    popularity.Conservatism_popularity = 0.38*x + 0.06 + 0.07*exp(-0.6*x)
    popularity.Fiscal_Conservatism_popularity = -0.28*x
    popularity.Progressivists_popularity = -0.13*exp(0.73*x) - 0.09


def narcotics_function(x):
    popularity.Liberalism_popularity = 0.37*x + 0.12*exp(0.63*x) + 0.09
    popularity.Parents_popularity = -0.15*(x**2)
    simulation_callout.crimerate = 0.2*(x**2)
    popularity.Conservatism_popularity = -0.33*x - 0.16*exp(-0.31*x)
    simulation_config.LegalDrugConsumption = 0.8*(simulation_config.GDP+0.2)*x
    simulation_config.global_liberalis = 0.23*(x**1.4)-0.11
    popularity.Young_popularity = 0.1*(x**2)-0.04
    simulation_config.Tourism = 0.04*(x**4)
    popularity.Progressivism_popularity = 0.26*x + 0.06*exp(-0.41*x)
    popularity.Drug_Reform_Advocates_popularity = 0.35*x + 0.06
    popularity.Law_and_Order_Advocates_popularity = -0.28*x - 0.16 - 0.17*exp(-0.54*x)
    popularity.Traditionalism_popularity = -0.13*x - 0.19*exp(0.95*x) - 0.12


def nationalanthematstartofnews_function(x):
    popularity.Patriot_popularity = 0.08+(x*0.04)
    simulation_config.ForeignRelations = -0.015-(x*0.015)
    config.Patriot_freq = 0.06+(x*0.14)
    popularity.Nationalism_popularity = 0.11*exp(0.3*x) + 0.09
    popularity.Conservatism_popularity = 0.09*exp(0.14*x)
    popularity.Patriot_popularityic_movements_popularity = 0.16*x
    popularity.Liberalism_popularity = -0.15*exp(0.67*x) - 0.12
    popularity.Internationalism_popularity = -0.24*x - 0.1*exp(0.98*x)
    popularity.Secularism_popularity = -0.32*x - 0.17


def nationalanthemsinschool_function(x):
    popularity.Patriot_popularity = 0.02+(x*0.06)
    popularity.Young_popularity = -0.02-(x*0.05)
    config.Patriot_freq = 0.02+(x*0.08)
    popularity.Nationalism_popularity = 0.38*x + 0.08*exp(0.15*x) + 0.19
    popularity.Patriot_popularityic_Education_Advocates_popularity = 0.21*x
    popularity.Conservatism_popularity = 0.12*x + 0.19
    popularity.Liberalism_popularity = -0.21*x - 0.11*exp(-0.57*x)
    popularity.Secularism_popularity = -0.27*x
    popularity.Internationalism_popularity = -0.29*x - 0.11


def nationalarmedforcesweek_function(x):
    popularity.Patriot_popularity = 0.02+(0.03*x)
    config.Patriot_freq = 0+(0.1*x)
    popularity.Nationalism_popularity = 0.38*x
    popularity.Military_Advocacy_popularity = 0.27*x + 0.12 + 0.09*exp(-0.63*x)
    popularity.Conservatism_popularity = 0.12 + 0.05*exp(-0.45*x)
    popularity.Peace_movements_popularity = -0.25*x - 0.1*exp(0.3*x) - 0.2
    popularity.Progressivism_popularity = -0.12*x
    popularity.Anti_Militarism_Advocates_popularity = -0.35*x - 0.08*exp(0.6*x)


def nationalbusinesscouncil_function(x):
    popularity.Capitalism_popularity = 0.02+(0.04*x)
    simulation_config.GDP = 0.01+(0.01*x)
    simulation_config.global_socialism = 0-(0.03*x)
    popularity.Economic_Nationalism_popularity = 0.17*x + 0.07*exp(0.81*x)
    Corporatist_Strategies = 0.37*x + 0.13*exp(0.17*x)
    popularity.Conservatism_popularity = 0.14*exp(0.48*x)
    popularity.Free_Market_Advocates_popularity = -0.38*x
    popularity.Neoliberalism_popularity = -0.38*x
    popularity.Libertarianism_popularity = -0.27*x - 0.12*exp(-0.29*x)


def nationalservice_function(x):
    popularity.Liberalism_popularity = -0.11*exp(-0.26*x)
    popularity.Patriot_popularity = 0.15+(0.03*x)
    popularity.Young_popularity = -0.20-(0.02*x)
    config.Patriot_freq = 0.10+(0.06*x)
    popularity.Unemployed_popularity = 0-(0.03*x)
    popularity.Nationalism_popularity = 0.22*x
    popularity.Conservatism_popularity = 0.17*exp(-0.84*x)
    popularity.Individualism_popularity = -0.2*x
    popularity.Progressivism_popularity = -0.13*x - 0.12


def needleexchangeprogram_function(x):
    popularity.Liberalism_popularity = 0.02+(0.02*x)
    simulation_config.health = 0+(0.04*x)
    popularity.Harm_Reduction_Advocates_popularitys = 0.08*exp(0.92*x) + 0.1
    popularity.Public_Health_Advocacy = 0.16*x + 0.06
    popularity.Hardline_Drug_Policy_Advocates_popularity = -0.05 - 0.14*exp(-0.73*x)
    popularity.Conservatism_popularity = -0.15*x - 0.05*exp(-0.54*x)
    popularity.Traditionalism_popularity = -0.17*x - 0.08


def newcarsubsidies_function(x):
    popularity.Motorist_popularity = 0.05+(x*0.13)
    simulation_config.OilDemand = simulation_config.inv_ElectricCarTransition*(x*-0.03)-0.02
    simulation_config.carusage = 0.02+(x*0.02)
    simulation_config.co2emissions = simulation_config.inv_ElectricCarTransition*(-0.02*x)-0.01
    simulation_config.environment = 0.02+(0.02*x)
    simulation_config.AsthmaEpidemic = simulation_config.inv_ElectricCarTransition*(-0.02*x)-0.02
    simulation_config.GDP = 0.01+(0.01*x)
    popularity.Economic_Stimulus_Advocates_popularity = 0.25*x + 0.13
    popularity.Liberalism_popularity = 0.17*exp(-0.37*x)
    popularity.Environmentalism_popularitys = -0.14*x - 0.09*exp(0.09*x) - 0.14
    popularity.Fiscal_Conservatism_popularity = -0.1*exp(0.39*x)
    popularity.Progressivism_popularity = -0.14*x - 0.17*exp(0.92*x)


def nuclearfission_function(x):
    simulation_config.GDP = -0.03+(x**4)*0.06
    simulation_config.OilDemand = 0.04-(x**4)*0.08
    simulation_config.co2emissions = -0.1*(x**4)
    simulation_callout.privateenergy = -0.05+(0.1*x)
    popularity.Energy_Independence_Advocates_popularity = 0.18 + 0.06*exp(-0.91*x)
    popularity.Environmentalism_popularitys = 0.18*x
    popularity.Technological_Optimism_popularity = 0.39*x + 0.15 + 0.17*exp(-0.43*x)
    popularity.Anti_Nuclear_Advocates_popularity = -0.36*x - 0.14*exp(0.28*x) - 0.13
    popularity.Environmentalism_popularity = -0.19*x - 0.19 - 0.06*exp(-0.33*x)


def oildrillingsubsidy_function(x):
    popularity.Environmentalism_popularity = -0.1-(0.35*x)**2
    simulation_config.GDP = 0+(0.04*x)
    simulation_config.co2emissions = 0.04+(0.06*x)
    simulation_callout.foreigninvestment = 0.03+(0.03*x)
    config.Environmentalism_freq = -0.38*(x**2)+0.05
    popularity.Conservatism_popularity = 0.13*x
    popularity.Economic_Nationalism_popularity = 0.16*x + 0.13
    popularity.Environmentalism_popularitys = -0.13 - 0.19*exp(-0.82*x)
    popularity.Climate_Change_Advocates_popularity = -0.17*x - 0.19
    popularity.Progressivism_popularity = -0.38*x - 0.19*exp(-0.74*x)


def onechildpolicy_function(x):
    popularity.Religious_Fundamentalism_popularity = -0.2*(x**0.8)
    popularity.Parents_popularity = -0.25-(0.2*x)
    popularity.Unemployed_popularity = 0.0-(0.13*x)
    config.Parents_freq = 0.0-(0.25*x)
    popularity.Liberalism_popularity = -0.24*x - 0.17
    simulation_callout.Population = -0.05-(0.1*x)
    simulation_config.global_liberalis = -0.10*(x**2)-0.03
    popularity.Human_Rights_Advocacy_popularity = -0.2*x


def organdonation_function(x):
    simulation_config.health = 0.05+(0.06*x)
    simulation_callout.lifespan = 0.02+(0.04*x)
    popularity.Public_Health_Advocacy = 0.14*x
    popularity.Progressivism_popularity = 0.14*x + 0.13
    popularity.Medical_Ethics_Advocates_popularity = 0.14*x + 0.08*exp(0.43*x) + 0.1
    popularity.Religious_Fundamentalism_popularity = -0.33*x - 0.07
    popularity.Individual_Rights_Advocates_popularity = -0.3*x - 0.17 - 0.17*exp(-0.47*x)
    popularity.Privacy_advocates_popularity = -0.13*exp(-0.19*x)


def organicsubsidy_function(x):
    popularity.Environmentalism_popularity = 0.01+(0.06*x)
    popularity.Farmers_popularity = 0.02+(0.13*x)
    popularity.Capitalism_popularity = -0.05-(0.02*x)
    simulation_config.health = 0.02+(0.05*x)
    simulation_callout.FoodPrice = -0.02-(0.06*x)
    popularity.Environmentalism_popularitys = 0.17*exp(-0.75*x)
    popularity.Fiscal_Conservatism_popularity = -0.18*exp(0.45*x)
    popularity.Neoliberalism_popularity = -0.16*exp(-0.55*x)


def payrolltax_function(x):
    popularity.Capitalism_popularity = -0.03-(0.04*x)
    popularity.Self_Employed_popularity = -0.04-(0.08*x)
    popularity.Socialism_popularity = 0.01+(0.02*x)
    simulation_config.Wages = 0-(0.12*x)
    simulation_config.GDP = -0.15*(x**5)
    popularity.Socialism_popularity = 0.14 + 0.17*exp(-0.05*x)
    popularity.Collectivism_popularity = 0.3*x
    popularity.Libertarian_Capitalism_popularity = -0.33*x - 0.09
    popularity.Individualism_popularity = -0.13*exp(0.26*x)


def petroltax_function(x):
    simulation_config.carusage = -0.4*(1.0-simulation_callout.ElectricCarTransition)*x
    popularity.Motorist_popularity = 0.00-(x**5)
    popularity.Environmentalism_popularity = 0.1*exp(0.41*x)
    simulation_config.GDP = -0.13*(x**7)
    popularity.Farmers_popularity = 0-(0.04*x)
    popularity.Progressivism_popularity = 0.05*exp(0.36*x) + 0.08
    popularity.Industrialism_popularity = -0.38*x
    popularity.Libertarianism_popularity = -0.09 - 0.11*exp(-0.44*x)


def phonetapping_function(x):
    popularity.Liberalism_popularity = -0.33*x - 0.11*exp(-0.67*x)
    simulation_callout.crimerate = -0.06*(x**0.8)-0.03
    simulation_config.Terrorism = -0.05-(0.15*x)
    simulation_config.security = (0.075+0.1*x)
    simulation_config.Corruption = 0-(0.15*x)
    simulation_config.global_liberalis = -0.12*(x**2)-0.03
    popularity.Totalitarianism_popularity_ = 0.39*x + 0.08
    popularity.Realism_popularty = 0.16*exp(0.09*x) + 0.11
    popularity.Anarchism_popularity = -0.16*exp(0.7*x)


def plasticbagtax_function(x):
    popularity.Environmentalism_popularity = 0.06 + 0.1*exp(-0.06*x)
    popularity.Capitalism_popularity = -0.02-(0.02*x)
    popularity.Progressivism_popularity = 0.13*x + 0.1 + 0.1*exp(-0.56*x)
    popularity.Libertarianism_popularity = -0.13*exp(-0.89*x)
    popularity.Industrialism_popularity = -0.2*x


def policedrones_function(x):
    popularity.Liberalism_popularity = -0.33*x
    simulation_callout.crimerate = -0.04*(x**0.8)-0.04
    simulation_config.ViolentCrimeRate = -0.04*(x**0.8)-0.02
    simulation_config.security = 0.03+(0.03*x)
    simulation_config.Terrorism = -0.1-(0.03*x)
    popularity.Conservatism_popularity = 0.33*x + 0.06*exp(0.94*x)
    popularity.Totalitarianism_popularity = 0.24*x + 0.07*exp(0.43*x) + 0.12
    popularity.Anarchism_popularity = -0.18*x


def pollutioncontrols_function(x):
    popularity.Environmentalism_popularity = 0.17*exp(0.08*x)
    popularity.Capitalism_popularity = -0.02-(0.08*x)
    simulation_config.environment = 0.1+(0.2*x)
    simulation_config.GDP = 0-(0.05*x)
    simulation_config.co2emissions = -0.01-(0.07*x)
    popularity.Progressivism_popularity = 0.3*x
    popularity.Industrialism_popularity = -0.12*exp(0.73*x) - 0.08
    popularity.Neoliberalism_popularity = -0.2*x - 0.09 - 0.06*exp(-0.37*x)


def pressfreedom_function(x):
    simulation_config.Democracy = 0.25-(x+1.25)**-3
    simulation_config.Corruption = 0-(x**6)*0.1
    popularity.Liberalism_popularity = 0.19*exp(-0.45*x)
    simulation_callout.privateschools = 0+(x+1.06)**-20
    simulation_config.security = -0.05*(x**10)
    simulation_config.global_liberalis = 0.11*(x**2)+0.03
    popularity.Secularism_popularity = 0.27*x
    popularity.Totalitarianism_popularity = -0.19*exp(0.4*x)
    popularity.Religious_Fundamentalism_popularity = -0.11 - 0.06*exp(-0.34*x)


def prisonertagging_function(x):
    popularity.Liberalism_popularity = -0.21*x - 0.05*exp(0.86*x) - 0.12
    simulation_callout.crimerate = -0.06*(x**0.8)-0.03
    simulation_config.ViolentCrimeRate = -0.08*(x**0.8)-0.05

    popularity.Conservatism_popularity = 0.18*exp(-0.17*x)
    popularity.Realism_popularty = 0.19*exp(0.27*x) + 0.2
    popularity.Anarchism_popularity = -0.19*x - 0.1


def prisonervoting_function(x):
    popularity.Conservatism_popularity = -0.1*exp(0.14*x)
    popularity.Liberalism_popularity = 0.38*x
    simulation_config.Democracy = 0.01+(0.02*x)
    popularity.Democratic_Socialism_popularity = 0.2 + 0.18*exp(-0.22*x)
    popularity.Traditionalism_popularity = -0.13*exp(-0.01*x)


def privateprisons_function(x):
    simulation_callout.crimerate = -0.05*(x**0.8)
    popularity.Liberalism_popularity = -0.05+(x**2)*0.11
    popularity.Conservatism_popularity = 0.00+(0.12*x)
    popularity.Unemployed_popularity = 0-(0.02*x)
    popularity.Capitalism_popularity = 0+(0.11*x)
    simulation_config.global_socialism = -0.02-(0.02*x)
    popularity.Neoliberalism_popularity = 0.11*x + 0.14 + 0.19*exp(-0.65*x)
    popularity.Libertarian_Capitalism_popularity = 0.15*exp(-0.31*x)
    popularity.Socialism_popularity = -0.32*x
    popularity.Progressivism_popularity = -0.34*x - 0.17*exp(0.69*x) - 0.07


def propertytax_function(x):
    simulation_config.GDP = 0.5+(0.5*x)
    simulation_config.MiddleIncome = 0-(0.025*x)
    simulation_config.HighIncome = -0.14*(x**2)
    popularity.Socialism_popularity = 0+(0.12*x)
    popularity.Capitalism_popularity = 0-(0.15*x)
    simulation_callout.Equality = 0+(0.15*x)
    simulation_config.MiddleIncome = 0-(0.32*x)
    popularity.Wealthy_popularity = 0-(x**11)*0.8
    popularity.Retired_popularity = 0-(0.28*x)
    popularity.Socialism_popularity = 0.23*x + 0.2
    popularity.Progressivism_popularity = 0.11*exp(0.21*x)
    popularity.Libertarian_Capitalism_popularity = -0.17*x - 0.09*exp(-0.69*x)
    popularity.Conservatism_popularity = -0.3*x - 0.13*exp(0.09*x) - 0.13


def proportionalfines_function(x):
    Wealthy_perc = 0.1+(0.9*x)
    simulation_config.HighIncome = -0.01*(x**2)
    simulation_callout.Equality = 0+(0.06*x)
    popularity.Wealthy_popularity = -0.15*(x**2)
    popularity.Poor_popularity = 0.04*(x**2)
    popularity.Socialism_popularity = 0+(0.04*x)
    simulation_config.global_socialism = 0.01+(0.03*x)
    popularity.Capitalism_popularity = -0.06*(x**2.2)
    popularity.Progressivism_popularity = 0.34*x
    popularity.Socialism_popularity = 0.13*exp(0.71*x) + 0.12
    popularity.Traditionalism_popularity = -0.2*x - 0.13*exp(0.42*x) - 0.05
    popularity.Neoliberalism_popularity = -0.09*exp(0.02*x)


def publiclibraries_function(x):
    simulation_callout.education = 0.02+(0.04*x)
    simulation_callout.Equality = 0.02+(0.02*x)
    popularity.Retired_popularity = 0.03+(0.03*x)
    popularity.Collectivism_popularity = 0.08 + 0.2*exp(-0.81*x)
    popularity.Socialism_popularity = 0.23*x + 0.14*exp(-0.21*x)
    popularity.Neoliberalism_popularity = -0.17*exp(0.87*x)
    popularity.Libertarianism_popularity = -0.15*x - 0.15


def publicreligiousbroadcasts_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.29*x + 0.07*exp(0.38*x)
    popularity.Liberalism_popularity = -0.11*exp(0.3*x)
    config.Religious_Fundamentalism_freq = 0.03+(x*0.1)
    simulation_callout.RacialTension = 0.05+(x**2)*0.15
    popularity.Nationalism_popularity = 0.22*x
    popularity.Secularism_popularity = -0.13*x - 0.1*exp(0.67*x) - 0.1


def publictaxreturns_function(x):
    popularity.Wealthy_popularity = -0.08*(x**2)
    simulation_callout.Equality = 0.03*(x**0.5)
    popularity.Liberalism_popularity = -0.04-(0.02*x)
    simulation_config.TaxEvasion = -0.05-(0.1*x)
    BlackMarket = -0.1-(0.10*x)
    popularity.Socialism_popularity = 0.02+(0.02*x)
    simulation_config.Corruption = -0.08-(0.11*x)
    popularity.Progressivism_popularity = 0.34*x + 0.06 + 0.18*exp(-0.89*x)
    popularity.Populism_popularity = 0.34*x
    Elitism_popularity = -0.15*exp(0.04*x) - 0.07
    popularity.Neoliberalism_popularity = -0.32*x - 0.11 - 0.19*exp(-0.33*x)


def punitivetaxonsuperstores_function(x):
    simulation_config.GDP = -0.01-(x*0.01)
    popularity.Capitalism_popularity = -0.04-(x*0.09)
    popularity.Self_Employed_popularity = 0.06+(x*0.12)
    config.Self_Employed_freq = 0.04+(x*0.08)
    simulation_config.carusage = -0.03-(x*0.03)
    popularity.Environmentalism_popularity = 0.01+(0.03*x)
    popularity.Socialism_popularity = 0.02+(0.06*x)
    popularity.Populism_popularity = 0.11*x + 0.2
    popularity.Protectionism_popularity = 0.31*x + 0.05 + 0.07*exp(-0.82*x)
    popularity.Neoliberalism_popularity = -0.26*x - 0.08
    popularity.Libertarian_Capitalism_popularity = -0.09*exp(0.38*x) - 0.09


def punitivewealthtax_function(x):
    simulation_config.GDP = 0.5+(0.5*x)
    Wealthy_perc = 0.5+(0.5*x)
    popularity.Wealthy_popularity = -0.02-(x*0.81)**2
    popularity.Capitalism_popularity = -0.09*(x**2)
    popularity.Socialism_popularity = 0.18*(x**2)
    simulation_config.BrainDrain = 0.15*(x**2)
    simulation_config.global_socialism = 0.065*(x**2)
    simulation_config.HighIncome = 0-(x*0.55)
    simulation_config.CorporateExodus = 0+(0.2*x)
    Marxism = 0.19*x
    popularity.Progressivism_popularity = 0.11*x
    popularity.Libertarian_Capitalism_popularity = -0.15*x - 0.17
    popularity.Neoliberalism_popularity = -0.11*x - 0.15 - 0.12*exp(-1.0*x)


def quantitativeeasing_function(x):
    simulation_callout.Inflation = 0.78*(x**4)
    popularity.Capitalism_popularity = 0.12+(0.08*x)
    popularity.Wealthy_popularity = 0.1+(0.1*x)
    simulation_config.HighIncome = 0.05+(0.05*x)
    simulation_config.GDP = 0.03+(0.06*x)
    simulation_callout.currencystrength = -0.08*(x**2)
    Keynesian_Economics = 0.22*x + 0.06
    popularity.Progressivism_popularity = 0.31*x
    Austrian_Economics = -0.17*exp(-0.55*x)
    popularity.Libertarian_Capitalism_popularity = -0.23*x - 0.18


def racediscriminationact_function(x):
    simulation_callout.RacialTension = 0-(0.14*x)
    popularity.Liberalism_popularity = 0.25*x + 0.16
    popularity.EthnicMinorities_popularity = 0.2+(0.1*x)
    popularity.Conservatism_popularity = -0.05*(x**4)
    simulation_config.global_liberalis = 0+(0.12*x)
    popularity.Progressivism_popularity = 0.36*x + 0.1 + 0.18*exp(-0.37*x)
    popularity.Feminism_popularity = 0.13 + 0.16*exp(-0.13*x)
    popularity.Cultural_Relativism_popularity = 0.16 + 0.14*exp(-0.81*x)
    popularity.Male_Supremacy_Advocates_popularity = -0.2*x
    popularity.Traditionalism_popularity = -0.15*x - 0.11
    popularity.Realism_popularty = -0.36*x - 0.19*exp(-0.3*x)


def racialprofiling_function(x):
    simulation_callout.crimerate = -0.08*(x**0.8)
    simulation_config.ViolentCrimeRate = -0.05*(x**0.8)
    popularity.Liberalism_popularity = -0.17*x - 0.15*exp(0.56*x) - 0.18
    simulation_callout.RacialTension = 0.2+(0.1*x)
    simulation_config.Terrorism = -0.04-(-0.05*x)
    popularity.Conservatism_popularity = 0.15*x + 0.14 + 0.17*exp(-0.07*x)
    popularity.Realism_popularty = 0.18*x + 0.07*exp(0.04*x)
    popularity.Nationalism_popularity = 0.05*exp(-0.47*x)
    popularity.Socialism_popularity = -0.21*x - 0.15
    popularity.Internationalism_popularity = -0.16*x - 0.12*exp(-0.47*x)
    popularity.Cultural_Relativism_popularity = -0.18*x - 0.07*exp(0.09*x)


def rareearthrefinement_function(x):
    popularity.Environmentalism_popularity = -0.15*x - 0.14*exp(-0.82*x)
    simulation_config.WorkerProductivity = 0+(0.05*x)
    popularity.Patriot_popularity = 0.05+(0.01*x)
    simulation_config.Technology = 0+(0.04*x)
    simulation_config.Pollution = 0+(0.2*x)
    popularity.Capitalism_popularity = 0.1+(0.1*x)
    popularity.Industrialism_popularity = 0.27*x + 0.12 + 0.08*exp(-0.55*x)
    popularity.Realism_popularty = 0.26*x + 0.1*exp(0.94*x)
    popularity.Nationalism_popularity = 0.18*exp(-0.35*x)
    popularity.Globalization_supporters_popularity = -0.09*exp(0.7*x) - 0.09


def recreationaldrugstax_function(x):
    simulation_config.LegalDrugConsumption = -0.1*(x**2)
    popularity.Young_popularity = -0.08*(simulation_config.LegalDrugConsumption*x)
    popularity.Poor_popularity = -0.05*(simulation_config.LegalDrugConsumption*x)
    simulation_config.PovertyRate = 0.06*(simulation_config.LegalDrugConsumption*x)
    popularity.Progressivism_popularity = 0.19*x
    popularity.Socialism_popularity = 0.11*exp(-0.66*x)
    popularity.Libertarianism_popularity = -0.16*x - 0.13*exp(0.4*x)
    popularity.Anarchism_popularity = -0.36*x - 0.12


def recycling_function(x):
    popularity.Environmentalism_popularity = 0.2*x + 0.17
    simulation_config.environment = 0.01+(0.04*x)
    config.Environmentalism_freq = 0.02+(0.08*x)
    popularity.Collectivism_popularity = 0.07*exp(0.56*x)
    popularity.Progressivism_popularity = 0.21*x + 0.16
    popularity.Industrialism_popularity = -0.29*x - 0.12
    popularity.Egoism_popularity = -0.13*x - 0.09*exp(0.69*x) - 0.19


def reforestation_function(x):
    popularity.Environmentalism_popularity = 0.22*x + 0.09
    simulation_config.Pollution = -0.05-(0.05*x)
    simulation_config.co2emissions = -0.01-(0.06*x)
    popularity.Unemployed_popularity = -0.01-(0.04*x)
    simulation_config.AsthmaEpidemic = -0.03-(0.10*x)
    simulation_config.environment = 0.04+(0.07*x)
    popularity.Globalization_supporters_popularity = 0.11*exp(0.68*x) + 0.07
    popularity.Industrialism_popularity = -0.23*x - 0.1
    popularity.Realism_popularty = -0.11*x - 0.16


def rentcontrols_function(x):
    simulation_config.PovertyRate = -0.03-(0.03*x)
    popularity.Socialism_popularity = 0.04+(0.04*x)
    popularity.Capitalism_popularity = -0.1-(0.2*x)
    simulation_callout.privatehousing = -0.1-(0.15*x)
    simulation_config.LowIncome = 0.03+(0.06*x)
    Capitalism_income = -0.09-(0.04*x)
    popularity.Socialism_popularity = 0.35*x + 0.14 + 0.12*exp(-0.62*x)
    popularity.Progressivism_popularity = 0.34*x + 0.14*exp(-0.39*x)
    popularity.Populism_popularity = 0.36*x
    popularity.Neoliberalism_popularity = -0.09 - 0.09*exp(-0.55*x)
    popularity.Libertarian_Capitalism_popularity = -0.21*x
    popularity.Realism_popularty = -0.21*x - 0.06


def retirementage_function(x):
    simulation_config.WorkerProductivity = -0.1+(0.25*x)
    popularity.Retired_popularity = 0.12-(0.30*x)
    config.Retired_freq = 0.04-0.08*x
    popularity.Unemployed_popularity = 0+(0.1*x)
    popularity.Socialism_popularity = 0.34*x + 0.1*exp(-0.23*x)
    popularity.Populism_popularity = 0.2*x + 0.14*exp(0.26*x)
    popularity.Neoliberalism_popularity = -0.18*exp(-0.34*x)
    popularity.Realism_popularty = -0.11*exp(-0.53*x)


def righttodie_function(x):
    popularity.Religious_Fundamentalism_popularity = -0.32*x - 0.13*exp(0.91*x) - 0.17
    popularity.Conservatism_popularity = -0.08-(0.1*x)
    popularity.Retired_popularity = 0.06+(0.08*x)
    simulation_config.HealthcareDemand = -0.05*(x**2)
    popularity.Liberalism_popularity = 0.05*exp(0.07*x) + 0.06
    simulation_callout.Population = -0.01-(0.02*x)
    simulation_config.global_liberalis = 0.14*(x**2)+0.02
    popularity.Secularism_popularity = 0.08*exp(0.18*x) + 0.09
    config.Postmodernism_popularity = 0.31*x + 0.13*exp(-0.62*x)
    popularity.Traditionalism_popularity = -0.19*x - 0.07*exp(0.82*x)


def righttoprivacy_function(x):
    popularity.Liberalism_popularity = 0.38*x
    simulation_config.GDP = -0.01-(0.02*x)
    simulation_config.global_liberalis = 0.12*(x**2)+0.04
    popularity.Capitalism_popularity = -0.02-(0.02*x)
    popularity.Anarchism_popularity = 0.23*x + 0.2
    config.Postmodernism_popularity = 0.07*exp(-0.76*x)
    popularity.Totalitarianism_popularity = -0.28*x - 0.08
    popularity.Conservatism_popularity = -0.08*exp(0.21*x)


def roadbuilding_function(x):
    popularity.Motorist_popularity = -0.25+(0.55*x)
    popularity.Environmentalism_popularity = -0.35*x - 0.09
    simulation_config.carusage = 0+(0.29*x)
    TrafficCongestion = -0.38*(x**1.2)
    popularity.Unemployed_popularity = 0-(0.05*x)
    popularity.Industrialism_popularity = 0.14*exp(0.82*x)
    popularity.Capitalism_popularity = 0.33*x + 0.09*exp(0.68*x)
    popularity.Realism_popularty = 0.24*x + 0.17*exp(0.84*x)
    popularity.Progressivism_popularity = -0.35*x
    config.Postmodernism_popularity = -0.17*x - 0.12


def roboticsresearch_function(x):
    simulation_config.Technology = 0.01+(0.05*x)
    simulation_config.WorkerProductivity = 0.02+(0.1*x)
    popularity.Unemployed_popularity = 0+(0.19*x)
    popularity.Progressivism_popularity = 0.1*x + 0.06 + 0.06*exp(-0.5*x)
    popularity.Liberalism_popularity = 0.08*exp(0.25*x)
    Modernism_popularity = 0.11*exp(0.11*x) + 0.09
    popularity.Traditionalism_popularity = -0.2*x
    popularity.Populism_popularity = -0.11*x - 0.1*exp(-0.55*x)


def rubberbullets_function(x):
    popularity.Liberalism_popularity = -0.1*exp(0.18*x)
    simulation_config.ClassWarfare = -0.09-(0.09*x)
    popularity.Conservatism_popularity = 0.32*x + 0.05 + 0.18*exp(-0.98*x)
    popularity.Realism_popularty = 0.37*x + 0.15
    popularity.Totalitarianism_popularity = 0.14 + 0.12*exp(-0.54*x)
    popularity.Anarchism_popularity = -0.17*exp(0.14*x) - 0.2
    popularity.Progressivism_popularity = -0.14*exp(0.7*x) - 0.15


def ruraldevelopmentgrants_function(x):
    simulation_config.LowIncome = 0.02+(0.13*x)
    popularity.Unemployed_popularity = 0.00-(0.15*x)
    simulation_callout.Equality = 0.00+(0.14*x)
    popularity.Farmers_popularity = 0.06+(0.18*x)
    simulation_config.GDP = 0.00+(0.05*x)
    config.Farmers_freq = 0.01+(0.05*x)
    simulation_config.carusage = 0.05*(x**2)
    simulation_config.railUsage = 0.08*(x**2)
    popularity.Socialism_popularity = 0.21*x
    popularity.Populism_popularity = 0.2*exp(-0.84*x)
    popularity.Environmentalism_popularity = 0.28*x + 0.08*exp(0.86*x)
    popularity.Neoliberalism_popularity = -0.3*x - 0.13*exp(-0.51*x)
    popularity.Libertarianism_popularity = -0.17*x - 0.09 - 0.12*exp(-0.55*x)
    popularity.Industrialism_popularity = -0.12*x


def salestax_function(x):
    simulation_config.GDP = -0.15*(x**4)
    simulation_config.PovertyRate = 0.00+(0.20*x)
    popularity.Self_Employed_popularity = 0.00-(0.21*x)
    popularity.Capitalism_popularity = 0.00-(0.15*x)
    simulation_callout.Equality = -0.02-(0.32*x)
    simulation_config.LowIncome = 0-(0.07*x)
    simulation_config.MiddleIncome = 0-(0.11*x)
    simulation_config.HighIncome = 0-(0.11*x)
    popularity.Capitalism_popularity = 0.08*exp(0.38*x) + 0.18
    popularity.Neoliberalism_popularity = 0.16*exp(-0.54*x)
    popularity.Realism_popularty = 0.27*x + 0.15
    popularity.Socialism_popularity = -0.3*x - 0.16*exp(-0.44*x)
    popularity.Progressivism_popularity = -0.15*x - 0.11


def sateliteroadpricing_function(x):
    simulation_config.carusage = -0.25*(x**4)
    popularity.Motorist_popularity = -0.08-(0.06*x)
    popularity.Environmentalism_popularity = 0.3*x + 0.07 + 0.11*exp(-0.06*x)
    popularity.Capitalism_popularity = 0.05+(0.02*x)
    popularity.Liberalism_popularity = 0.28*x + 0.19
    popularity.Progressivism_popularity = 0.16*exp(0.9*x)
    popularity.Libertarianism_popularity = -0.24*x - 0.1*exp(-0.28*x)
    popularity.Populism_popularity = -0.24*x - 0.2
    popularity.Nationalism_popularity = -0.11*exp(0.14*x) - 0.1


def schoolbuses_function(x):
    popularity.Parents_popularity = 0.07+(0.07*x)
    simulation_config.bususage = 0.05+(0.15*x)
    popularity.Collectivism_popularity = 0.26*x + 0.08 + 0.08*exp(-0.57*x)
    popularity.Socialism_popularity = 0.37*x + 0.12
    popularity.Progressivism_popularity = 0.24*x + 0.17*exp(0.15*x)
    popularity.Neoliberalism_popularity = -0.3*x
    popularity.Libertarianism_popularity = -0.13*x - 0.18*exp(0.79*x)


def schoolprayers_function(x):
    popularity.Religious_Fundamentalism_popularity = 0.33*x + 0.14*exp(-0.79*x)
    popularity.Liberalism_popularity = -0.14 - 0.14*exp(-0.56*x)
    config.Religious_Fundamentalism_freq = 0.04+(0.25*x)
    simulation_callout.RacialTension = 0.1+(0.11*x)
    popularity.Conservatism_popularity = 0.13*x + 0.15
    popularity.Secularism_popularity = -0.21*x - 0.15*exp(0.48*x) - 0.13
    popularity.Cultural_Relativism_popularity = -0.07*exp(0.48*x)


def schooltaxcredits_function(x):
    simulation_callout.privateschools = 0+(0.4*x)
    simulation_config.MiddleIncome = 0+(0.06*x)
    simulation_config.HighIncome = 0+(0.04*x)
    popularity.Wealthy_popularity = 0.02+(0.06*x)
    simulation_config.MiddleIncome = 0.04+(0.06*x)
    popularity.Socialism_popularity = -0.01-(0.05*x)
    popularity.Poor_popularity = -0.01-(0.05*x)
    popularity.Capitalism_popularity = 0.02+(0.04*x)
    popularity.Neoliberalism_popularity = 0.11*x + 0.07
    popularity.Conservatism_popularity = 0.21*x + 0.17 + 0.19*exp(-0.28*x)
    popularity.Libertarianism_popularity = 0.11*x
    popularity.Socialism_popularity = -0.39*x - 0.17*exp(0.89*x)
    popularity.Democratic_Socialism_popularity = -0.16*exp(0.38*x)
    popularity.Progressivism_popularity = -0.33*x - 0.07 - 0.05*exp(-0.78*x)


def schoolvouchers_function(x):
    simulation_callout.privateschools = 0+(0.6*x)
    simulation_callout.Equality = 0.05*(x**3)
    simulation_config.PovertyRate = -0.05*(x**3)
    simulation_config.global_socialism = -0.01-(0.12*x)
    simulation_config.privateschools_income_fixed = 500+(2500*x)
    popularity.Capitalism_popularity = 0.02+(0.05*x)
    popularity.Neoliberalism_popularity = 0.39*x + 0.08 + 0.2*exp(-0.8*x)
    popularity.Libertarian_Capitalism_popularity = 0.22*x + 0.15*exp(-0.41*x)
    popularity.Conservatism_popularity = 0.19 + 0.1*exp(-0.25*x)
    popularity.Socialism_popularity = -0.14*exp(0.25*x)
    popularity.Progressivism_popularity = -0.29*x - 0.11*exp(-0.95*x)
    popularity.Democratic_Socialism_popularity = -0.17*x


def sciencefunding_function(x):
    simulation_config.Technology = -0.10+(0.19*x)
    simulation_callout.energyefficiency = -0.1+(0.2*x)
    simulation_config.GDP = 0.07*(x**0.75)
    popularity.Self_Employed_popularity = -0.15+(0.3*x)
    config.Self_Employed_freq = -0.05+(0.1*x)
    popularity.Unemployed_popularity = 0-(0.03*x)
    popularity.Progressivism_popularity = 0.14*x
    popularity.Internationalism_popularity = 0.36*x + 0.13
    popularity.Liberalism_popularity = 0.17*x + 0.07*exp(-0.68*x)
    popularity.Traditionalism_popularity = -0.1*exp(-0.15*x)
    popularity.Conservatism_popularity = -0.19*exp(0.4*x)


def secretcourts_function(x):
    popularity.Liberalism_popularity = -0.2*x - 0.06
    simulation_callout.crimerate = -0.02+(x**0.7)*-0.07
    simulation_config.Terrorism = -0.03+(x**2)*-0.14
    simulation_config.ForeignRelations = -0.05+(x**2)*-0.11
    simulation_config.global_liberalis = -0.10*(x**2)-0.03
    simulation_config.security = 0.03+(0.05*x)
    popularity.Totalitarianism_popularity = 0.22*x + 0.19
    popularity.Realism_popularty = 0.17 + 0.11*exp(-0.49*x)
    popularity.Conservatism_popularity = 0.07 + 0.15*exp(-0.73*x)
    popularity.Anarchism_popularity = -0.4*x - 0.11
    popularity.Secularism_popularity = -0.17*x - 0.2*exp(0.3*x)


def selectiveschooling_function(x):
    popularity.Liberalism_popularity = 0.07-(0.14*x)
    popularity.Conservatism_popularity = 0.31*x + 0.17
    popularity.Socialism_popularity = 0.04-(0.08*x)
    popularity.Capitalism_popularity = -0.04+(0.04*x)
    simulation_callout.Equality = 0.03-(0.06*x)
    simulation_config.global_socialism = 0.03-(0.06*x)
    simulation_callout.education = -0.02+(0.04*x)
    simulation_callout.mentalhealth = -0.06*(x**6)
    Elitism_popularity = 0.07*exp(0.07*x)
    popularity.Neoliberalism_popularity = 0.3*x + 0.07*exp(0.88*x)
    popularity.Collectivism_popularity = -0.2*x - 0.19
    popularity.Socialism_popularity = -0.16*exp(0.24*x) - 0.11
    popularity.Progressivism_popularity = -0.17*x - 0.09


def smallbusinessgrants_function(x):
    popularity.Self_Employed_popularity = 0.10+(0.25*x)
    simulation_config.GDP = 0.04*(x**0.75)+0.01
    popularity.Capitalism_popularity = 0+(0.11*x)
    simulation_config.global_socialism = -0.04-(0.1*x)
    config.Self_Employed_freq = 0.02+(0.06*x)
    popularity.Populism_popularity = 0.12 + 0.05*exp(-0.53*x)
    popularity.Socialism_popularity = 0.17*exp(-0.68*x)
    popularity.Progressivism_popularity = 0.18*exp(-0.01*x)
    popularity.Neoliberalism_popularity = -0.36*x - 0.08*exp(0.34*x) - 0.07
    popularity.Libertarian_Capitalism_popularity = -0.15*x
    popularity.Realism_popularty = -0.11*x - 0.14*exp(0.87*x) - 0.16


def smartmeterprogram_function(x):
    simulation_callout.energyefficiency = 0+(0.07*x)
    popularity.Environmentalism_popularity = 0.06*exp(0.95*x) + 0.11
    config.Environmentalism_freq = 0+(0.05*x)
    popularity.Progressivism_popularity = 0.12*x + 0.17*exp(-0.35*x)
    Modernism_popularity = 0.29*x + 0.05
    popularity.Conservatism_popularity = -0.37*x - 0.15
    popularity.Anarchism_popularity = -0.15*x - 0.1*exp(0.27*x) - 0.17
    popularity.Traditionalism_popularity = -0.17*x - 0.2*exp(0.57*x)


def socialcare_function(x):
    popularity.Retired_popularity = 0.05+(0.10*x)
    popularity.Retired_popularity_income_fixed = 500+(5000*x)
    popularity.Socialism_popularity = 0.02+(0.07*x)
    popularity.Capitalism_popularity = -0.03-(0.07*x)
    popularity.Unemployed_popularity = 0-(0.02*x)
    simulation_config.HealthcareDemand = -0.03-(0.03*x)
    simulation_config.health = 0.02+(0.04*x)
    simulation_callout.mentalhealth = 0.01+(0.05*x)
    popularity.Socialism_popularity = 0.18*x + 0.11*exp(0.44*x)
    popularity.Collectivism_popularity = 0.36*x + 0.2
    popularity.Progressivism_popularity = 0.24*x + 0.18*exp(0.36*x)
    popularity.Neoliberalism_popularity = -0.09*exp(0.43*x)
    popularity.Libertarian_Capitalism_popularity = -0.09*exp(-0.47*x)
    popularity.Individualism_popularity = -0.16*x


def socialjusticefoundation_function(x):
    simulation_config.global_liberalis = 0.01+(0.02*x)
    popularity.Progressivism_popularity = 0.14*exp(0.74*x)
    popularity.Liberalism_popularity = 0.34*x
    popularity.Feminism_popularity = 0.33*x + 0.17*exp(0.74*x) + 0.07
    popularity.Conservatism_popularity = -0.11*x - 0.13*exp(0.55*x) - 0.08
    popularity.Traditionalism_popularity = -0.36*x
    popularity.Male_Supremacy_Advocates_popularity = -0.39*x - 0.17 - 0.13*exp(-0.94*x)


def spaceprogram_function(x):
    popularity.Patriot_popularity = 0.05+(0.15*x)
    config.Patriot_freq = 0.05+(0.15*x)
    popularity.Unemployed_popularity = -0.02-(0.05*x)
    popularity.Self_Employed_popularity = 0.035+(0.075*x)
    simulation_config.Technology = 0+(0.11*x)
    config.Religious_Fundamentalism_freq = -0.02-(0.06*x)
    simulation_callout.InternetSpeed = 0.20*(x**3)
    popularity.Progressivism_popularity = 0.14*x + 0.18 + 0.08*exp(-0.72*x)
    popularity.Internationalism_popularity = 0.14*x + 0.16*exp(-0.13*x)
    popularity.Populism_popularity = -0.33*x
    popularity.Libertarianism_popularity = -0.11*x


def statebroadcaster_function(x):
    popularity.Capitalism_popularity = -0.02-(0.05*x)
    popularity.Socialism_popularity = 0.02+(0.05*x)
    simulation_callout.education = 0.01+(0.012*x)
    popularity.Unemployed_popularity = 0-(0.01*x)
    simulation_config.ForeignRelations = 0.02+(0.06*x)
    popularity.Collectivism_popularity = 0.27*x + 0.06*exp(-0.49*x)
    popularity.Nationalism_popularity = 0.12*x + 0.11*exp(-0.65*x)
    popularity.Libertarian_Capitalism_popularity = -0.17*exp(0.12*x) - 0.11
    popularity.Neoliberalism_popularity = -0.18*x - 0.08*exp(-0.66*x)


def statehealthservice_function(x):
    popularity.Poor_popularity = -0.02+(0.21*x)
    popularity.Capitalism_popularity = -0.02-(0.10*x)
    popularity.Wealthy_popularity = 0.00-(0.10*x)
    popularity.Socialism_popularity = -0.01+(0.16*x)
    simulation_config.health = 0.3*(x**0.6)-0.05
    popularity.Retired_popularity = 0.00+(0.16*x)
    popularity.Unemployed_popularity = 0.02-(0.34*x)
    popularity.Self_Employed_popularity = 0.00+(0.22*x)
    config.Self_Employed_freq = -0.02+(0.25*x)
    simulation_config.global_socialism = -.02+(0.072*x)
    simulation_config.HospitalOvercrowding = 0.05-(0.5*x)
    simulation_config.PovertyRate = -0.08*(x**6)
    popularity.Socialism_popularity = 0.17*x + 0.12*exp(0.77*x) + 0.09
    popularity.Collectivism_popularity = 0.2*x + 0.08*exp(-0.05*x)
    popularity.Libertarian_Capitalism_popularity = -0.35*x - 0.17 - 0.17*exp(-0.66*x)
    popularity.Neoliberalism_popularity = -0.1*x


def stateschools_function(x):
    popularity.Poor_popularity = 0.04+(0.11*x)
    popularity.Socialism_popularity = 0.00+(0.18*x)
    simulation_callout.education = 0.35*(x**0.6)
    simulation_config.PovertyRate = -0.02-(0.16*x)
    popularity.Self_Employed_popularity = 0.00+(0.14*x)
    popularity.Unemployed_popularity = 0-(0.39*x)
    config.Self_Employed_freq = 0+(0.29*x)
    simulation_config.global_socialism = 0+(0.03*x)
    config.Parents_freq = 0+(0.025*x)
    popularity.Capitalism_popularity = 0.00-(0.10*x)
    simulation_config.Corruption = 0.03*(x**8)
    popularity.Collectivism_popularity = 0.18*exp(-0.51*x)
    popularity.Socialism_popularity = 0.14*exp(-0.55*x)
    popularity.Libertarianism_popularity = -0.15*x
    popularity.Neoliberalism_popularity = -0.16*exp(0.98*x) - 0.16


def stemcells_function(x):

    simulation_config.GDP = 0.02+(0.03*x)
    popularity.Religious_Fundamentalism_popularity = -0.1*exp(0.75*x)
    popularity.Conservatism_popularity = -0.02-(0.04*x)
    simulation_config.health = 0.01+(0.02*x)
    simulation_config.Technology = 0.01+(0.04*x)
    popularity.Progressivism_popularity = 0.06 + 0.07*exp(-0.96*x)
    popularity.Secularism_popularity = 0.07*exp(0.09*x)
    popularity.Traditionalism_popularity = -0.21*x - 0.07*exp(-0.25*x)


def syntheticmeatresearchgrants_function(x):
    simulation_callout.FoodPrice = -0.1-(0.08*x)
    popularity.Farmers_popularity = -0.18-(0.20*x)
    config.Farmers_freq = -0.05-(0.16*x)
    popularity.Environmentalism_popularity = 0.28*x + 0.2
    popularity.Progressivism_popularity = 0.2*x
    popularity.Industrialism_popularity = -0.37*x - 0.11
    popularity.Traditionalism_popularity = -0.2*x


def universalbasicincome_function(x):
    popularity.Capitalism_popularity = -0.1-(0.2*x)
    popularity.Socialism_popularity = 0.12+(0.12*x)
    simulation_config.PovertyRate = -0.1-(0.3*x)
    simulation_config.Wages = 0.1+(0.1*x)
    simulation_config.global_socialism = 0+(0.10*x)
    simulation_config.privateschools_income_fixed = 4000+(10000*x)
    popularity.Socialism_popularity = 0.17*x
    popularity.Progressivism_popularity = 0.12*x + 0.14
    popularity.Neoliberalism_popularity = -0.39*x - 0.16*exp(0.57*x) - 0.06
    popularity.Libertarian_Capitalism_popularity = -0.11*x - 0.11*exp(0.08*x) - 0.19


def refugeepolicy_function(x):
    simulation_callout.ImmigrationDemand = 0.19*(x**1.25)
    popularity.Liberalism_popularity = 0+(0.06*x)
    popularity.Patriot_popularity = -0.12*(x**1.4)
    popularity.EthnicMinorities_popularity = 0.+(0.15*x)
    simulation_config.ForeignRelations = 0+(0.15*x)
    popularity.Internationalism_popularity = 0.28*x + 0.14 + 0.13*exp(-0.23*x)
    popularity.Nationalism_popularity = -0.39*x - 0.08
    popularity.Populism_popularity = -0.2*x


def statereligion_function(x):

    popularity.Religious_Fundamentalism_popularity = 0.37*x + 0.05 + 0.11*exp(-0.44*x)
    popularity.Liberalism_popularity = -0.37*x
    config.Religious_Fundamentalism_freq = 0.03+(0.03*x)
    simulation_config.Democracy = -0.05*(x**2)
    simulation_config.global_liberalis = -0.01-(0.02*x)
    popularity.Nationalism_popularity = 0.12 + 0.12*exp(-0.01*x)
    popularity.Secularism_popularity = -0.28*x - 0.19 - 0.07*exp(-0.75*x)


def desalination_function(x):
    simulation_callout.energyefficiency = -0.02-(0.03*x)
    popularity.Realism_popularty = 0.1*exp(0.31*x)
    popularity.Environmentalism_popularity = 0.3*x + 0.17 + 0.13*exp(-0.55*x)
    popularity.Industrialism_popularity = -0.11*exp(0.92*x)
    popularity.Environmentalism_popularitys = -0.05 - 0.19*exp(-0.24*x)


def immigrationrules_function(x):
    popularity.Liberalism_popularity = -0.12 - 0.09*exp(-0.71*x)
    popularity.Patriot_popularity = 0.12-(0.24*x)
    popularity.EthnicMinorities_popularity = -0.12+(0.24*x)
    simulation_config.ForeignRelations = -0.18+(0.32*x)
    popularity.Nationalism_popularity = 0.18*x + 0.12
    popularity.Conservatism_popularity = 0.12*x + 0.14*exp(-0.75*x)
    popularity.Internationalism_popularity = -0.2*x - 0.14


def nuclearweapons_function(x):
    popularity.Patriot_popularity = 0.06+(0.03*x)
    popularity.Liberalism_popularity = -0.03-(0.03*x)
    simulation_config.Technology = 0.02+(0.02*x)
    _percept_strength = 0.05+(0.3*x)
    popularity.Environmentalism_popularity = -0.05-(0.09*x)
    popularity.Realism_popularty = 0.17*x
    popularity.Nationalism_popularity = 0.19*exp(0.31*x) + 0.17
    popularity.Globalization_supporters_popularity = -0.39*x - 0.15
    popularity.Progressivism_popularity = -0.09*exp(0.71*x)


def co2campaign_function(x):
    popularity.Environmentalism_popularity = 0.37*x + 0.05
    config.Environmentalism_freq = 0.03+(0.06*x)
    simulation_config.co2emissions = -0.02-(0.02*x)
    simulation_config.carusage = -0.01-(0.03*x)
    popularity.Progressivism_popularity = 0.39*x + 0.1*exp(0.07*x) + 0.11
    popularity.Industrialism_popularity = -0.19*x
    popularity.Nationalists_popularity = -0.26


def banalcohol_function(x):
    popularity.Liberalism_popularity = -0.08 - 0.14*exp(-0.5*x)
    simulation_config.AlcoholConsumption = -0.96*(x**5.1)
    simulation_config.Tourism = -0.5*(x**3.1)
    simulation_config.global_liberalis = -0.02-(0.04*x)
    popularity.Conservatism_popularity = 0.22*x
    popularity.Totalitarianism_popularity = 0.16*exp(0.85*x) + 0.13
    popularity.Libertarianism_popularity = -0.32*x


def bantobacco_function(x):
    popularity.Liberalism_popularity = -0.16*x - 0.18 - 0.05*exp(-0.6*x)
    simulation_callout.tobaccouse = -0.96*(x**5.1)
    simulation_config.global_liberalis = -0.02-(0.04*x)
    popularity.Conservatism_popularity = 0.19*x + 0.15*exp(-0.63*x)
    popularity.Totalitarianism_popularity = 0.09*exp(-0.59*x)
    popularity.Libertarianism_popularity = -0.21*x - 0.17


def bancrypto_function(x):
    popularity.Liberalism_popularity = -0.26*x
    simulation_callout.internetcurrencyadoption = -0.25-(0.75*x)
    simulation_config.global_liberalis = -0.01-(0.02*x)
    popularity.Conservatism_popularity = 0.07*exp(0.2*x) + 0.09
    popularity.Totalitarianism_popularity = 0.25*x + 0.08*exp(0.85*x) + 0.19
    popularity.Libertarianism_popularity = -0.23*x - 0.18


def workersdividend_function(x):
    popularity.Capitalism_popularity = -0.14-(x*0.1)
    popularity.Socialism_popularity = 0.14+(0.16*x)
    simulation_config.global_socialism = 0.08+(0.12*x)
    popularity.Self_Employed_popularity = -0.08-(0.12*x)
    simulation_config.LowIncome = 0.05+(x*0.15)
    simulation_config.HighIncome = -0.05-(0.08*x)
    simulation_callout.foreigninvestment = -0.06-(0.13*x)
    GeneralStrike = -0.10-(0.20*x)
    TeachersStrike = -0.10-(0.20*x)
    DoctorsStrike = -0.10-(0.20*x)
    Rail_Strike = -0.10-(0.20*x)
    simulation_config.CorporateExodus = 0.06+(0.14*x)
    popularity.Socialism_popularity = 0.34*x + 0.16
    popularity.Progressivism_popularity = 0.2*exp(0.51*x) + 0.18
    popularity.Neoliberalism_popularity = -0.33*x - 0.06
    popularity.Libertarian_Capitalism_popularity = -0.2*exp(0.59*x) - 0.05
