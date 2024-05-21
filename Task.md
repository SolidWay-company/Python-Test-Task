# Test Task for Python Developer

## Part 1: Web Development
Create a web application using Django that includes the following features:
Authentication and user authorization:
- User registration.
- Login/logout.
- Password recovery.
User profile management:
- Profile editing (name, email, avatar).
CRUD for blog articles:
- Create, read, update, and delete articles.
- Each article should have a title, content, and publication date.
- Articles should be visible only to authorized users.
API:
- Implement a REST API for managing articles (CRUD operations).
Testing:
- Write unit tests for the core functionalities of the application.
Technical Requirements:
- Use Django and Django REST Framework.
- Store data in PostgreSQL.
- Deploy the application on a local server (e.g., using Docker).
- Utilize Django ORM for database operations.

## Part 2: Bot Development
Develop a Telegram bot that will perform the following tasks:
Bot Commands:
- /start - welcome message.
- /help - list of available commands and their descriptions.
- /latest - get the latest article from the blog (from Part 1).
Interactive Features:
- Subscription to blog updates: users should receive notifications in Telegram when a new article is added.
Technical Requirements:
- The bot should interact with the API of your Django application to retrieve data.

## Part 3: Data Parsing
Write a script for parsing data from a specified website. For example, from the site https://news.ycombinator.com/, parse the latest news and save them to a database.
Script Tasks:
- Collect headlines and URLs of news articles.
- Save this data in a database (you can use the same PostgreSQL database).
Technical Requirements:
- Use BeautifulSoup or Scrapy libraries.
- Implement error handling and logging.
- The script should be scheduled to run (e.g., using cron).

General Requirements
Code Quality:
- Adherence to PEP 8.
- Well-structured and readable code.
- Code documentation and comments where necessary.
Flexibility:
- Ability to easily change configurations (e.g., database connection details).
- Consider scalability of the application.
Repository:
- Host the code in a public repository on GitHub.
- Write a README file with instructions for running and using the application and script.
Evaluation Criteria
Completeness of the task.
Code quality and readability.
Adherence to requirements.
Testing and documentation.
Integration and interaction of all parts of the task (web application, bot, parsing).
