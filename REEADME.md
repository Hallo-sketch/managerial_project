# Cost of Poor Quality: Quantifying the Cyberpunk 2077 Launch Disaster
**Context:** Managerial Accounting Class Presentation on Cost-of-Quality Failures

## 📌 Project Overview

This repository contains a synthetic control / counterfactual forecasting model. It was built to illustrate how a single data-quality error can cascade into wildly misleading analysis, and to quantify the devastating financial impact of a botched product launch.

Using CD Projekt Red (Ticker: `CDR.WA`) and the disastrous *Cyberpunk 2077* release as a backdrop, this project uses a Long Short-Term Memory (LSTM) neural network to model a "parallel universe" where the quality failure never happened, allowing us to measure the exact market capitalization wiped out by the event.

Two versions of the analysis are included:
- **`research3.ipynb`** – version with the deliberate data-quality bug.
- **`research-1.ipynb`** – A cleaner version using proper dynamic currency conversion.

## 🧠 Methodology: The Counterfactual Forecast

### 1. The "Happy Path" LSTM
The model utilizes a lightweight LSTM architecture (10-5-5 units, 15 epochs). This was an intentional design choice. The goal was not to build a hyper-accurate, stationary algorithmic trading model. Instead, the LSTM was configured to produce a smooth, optimistic, momentum-driven forecast—exactly the kind of overly confident projection stakeholders would have relied on right before the quality failure became visible.

### 2. Strict Pre-Disaster Training Window
To accurately simulate a counterfactual, the model had to be completely blind to the upcoming disaster.
- The training data was explicitly cut off on **August 27, 2020**.
- We used a strict 40-record holdout to ensure the model was trained entirely on pre-launch hype data, representing the exact view leadership would have had weeks before the game released.

### 3. The 120-Day Event Horizon
The model was asked to forecast 120 days into the future. This specific window was chosen very deliberately because it perfectly captures:
1. The final, aggressive marketing hype phase leading up to the December 2020 launch.
2. The immediate post-launch collapse triggered by game-breaking bugs, platform delistings, and mass refunds.

## 📉 The "Data Quality" Injection

To illustrate how vulnerable financial pipelines are to poor data quality, a deliberate scaling factor was introduced early in the preprocessing pipeline in the teaching version (`research3.ipynb`):

```python
dq = 0.25
cdr.iloc[:, :5] = cdr.iloc[:, :5].mul(dq)
```

This single line serves as the root cause of the entire misleading analysis. (The cleaner notebook `research-1.ipynb` uses the correct dynamic PLN→USD conversion via OpenBB instead.)

## 📊 Real-World Analyst Context (2020)

The LSTM forecast was intentionally calibrated to match the overly optimistic analyst sentiment that actually existed at the time. Specific examples include:

- **DM BOŚ** — Targets in the **480–520 PLN** range (≈ $120–$130+ USD).
- **Trigon Dom Maklerski** — Very bullish targets around **480–500 PLN** (≈ $120–$125 USD).
- **mBank Securities** — Strong Buy ratings with targets near **450 PLN** (≈ $112–$115 USD).
- **Erste Group** — Targets around **400–430 PLN** (≈ $100–$108 USD).

The model’s peak near $150 USD after conversion was realistic and consistent with the upper end of these forecasts — before the quality disaster became visible.

## 💰 The $22 Billion Impact Calculation

The final figure was calculated by comparing:
- The **endpoint** of the LSTM forecast (predicted price at the end of the 120-day window)
- The **actual stock price endpoint** on the same date

This difference was multiplied by the approximate number of shares outstanding. The result shows the market capitalization that would have been preserved in the “parallel universe” where the quality failure never occurred.

## 🎯 Key Takeaway

**One tiny data-quality mistake** — such as an incorrect scaling factor applied early in the pipeline — can produce forecasts that look completely reasonable and match professional analyst consensus at the time. Yet when reality hits, the financial impact can be catastrophic.

This project demonstrates that data quality is not a technical detail. It is a strategic business risk. Even sophisticated models and optimistic market sentiment cannot protect you from the downstream consequences of bad data.
