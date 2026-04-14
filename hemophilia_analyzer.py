num_hemophilia_a_patients=0
num_hemophilia_b_patients=0
num_level_severe=0
num_level_moderate=0
num_level_mild=0
hem_A_inhibitor_positive_patients=0
hem_B_inhibitor_positive_patients=0
hem_A_prophylaxis=0
hem_B_prophylaxis=0
moderate_level_with_prophylaxis=0
hem_A_recombinant=0
hem_B_recombinant=0
hem_A_plasma=0
hem_B_plasma=0
annual_total_medication_amount=0
annual_medication_cost=0
highest_four_weeks_medication=-1
hem_A_highest_four_weeks_medication=-1
hem_B_highest_four_weeks_medication=-1

A_highest_tc=None
B_highest_tc=None
highest_tc=None

plasma_factor_8_vial_2000=0
plasma_factor_8_vial_1500=0
plasma_factor_8_vial_1000=0
plasma_factor_8_vial_500=0
plasma_factor_8_vial_250=0
plasma_factor_8_total_amount=0

plasma_factor_9_vial_2000=0
plasma_factor_9_vial_1500=0
plasma_factor_9_vial_1000=0
plasma_factor_9_vial_500=0
plasma_factor_9_vial_250=0
plasma_factor_9_total_amount=0

recombinant_factor_8_vial_2000=0
recombinant_factor_8_vial_1500=0
recombinant_factor_8_vial_1000=0
recombinant_factor_8_vial_500=0
recombinant_factor_8_vial_250=0
recombinant_factor_8_total_amount=0

recombinant_factor_9_vial_2000=0
recombinant_factor_9_vial_1500=0
recombinant_factor_9_vial_1000=0
recombinant_factor_9_vial_500=0
recombinant_factor_9_vial_250=0
recombinant_factor_9_total_amount=0

