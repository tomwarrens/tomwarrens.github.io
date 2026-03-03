---
title: "Work"
---

Selected projects and technical work relevant to fraud detection, churn prediction, credit risk, and ML system design.

## Demos and Previews

{{< rawhtml >}}
<div class="work-preview-grid">
  <a class="work-preview-card" href="https://drive.google.com/drive/folders/1hFaDuKcl0l3bf48sGy5Hf7hI0S_D-5qj" target="_blank" rel="noopener noreferrer">
    <img src="/yesalpsscreen.png" alt="YesAlps app preview screenshot" loading="lazy">
    <span>YesAlps app demo (Google Drive)</span>
  </a>

  <a class="work-preview-card" href="https://www.kaggle.com/tomwarrens/code" target="_blank" rel="noopener noreferrer">
    <img src="/cardkaggle.png" alt="Kaggle code page preview" loading="lazy">
    <span>Kaggle code portfolio</span>
  </a>

  <a class="work-preview-card" href="https://medium.com/@guerrinitom/run-for-your-leaves-a-simple-path-to-feature-importance-at-inference-time-in-tree-based-models-63afaf5a8c77" target="_blank" rel="noopener noreferrer">
    <img src="/mediumarticle.png" alt="Medium article preview for LightGBM inference-time feature importance" loading="lazy">
    <span>Medium article: LightGBM inference-time FI</span>
  </a>
</div>
{{< /rawhtml >}}

## Portfolio Projects

### YesAlps Ski Booking Web App

**Problem**  
YesAlps had no product comparable to modern booking and marketplace experiences.

**Approach**  
I built a Java web app concept inspired by Airbnb/Booking flows, and added a ski-slopes layer by scraping and integrating slope data directly.

**Result**  
An end-to-end prototype combining backend development, data collection, and interactive map navigation.

{{< rawhtml >}}
<details class="work-tech-details">
  <summary>Show technical details</summary>
  <div class="work-tech-content">
    <p><strong>Stack:</strong> Java web stack, SQL, HTML/CSS, data scraping, geospatial data integration.</p>
    <p><strong>Deployment:</strong> End-to-end web prototype with booking flow and interactive ski-slopes layer.</p>
    <p><strong>Role:</strong> Built product logic and data pipeline from scratch, including scraped slope data.</p>
  </div>
</details>
{{< /rawhtml >}}

### TIM / CladAG Churn Classification Challenge

**Problem**  
Identify high-risk churn users for TIM, Italy's largest telecom operator.

**Approach**  
I designed a churn classification pipeline with feature engineering and robust model validation.

**Result**  
I won the challenge.

{{< rawhtml >}}
<details class="work-tech-details">
  <summary>Show technical details</summary>
  <div class="work-tech-content">
    <p><strong>Stack:</strong> Python, pandas, scikit-learn, gradient boosting workflows, feature engineering.</p>
    <p><strong>Validation:</strong> Structured offline evaluation with strong train/validation split discipline.</p>
    <p><strong>Focus:</strong> Prioritization-ready churn scoring and robust model selection.</p>
  </div>
</details>
{{< /rawhtml >}}

### Kaggle Modeling Portfolio

**Problem**  
Show practical ability to explore datasets and build strong predictive models across different domains.

**Approach**  
I published notebooks covering exploratory analysis, gradient boosting models, and neural network workflows with reproducible evaluation.

**Result**  
Kaggle Code Master, career-high world rank: **#163**.

