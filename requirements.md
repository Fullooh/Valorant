
# **Project Requirements**

## **1. Development Tools**
### **IDEs**
- **C++: CLion** - For efficient C++ development, debugging, and project management.
- **Python: PyCharm** - For Python script development, including data processing, model training, and frontend implementation.

### **Other Tools**
- **Git:** Version control to manage your codebase and collaborate.
- **PostgreSQL:** For data storage and retrieval, allowing both C++ and Python to access preprocessed data.

---

## **2. Libraries and Dependencies**

### **C++ Dependencies**
- **Eigen:** For matrix operations and linear algebra in the C++ backend.
  - Installation: Follow the instructions on the [Eigen website](https://eigen.tuxfamily.org/dox/GettingStarted.html).
- **MLPack:** For implementing machine learning algorithms in the C++ backend.
  - Installation: Use package managers like `apt` (on Ubuntu) or [build from source](https://www.mlpack.org/).
- **CppREST SDK (Casablanca):** To build the REST API for communication between the Python frontend and C++ backend.
  - Installation: Follow instructions on the [CppREST SDK GitHub](https://github.com/microsoft/cpprestsdk).
- **libpqxx:** PostgreSQL client library for C++ to interact with the database.
  - Installation: Use a package manager (`apt-get install libpqxx-dev` for Ubuntu) or build from source.

### **Python Dependencies**
- **Pandas:** For data processing, cleaning, and manipulation.
  - Installation: `pip install pandas`
- **scikit-learn:** For initial model prototyping and machine learning operations in Python.
  - Installation: `pip install scikit-learn`
- **SQLAlchemy:** For interacting with the PostgreSQL database to store and retrieve data.
  - Installation: `pip install SQLAlchemy`
- **Flask:** To develop the web-based frontend for user input and visualizations.
  - Installation: `pip install flask`
- **Requests:** For making API calls from the Python frontend to the C++ backend.
  - Installation: `pip install requests`
- **BeautifulSoup & Selenium (Optional):** For web scraping player stats and match history if APIs are not available.
  - Installation: 
    ```bash
    pip install beautifulsoup4
    pip install selenium
    ```
- **psycopg2:** PostgreSQL adapter for Python to interact with the database.
  - Installation: `pip install psycopg2`

---

## **3. API Endpoints**

### **REST API (C++ Backend)**
1. **`/predict`**
   - **Method:** POST
   - **Description:** Accepts player stats, match data, and team compositions from the Python frontend. Uses the C++ backend to run predictions and returns the results.
   - **Request Body (JSON):**
     ```json
     {
       "player_stats": {...},
       "team_compositions": [...],
       "map": "Ascent",
       "round_economy": {...}
     }
     ```
   - **Response (JSON):**
     ```json
     {
       "win_probability": 0.75,
       "recommended_strategy": "Aggressive push"
     }
     ```

2. **`/data`**
   - **Method:** GET
   - **Description:** Fetches the processed data from the PostgreSQL database for analysis or debugging purposes.
   - **Response (JSON):**
     ```json
     {
       "data": [...]
     }
     ```

3. **`/train`** (Optional)
   - **Method:** POST
   - **Description:** Triggers model training on the C++ backend using the latest dataset.
   - **Response:** Status message indicating success or failure.

---

## **4. Database Schema Overview**
- **Tables:**
  1. **`player_stats`** - Contains columns for player performance metrics (e.g., KDA, win rate, average damage).
  2. **`match_history`** - Stores data for historical matches (e.g., map, agent compositions, round outcomes).
  3. **`round_economy`** - Records the economy status for each round in historical match data.

---

## **5. Additional Considerations**
- **Security:** Implement API key authentication for REST API endpoints to secure communication between the frontend and backend.
- **Error Handling:** Add proper error handling and validation mechanisms for API requests.
- **Logging:** Implement logging (both in Python and C++) for debugging and monitoring purposes.

---

This `requirements.md` file outlines the tools, libraries, dependencies, and API endpoints needed for the project, ensuring you have a clear roadmap for the technical aspects. You can expand on each section as needed during development.