another_patient="y"
while another_patient=="y" or another_patient=="Y":
    level_factor8=0
    level_factor9=0
    monthly_medication_amount=0
    yearly_medication_amount=0
    total_of_medication=0
    vial2000=0
    vial1500=0
    vial1000=0
    vial500=0
    vial250=0
    tc=input("Enter your TR identification number:")
    name_surname=input("Enter your name surname:")
    factor_num=int(input("Enter your the deficient factor proteins number(8 or 9):"))
    while factor_num!=8 and factor_num!=9:
        print("There was an invalid number entry")
        factor_num=int(input("Enter the deficient factor proteins number again:"))

    if factor_num==8:
        hemophilia_type="Hemophilia A"
        num_hemophilia_a_patients+=1
    else:
        hemophilia_type="Hemophilia B"
        num_hemophilia_b_patients+=1

    if factor_num==8:
        level_factor8=float(input("Enter the level of factor-8 in the blood:"))
        while level_factor8<0 or level_factor8>50:
            print("There was an invalid number entry")
            level_factor8=float(input("Enter the level of factor-8 in the blood again:"))
        level_factor9=0
    else:
        level_factor9=float(input("Enter the level of factor-9 in the blood:"))
        while level_factor9<0 or level_factor9>50:
            print("There was an invalid number entry")
            level_factor9=float(input("Enter the level of factor-9 in the blood again:"))
        level_factor8=0

    amount_BU=float(input("Enter the amount of antibody in blood produced against factor medication (BU):"))
    while amount_BU<0:
        print("There was an invalid number entry")
        amount_BU=float(input("Enter the amount of antibody in blood produced against factor medication (BU):"))


    if 0<level_factor9<1 or 0<level_factor8<1:
        severity_hemophilia="severe"
        num_level_severe+=1
    elif (level_factor8>=1 and level_factor8<=5) or (level_factor9>=1 and level_factor9<=5):
        severity_hemophilia="moderate"
        num_level_moderate+=1
    else:
        severity_hemophilia="mild"
        num_level_mild+=1

    if severity_hemophilia=="moderate":
        num_bleeding_episodes=int(input("Enter the number of bleeding episodes in the past year:"))
        while num_bleeding_episodes<0:
            print("There was an invalid number entry")
            num_bleeding_episodes=int(input("Enter the number of bleeding episodes in the past year:"))

        monthly_average_bleeding=num_bleeding_episodes/12
    else:
        monthly_average_bleeding=0
        
    if amount_BU>=5:
        inhibitor="positive"
    else:
        inhibitor="negative"

    if factor_num==8 and inhibitor=="positive":
        hem_A_inhibitor_positive_patients+=1
    elif factor_num==9 and inhibitor=="positive":
        hem_B_inhibitor_positive_patients+=1


    if (inhibitor=="negative" and severity_hemophilia=="severe") or (monthly_average_bleeding>=3 and severity_hemophilia=="moderate"):
        prophylaxis=True
        if factor_num==8:
            hem_A_prophylaxis+=1
        else:
            hem_B_prophylaxis+=1
    else:
        prophylaxis=False
        

    if prophylaxis==True:

        if severity_hemophilia=="moderate":
            moderate_level_with_prophylaxis+=1


        weight=float(input("Enter his/her weight (kg):"))
        while weight<0:
            print("There was an invalid number entry")
            weight=float(input("Enter his/her weight (kg)"))
    
        production_type_of_medication=input("Enter the production type of factor medication to be used (Plasma-derived/Recombinant(Use P/p/R/r characters)):")
        while production_type_of_medication!="P" and production_type_of_medication!="p" and production_type_of_medication!="R" and production_type_of_medication!="r":
            print("There was an invalid value entry")
            production_type_of_medication=input("Enter the production type of factor medication to be used (Plasma-derived/Recombinant(Use P/p/R/r characters)):")

        if production_type_of_medication=="P" or production_type_of_medication=="p":
            type_of_medication="plasma"
            if  factor_num==8:
                hem_A_plasma+=1
            else:
                hem_B_plasma+=1
        else:
            type_of_medication="recombinant"
            if factor_num==8:
                hem_A_recombinant+=1
            else:
                hem_B_recombinant+=1
    
        needs_factor=40-level_factor8-level_factor9
        WEEK=52
        FOUR_WEEK=4
        if factor_num==8:
            AMOUNT_FACTOR_A_WEEK_HEM=3
            amount_of_iu=weight*needs_factor/2
            yearly_medication_amount=WEEK*amount_of_iu
            monthly_medication_amount=amount_of_iu*FOUR_WEEK
        else:
            AMOUNT_FACTOR_A_WEEK_HEM=2
            amount_of_iu=weight*needs_factor/1
            yearly_medication_amount=WEEK*amount_of_iu
            monthly_medication_amount=amount_of_iu*FOUR_WEEK
        
        if factor_num==8 and type_of_medication=="recombinant":
            if amount_of_iu >=2000:
                vial2000=amount_of_iu//2000
            remain=amount_of_iu % 2000
            if remain>1750:
                vial2000+=1
            elif 1750>=remain>1500:
                vial1500+=1
                vial250+=1
            elif 1500>=remain>1250:
                vial1500+=1
            elif 1250>=remain>1000:
                vial1000+=1
                vial250+=1
            elif 1000>=remain>750:
                vial1000+=1
            elif 750>=remain>500:
                vial500+=1
                vial250+=1
            elif 500>=remain>250:
                vial500+=1
            else:
                vial250+=1           

            recombinant_factor_8_vial_2000+=vial2000
            recombinant_factor_8_vial_1500+=vial1500
            recombinant_factor_8_vial_1000+=vial1000
            recombinant_factor_8_vial_500+=vial500
            recombinant_factor_8_vial_250+=vial250

            total_of_medication=vial2000*2000+vial1500*1500+vial1000*1000+vial500*500+vial250*250
            annual_total_medication_amount+=total_of_medication
            recombinant_factor_8_total_amount+=total_of_medication


        elif factor_num==9 and type_of_medication=="recombinant":
            if amount_of_iu >=2000:
                vial2000=amount_of_iu//2000
            remain=amount_of_iu % 2000
            if remain>1750:
                vial2000+=1
            elif 1750>=remain>1500:
                vial1500+=1
                vial250+=1
            elif 1500>=remain>1250:
                vial1500+=1
            elif 1250>=remain>1000:
                vial1000+=1
                vial250+=1
            elif 1000>=remain>750:
                vial1000+=1
            elif 750>=remain>500:
                vial500+=1
                vial250+=1
            elif 500>=remain>250:
                vial500+=1
            else:
                vial250+=1                       

            recombinant_factor_9_vial_2000+=vial2000
            recombinant_factor_9_vial_1500+=vial1500
            recombinant_factor_9_vial_1000+=vial1000
            recombinant_factor_9_vial_500+=vial500
            recombinant_factor_9_vial_250+=vial250

            total_of_medication=vial2000*2000+vial1500*1500+vial1000*1000+vial500*500+vial250*250
            annual_total_medication_amount+=total_of_medication
            recombinant_factor_9_total_amount+=total_of_medication

        elif factor_num==9 and type_of_medication=="plasma":
            if amount_of_iu >=2000:
                vial2000=amount_of_iu//2000
            remain=amount_of_iu % 2000
            if remain>1750:
                vial2000+=1
            elif 1750>=remain>1500:
                vial1500+=1
                vial250+=1
            elif 1500>=remain>1250:
                vial1500+=1
            elif 1250>=remain>1000:
                vial1000+=1
                vial250+=1
            elif 1000>=remain>750:
                vial1000+=1
            elif 750>=remain>500:
                vial500+=1
                vial250+=1
            elif 500>=remain>250:
                vial500+=1
            else:
                vial250+=1           

            plasma_factor_9_vial_2000+=vial2000
            plasma_factor_9_vial_1500+=vial1500
            plasma_factor_9_vial_1000+=vial1000
            plasma_factor_9_vial_500+=vial500
            plasma_factor_9_vial_250+=vial250

            total_of_medication=vial2000*2000+vial1500*1500+vial1000*1000+vial500*500+vial250*250
            annual_total_medication_amount+=total_of_medication
            plasma_factor_9_total_amount+=total_of_medication
        else:
            if amount_of_iu >=2000:
                vial2000=amount_of_iu//2000
            remain=amount_of_iu % 2000
            if remain>1750:
                vial2000+=1
            elif 1750>=remain>1500:
                vial1500+=1
                vial250+=1
            elif 1500>=remain>1250:
                vial1500+=1
            elif 1250>=remain>1000:
                vial1000+=1
                vial250+=1
            elif 1000>=remain>750:
                vial1000+=1
            elif 750>=remain>500:
                vial500+=1
                vial250+=1
            elif 500>=remain>250:
                vial500+=1
            else:
                vial250+=1           

            plasma_factor_8_vial_2000+=vial2000
            plasma_factor_8_vial_1500+=vial1500
            plasma_factor_8_vial_1000+=vial1000
            plasma_factor_8_vial_500+=vial500
            plasma_factor_8_vial_250+=vial250

            total_of_medication=vial2000*2000+vial1500*1500+vial1000*1000+vial500*500+vial250*250
            annual_total_medication_amount+=total_of_medication
            plasma_factor_8_total_amount+=total_of_medication
        
        
        PRICE_PLASMA_FOR_ONE_IU=0.3
        PRICE_RECOMBINANT_FOR_ONE_IU=0.4
        if type_of_medication=="plasma":
            cost_plasma_yearly=total_of_medication*PRICE_PLASMA_FOR_ONE_IU*WEEK
            cost_plasma_four_week=total_of_medication*PRICE_PLASMA_FOR_ONE_IU*FOUR_WEEK
            annual_medication_cost+=cost_plasma_yearly
            cost_recombinant_four_week=0
            cost_recombinant_yearly=0

        else:
            cost_recombinant_yearly=total_of_medication*PRICE_RECOMBINANT_FOR_ONE_IU*WEEK
            cost_recombinant_four_week=total_of_medication*PRICE_RECOMBINANT_FOR_ONE_IU*FOUR_WEEK
            annual_medication_cost+=cost_recombinant_yearly
            cost_plasma_yearly=0
            cost_plasma_four_week=0
    
        if factor_num==9 and monthly_medication_amount>hem_B_highest_four_weeks_medication:
            B_highest_tc=tc
            B_highest_name_surname=name_surname
            B_highest_type_of_disease=hemophilia_type
            B_highest_disease_severities=severity_hemophilia
            B_highest_weight=weight
            B_highest_type_medication=type_of_medication
            hem_B_highest_four_weeks_medication=total_of_medication*FOUR_WEEK
            B_highest_cost=cost_plasma_four_week+cost_recombinant_four_week

        if factor_num==8 and monthly_medication_amount>hem_A_highest_four_weeks_medication:
            A_highest_tc=tc
            A_highest_name_surname=name_surname
            A_highest_type_of_disease=hemophilia_type
            A_highest_disease_severities=severity_hemophilia
            A_highest_weight=weight
            A_highest_type_medication=type_of_medication
            hem_A_highest_four_weeks_medication=total_of_medication*FOUR_WEEK
            A_highest_cost=cost_plasma_four_week+cost_recombinant_four_week

        if monthly_medication_amount>highest_four_weeks_medication:
            highest_tc=tc
            highest_name_surname=name_surname
            highest_type_of_disease=hemophilia_type
            highest_disease_severities=severity_hemophilia
            highest_weight=weight
            highest_type_medication=type_of_medication
            highest_four_weeks_medication=total_of_medication*FOUR_WEEK
            highest_cost=cost_plasma_four_week+cost_recombinant_four_week

        
  
    print(f"TR identification number:{tc}")
    print(f"Name and Surname:{name_surname}")
    print(f"Type and Severity of the disease:{hemophilia_type, severity_hemophilia}")
    if prophylaxis==False:
        print("Prophylaxis not applied.")
    else:
        print("Prophylaxis applied.")
        print(f"The factor medication to be used: {factor_num},  The medication type to be used: {type_of_medication}")
        print(f"The number of uses of the medication in a week: {AMOUNT_FACTOR_A_WEEK_HEM}")
        print(f"Minimum required dose of medication at one time: {amount_of_iu:.2f}")
        print(f"Amount of medication to be used at one time: {total_of_medication}IU,  Types and quantities of vials:  2000 IU:{vial2000}, 1500 IU:{vial1500}, 1000 IU:{vial1000}, 500IU: {vial500}, 250IU:{vial250} , type:{type_of_medication}")
        print(f"Total amount of medication for 4 weeks: {total_of_medication*FOUR_WEEK}IU, Types and quantities of vials for 4 weeks:  2000 IU:{vial2000*FOUR_WEEK}, 1500 IU:{vial1500*FOUR_WEEK}, 1000 IU:{vial1000*FOUR_WEEK}, 500 IU:{vial500*FOUR_WEEK}, 250 IU:{vial250*FOUR_WEEK}, type:{type_of_medication}")
        print(f"Total medication cost for four weeks: {cost_plasma_four_week+cost_recombinant_four_week:.2f}$")

    another_patient=input("Are there any other patients? (please use y/Y/n/N characters).")
    if another_patient!="y" and another_patient!="Y" and another_patient!="N" and another_patient!="n":
        another_patient=input("There was an invalid value entry. Enter again please.")


