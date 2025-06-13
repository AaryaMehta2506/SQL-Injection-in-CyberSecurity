# 🚨 SQL Injection in CyberSecurity

This project demonstrates **SQL Injection**, a critical web vulnerability, through interactive examples and secure coding practices. It showcases how attackers exploit unvalidated input to inject SQL commands, and how parameterized queries can mitigate such attacks.

## 🚀 Features

- 🛠️ **Vulnerable Web App Demo**: Input fields susceptible to SQL injection.
- 🧪 **Attack Examples**:  
  - `OR 1=1` payload to extract full tables.  
  - `; DROP TABLE` to delete database tables.
- 🔐 **Secure Coding Section**: Rewrite using **parameterized queries** (prepared statements) to prevent injection.
- 📘 **Educational Notebook**: Step-by-step walkthrough of attack mechanics and defenses.
- 🌐 **Technology Stack**: Simple backend (e.g. Node.js/Express or PHP), HTML forms, and SQLite/MySQL.

## 🗂️ Project Structure
SQL-Injection-in-CyberSecurity/
├── vulnerable_app/ # Insecure code sample
│ ├── index.html
│ └── demo.php # Or server.js for Node.js
├── secure_app/ # Fixed version using prepared statements
├── notebook.ipynb # Analysis, payloads, prevention techniques
├── data/ # Sample SQL database files
├── requirements.txt # Dependencies
├── README.md # Project overview
└── LICENSE # MIT License

## ⚙️ Setup Instructions

### 1. 🔄 Clone the Repository
```
git clone https://github.com/AaryaMehta2506/SQL-Injection-in-CyberSecurity.git
cd SQL-Injection-in-CyberSecurity
```
### 2. 🧪 Install Dependencies
Depending on the stack:
For Python/Flask/SQLite:
```
pip install -r requirements.txt
```
For PHP/MySQL:
Ensure PHP and MySQL are installed.
For Node.js/Express:
```
npm install
```
### 3. 🚀 Run the Vulnerable Demo
```
python vulnerable_app/app.py
```
PHP:
```
php -S localhost:8000 -t vulnerable_app
```

## 💡 How Attacks Work
Input like:
```
' OR '1'='1
```
Turns dynamic query:
```
SELECT * FROM users WHERE user = '' OR '1'='1';
```
→ Returns all records due to OR '1'='1' 
Malicious input:
```
'; DROP TABLE users; --
```
→ Executes inline DROP command to delete data

## 🔐 Prevention Best Practices
✅ Parameterized Queries: Use placeholders to separate data from code.

✅ Input Sanitization: Whitelist acceptable formats.

✅ Least Privilege: Database account should have minimal access.

✅ ORM Use: Employ ORM layer to abstract raw SQL

## 🤝 Contributing
Contributions are welcome:

Fork the repo

Create a branch (git checkout -b feature-name)

Commit changes (git commit -m 'Add feature')

Push to your fork and open a Pull Request

## 📄 License
This project is licensed under the [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)

## 👩‍💻 Author

**Aarya Mehta**  
🔗 [GitHub Profile](https://github.com/AaryaMehta2506)

