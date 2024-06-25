import psycopg2

class Food:
    def __init__(self, id, name, price, rating):
        self.id = id
        self.name = name
        self.price = price
        self.rating = rating

conn = psycopg2.connect(
    host='127.0.0.1',
    port=5432,
    dbname='postgres',
    user='postgres',
    password='12345'
)
cursor = conn.cursor()

def read_all_food():
    select_query = "SELECT * FROM food"
    cursor.execute(select_query)
    foods = cursor.fetchall()
    for food in foods:
        print(food)

def read_one_food(food_id):
    select_query = "SELECT * FROM food WHERE id = %s"
    cursor.execute(select_query, (food_id,))
    food = cursor.fetchone()
    if food:
        print(food)
    else:
        print(f"No food found with ID {food_id}")

def add_food():
    name = input('Enter name of food: ')
    price = float(input('Enter price of food: '))
    rating = int(input('Enter rating of food: '))
    insert_query = f"INSERT INTO food (name, price, rating) VALUES ('{name}', {price}, {rating})"
    cursor.execute(insert_query)
    conn.commit()
    print('Food added successfully!')

def update_food():
    food_id = int(input('Enter food ID to update: '))
    new_price = float(input('Enter new price: '))
    update_query = f"UPDATE food SET price = {new_price} WHERE id = {food_id}"
    cursor.execute(update_query)
    conn.commit()
    print('Food updated successfully!')

def delete_food():
    food_id = int(input('Enter food ID to delete: '))
    delete_query = f"DELETE FROM food WHERE id = {food_id}"
    cursor.execute(delete_query)
    conn.commit()
    print('Food deleted successfully!')

while True:
    print("\n1. Add food\n2. View all food\n3. View one food\n4. Update food\n5. Delete food\n6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_food()
    elif choice == 2:
        read_all_food()
    elif choice == 3:
        food_id = int(input("Enter food ID to view: "))
        read_one_food(food_id)
    elif choice == 4:
        update_food()
    elif choice == 5:
        delete_food()
    elif choice == 6:
        break
    else:
        print("Choose only from 1 to 6!")

cursor.close()
conn.close()
