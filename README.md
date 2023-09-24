# grade_project
this is grade project for my university


# About The Project
White-lamp is an eCommerce application built with Python Django Framework. Some of the features of this project includes custom user model, categories and products, Carts, Incrementing, Decrementing and removing car items, Unlimited Product image gallery, Orders, Payments, after-order functionalities such as reduce the quantify of sold products, send the order received email, clearing the cart, Order completion page as well as generating an invoice for the order. Also we have a Review and Rating system with the interactive rating stars that even allows you to rate a half-star rating. My account functionalities for the customer who can easily edit his profile, profile pictures, change his account password, and also manage his orders and much more.

# Setup Instructions

1. Clone the repository `git clone https://github.com/yahyakmail59/grade_project.git`
2. Navigrate to the working directory `cd grade_project`
3. Open the project from the code editor `code .` or `atom .`
4. Create virtual environment `python -m venv env`
5. Activate the virtual environment `source env/Scripts/activate`
6. Install required packages to run the project `pip install -r requirements.txt`



7. Create database tables
    ```sh
    python manage.py migrate
    ```
8. Create a super user
    ```sh
    python manage.py createsuperuser
    ```
    _GitBash users may have to run this to create a super user - `winpty python manage.py createsuperuser`_
9. Run server
    ```sh
    python manage.py runserver
    ```
10. Login to admin panel - (`http://127.0.0.1:8000`)




Detailed description


1.Login and User Profiles:
    
Patients can create their personal accounts and log in to access their profiles.
2.Hospital Departments:

You can explore different hospital departments, each with its own description and available services.
Doctor Profiles:
 
  Discover detailed profiles of our doctors, including their names, specialties, and contact information.
3.Appointment Booking:
 
  Schedule appointments with your preferred doctors at your convenience.
4.Medical Records:
 
  Access your medical history, including diagnoses, prescriptions, and treatment records.
5.Hospital Store (E-commerce):
  
  Browse and purchase medical supplies and medications securely.
5.Hospital News and Announcements:
  Stay informed about the latest hospital news, announcements, and health articles.
6.Admin Panel:
 
  Our hospital staff uses an admin panel to manage the entire system, ensuring smooth operations.
7.Notification System:
 
  Receive email or SMS notifications for appointment confirmations, reminders, and updates.
8.Search and Filters:
  
  Easily find doctors, departments, and products using our search and filter features.
9.Security and Privacy:
  We prioritize the confidentiality and security of your medical data.
10.Scalability and Performance:
 
  Count on us for a fast and reliable experience, even with a large number of users and data.
11.Backup and Data Recovery:
  We regularly back up your data to prevent any loss.
12.Testing and Quality Assurance:
 
  We've rigorously tested the application to ensure its reliability.
13.Documentation:
 
  You can find comprehensive user and developer documentation for easy reference.
14.Deployment and Hosting:
 
  Our application is hosted on a secure and reliable platform.
15.Maintenance and Support:

  We're here to provide ongoing maintenance and support to address any issues or updates.






  


