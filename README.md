# Multi-Month Sales Analyzer

A Python-based command-line tool designed to track, analyze, and visualize monthly sales data.  
This application allows users to input weekly sales figures for multiple months, generates detailed statistical summaries, and produces a graphical bar chart comparison.

---

## 🚀 Features

### Robust Data Entry
- Collects sales data week-by-week (4 weeks per month).
- Validates input to ensure data is numeric and non-negative.

### Comprehensive Analysis
- Calculates **Grand Total Sales** across all months.
- Calculates **Average Monthly Sales**.
- Identifies the **Best** and **Worst** performing months.
- Identifies the **Highest** and **Lowest** single weekly sales figures across the entire dataset.

### Data Visualization
- Uses **Matplotlib** to generate a bar chart comparing total sales per month.
- Visuals include:
  - Data labels
  - Gridlines
  - Properly formatted currency (₹ – Indian Rupees)

---

## 🛠️ Prerequisites

To run this project, you need:

- Python **3.x** installed on your system
- The **Matplotlib** library

---

## 📦 Installation

1. **Save the script**

   Save your Python code into a file named:
2. Install dependencies

   Open your terminal or command prompt and run:

   pip install matplotlib

📖 How to Use

1. Run the script

   python sales_analyzer.py


2. Enter Data

-> Input the sales amount (integer) for Week 1 through Week 4 for the current month.

-> The inputs and outputs are formatted for Indian Rupees (₹).

3. Continue or Finish

After entering data for a month, the system will ask:

Do you want to enter data for another month? (yes/no)

-> Type yes to add another month.

-> Type no to stop input and generate the final report.

4. View Results

-> A text summary will appear in the console.

-> A popup window will display the bar chart comparing total sales per month.
   ```bash
   sales_analyzer.py
