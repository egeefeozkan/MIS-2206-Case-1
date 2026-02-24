import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. VERİ YÜKLEME
# Dosya adının 'Coffe_sales.csv' olduğundan emin ol
df = pd.read_csv('/content/Coffe_sales.csv') 

# 2. ETL VE DÜZENLEME
# Tarih sütununu gerçek tarih formatına çevirelim
df['Date'] = pd.to_datetime(df['Date'])

# 3. GÖRSELLEŞTİRME
plt.figure(figsize=(16, 7))
sns.set_theme(style="whitegrid")

# [CHART 1]: SAATLİK GELİR AKIŞI
plt.subplot(1, 2, 1)
hourly_rev = df.groupby('hour_of_day')['money'].sum()
sns.lineplot(x=hourly_rev.index, y=hourly_rev.values, marker='o', color='#d95f02', linewidth=3)
plt.fill_between(hourly_rev.index, hourly_rev.values, color='#d95f02', alpha=0.1)
plt.title('Chart 1: Hourly Sales Velocity (Peak Analysis)', fontsize=15, fontweight='bold')
plt.xlabel('Hour of the Day (0-23)', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)

# [CHART 2]: ÜRÜN BAZLI GELİR DAĞILIMI
plt.subplot(1, 2, 2)
coffee_rev = df.groupby('coffee_name')['money'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=coffee_rev.values, y=coffee_rev.index, palette='copper')
plt.title('Chart 2: Top 10 Products by Revenue', fontsize=15, fontweight='bold')
plt.xlabel('Total Revenue ($)', fontsize=12)

plt.tight_layout()
plt.show()

# Rapor için kaydet
plt.savefig('Coffee_Final_Analysis.png', dpi=300)

