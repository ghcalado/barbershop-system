# 💈 Barbershop System

> A complete barbershop management system built with Python and SQLite — running in production for a real client.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/status-production-brightgreen?style=flat-square)

---

## 📌 Overview

The **Barbershop System** is a terminal-based management tool designed to help barbershops handle their day-to-day operations efficiently. It covers everything from staff and client registration to appointment scheduling — all stored locally with SQLite, no internet required.

Built for a real client, this project solves real problems: no more paper schedules, no more lost appointments.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🔐 Authentication | Login system with password validation and attempt limiting |
| ✂️ Barber Management | Register and list barbers with contact info |
| 👤 Client Management | Register and list clients with contact info |
| 💰 Service Management | Register services with pricing |
| 📅 Appointment Scheduling | Book appointments with barber, client, date, time and services |
| 📋 Agenda View | View all scheduled appointments sorted by date and time |
| 🗑️ Agenda Reset | Clear all appointments with confirmation prompt |

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Database:** SQLite3 (built-in, no external dependencies)
- **Architecture:** Modular functions with a clean menu-driven CLI

---

## ⚡ Getting Started

### Prerequisites

- Python 3.x installed ([download here](https://www.python.org/downloads/))
- No external libraries needed

### Installation

```bash
# Clone the repository
git clone https://github.com/ghcalado/barbershop-system.git

# Navigate to the project folder
cd barbershop-system
```

### Configuration (recommended)

Set your admin password via environment variable before running:

```bash
# Linux / macOS
export SENHA_BARBEARIA=your_password_here

# Windows
set SENHA_BARBEARIA=your_password_here
```

> If not set, the system falls back to the default password `1234`. **Change this before using in production.**

### Running

```bash
python barbearia.py
```

The database file `barbearia.db` will be created automatically on first run.

---

## 🗂️ Project Structure

```
barbershop-system/
├── barbearia.py     # Main application
├── .gitignore       # Excludes local database from version control
└── README.md        # Project documentation
```

---

## 🖥️ How It Works

```
1. Enter the barbershop name and set up your login
2. Authenticate with your admin password (3 attempts max)
3. Navigate the menu to manage barbers, clients, services and appointments
4. All data is persisted locally in a SQLite database
```

---

## 🔒 Security Notes

- Password is read from the `SENHA_BARBEARIA` environment variable
- The database file (`barbearia.db`) is excluded from version control via `.gitignore` to protect client data
- Login confirmation prevents typos on first access

---

## 🚀 Roadmap

- [ ] Web interface with Flask
- [ ] WhatsApp notifications for appointment reminders
- [ ] Appointment cancellation and rescheduling
- [ ] Financial reports by barber and service
- [ ] Multi-barbershop support

---

## 👨‍💻 Author

**Ghabriel Calado**
Python & Web Developer | CS Student

[![GitHub](https://img.shields.io/badge/GitHub-ghcalado-181717?style=flat-square&logo=github)](https://github.com/ghcalado)

---

> *This project is part of a portfolio of real-world systems built for small businesses.*
