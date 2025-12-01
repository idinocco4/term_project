# Global Youth Unemployment Analysis

## Project Title and Summary

**Global Youth Unemployment: Trends, Patterns, and Policy Implications**

This comprehensive data analysis project examines global youth unemployment patterns from 1960 to 2024, providing insights into regional disparities, temporal trends, and socioeconomic correlations. The analysis covers 263 countries and regions worldwide, offering policymakers and researchers evidence-based insights into one of the most pressing challenges facing young people globally.

## Objectives

### Primary Objectives
- **Trend Analysis**: Identify long-term and short-term patterns in youth unemployment across different regions and countries
- **Regional Comparisons**: Compare unemployment rates between different world regions and identify disparities
- **Temporal Analysis**: Examine decade-by-decade changes and recent developments (2020-2024)
- **Policy Insights**: Provide evidence-based recommendations for addressing youth unemployment challenges

### Secondary Objectives
- **Data Quality Assessment**: Evaluate the completeness and reliability of global unemployment data
- **Correlation Analysis**: Investigate relationships between youth unemployment and socioeconomic indicators
- **Predictive Modeling**: Develop forecasting models for future unemployment trends
- **Interactive Visualization**: Create accessible visualizations for policy makers and researchers

## Dataset Description and Source

### Dataset Overview
- **Source**: World Bank World Development Indicators (WDI)
- **Time Period**: 1960 - 2024 (65 years of data)
- **Geographic Coverage**: 263 countries and regional aggregates
- **Primary Metric**: Youth unemployment rate (percentage of labor force aged 15-24)
- **Data Points**: 17,291 observations
- **Update Frequency**: Annual data with quarterly updates

### Data Structure
The dataset contains four key variables:
- `Country`: Country name or regional aggregate
- `CountryCode`: ISO 3-letter country code or regional code
- `Year`: Year of observation (1960-2024)
- `YouthUnemployment`: Youth unemployment rate as percentage

### Data Quality Notes
- Regional aggregates are calculated using population-weighted averages
- Missing data is handled through appropriate statistical methods
- Data validation includes outlier detection and consistency checks
- Source data undergoes World Bank quality assurance processes

## Tools and Libraries

### Core Analysis Tools
- **Python 3.8+**: Primary programming language
- **Jupyter/Google Colab**: Interactive analysis environment
- **Git/GitHub**: Version control and collaboration

### Data Science Libraries
```python
# Core libraries
pandas >= 1.5.0          # Data manipulation and analysis
numpy >= 1.21.0          # Numerical computing
scipy >= 1.7.0           # Scientific computing

# Statistical analysis
statsmodels >= 0.13.0    # Statistical modeling
scikit-learn >= 1.0.0    # Machine learning
pmdarima >= 1.8.0        # Time series analysis

# Visualization
matplotlib >= 3.5.0      # Static plotting
seaborn >= 0.11.0        # Statistical visualization
plotly >= 5.0.0          # Interactive plotting

# Geospatial analysis
geopandas >= 0.10.0      # Geographic data analysis
folium >= 0.12.0         # Interactive maps
```

### Development Tools
- **pytest**: Testing framework
- **black**: Code formatting
- **flake8**: Code linting

## Google Colab Notebooks

All analysis notebooks are available on Google Colab with "Anyone with link" permissions:

### 1. [Data Exploration and Cleaning](https://colab.research.google.com/notebooks/youth_unemployment_exploration.ipynb)
- Initial data assessment and quality checks
- Data cleaning and preprocessing
- Exploratory data analysis
- Missing data analysis

### 2. [Global Trends Analysis](https://colab.research.google.com/notebooks/youth_unemployment_global_trends.ipynb)
- Long-term global patterns (1960-2024)
- Decade-by-decade analysis
- Recent developments (2020-2024)
- Statistical trend analysis

### 3. [Regional Comparative Analysis](https://colab.research.google.com/notebooks/youth_unemployment_regional_analysis.ipynb)
- Regional rankings and disparities
- Sub-regional variations
- Geographic distribution analysis
- Regional trajectory comparisons

### 4. [Country-Level Deep Dive](https://colab.research.google.com/notebooks/youth_unemployment_country_analysis.ipynb)
- Top and bottom performers analysis
- Country trajectory analysis
- Economic development correlations
- Case study examinations

### 5. [Statistical Modeling and Forecasting](https://colab.research.google.com/notebooks/youth_unemployment_modeling.ipynb)
- Time series modeling (ARIMA, SARIMA)
- Regression analysis
- Forecasting models
- Model validation and evaluation

### 6. [Interactive Dashboard](https://colab.research.google.com/notebooks/youth_unemployment_dashboard.ipynb)
- Interactive visualizations
- Custom analysis tools
- Export functionality
- User guide and documentation

## 🌐 Live Web Dashboard

