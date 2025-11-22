import sys
import matplotlib.pyplot as plt

def get_monthly_sales(month_number):
    """Collects weekly sales data for a specific month."""
    weeks_of_month = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
    weekly_sales = {}

    print(f"\n--- Enter Sales Data for MONTH {month_number} (in ₹) ---")

    for week in weeks_of_month:
        while True:
            try:
                sales = int(input(f"Enter sales for {week} (₹): "))
                if sales < 0:
                    print("Sales cannot be negative. Please enter a positive value.")
                    continue
                weekly_sales[week] = sales
                break
            except ValueError:
                print("Invalid input. Please enter a numeric integer value.")

    return weekly_sales

def summarize_all_months(all_months_data):
    """Calculates and prints text-based statistics."""
    if not all_months_data:
        print("\nNo sales data entered to summarize.")
        return

    grand_total = 0
    best_month = {'month': 0, 'total': -1}
    worst_month = {'month': 0, 'total': sys.maxsize}
    highest_single_sale = {'month': 0, 'week': '', 'value': -1}
    lowest_single_sale = {'month': 0, 'week': '', 'value': sys.maxsize}

    for month_num, total_sales, weekly_sales_dict in all_months_data:
        grand_total += total_sales

        # Track Best and Worst Month
        if total_sales > best_month['total']:
            best_month.update({'month': month_num, 'total': total_sales})
        if total_sales < worst_month['total']:
            worst_month.update({'month': month_num, 'total': total_sales})

        # Track Best and Worst Specific Week
        for week_name, sale_value in weekly_sales_dict.items():
            if sale_value > highest_single_sale['value']:
                highest_single_sale.update({'month': month_num, 'week': week_name, 'value': sale_value})
            if sale_value < lowest_single_sale['value']:
                lowest_single_sale.update({'month': month_num, 'week': week_name, 'value': sale_value})

    num_months = len(all_months_data)
    average_monthly_sales = grand_total / num_months

    print("\n" + "="*50)
    print("        COMPREHENSIVE MULTI-MONTH SALES ANALYSIS")
    print("="*50)
    print(f"Total Months Analyzed: {num_months}")
    print(f"Grand Total Sales:     ₹{grand_total:,.2f}")
    print(f"Average Monthly Sales: ₹{average_monthly_sales:,.2f}")
    print("-" * 50)
    print(f"Best Performing Month:  Month {best_month['month']} (Total: ₹{best_month['total']:,.2f})")
    print(f"Worst Performing Month: Month {worst_month['month']} (Total: ₹{worst_month['total']:,.2f})")
    print("-" * 50)
    print(f"Highest Single Week Sale:")
    print(f"₹{highest_single_sale['value']:,.2f} in {highest_single_sale['week']} (Month {highest_single_sale['month']})")
    print(f"Lowest Single Week Sale:")
    print(f"₹{lowest_single_sale['value']:,.2f} in {lowest_single_sale['week']} (Month {lowest_single_sale['month']})")
    print("="*50)

def plot_monthly_sales_chart(all_months_data):
    """Generates a bar chart comparing total sales per month."""
    if not all_months_data:
        return

    # Extract data for plotting
    month_labels = [f"Month {data[0]}" for data in all_months_data]
    totals = [data[1] for data in all_months_data]

    # Create the figure
    plt.figure(figsize=(10, 6))

    # Create bars
    bars = plt.bar(month_labels, totals, color='skyblue', edgecolor='navy')

    # Add title and labels
    plt.title('Total Sales Comparison Per Month', fontsize=16, fontweight='bold')
    plt.xlabel('Months', fontsize=12)
    plt.ylabel('Total Sales (₹)', fontsize=12)

    # Add grid lines behind bars (axis='y')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Add text labels on top of each bar
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height,
                 f'₹{height:,.0f}',
                 ha='center', va='bottom')

    # Adjust layout to prevent clipping
    plt.tight_layout()

    print("\nGenerating Sales Chart...")
    plt.show()

def main():
    all_months_data = []
    month_counter = 1

    print("Welcome to the Multi-Month Sales Analyzer!")

    while True:
        weekly_sales_dict = get_monthly_sales(month_counter)
        month_total = sum(weekly_sales_dict.values())

        # Store tuple: (Month Number, Month Total, Dictionary of Weeks)
        all_months_data.append((month_counter, month_total, weekly_sales_dict))

        print(f"\n>>> Month {month_counter} Total Sales: ₹{month_total:,.2f} recorded.")

        month_counter += 1
        user_input = input("\nDo you want to enter data for another month? (yes/no): ").strip().lower()
        if user_input not in ['yes', 'y']:
            break

    summarize_all_months(all_months_data)

    # Call the plotting function here
    plot_monthly_sales_chart(all_months_data)

    print("\nAnalysis Complete. Thank you!")

if __name__ == "__main__":
    main()