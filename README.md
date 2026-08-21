# Restaurant-System-with-Admin-Functionality

I create a database driven restaurant menu ordering system. The menu will include options for selecting: 
  
  ● Restaurant Information  
  ● Admin Menu <br>
  ● Start New Order

I use Python code to create table in phpLiteAdmin

Table:

<img width="835" height="428" alt="image" src="https://github.com/user-attachments/assets/1d4c98f9-ad04-4866-adb7-644eef6d0e93" />

Menu table: 

<img width="772" height="299" alt="image" src="https://github.com/user-attachments/assets/dd503711-e0ab-433a-aa07-11eee8ae728c" />

Customers table:

<img width="764" height="49" alt="image" src="https://github.com/user-attachments/assets/5458e05e-fbc7-440f-b7e7-8c1a25012c03" />
<img width="762" height="338" alt="image" src="https://github.com/user-attachments/assets/799f49b7-dc23-4682-a250-655edfa7dc25" />

Orders table:

<img width="766" height="402" alt="image" src="https://github.com/user-attachments/assets/3e0a89a8-ee65-4837-bd92-755470144ed7" />

Order_items table:

<img width="764" height="49" alt="image" src="https://github.com/user-attachments/assets/5458e05e-fbc7-440f-b7e7-8c1a25012c03" />
<img width="764" height="206" alt="image" src="https://github.com/user-attachments/assets/2b2ec507-ad99-4038-abd9-24af7c7c98bf" />

Specifications:
main function <br>
  ● Admin Menu <br>
      ● Create menu table <br>
      ● Create orders table <br>
      ● Create order_items table <br>
      ● Create customers table <br>
      ● View all menu items <br>
      ● View all customers table <br>
      ● View past orders <br>
          ○ Show all past order numbers  
          ○ Ask the user for the order number 
              - Display the items in the order number 
      ● Insert menu items 
  ● Start New Order 
      ● Description: The restaurant ordering menu will display the following based on the item’s category. 
      ● Ask the user if they are a new or existing customer. 
          ● If they are a new customer, create a new customer. 
              ○ Ask the user for their name, address, state, city, zip phone number 
              ○ Insert into the customer table 
          ● If they are an existing customer: 
              ○ Ask them for their customer_id (display the current customers so they can see their id) or 
              ○ Search by the customer’s name. 
      ● Create a new order_number (a unique string) with customer_id and date_time 
      ● Insert the customer_id, order_number and date_time into orders 
      ● For example, when you place an order at a store, there is a unique order number. 
        Order Number: ABC-123 
        Order Place: 2026-04-15 19:92:23 00:00:00 
      ● Ask the user what category they’d like to order. 
          ● Appetizers                             
          ● Entrees 
          ● Desserts 
          ● Beverages 
          ● Display the items on the menu with a brief description and allow the customer to order. 
          ● Prompt the user to enter the ID of the menu item they wish to order and the quantity. 
          ● Insert the order_id, menu_id, quantity into order_items 
          ● Think about the scenario when someone tries to order an item that they’ve already ordered. Should you add a new row or change the quantity? 
          ● Allow the user to continue ordering from the menu until they are finished.  
      ● Modify Order 
          ● Display the current order. 
          ● Prompt the user to enter the ID of the item they wish to update/delete. 
          ● Modify accordingly. 
      ● Place Order 
          ● Display all the items in the order in a readable format, including the name, quantity, price, and order time. 
          ● Add them together to print a subtotal. 
          ● Ask the user if they have a coupon. 
              ○ Ask the user if the coupon is a % off or a specific amount off. 
              ○ Subtract the appropriate amount. 
          ● Ask the user if they’d like to tip 15%, 18% or 20%. 
          ● Add New Jersey sales tax of 6.625%. 
          ● Ask the user if they’d like pickup or delivery. 
              ○ If the user chooses delivery, add $5 to their order. 
          ● Print the total of the order. 

Notes:
  ● To reset the AUTOINCREMENT, use this command: 
      ○ DELETE from sqlite_sequence where name='table_name'; 