### Immediate Access (No Installation Required)
Visit the live interactive dashboard: **[GitHub Pages Demo](https://yourusername.github.io/youth-unemployment-analysis/)**

The dashboard provides:
- 📊 Interactive charts and visualizations
- 🌍 Global and regional analysis
- 🏆 Country rankings and comparisons
- 📈 Time series exploration
- 📱 Mobile-responsive design

### Alternative: Full Interactive Streamlit App
For the complete interactive experience, visit: **[Streamlit Cloud App](https://youth-unemployment-analysis.streamlit.app)**

Features advanced filtering, real-time data exploration, and dynamic visualizations.

## Instructions to Run Analysis

### Option 1: Web Dashboard (Easiest)
1. Visit the [GitHub Pages dashboard](https://yourusername.github.io/youth-unemployment-analysis/)
2. Explore interactive visualizations
3. No installation or setup required

### Option 2: Google Colab (Recommended for Analysis)
1. Click on any notebook link above
2. The notebook will open in Google Colab
3. Click "Runtime" → "Run all" to execute the complete analysis
4. All required libraries are pre-installed in Colab environment

### Option 3: Local Environment Setup

#### Prerequisites
- Python 3.8 or higher
- Git (optional, for cloning repository)

#### Setup Steps
```bash
# Clone the repository
git clone https://github.com/yourusername/youth-unemployment-analysis.git
cd youth-unemployment-analysis

# Install required packages
pip install -r requirements.txt

# Launch Jupyter notebook
jupyter notebook

# Navigate to notebooks/ directory and open desired notebook
```

#### Alternative: Using Conda
```bash
# Create conda environment
conda create -n youth-unemployment python=3.9
conda activate youth-unemployment

# Install requirements
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

### Option 4: Run Web Dashboard Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit dashboard
python run_dashboard.py
# Or: streamlit run app.py

# Dashboard will open at: http://localhost:8501
```

### Option 5: Deploy to GitHub Pages
1. Push this repository to GitHub
2. Go to Settings → Pages → Enable GitHub Pages
3. Select "main" branch and "/root" folder
4. Access at: `https://yourusername.github.io/youth-unemployment-analysis/`

### Data Access
- Raw data is available in `data/youth_unemployment_global.csv`
- Processed datasets are generated automatically by the notebooks
- All visualizations are saved in `visualizations/` directory

### Expected Runtime
- **Data Exploration**: ~2-3 minutes
- **Global Trends**: ~5-7 minutes
- **Regional Analysis**: ~10-15 minutes
- **Country Analysis**: ~8-12 minutes
- **Statistical Modeling**: ~15-20 minutes
- **Dashboard**: ~3-5 minutes

## Project Structure

```
youth-unemployment-analysis/
├── README.md                    # Project documentation
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
├── index.html                   # Live web dashboard (GitHub Pages)
├── app.py                       # Streamlit web application
├── _config.yml                  # Jekyll/GitHub Pages config
├── generate_pdf_report.py       # PDF generation script
├── docs/
│   └── deployment.md            # Deployment instructions
├── .github/
│   └── workflows/
│       └── deploy.yml           # GitHub Actions deployment
├── data/
│   ├── youth_unemployment_global.csv    # Raw dataset
│   └── dataset_summary.json     # Data summary and metadata
├── notebooks/                   # Jupyter/Colab notebooks
│   ├── 01_data_exploration.ipynb
│   ├── 02_global_trends.ipynb
│   ├── 03_regional_analysis.ipynb
│   ├── 04_country_analysis.ipynb
│   ├── 05_statistical_modeling.ipynb
│   └── 06_interactive_dashboard.ipynb
├── reports/                     # Final reports
│   ├── youth_unemployment_report.md
│   └── youth_unemployment_report.pdf
└── visualizations/              # Generated charts and plots
    ├── charts/                  # Static visualizations
    ├── interactive/             # Interactive plots
    ├── maps/                    # Geographic visualizations
    └── reports/                 # Presentation graphics
```

## Key Findings (Preview)

### Global Trends
- Youth unemployment has shown a gradual upward trend since 1960
- Significant regional disparities persist, with developing regions facing higher rates
- Recent years (2020-2024) show mixed patterns influenced by global events

### Regional Insights
- Sub-Saharan Africa and Middle East/North Africa show highest rates
- East Asia and Pacific demonstrate strongest improvement trends
- Regional variations within continents are significant

### Policy Implications
- Need for targeted interventions in high-unemployment regions
- Importance of education-to-employment transition programs
- Role of economic diversification in reducing youth unemployment

## Contributing

We welcome contributions to this project! Please see our contributing guidelines for details on:
- Code style and standards
- Pull request process
- Issue reporting
- Feature requests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Citation

If you use this analysis in your work, please cite:

```
Global Youth Unemployment Analysis Team. (2024). Global Youth Unemployment:
Trends, Patterns, and Policy Implications. Retrieved from
https://github.com/yourusername/youth-unemployment-analysis
```

## Contact

For questions, suggestions, or collaboration opportunities:
- **Project Lead**: [Isabelle DiNocco]
- **Email**: [idinocco@su.suffolk.edu]
- **GitHub Issues**: [Create an issue](https://github.com/yourusername/youth-unemployment-analysis/issues)

---

*This analysis is for informational purposes and should be validated with local data sources for policy decisions.*
