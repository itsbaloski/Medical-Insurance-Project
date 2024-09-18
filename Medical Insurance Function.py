# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

print("This person's insurance cost is " + str(insurance_cost) + " dollars.")
# Age Factor
age += 4

new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print( "The change in cost of insurance after increasing the age by 4 years is " + str(change_in_insurance_cost) + " dollars.")

# BMI Factor
age = 28
bmi += 3.1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
change_in_insurance_cost = new_insurance_cost - insurance_cost
print('The change in estimated insurance cost after increasing BMI by 3.1 is ' +str(change_in_insurance_cost) + ' dollars.')

# Male vs. Female Factor
bmi = 26.2
sex = 1
new_insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost
print('The change in estimated cost for being male instead of female is ' + str(change_in_insurance_cost) + ' dollars.')



# Create calculate_insurance_cost() function below: 
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print('The estimated insurance cost for this ' + name + str(estimated_cost) + ' dollars.')
  return estimated_cost

# Initial variables for Maria 

# Estimate Maria's insurance cost
maria_insurance_costt = calculate_insurance_cost(name = "Maria ", age = 28, sex = 0, bmi = 26.2, num_of_children = 3, smoker = 0)


# Initial variables for Omar


# Estimate Omar's insurance cost 
omar_insurance_cost = calculate_insurance_cost(name = "Omar ", age = 35, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

#Estimate Balo's Insurance cost
balo_insurance_cost = calculate_insurance_cost(name = "Balogun ", age = 27, sex = 1, bmi = 22.2, num_of_children = 0, smoker = 1)

# Add your code here
def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
 

# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 29, sex = 1, num_of_children = 3, smoker = 1)

balo_insurance_cost = estimate_insurance_cost(name = 'balo', age = 27, sex = 1, num_of_children = 0, smoker = 0)

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here
names.append("Priscilla")
insurance_costs.append(8320.0)

medical_records = list(zip(insurance_costs, names))
print(medical_records)

num_medical_records = len(medical_records)
print("There are " + str(num_medical_records) + " medical records.")

first_medical_record = medical_records[0]
print("Here is the first medical record " + str(first_medical_record))

sorted_list = sorted(medical_records)
print("Here are the medical records sorted by insurance cost " + str(sorted_list))

cheapest_three = medical_records[:3]
print("Here are the three cheapest insurance costs in our medical records: " + str(cheapest_three))

priciest_three = medical_records[-3:]
print("Here are the three most expensive insurance costs in our medical records: " + str(priciest_three))

occurrences_paul = names.count("Paul")
print('There are ' + str(occurrences_paul) + ' individuals with the name Paul in our medical records.')

names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here
total_cost = 0
for cost in actual_insurance_costs:
  total_cost += cost 
average_cost = total_cost / len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) + " dollars.")

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  print("The insurance cost for " + name + " is " + str(insurance_cost) + " dollars.")
if insurance_cost > average_cost:
  print("The insurance cost for " + name + " is above average.")
elif insurance_cost < average_cost:
  print("The insurance cost for " + name + " is below average.")
else:
  print("The insurance cost for " + name + " is equal average.")

updated_estimated_costs = [num * 11/10 for num in estimated_insurance_costs]
print(updated_estimated_costs)

medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
# print(medical_data)
updated_medical_data = medical_data.replace('#', '$')
# print(updated_medical_data)

num_records = 0

for data in updated_medical_data:
  if data == '$':
    num_records += 1

# print("There are " + str(num_records) + " medical records in the data.")

medical_data_split = updated_medical_data.split(';')
# print(medical_data_split)

medical_records = []

for data in medical_data_split:
  medical_records.append(data.split(','))

# print(medical_records)

medical_records_clean = []

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
# print(medical_records_clean)

for record in medical_records_clean:
  record[0] = record[0].upper()
  print(record[0])

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])

print("Names: " + str(names))
print("Ages: " + str(ages))
print("BMI: "  + str(bmis))
print("Insurance Costs: " + str(insurance_costs))

total_bmi = 0
for n in bmis:
  total_bmi += float(n)

average_bmi = total_bmi / len(bmis)
print("Average BMI: "+ str(average_bmi))

total_cost = 0

for cost in insurance_costs:
    total_cost += float(cost.replace('$', ''))

average_cost = total_cost / len(insurance_costs)
print("Average Insurance Cost: " + str(average_cost))


for i in range(len(names)):
    print(f"{names[i]} is {ages[i]} years old with a BMI of {bmis[i]} and an insurance cost of {insurance_costs[i]}.")



# Add your code here
medical_costs = {}
medical_costs["Marina"] = 6607.0
medical_costs["Vinay"] = 3225.0
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
print(medical_costs)

medical_costs["Vinay"] = 3325.0
print(medical_costs)

total_cost = 0
for cost in medical_costs.values():
  total_cost += cost

average_cost = total_cost / len(medical_costs)
print("Average Insurance Cost: " + str(average_cost))

names = ["Marina", "Vinay", "Connie", "Isaac", "Valentina"]
ages = [27, 24, 43, 35, 52]
zipped_ages = zip(names, ages)

names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)
marina_age = names_to_ages.get("Marina", None)
print("Marina's age is " + str(marina_age))

medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}

medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}

medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}

medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}

medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

print(medical_records)

print("Connie's insurance cost is " + str(medical_records["Connie"]["Insurance_cost"]) + " dollars.")


medical_records.pop("Vinay")

for name, record in medical_records.items():
  print(name + " is a " + str(record["Age"]) + \
  " year old " + record["Sex"] + " " + record["Smoker"] \
  + " with a BMI of " + str(record["BMI"]) + \
  " and insurance cost of " + str(record["Insurance_cost"]))







