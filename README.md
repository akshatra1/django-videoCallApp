
# Django Video Call App with ZegoClouD API

This Django application provides a simple platform for users to register, log in, create and join meetings, and participate in video and audio calls using the Zego Video Call API.

## Features

- User Registration: Users can create accounts with email and password.
- User Authentication: Secure login system for registered users.
- Create Meeting Rooms: Registered users can create new meeting rooms.
- Join Meetings: Users can join meetings created by others.
- Video Call: Real-time video calls powered by the Zego Video Call API.
- Audio Call: Real-time audio calls powered by the Zego Video Call API.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/videoCallapp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd videoCallapp
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Configure Zego Video Call API:

   - Sign up for a Zego account and obtain API credentials.
   - Update the `videocall.html` file with your Zego API credentials.
     - update the appID
     - serverSecret

7. Migrate the database:

   ```bash
   python manage.py migrate
   ```

8. Create a superuser (admin):

   ```bash
   python manage.py createsuperuser
   ```

9. Start the development server:

   ```bash
   python manage.py runserver
   ```

10. Access the app in your web browser at `http://localhost:8000/`.

## Usage

1. Register an account or log in with your existing credentials.
2. Create a new meeting room or join an existing one.
3. Initiate video or audio calls within the meeting room using the provided buttons.

## Contributing

Contributions are welcome! Please follow these guidelines when contributing to this project:

- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and ensure they work as expected.
- Create clear and concise commit messages.
- Push your branch to your forked repository.
- Open a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Zego Video Call API documentation: [https://www.zego.im](https://www.zego.im)
- Django documentation: [https://docs.djangoproject.com](https://docs.djangoproject.com)

## Contact

If you have any questions or need further assistance, feel free to contact us at akshatrauday@gmail.com.

Happy coding! 🚀
![Screenshot (21)](https://github.com/akshatra1/django-videoCallApp/assets/71605280/90df2383-7893-4b8d-92f0-b85a3ceba1a1)
![Screenshot (22)](https://github.com/akshatra1/django-videoCallApp/assets/71605280/6a066f24-8b17-486a-b564-a834accb8aed)
![Screenshot (23)](https://github.com/akshatra1/django-videoCallApp/assets/71605280/3498d320-2ec6-44ac-8765-f1005eb8acfe)
![Screenshot (28)](https://github.com/akshatra1/django-videoCallApp/assets/71605280/e80364cf-9ed6-4838-ae3c-6be091b77f03)
![Screenshot (29)](https://github.com/akshatra1/django-videoCallApp/assets/71605280/0c0cccfd-1f8f-4534-bb14-edcae895dafb)
![Screenshot (27)](https://github.com/akshatra1/django-videoCallApp/assets/71605280/508afc62-807e-4c9d-93c4-d3c2569da511)


