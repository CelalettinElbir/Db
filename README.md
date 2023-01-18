# E-commerce Website
This project allows users to filter and buy the product they want.

### What can you do?

1. You can filter products by categories like Man/T-shirt.
2. You can filter products by their price size and name.
3. Users can add the product to their favorites. 
4. User can add products to the shop basket. 
5. In the basket user can delete or update products.
6. In favorites user can add the product to the shop basket.
7. User can see his/her old orders.  
8. Users can add a comment to the product they bought and rate them.

### How to Install and Run the Project
#### Packages
1. pip install django-crispy-forms
2. pip install pillow
3. pip install django-mptt


#### Installing 
1. you need to install the packages specified above. 
2. you should go to the directory where the project exists and run manage.py makemigrations and manage.py migrate.
3. run the command 'manage.py runserver' now you can see my website at http://127.0.0.1:8000/.


### How to Use the Project

When you enter the website you will see a page where you can filter by categories.


![T-shirt-1](https://user-images.githubusercontent.com/73540960/212908707-1ba20056-114b-4e97-9f33-b44f2c25ee0e.jpg)


After you filter by category you will redirect to a page like below. You can filter by price and color and size.

![image](https://user-images.githubusercontent.com/73540960/213199594-a1584b9c-8c9f-4c90-91a1-fe79ce420284.png)

after you click on the product you want you will redirect to a detail page. On this page, you can add the product to your favorites or you can add the product to your Shop basket.

![image](https://user-images.githubusercontent.com/73540960/213201386-8903c4ac-c7ac-4843-b6e9-c010e7945ac6.png)

in the profile, the page user can edit and update his addresses, credit card, and personal information and see comments. 

![image](https://user-images.githubusercontent.com/73540960/213202810-8af8216e-02ef-48a1-ade4-18388e046ae8.png)

### Favorite Page

On the favorites page, you can add the product to the card or delete it from favorites.
![image](https://user-images.githubusercontent.com/73540960/213203778-28b6457f-3d4f-4adf-80c9-e4f924fa9cb6.png)

### Shop Basket Page

you can edit the amount of product and delete your productsç
![image](https://user-images.githubusercontent.com/73540960/213210187-3a983e38-fb08-4539-b4e8-175da3856f23.png)

### Checkout page

you need to set the default address and credit card to buy items.

![image](https://user-images.githubusercontent.com/73540960/213210932-3f0aa695-ec51-4f76-9787-b3acd4ea27d5.png)

### Address Page

![image](https://user-images.githubusercontent.com/73540960/213211129-a542b5b1-5a7a-4f28-90c4-8cc8abaf7ecf.png)


### Credit Card Page

![image](https://user-images.githubusercontent.com/73540960/213211223-efc9e534-f269-488f-86ed-e1a2887342dc.png)


### Order Page 

after you bought your items. you can add see the product you bought. you can go previous order page from your profile.

![image](https://user-images.githubusercontent.com/73540960/213212436-269afee7-adc2-4838-96ba-1cef1d8d1a6a.png)

### Order Detail Page

On the order detail page, you can see the items and add comments.

### Add Comment Page 

![image](https://user-images.githubusercontent.com/73540960/213212921-4741b9af-e2af-4e13-8e91-7e95687f15a0.png)







### should be added 
1. order list page 
2. password forgot page.
3. User addresses can store in different tables.





