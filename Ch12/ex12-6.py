df = pd.read_excel("季業績資料 4.xlsx", sheet_name="業務部")

print("每一列:")
print(df)

print("\n每一欄:")
for col in df.columns:
    print(f"{col}: {df[col].tolist()}")