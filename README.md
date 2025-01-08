# Django Infboard API

![alt text](<Captura de tela 2025-01-07 223849.png>)

## Description
The Django Infboard API is a service to collect and manage information from Twitter influencers. This API allows you to read, update, and delete tweets on the dashboard. The application uses SQLite DB to save the data.
Returns a list of all tweets from the chosen filter.

### GPT
```
POST /api/ai/
```
Creates an interaction with ChatGPT.
#### Parameters:
- `Question` (string): Question body.

#### SQLite DB:
![alt text](<Captura de tela 2025-01-07 230152.png>)

## Installation
### Using Docker
1. Clone the repository:
    ```bash
    git clone https://github.com/tdiascontato/django-infboard.git
    ```
2. Navigate to the project directory:
    ```bash
    cd django-infboard
    ```
3. Build the Docker image:
    ```bash
    docker build -t django-infboard .
    ```
4. Run the Docker container:
    ```bash
    docker run -d -p 8000:8000 django-infboard
    ```

### Without Docker
1. Clone the repository:
    ```bash
    git clone https://github.com/tdiascontato/django-infboard.git
    ```
2. Navigate to the project directory:
    ```bash
    cd django-infboard
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the migrations:
    ```bash
    python manage.py migrate
    ```
5. Build the project:
    ```bash
    python manage.py collectstatic
    ```
6. Start the server:
    ```bash
    python manage.py runserver
    ```

## Contribution
1. Fork the project.
2. Create a new branch:
    ```bash
    git checkout -b my-new-feature
    ```
3. Make your changes and commit:
    ```bash
    git commit -m 'Add new feature'
    ```
4. Push to the remote repository:
    ```bash
    git push origin my-new-feature
    ```
5. Open a Pull Request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact
For more information, contact [your-email@example.com](mailto:your-email@example.com).
