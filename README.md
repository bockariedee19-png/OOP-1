# OOP-1
# 🌾 Crop Yield Monitoring System

### A Python-Based Object-Oriented Programming Project

The **Crop Yield Monitoring System** is a simple Python application designed to help farmers record crop production information and calculate crop yield per hectare. It allows users to add crop records, view stored records, and monitor the productivity of different crops through a menu-driven interface.

## 📌 Table of Contents

- [About the Project](#-about-the-project)
- [Project Objectives](#-project-objectives)
- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Object-Oriented Programming Concepts](#-object-oriented-programming-concepts)
- [How to Run the Project](#-how-to-run-the-project)
- [Sample Output](#-sample-output)
- [Project Structure](#-project-structure)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

## 📖 About the Project

Crop production is an important part of agriculture. Keeping accurate records of farm size and harvested crops can help farmers understand their farm productivity.

This project provides a basic digital solution for recording crop names, farm areas in hectares, and harvest quantities in kilograms. The system calculates yield per hectare to make crop production information easier to understand.

## 🎯 Project Objectives

- To apply Object-Oriented Programming (OOP) concepts in Python.
- To create and manage crop records.
- To calculate crop yield per hectare.
- To store multiple crop objects using a Python list.
- To provide a simple, user-friendly menu.
- To demonstrate how programming can support agricultural activities.

## ✨ Features

- **Add Crop Records:** Enter the crop name, farm area, and harvest quantity.
- **Calculate Crop Yield:** Calculate the yield per hectare.
- **Display Crop Records:** View saved crop information.
- **Menu-Driven Interface:** Navigate through the system using numbered options.
- **Input Handling:** Reject invalid menu choices and handle non-positive farm areas in the yield calculation.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **IDE:** PyCharm
- **Version Control:** Git
- **Repository Hosting:** GitHub

## 🧠 Object-Oriented Programming Concepts

The project demonstrates the following concepts:

- **Class:** `CropRecord` defines the structure of a crop record.
- **Object:** Each crop entered into the system is represented by a `CropRecord` object.
- **Constructor:** The `__init__()` method initializes crop details.
- **Attributes:** `crop_name`, `area`, and `harvest` store crop information.
- **Instance Method:** `calculate_yield()` calculates crop yield per hectare.
- **List:** A Python list stores multiple crop records.
- **Functions:** `add_crop()` and `display_crops()` organize the program's operations.
- **Loop and Conditional Statements:** The menu allows users to select actions until they choose to exit.

## ▶️ How to Run the Project

### Requirements

- Python 3 installed on your computer.
- PyCharm or another Python-compatible code editor.

### Installation Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/Crop-Yield-Monitoring-System.git
   ```

2. Open the project folder in PyCharm.

3. Run the Python file containing the Crop Yield Monitoring System.

4. Follow the on-screen menu to add or display crop records.

## 💻 Sample Output

```text
=== CROP YIELD MONITORING SYSTEM ===
1. Add Crop Record
2. Display Crop Records
3. Exit

Enter your choice: 1

Enter crop name: Rice
Enter farm area in hectares: 2
Enter harvest in kg: 600

Crop record added successfully!

=== CROP RECORDS ===

Crop Name: Rice
Farm Area: 2.0 hectares
Harvest: 600.0 kg
Yield per Hectare: 300.0 kg
```

### Yield Calculation

The system calculates crop yield using the formula:

**Crop Yield = Total Harvest ÷ Farm Area**

For example:

600 kg ÷ 2 hectares = **300 kg per hectare**

## 📁 Project Structure

```text
Crop-Yield-Monitoring-System/
│
├── crop_yield_monitoring.py
├── README.md
└── .gitignore
```

*Note: Replace `crop_yield_monitoring.py` with your actual Python filename if it is different.*

## 🚀 Future Improvements

Possible improvements include:

- Adding farmer and farm management classes.
- Saving crop records to a file or database.
- Validating user inputs more thoroughly.
- Searching for crops by name.
- Comparing the yields of different crops.
- Generating crop productivity reports.
- Adding a graphical user interface.

## 🌍 Digital Public Goods Principles

The project can support Digital Public Goods principles through:

- **Open Source:** Making the source code publicly available on GitHub.
- **Reusability:** Organizing the code into classes and functions that can be extended.
- **Privacy:** Avoiding unnecessary collection of personal information.
- **Accessibility:** Keeping the menu simple and easy to navigate.

*These principles are project goals; full compliance would require further review and development.*

## 👩‍💻 Author

**Student Project — Crop Yield Monitoring System**

Developed as a Python Object-Oriented Programming project to demonstrate how software can be used to support agricultural record keeping.

---

⭐ *Thank you for checking out the Crop Yield Monitoring System!*