num_total_patient=num_hemophilia_a_patients+num_hemophilia_b_patients
print(f"Numbers of hemophilia-A:{num_hemophilia_a_patients} , Numbers of hemophilia-B:{num_hemophilia_b_patients}, Numbers of all patients:{num_total_patient}")

percentage_severe=num_level_severe/num_total_patient*100
percentage_moderate=num_level_moderate/num_total_patient*100
percentage_mild=num_level_mild/num_total_patient*100

print(f"Numbers of patients with severe:{num_level_severe}, percentages of patients with severe:{percentage_severe:.2f}%")
print(f"Numbers of patients with moderate:{num_level_moderate}, percentages of patients with moderate:{percentage_moderate:.2f}%")
print(f"Numbers of patients with mild:{num_level_mild}, percentages of patients with mild:{percentage_mild:.2f}%")

if num_hemophilia_a_patients==0:
    print("Percentages of inhibitor presence in Hemophilia-A: 0%")
else:
    print(f"Percentages of inhibitor presence in Hemophilia-A: {hem_A_inhibitor_positive_patients/num_hemophilia_a_patients*100:.2f}%")
if num_hemophilia_b_patients==0:
    print("Percentages of inhibitor presence in Hemophilia-B: 0%")
else:
    print(f"Percentages of inhibitor presence in Hemophilia-B: {hem_B_inhibitor_positive_patients/num_hemophilia_b_patients*100:.2f}%")

