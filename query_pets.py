import sqlite3
# 2. The purpose of the person_pet table is to estabilish relatinoships. A owner can have multiple pets this solves that edge case. 
# Also l created create_pets_data.py to create the database and tables. I couldnt the pets.db set up with no code from the pdf 

def main():
    conn = sqlite3.connect('pets.db')
    cursor = conn.cursor()

    while True:
        user_input = input("Enter person's ID (-1 to exit): ")
        if user_input.strip() == "-1":
            break

        try:
            person_id = int(user_input)
        except ValueError:
            print("That is not a number try again")
            continue

        cursor.execute("SELECT * FROM person WHERE id = ?", (person_id,))
        person = cursor.fetchone() # Fetch the person with the given ID

        if not person:
            print("Person id entered does not exist.") 
            continue
        # The numbers are columns l am targeting what l want to output 
        print(f"{person[1]} {person[2]}, {person[3]} years old")

        # 3.C.2 Print all the data of that specific persion 
        cursor.execute("""
            SELECT pet.name, pet.breed, pet.age, pet.dead
            FROM pet
            JOIN person_pet ON pet.id = person_pet.pet_id
            WHERE person_pet.person_id = ?
        """, (person_id,))

        pets = cursor.fetchall()

        if pets:
            print("\nAll the pets of the owner below :")
            for pet in pets:
                print(f"{person[1]} {person[2]} owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old.")
        else:
            print("No pets found for the person id you entered person.\n")

    conn.close()

if __name__ == "__main__":
    main()