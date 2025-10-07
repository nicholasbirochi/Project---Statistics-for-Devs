import pandas as pd
import matplotlib.pyplot as plt

# Base Data
dict_faturamento = {
    'data_ref': [
        '2023-01-01', 
        '2020-02-01', 
        '2021-03-01', 
        '2022-04-01', 
        '2023-05-01',
        '2023-06-01', 
        '2020-07-01', 
        '2021-08-01', 
        '2022-09-01', 
        '2023-10-01',
        '2022-11-01', 
        '2023-12-01',
    ],
    'valor': [
        400000, 
        890000, 
        760000, 
        430000, 
        920000,
        340000, 
        800000, 
        500000, 
        200000, 
        900000,
        570000, 
        995000,
    ]
}

# DataFrame + dates
df = pd.DataFrame(dict_faturamento)
df['data_ref'] = pd.to_datetime(df['data_ref'], errors='coerce')
df = df.sort_values('data_ref').reset_index(drop=True)

# formatted month for x-axis
df['month_ref'] = df['data_ref'].dt.strftime('%Y-%m')

# Average sales
avg_sales = df['valor'].mean()
print(f"Average sales: {avg_sales:,.2f}")

# Bar chart (month × value)
plt.figure()
plt.bar(df['month_ref'], df['valor'])
plt.title('Revenue by Month (Bar)')
plt.xlabel('Month')
plt.ylabel('Value')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('bar_chart.png', dpi=150, bbox_inches='tight')
plt.show()

# Line chart (month × value)
plt.figure()
plt.plot(df['month_ref'], df['valor'], marker='o')
plt.title('Revenue by Month (Line)')
plt.xlabel('Month')
plt.ylabel('Value')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('line_chart.png', dpi=150, bbox_inches='tight')
plt.show()
