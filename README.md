# Human Development Index (HDI) Prediction Project

Machine learning project that predicts Human Development Index scores using Linear Regression and deploys the model through a Flask web application.

## Project Structure

```
smart bridge/
├── Dataset/
│   └── Human Development Index.csv
├── models/
│   └── hdi_model.pkl
├── src/
│   ├── prepare_dataset.py
│   ├── data_analysis.py
│   ├── train_model.py
│   └── app.py
├── static/
│   └── style.css
├── templates/
│   ├── home.html
│   └── indexnew.html
└── requirements.txt
```

## Setup

```powershell
pip install -r requirements.txt
python src/prepare_dataset.py
python src/data_analysis.py
python src/train_model.py
python src/app.py
```

Open http://127.0.0.1:5000 in your browser.

## Model Features

| Index | Feature |
|------:|---------|
| 2 | Country |
| 4 | HDI Score (target) |
| 5 | Life Expectancy at Birth |
| 6 | Expected Years of Schooling |
| 7 | Mean Years of Schooling |
| 8 | GNI per Capita (PPP $) |

## HDI Tiers

- **Very High**: HDI >= 0.800
- **High**: HDI >= 0.700
- **Medium**: HDI >= 0.550
- **Low**: HDI < 0.550

## Dataset Note

The original Guided-Projects dataset link is unavailable. `prepare_dataset.py` builds a UNDP-style dataset from the open [worldhdi](https://github.com/openwashdata/worldhdi) source with realistic HDI component values.
