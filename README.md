 

Breast Cancer Classification Using Machine Learning

This repository contains a machine learning pipeline to classify breast cancer diagnoses as malignant or benign using the Breast Cancer Wisconsin (Diagnostic) dataset. The project demonstrates data preprocessing, exploratory data analysis, and model preparation to achieve effective predictions.

---

 Dataset

The dataset used in this project is the **Breast Cancer Wisconsin (Diagnostic)** dataset, sourced from [Kaggle](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data).

- *ath to dataset files: `C:\Users\User\.cache\kagglehub\datasets\uciml\breast-cancer-wisconsin-data\versions\2\data.csv`
- Number of rows: 569
- Number of columns: 33
- Target variable: `diagnosis`
  - `M` = Malignant
  - `B` = Benign

---

 Project Workflow

 1. Data Loading and Exploration
- The dataset was loaded into a Pandas DataFrame.
- Null values in the `Unnamed: 32` column were removed as it contained no meaningful information.
- The `diagnosis` column was encoded:
  - `M` → 1
  - `B` → 0
- Basic dataset statistics and data types were inspected using `.info()` and `.describe()`.

2. Data Preprocessing
- **StandardScaler**: Features were normalized to improve model performance.
- **Train-test split**: Dataset was divided into training and testing sets (80% training, 20% testing).

3. Exploratory Data Analysis
- **Distribution of the target variable**: A bar chart visualized the count of malignant and benign cases.
- **Correlation matrix**: A heatmap was generated to show feature correlations.

4. Feature Selection
- Correlation analysis was used to identify features with the strongest relationships to the target variable.

---

Code Usage

 1. Clone Repository

```bash
git clone <repository_url>
cd <repository_name>
```
2. Install Dependencies
Ensure you have Python installed with the required libraries:
```bash
pip install numpy pandas seaborn scikit-learn matplotlib
```

3. Run the Code
The primary script (`classification_pipeline.py`) preprocesses the dataset and trains the model:
```bash
python classification_pipeline.py
```

---

Results
- **Exploratory Data Analysis**:
  - Visualizations showed that `radius_mean`, `perimeter_mean`, and `area_mean` had strong positive correlations with the diagnosis.
- **Train-Test Split**:
  - The dataset was effectively split for training and evaluation.
- **Normalization**:
  - Data scaling improved the model's interpretability and accuracy.

---

Future Work
- Implement advanced machine learning models like Support Vector Machines (SVM), Random Forests, or Neural Networks.
- Perform hyperparameter tuning for better performance.
- Add deployment capabilities via a web interface or API.

---

Contributing
Feel free to contribute by submitting issues or pull requests. Your help is appreciated!

---
License
This project is open-source and available under the MIT License.