if num_hemophilia_a_patients==0:
    print("Numbers of patients receiving prophylaxis for Hemophilia-A:0 , Percentages of patients receiving prophylaxis for Hemophilia-A: 0")
else:
    print(f"Numbers of patients receiving prophylaxis for Hemophilia-A {hem_A_prophylaxis}, Percentages of patients receiving prophylaxis for Hemophilia-A {hem_A_prophylaxis/num_hemophilia_a_patients*100:.2f}%")
if num_hemophilia_b_patients==0:
    print("Numbers of patients receiving prophylaxis for Hemophilia-B:0 , Percentages of patients receiving prophylaxis for Hemophilia-B:0")
else:
    print(f"Numbers of patients receiving prophylaxis for Hemophilia-B {hem_B_prophylaxis}, Percentages of patients receiving prophylaxis for Hemophilia-B {hem_B_prophylaxis/num_hemophilia_b_patients*100:.2f}%")
if num_level_moderate==0:
    print("The percentage of patients receiving prophylaxis among hemophilia patients whose disease severity is moderate:0%")
else:
    print(f"The percentage of patients receiving prophylaxis among hemophilia patients whose disease severity is moderate: {moderate_level_with_prophylaxis/num_level_moderate*100:.2f}%")

if hem_A_prophylaxis==0:
    print("Percentage of Hemophilia-A patients using plasma-derived factor medication receiving prophylaxis:0%")
