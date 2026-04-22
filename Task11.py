import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

df = pd.read_csv('Smartphones.csv')

df[df.select_dtypes(include='number').columns] = (
    df.select_dtypes(include='number')
    .fillna(df.mean(numeric_only=True))
)

for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].fillna(df[col].mode()[0])

for col in df.select_dtypes(include='float').columns:
    df[col] = df[col].astype(int)

target_col = 'rating' if 'rating' in df.columns else df.columns[-1]

X = df.select_dtypes(include='number').drop(columns=[target_col], errors='ignore')

if df[target_col].dtype == object:
    y = pd.factorize(df[target_col])[0]
else:
    y = df[target_col].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Training samples {len(X_train)}")
print(f"Testing  samples {len(X_test)}\n")

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

accuracy  = metrics.accuracy_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred, average='weighted', zero_division=0)
recall    = metrics.recall_score(y_test, y_pred, average='weighted', zero_division=0)
f1        = metrics.f1_score(y_test, y_pred, average='weighted', zero_division=0)

print(f"accuracy  {accuracy:.4f}")
print(f"Precision {precision:.4f}")
print(f"Recall    {recall:.4f}")
print(f"F1 Score  {f1:.4f}")

s_names  = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
s_values = [accuracy, precision, recall, f1]
color_bar   = ['#08737f', '#00898a', '#089f8f', '#39b48e']
plt.figure(figsize=(8, 5))
bars = plt.bar(s_names, s_values, color=color_bar, width=0.5)

for bar, val in zip(bars, s_values):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height() + 0.01,
        f"{val:.2f}",
        ha='center', fontsize=11
    )

plt.ylim(0, 1.1)
plt.xlabel('metric')
plt.ylabel('score')
plt.title('Lab 11')
plt.tight_layout()
plt.show()
