#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 03:20:52 2024

@author: alecbiddinger
"""

def AskForDetails():
    UserAge = float(input("Please enter your age: "))
    UserBodyWeightInLbs = float(input("Please enter your body weight in lbs: "))
    UserHeightInInches = float(input("Please enter your height in inches: "))
    UserSex = input("Please enter your biological sex (Male or Female): ")
    ActivityFactor = input("Please enter which activity factor best describes you (Sedentary, Moderate, Strenous): ")
    UserName = input("Please enter your name for personalized results: ")
    return UserAge, UserBodyWeightInLbs, UserHeightInInches, UserSex, ActivityFactor, UserName


def ConvertLbsToKg(UserBodyWeightInLbs):
    UserBodyWeightInKg = UserBodyWeightInLbs * 0.45359237
    return UserBodyWeightInKg


def ConvertInchesToCm(UserHeightInInches):
    UserHeightInCm = UserHeightInInches * 2.54
    return UserHeightInCm


def DetermineBEE(UserAge, UserBodyWeightInKg, UserHeightInCm, UserSex):
    if (UserSex == "male"):
        BEE = 66 + (13.7 * UserBodyWeightInKg) + (5 * UserHeightInCm) - (6.8 * UserAge)
        return BEE
    elif (UserSex == "female"):
        BEE = 655 + (9.6 * UserBodyWeightInKg) + (1.8 * UserHeightInCm) - (4.7 * UserAge)
        return BEE


def DetermineTEE(BEE, ActivityFactor):
    if (ActivityFactor == "sedentary"):
        TEE = BEE + (0.3 * BEE)
        return TEE
    elif (ActivityFactor == "moderate"):
        TEE = BEE + (0.5 * BEE)
        return TEE
    elif (ActivityFactor == "strenous"):
        TEE = BEE + BEE
        return TEE


def PrintDetails(TEE, UserName):
    print("\n", UserName, "has a calculated total energy expenditure (TEE) of approximately", format(TEE, ",.2f"), "kcals per day.")


def AskForCaloricIntake(TEE, UserBodyWeightInKg):
    UserCaloricIntake = input("\nDo you know your daily caloric intake? Yes or No: ")
    if(UserCaloricIntake=="yes"):
        UserCalIntakeNum = float(input("\nPlease enter your current daily caloric intake: "))
        CaloricDifference = abs(TEE - UserCalIntakeNum)
        print("\nThe difference between your daily caloric intake and your calculated TEE is", format(CaloricDifference, ",.2f"), "calories.")
        if(UserCalIntakeNum > TEE):
            print("\nYou are consuming more calories than your estimated TEE. You should consume approximately", format(CaloricDifference, ",.2f"), "less calories to prevent weight gain and maintain your weight.")
            WantWeightLoss = input("\nDo you want to lose weight? Yes or No: ")
            if(WantWeightLoss=="yes"):
                RecCalIntakeMinForLoss = TEE - 500
                RecCalIntakeMaxForLoss = TEE - 1000
                print("\nTo lose 1 to 2 pounds a week, a rate that experts consider safe, your calorie intake should be between", format(RecCalIntakeMinForLoss, ",.2f"), "and", format(RecCalIntakeMaxForLoss, ",.2f"), "calories a day.")
        elif(UserCalIntakeNum < TEE):
             print("\nYou are consuming fewer calories than your estimated TEE. You should consume approximately", format(CaloricDifference, ",.2f"), "more calories a day to prevent weight loss and maintain your weight.")
             WantWeightGain = input("\nDo you want to gain weight? Yes or No: ")
             if(WantWeightGain=="yes"):
                 RecCalIntakeSlowGain = TEE + 500
                 RecCalIntakeFastGain = TEE + 1000
                 RecProteinIntakeMin = UserBodyWeightInKg * 1.2
                 RecProteinIntakeMax = UserBodyWeightInKg * 2
                 print("\nTo gain weight your calorie intake should be", format(RecCalIntakeSlowGain, ",.2f"), "calories a day for a slow weight gain or", format(RecCalIntakeFastGain, ",.2f"), "calories a day for a fast weight gain. If you goal is to build muscle, then you should intake between", format(RecProteinIntakeMin, ",.2f"), "and", format(RecProteinIntakeMax, ",.2f"), "grams of protein a day.")
    else:
         print("\nContinue")


def PrintRecipes():
    CalorieGainOrLose = input("\nWould you like to add or subtract calories to your diet? Type Add or Subtract: ")
    if(CalorieGainOrLose=="add"):
        CalorieAmount = float(input("\nHow many calories would you like to add to your diet? "))
        if(0 < CalorieAmount <= 300):
            print("\nThere are many small meals you can enjoy to meet your calorie goal, one being chicken noodle soup which comes in at approximately 200 calories, depending on your ingredients.")
        elif(300 < CalorieAmount <= 500):
            print("\nTo meet your calorie goal, you could add a serving of shrimp tacos to your diet. One serving of shrimp tacos has 400 calories.")
        elif(500 < CalorieAmount <= 700):
            print("\nTo meet your calorie goal, you should add an additional meal to your diet. One option would be a rib-eye steak with white beans and mushrooms, which has approximately 550 calories.")
        elif(CalorieAmount > 700):
            print("\nTo meet your calorie goal, you may want to add multiple additional meals to your diet or calorie-dense snacks. I would recommend trying Italian baked rice, which has 500 calories, and adding a protein of your choice to add additional calories. You could also add advocados to your diet, as just one possesses 322 calories.")
    elif(CalorieGainOrLose=="subtract"):
        print("\nIf your goal is to lose weight, then you should consume 500 to 1000 calories less per day. An example of a meal between 500 and 1000 calories would be a Big Mac, which has 600 calories. It is also recommended that you increase your physical activity to lose weight, so you can burn more calories.")
            

def main():
    UserAge, UserBodyWeightInLbs, UserHeightInInches, UserSex, ActivityFactor, UserName = AskForDetails()
    UserBodyWeightInKg = ConvertLbsToKg(UserBodyWeightInLbs)
    UserHeightInCm = ConvertInchesToCm(UserHeightInInches)
    BEE = DetermineBEE(UserAge, UserBodyWeightInKg, UserHeightInCm, UserSex)
    TEE = DetermineTEE(BEE, ActivityFactor)
    PrintDetails(TEE, UserName)
    AskForCaloricIntake(TEE, UserBodyWeightInKg)
    PrintRecipes()
    


main()


