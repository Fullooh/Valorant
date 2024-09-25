# Valorant Predictive Model

## Project Overview
This project aims to build a predictive model for Valorant, focusing on player performance, match outcomes, and team composition strategies. The system is designed to provide real-time insights during gameplay by collecting data from third-party websites, processing and storing the data in a PostgreSQL database, and utilizing machine learning models for predictions. The project utilizes a C++ backend for performance-critical tasks and a Python frontend for data input and visualization.

## Key Features
- **Data Collection:** Scraping data from platforms like tracker.gg and blitz.gg to gather player stats, match histories, and agent compositions.
- **Data Processing:** Cleaning and preprocessing the data using Python libraries such as Pandas and SQLAlchemy.
- **Model Training:** Using scikit-learn for initial model prototyping in Python, then porting the logic to a high-performance C++ backend using MLPack.
- **C++ Backend:** High-performance core for predictions, interacting with PostgreSQL for data storage.
- **REST API:** A C++ REST API using CppREST SDK to facilitate communication between the Python frontend and C++ backend.
- **Python Frontend:** Flask-based web UI for user input, data visualization, and sending data to the C++ backend for predictions.

## Technology Stack
- **Languages:** C++, Python
- **Libraries:**
  - **C++:** Eigen, MLPack, CppREST SDK, libpqxx
  - **Python:** Pandas, scikit-learn, SQLAlchemy, Flask, BeautifulSoup, Selenium
- **Database:** PostgreSQL
- **Tools:** CLion, PyCharm, Git, GitHub Actions for CI/CD

## Project Structure
- `/src` - Source code for C++ and Python modules.
- `/data` - Directory for raw and preprocessed datasets.
- `/models` - Trained models stored as binary files.
- `/docs` - Project documentation, architecture diagrams, and reports.
- `/tests` - Unit and integration tests for both C++ and Python.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for review.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