else:
    print(f"Percentage of Hemophilia-A patients using plasma-derived factor medication receiving prophylaxis:{hem_A_plasma/hem_A_prophylaxis*100:.2f}%")
if hem_A_prophylaxis==0:
    print("Percentage of Hemophilia-A patients using recombinant factor medication receiving prophylaxis:0%")
else:
    print(f"Percentage of Hemophilia-A patients using recombinant factor medication receiving prophylaxis:{hem_A_recombinant/hem_A_prophylaxis*100:.2f}%")
if hem_B_prophylaxis==0:
    print("Percentage of Hemophilia-B patients using plasma-derived factor medication receiving prophylaxis:0%")
else:
    print(f"Percentage of Hemophilia-B patients using plasma-derived factor medication receiving prophylaxis:{hem_B_plasma/hem_B_prophylaxis*100:.2f}%")
if hem_B_prophylaxis==0:
    print("Percentage of Hemophilia-B patients using recombinant factor medication receiving prophylaxis:0%")
else:
    print(f"Percentage of Hemophilia-B patients using recombinant factor medication receiving prophylaxis:{hem_B_recombinant/hem_B_prophylaxis*100:.2f}%")

print(f"Total plasma-derived and 4-week prophylaxis medication quantities for factor-8:{plasma_factor_8_total_amount}IU ,Vial types and quantities to be sent to all patients for factor 8:  2000iu vial:{plasma_factor_8_vial_2000}, 1500iu vial:{plasma_factor_8_vial_1500}, 1000iu vial:{plasma_factor_8_vial_1000}, 500iu vial:{plasma_factor_8_vial_500}, 250iu vial:{plasma_factor_8_vial_250}")
print(f"Total plasma-derived and 4-week prophylaxis medication quantities for factor-9:{plasma_factor_9_total_amount}IU ,Vial types and quantities to be sent to all patients for factor 9:  2000iu vial:{plasma_factor_9_vial_2000}, 1500iu vial:{plasma_factor_9_vial_1500}, 1000iu vial:{plasma_factor_9_vial_1000}, 500iu vial:{plasma_factor_9_vial_500}, 250iu vial:{plasma_factor_9_vial_250}")
print(f"Total recombinant and 4-week prophylaxis medication quantities for factor-8:{recombinant_factor_8_total_amount}IU ,Vial types and quantities to be sent to all patients for factor 8:  2000iu vial:{recombinant_factor_8_vial_2000}, 1500iu vial:{recombinant_factor_8_vial_1500}, 1000iu vial:{recombinant_factor_8_vial_1000}, 500iu vial:{recombinant_factor_8_vial_500}, 250iu vial:{recombinant_factor_8_vial_250}")
print(f"Total recombinant and 4-week prophylaxis medication quantities for factor-9:{recombinant_factor_9_total_amount}IU ,Vial types and quantities to be sent to all patients for factor 9:  2000iu vial:{recombinant_factor_9_vial_2000}, 1500iu vial:{recombinant_factor_9_vial_1500}, 1000iu vial:{recombinant_factor_9_vial_1000}, 500iu vial:{recombinant_factor_9_vial_500}, 250iu vial:{recombinant_factor_9_vial_250}")

