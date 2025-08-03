# Passbolt User Bootstrap Tool

A simple Python CLI tool to bulk-register users in a Passbolt server using Docker Compose.  
It reads user details from a CSV file and registers them via Passbolt's CLI, capturing the setup URLs for each user.

---

## 🧩 Features

- Bulk user registration using `docker compose exec`
- Reads user data from a CSV file
- Captures registration links
- Outputs results in a timestamped file
- Saves output to a specific directory

---

## 📁 Folder Structure

```
.
├── create_passbolt_users.py       # The main script
├── users.csv                      # Sample CSV input
└── README.md                      # You are here
```

---

## 📄 CSV Format (`users.csv`)

Ensure your CSV file follows this format:

```csv
"FirstName","LastName","Username"
"Jane","Doe","jane.doe@domain.com"
"John","Doe","john.doe@domain.com"
...
```

---

## 🚀 How to Use

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/passbolt-user-bootstrap.git
cd passbolt-bulk-user-register
```

2. **Edit `users.csv`** and add your user data.

3. **Run the script** inside the Passbolt server environment:

```bash
python3 create_passbolt_users.py
```

4. **Check the output file** in the following directory:

```
/opt/passbolt/passbolt_links/passbolt_registration_links/
```

Each line pair contains the email and the setup link:

```
john.doe@domain.com
https://pass.example.org/setup/start/abc.../xyz...
------------------------------
```

---

## 🛠 Requirements

- Python 3.x
- Passbolt running via Docker Compose
- Run the script from inside the Passbolt server host

---

## 🤝 Contributing

Contributions are welcome!  
Please open an issue or submit a pull request to improve the tool.

---

## 📄 License

MIT License – feel free to use, modify, and distribute.
