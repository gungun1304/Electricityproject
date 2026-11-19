 def calculate_energy_charge(units):  
   if units <= 100:      
     energy = units * 3     elif units <= 200:  
       energy = (100 * 3) + (units - 100) * 5     else:      
         energy = (100 * 3) + (100 * 5) + (units - 200) * 8      return energy   def generate_bill(name, units):   
           fixed_charge = 50     energy_charge = calculate_energy_charge(units)     tax = (energy_charge + fixed_charge) * 0.05     total_bill = energy_charge + fixed_charge + tax   
           print("\n========== ELECTRICITY BILL ==========")   
           print(f"Consumer Name : {name}")   
           print(f"Units Consumed: {units}")   
           print("--------------------------------------")  
           print(f"Energy Charge : Rs. {energy_charge:.2f}")    
           print(f"Fixed Charge  : Rs. {fixed_charge:.2f}") 
           print(f"Tax (5%)      : Rs. {tax:.2f}")    
           print("--------------------------------------")  
           print(f"Total Bill    : Rs. {total_bill:.2f}")    
           print("======================================")  
           try:     name = input("Enter consumer name: ").strip()  
             units = int(input("Enter units consumed: ")) 
           if not name:     
             print("Invalid name. Please enter a name."
                   elif units < 0:       
                   print("Invalid units. Enter a non-negative number.")  
           else:         generate_bill(name, units)  except ValueError:  
           print("Invalid input. Enter units as a whole number.") 
                   