- [Kaggle code portfolio](https://www.kaggle.com/tomwarrens/code)

{{< rawhtml >}}
<details class="work-tech-details">
  <summary>Show technical details</summary>
  <div class="work-tech-content">
    <p><strong>Stack:</strong> Python, notebook-driven experimentation, gradient boosting and neural network baselines.</p>
    <p><strong>Workflow:</strong> EDA, feature engineering, model training, error analysis, reproducible comparisons.</p>
    <p><strong>Output:</strong> Public notebooks that show both exploration and modeling depth.</p>
  </div>
</details>
{{< /rawhtml >}}

### LightGBM Inference-Time Feature Importance

**Problem**  
Standard feature importance methods are often disconnected from real-time scoring behavior.

**Approach**  
I implemented and documented a method to compute feature importance at inference time for tree-based models.

**Result**  
Published as open-source code and a technical article.

- [GitHub repository](https://github.com/tomwarrens/lightgbm_inference_fi)
- [Medium article](https://medium.com/@guerrinitom/run-for-your-leaves-a-simple-path-to-feature-importance-at-inference-time-in-tree-based-models-63afaf5a8c77)

{{< rawhtml >}}
<details class="work-tech-details">
  <summary>Show technical details</summary>
  <div class="work-tech-content">
    <p><strong>Stack:</strong> Python, LightGBM internals, custom inference-time feature attribution logic.</p>
    <p><strong>Deployment relevance:</strong> Designed to keep feature-importance computation aligned with production scoring behavior.</p>
    <p><strong>Output:</strong> Open-source implementation plus long-form technical explanation.</p>
  </div>
</details>
{{< /rawhtml >}}

## Production ML Case Highlights (Anonymized)

### Insurance Fraud Detection

**Scope**  
Built and deployed fraud-risk scoring to support claim triage.

**Delivery**  
From feature engineering to model training, evaluation, and integration in decision workflows.

{{< rawhtml >}}
<details class="work-tech-details">
  <summary>Show technical details</summary>
  <div class="work-tech-content">
    <p><strong>Stack:</strong> Python, SQL, gradient boosting models, feature pipelines.</p>
    <p><strong>Deployment:</strong> Production scoring integrated into operational claim-review process.</p>
    <p><strong>Operational layer:</strong> Monitoring of model quality and periodic refresh workflow.</p>
  </div>
</details>
{{< /rawhtml >}}

### Loan Default Prediction

**Scope**  
Developed and deployed default-risk models for underwriting and portfolio monitoring.

**Delivery**  
Risk-score generation with model validation, calibration, and business-oriented thresholding.

{{< rawhtml >}}
<details class="work-tech-details">
  <summary>Show technical details</summary>
  <div class="work-tech-content">
    <p><strong>Stack:</strong> Python, SQL, classification models, calibration and scorecard-style reporting.</p>
    <p><strong>Deployment:</strong> Risk scores consumed by credit and risk teams in daily workflows.</p>
    <p><strong>Operational layer:</strong> Versioned training/scoring pipeline with performance checks.</p>
  </div>
</details>
{{< /rawhtml >}}

### Multi-Series Forecasting

**Scope**  
Delivered forecasting systems across multiple time series for planning use cases.

**Delivery**  
Built forecasting pipelines with backtesting and periodic model refresh.

{{< rawhtml >}}
<details class="work-tech-details">
  <summary>Show technical details</summary>
  <div class="work-tech-content">
    <p><strong>Stack:</strong> Python, SQL, time-series feature engineering and model-based forecasting.</p>
    <p><strong>Deployment:</strong> Automated recurring forecasts for planning and operational decision support.</p>
    <p><strong>Operational layer:</strong> Multi-series backtesting framework and accuracy tracking over time.</p>
  </div>
</details>
{{< /rawhtml >}}

## Technologies Used

{{< rawhtml >}}
<div class="work-tech-groups">
  <section class="work-tech-group">
    <h3>Modeling</h3>
    <ul class="work-tech-chip-list">
      <li>Python</li>
      <li>LightGBM</li>
      <li>Gradient Boosting</li>
      <li>Neural Networks</li>
      <li>Classification</li>
      <li>Time Series Forecasting</li>
    </ul>
  </section>

  <section class="work-tech-group">
    <h3>Data and Pipelines</h3>
    <ul class="work-tech-chip-list">
      <li>SQL</li>
      <li>Feature Engineering</li>
      <li>Data Scraping</li>
      <li>Model Validation</li>
      <li>Backtesting</li>
      <li>Monitoring</li>
    </ul>
  </section>

  <section class="work-tech-group">
    <h3>Product and Delivery</h3>
    <ul class="work-tech-chip-list">
      <li>Production Scoring Workflows</li>
      <li>Decision-System Integration</li>
      <li>Risk Prioritization</li>
      <li>Java Web Application Development</li>
      <li>Interactive Map Features</li>
      <li>Technical Communication</li>
    </ul>
  </section>
</div>
{{< /rawhtml >}}
