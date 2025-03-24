# ✈ Flight Landing Forecast

## 📌 Project Overview
This project predicts future flight landing counts using historical flight landing data. The goal is to analyze trends, detect anomalies, and forecast landings for the next two years using AI/ML models.

erDiagram
    FACT_AIRLINE_TRAFFIC {
        STRING Operating_Airline
        STRING Operating_Airline_IATA_Code
        STRING Aircraft_Model
        STRING Aircraft_Body_Type
        STRING Aircraft_Manufacturer
        STRING GEO_Summary
        STRING GEO_Region
        INT Activity_Period
        DATE Activity_Period_Start_Date
        INT Landing_Count
        INT Total_Landed_Weight
    }

    DIM_AIRLINE {
        STRING Operating_Airline
        STRING Operating_Airline_IATA_Code
    }
    
    DIM_AIRCRAFT {
        STRING Aircraft_Model
        STRING Aircraft_Body_Type
        STRING Aircraft_Manufacturer
    }
    
    DIM_REGION {
        STRING GEO_Summary
        STRING GEO_Region
    }
    
    DIM_DATE {
        DATE FULL_DATE
        INT YEAR
        INT MONTH
        INT DAY
        INT WEEKDAY
        INT QUARTER
    }

    FACT_AIRLINE_TRAFFIC ||--o{ DIM_AIRLINE : "references"
    FACT_AIRLINE_TRAFFIC ||--o{ DIM_AIRCRAFT : "references"
    FACT_AIRLINE_TRAFFIC ||--o{ DIM_REGION : "references"
    FACT_AIRLINE_TRAFFIC ||--o{ DIM_DATE : "references"


## 🔍 Features
- **Data Processing:** Cleans and prepares historical flight landing data.
- **Trend Analysis:** Identifies seasonality, anomalies, and growth patterns.
- **Forecasting:** Predicts flight landings using AI models.
- **LLM Integration:** Uses a lightweight language model to interpret trends.
- **Visualization:** Generates insightful charts for trend analysis.

## 📂 Folder Structure
```
Flight-Landing-Forecast/
│── data/                 # Raw & Processed datasets
│── notebooks/            # Jupyter Notebooks for EDA & modeling
│── src/                  # Source code for data processing & ML
│── outputs/              # Generated reports & plots
│── README.md             # Project documentation
│── requirements.txt      # Dependencies
│── main.py               # Main script for forecasting
```

## 🔧 Setup Instructions
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ShanthoshSaravanan/Flight-Landing-Forecast.git
cd Flight-Landing-Forecast
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Forecasting Model
```sh
python main.py
```

## 📊 Sample Data Preview
| Year | Landing Count |
|------|--------------|
| 2020 | 5000         |
| 2021 | 5200         |
| 2022 | 4800         |
| 2023 | 5100         |
| 2024 | 5300         |

## 📈 Forecast Results (Next 2 Years)
The model predicts the following:
- **2025:** ~5,700 landings (expected growth)
- **2026:** ~5,900 landings (steady increase)

## 🚀 Future Improvements
- Use a more robust ML model for improved accuracy.
- Deploy the model using a web app (Streamlit / Flask).
- Automate data fetching and updates.

## 👨‍💻 Author
**Shanthosh Saravanan**  
 🔗 https://www.linkedin.com/in/shanthosh-saravanan | 🌐 https://portfolium.com/ShanthoshSaravanan/portfolio

---
📌 *If you find this project useful, give it a ⭐ on GitHub!*

