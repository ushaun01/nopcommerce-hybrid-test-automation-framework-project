 🚀 NopCommerce Hybrid Test Automation Framework using Selenium, Python & PyTest 

 🎯 Project Objective

To automate critical functionalities of the NopCommerce Admin Application using Selenium WebDriver and PyTest by implementing a Hybrid Automation Framework that supports reusable components, data-driven testing, logging, reporting, screenshot capture, and maintainable test scripts.

---

 📌 Project Overview

This project is a Hybrid Test Automation Framework developed for the NopCommerce Admin Application using Python, Selenium WebDriver, and PyTest.

The framework follows industry-standard automation practices such as:

✅ Page Object Model (POM)

✅ Data-Driven Testing

✅ Configuration Management

✅ Logging

✅ Screenshot Capture

✅ HTML Reporting

✅ Reusable Utilities

The framework is scalable, maintainable, and easy to extend for future automation requirements.

---

 🤔 Why Hybrid Framework?

This framework combines multiple automation framework concepts:

🔹 Page Object Model (POM)

🔹 Data-Driven Testing

🔹 PyTest Framework

🔹 Configuration Management

🔹 Logging

🔹 HTML Reporting

Hence, it is designed as a Hybrid Test Automation Framework.

---

 🛠️ Tech Stack

* 🐍 Python
* 🌐 Selenium WebDriver
* 🧪 PyTest
* 📊 OpenPyXL
* 📄 Page Object Model (POM)
* 📈 HTML Reports
* 🔧 Git
* 💻 GitHub

---

📋 Requirements

* Python 3.x
* Selenium WebDriver
* PyTest
* OpenPyXL
* Google Chrome Browser
* ChromeDriver

---

📁 Project Structure

```text
nopcommerce-hybrid-test-automation-framework-project

├── base_pages
├── configurations
├── logs
├── reports
├── screenshots
├── test_cases
├── test_data
├── utilities
└── README.md
```

---

✅ Test Scenarios Covered

### 🔐 Admin Login Test

* Verify login with valid credentials
* Verify successful dashboard navigation

**File:** `test_admin_login.py`

---

### 📊 Data-Driven Login Test

* Read multiple login credentials from Excel
* Execute login test for each dataset
* Validate expected results

**File:** `test_admin_login_datadriven.py`

**Data Source:** `admin_login_data.xlsx`

---

### 👤 Add Customer Test

* Login to Admin Panel
* Navigate to Customer Module
* Add New Customer
* Verify customer creation

**File:** `test_add_customer.py`

---

### 🔎 Search Customer Test

* Search Customer by Email
* Search Customer by Name
* Validate search results

**File:** `test_search_customer.py`

---

## ⚙️ Utilities Implemented

### 📄 Configuration Reader

Reads application configuration data such as:

* URL
* Username
* Password

**File:** `read_properties.py`

---

 📊 Excel Utilities

Used for Data-Driven Testing.

Functions include:

* Get Row Count
* Get Column Count
* Read Cell Data
* Write Cell Data

**File:** `excel_utilities.py`

---

📝 Custom Logger

Generates detailed execution logs to support debugging and result tracking.

**File:** `custom_logger.py`

📍 Log Location: `logs/nopcommerce.log`

---

📸 Screenshot Capture

The framework automatically captures screenshots when test execution fails.

📂 Screenshot Location:

```text
screenshots/
```

Example:

```text
invalid_login.png
```

---

 ⚡ Installation

 📥 Clone Repository

```bash
git clone https://github.com/ushaun01/nopcommerce-hybrid-test-automation-framework-project.git
```

📂 Navigate to Project Directory

```bash
cd nopcommerce-hybrid-test-automation-framework-project
```

 📦 Install Required Packages

```bash
pip install -r requirements.txt
```

---

 ▶️ Test Execution

Run All Test Cases

```bash
pytest -v
```

Run Login Test

```bash
pytest test_cases/test_admin_login.py -v
```

### Run Data-Driven Login Test

```bash
pytest test_cases/test_admin_login_datadriven.py -v
```

### Run Add Customer Test

```bash
pytest test_cases/test_add_customer.py -v
```

### Run Search Customer Test

```bash
pytest test_cases/test_search_customer.py -v
```

---

 📈 Reporting

PyTest HTML Reports are generated after test execution.

The report provides:

✅ Total Test Cases Executed

✅ Passed Test Cases

✅ Failed Test Cases

✅ Execution Time

✅ Detailed Execution Results

📂 Report Location:

```text
reports/
```

---

 ⭐ Key Features

✔ Page Object Model (POM)

✔ Hybrid Framework Design

✔ Data-Driven Testing

✔ Excel Integration using OpenPyXL

✔ Configuration Management

✔ Custom Logging

✔ Screenshot Capture on Failure

✔ HTML Reporting

✔ Reusable Utilities

✔ Selenium WebDriver Automation

✔ PyTest Framework

---

 👩‍💻 Author

 Usha Nazare

🔹 Former Quality Engineer with 3 years of experience in the Automobile Manufacturing Industry.

🔹 Transitioned into Software Testing with hands-on experience in Manual Testing and Automation Testing.

🔹 Skilled in Python, Selenium WebDriver, PyTest, API Testing, MySQL, Git, GitHub, and Jira.

🌟 Passionate about Quality Assurance, Test Automation, and Continuous Learning.