four_weeks_medication_cost_ssi=annual_medication_cost*FOUR_WEEK/WEEK

print(f"4-weeks factor medication costs for prophylaxis covered by the SSI: {four_weeks_medication_cost_ssi:.2f}$")
print(f"1-year factor medication costs for prophylaxis covered by the SSI: {annual_medication_cost:.2f}$")

total_prophylaxis_patients=hem_A_prophylaxis+hem_B_prophylaxis

if total_prophylaxis_patients==0:
    print("Average annual total medicaiton amount per patient for prophylaxis covered by the SSI:0")
    print("Average annual total cost per patient for prophylaxis covered by the SSI:0")
else:
    print(f"Average annual total medicaiton amount per patient for prophylaxis covered by the SSI:{annual_total_medication_amount/total_prophylaxis_patients:.2f}")
    print(f"Average annual total cost per patient for prophylaxis covered by the SSI:{annual_medication_cost/total_prophylaxis_patients:.2f}")
if A_highest_tc!=None:
    print(f"Information of the patients with the highest four week amount of medication for Hemophilia-A    Tc:{A_highest_tc} , Name-Surname:{A_highest_name_surname} , Disease severities: {A_highest_disease_severities} , Weight:{A_highest_weight} , types of medication used:{A_highest_type_medication} , total medication amount for four weeks:{hem_A_highest_four_weeks_medication:.2f} , total medication costs for four week:{A_highest_cost:.2f}$")
else:
    print("There are no patients Hemophilia-A")
if B_highest_tc!=None:
    print(f"Information of the patients with the highest four week amount of medication for Hemophilia-B    Tc:{B_highest_tc} , Name-Surname:{B_highest_name_surname} , Disease severities: {B_highest_disease_severities} , Weight:{B_highest_weight} , types of medication used:{B_highest_type_medication} , total medication amount for four weeks:{hem_B_highest_four_weeks_medication:.2f} , total medication costs for four week:{B_highest_cost:.2f}$")
else:
    print("There are no patients Hemophilia-B")
if highest_tc!=None:
    print(f"Information of the patients with the highest four week amount of medication for all patients   Tc:{highest_tc} , Name-Surname:{highest_name_surname} , Disease severities: {highest_disease_severities} , Weight:{highest_weight} , types of medication used:{highest_type_medication} , total medication amount for four weeks:{highest_four_weeks_medication:.2f} , total medication costs for four week:{highest_cost:.2f}$")