
#Multi-Month Sales Analyzer

A Python-based command-line tool designed to track, analyze, and visualize monthly sales data.
This application allows users to input weekly sales figures for multiple months, generates detailed
statistical summaries, and produces a graphical bar chart comparison.

🚀 Features

Robust Data Entry:
• Collects sales data week-by-week (4 weeks per month).
• Validates input to ensure data is numeric and non-negative.

Comprehensive Analysis:
• Calculates Grand Total Sales across all months.
• Calculates Average Monthly Sales.
• Identifies the Best and Worst performing months.
• Identifies the Highest and Lowest single weekly sales figures across the entire dataset.

Data Visualization:
• Uses matplotlib to generate a bar chart comparing total sales per month.
• Visuals include data labels, gridlines, and formatted currency (₹).

🛠️ Prerequisites

To run this project, you need:
• Python 3.x installed on your system.
• The Matplotlib library.

📦 Installation

Save the script:
Save your Python code into a file named sales_analyzer.py.

Install Dependencies:
pip install matplotlib

📖 How to Use

Run the script:
python sales_analyzer.py

Enter Data:
Input the sales amount (integer) for Week 1 through Week 4 for the current month.
The inputs are formatted for Indian Rupees (₹).

Continue or Finish:
The system will ask if you want to enter data for another month (yes/no).

View Results:
• A text summary will appear in the console.
• A popup window will display the bar chart.

📊 Example Output

Console Output:
==================================================
        COMPREHENSIVE MULTI-MONTH SALES ANALYSIS
==================================================
Total Months Analyzed: 3
Grand Total Sales:     ₹150,000.00
Average Monthly Sales: ₹50,000.00
--------------------------------------------------
Best Performing Month:  Month 2 (Total: ₹60,000.00)
Worst Performing Month: Month 1 (Total: ₹40,000.00)
--------------------------------------------------
Highest Single Week Sale:
₹20,000.00 in Week 3 (Month 2)
Lowest Single Week Sale:
₹8,000.00 in Week 1 (Month 1)
==================================================

📝 License
This project is open-source and free to use for educational and personal tracking purposes.

