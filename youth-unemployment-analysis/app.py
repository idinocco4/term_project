"""
Youth Unemployment Global Analysis Dashboard
===========================================

A Streamlit web application for interactive exploration of global youth unemployment data.

Run locally: streamlit run app.py
Deploy to Streamlit Cloud, Heroku, or other platforms.

Author: Data Analysis Team
Date: November 2024
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Set page configuration
st.set_page_config(
    page_title="Global Youth Unemployment Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sub-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2ca02c;
        margin-bottom: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 0.25rem solid #1f77b4;
    }
    .sidebar-content {
        padding: 1rem;
        background-color: #ffffff;
        border-radius: 0.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Load data function
@st.cache_data
def load_data():
    """Load and cache the cleaned dataset."""
    try:
        df = pd.read_csv('data/youth_unemployment_cleaned.csv')
        df['Year'] = df['Year'].astype(int)
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please ensure 'data/youth_unemployment_cleaned.csv' exists.")
        return None

def create_global_trends_plot(df):
    """Create global trends visualization."""
    global_trends = df.groupby('Year')['YouthUnemployment'].agg(['mean', 'count']).reset_index()

    fig = px.line(global_trends, x='Year', y='mean',
                  title='Global Average Youth Unemployment Rate (1960-2024)',
                  labels={'mean': 'Youth Unemployment Rate (%)'},
                  markers=True)

    fig.update_layout(
        hovermode='x unified',
        template='plotly_white',
        height=500
    )

    return fig

def create_regional_comparison(df, latest_year):
    """Create regional comparison visualization."""
    latest_data = df[df['Year'] == latest_year].copy()

    # Simplified regional mapping
    region_mapping = {
        'ZAF': 'Africa', 'ZWE': 'Middle East & North Africa', 'ZAR': 'South Asia',
        'ZQE': 'East Asia & Pacific', 'ZQB': 'Europe & Central Asia',
        'ZQA': 'North America', 'ZQC': 'Latin America & Caribbean'
    }

    latest_data['Region'] = latest_data['CountryCode'].map(region_mapping)
    regional_data = latest_data.dropna(subset=['Region']).groupby('Region')['YouthUnemployment'].mean().reset_index()

    fig = px.bar(regional_data, x='Region', y='YouthUnemployment',
                 title=f'Regional Youth Unemployment Rates ({latest_year})',
                 labels={'YouthUnemployment': 'Youth Unemployment Rate (%)'},
                 color='YouthUnemployment',
                 color_continuous_scale='YlOrRd')

    fig.update_layout(
        xaxis_tickangle=-45,
        template='plotly_white',
        height=500
    )

    return fig

def create_country_ranking(df, latest_year, top_n=10):
    """Create country ranking visualization."""
    latest_data = df[df['Year'] == latest_year].dropna(subset=['YouthUnemployment'])

    # Top countries with lowest unemployment
    top_countries = latest_data.nsmallest(top_n, 'YouthUnemployment')[['Country', 'YouthUnemployment']]

    fig = px.bar(top_countries, x='YouthUnemployment', y='Country',
                 title=f'Top {top_n} Countries - Lowest Youth Unemployment ({latest_year})',
                 labels={'YouthUnemployment': 'Youth Unemployment Rate (%)'},
                 orientation='h',
                 color='YouthUnemployment',
                 color_continuous_scale='Greens')

    fig.update_layout(
        template='plotly_white',
        height=500
    )

    return fig

def create_time_series_plot(df, countries):
    """Create time series comparison for selected countries."""
    if not countries:
        return None

    country_data = df[df['Country'].isin(countries)]

    fig = px.line(country_data, x='Year', y='YouthUnemployment', color='Country',
                  title=f'Youth Unemployment Trends: {", ".join(countries)}',
                  labels={'YouthUnemployment': 'Youth Unemployment Rate (%)'},
                  markers=True)

    fig.update_layout(
        hovermode='x unified',
        template='plotly_white',
        height=500
    )

    return fig

def main():
    """Main application function."""

    # Load data
    df = load_data()
    if df is None:
        return

    # Main header
    st.markdown('<h1 class="main-header">🌍 Global Youth Unemployment Analysis</h1>', unsafe_allow_html=True)
    st.markdown("---")

    # Sidebar
    with st.sidebar:
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
        st.markdown("## 📊 Dashboard Controls")

        # Analysis type selection
        analysis_type = st.selectbox(
            "Choose Analysis Type:",
            ["Global Overview", "Regional Comparison", "Country Rankings", "Time Series Comparison", "Data Explorer"]
        )

        # Year selection
        latest_year = df['Year'].max()
        selected_year = st.slider("Select Year:", min_value=df['Year'].min(), max_value=latest_year, value=latest_year)

        st.markdown("---")

        # Country selection for time series
        if analysis_type == "Time Series Comparison":
            countries = st.multiselect(
                "Select Countries:",
                options=sorted(df['Country'].unique()),
                default=['Germany', 'United States', 'Japan', 'Brazil'],
                max_selections=5
            )

        st.markdown("</div>", unsafe_allow_html=True)

    # Main content area
    if analysis_type == "Global Overview":
        st.markdown('<h2 class="sub-header">🌐 Global Overview</h2>', unsafe_allow_html=True)

        # Key metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Total Countries", f"{df['Country'].nunique():,}")
            st.markdown('</div>', unsafe_allow_html=True)

        with col2:
            latest_avg = df[df['Year'] == selected_year]['YouthUnemployment'].mean()
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric(f"Average Rate ({selected_year})", f"{latest_avg:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)

        with col3:
            data_points = len(df[df['Year'] == selected_year])
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Data Points", f"{data_points:,}")
            st.markdown('</div>', unsafe_allow_html=True)

        with col4:
            completeness = (len(df[df['Year'] == selected_year].dropna()) / len(df[df['Year'] == selected_year])) * 100
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Data Completeness", f"{completeness:.1f}%")
            st.markdown('</div>', unsafe_allow_html=True)

        # Global trends plot
        st.markdown("### Global Trends Over Time")
        fig = create_global_trends_plot(df)
        st.plotly_chart(fig, use_container_width=True)

    elif analysis_type == "Regional Comparison":
        st.markdown('<h2 class="sub-header">🗺️ Regional Comparison</h2>', unsafe_allow_html=True)

        fig = create_regional_comparison(df, selected_year)
        st.plotly_chart(fig, use_container_width=True)

        # Regional statistics table
        st.markdown("### Regional Statistics")
        latest_data = df[df['Year'] == selected_year].copy()
        region_mapping = {
            'ZAF': 'Africa', 'ZWE': 'Middle East & North Africa', 'ZAR': 'South Asia',
            'ZQE': 'East Asia & Pacific', 'ZQB': 'Europe & Central Asia',
            'ZQA': 'North America', 'ZQC': 'Latin America & Caribbean'
        }
        latest_data['Region'] = latest_data['CountryCode'].map(region_mapping)
        regional_stats = latest_data.dropna(subset=['Region']).groupby('Region')['YouthUnemployment'].agg(['mean', 'count', 'std']).round(2)
        st.dataframe(regional_stats)

    elif analysis_type == "Country Rankings":
        st.markdown('<h2 class="sub-header">🏆 Country Rankings</h2>', unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Lowest Unemployment Rates")
            fig_lowest = create_country_ranking(df, selected_year, 10)
            st.plotly_chart(fig_lowest, use_container_width=True)

        with col2:
            st.markdown("### Highest Unemployment Rates")
            latest_data = df[df['Year'] == selected_year].dropna(subset=['YouthUnemployment'])
            bottom_countries = latest_data.nlargest(10, 'YouthUnemployment')[['Country', 'YouthUnemployment']]

            fig_highest = px.bar(bottom_countries, x='YouthUnemployment', y='Country',
                               title=f'Bottom 10 Countries - Highest Youth Unemployment ({selected_year})',
                               labels={'YouthUnemployment': 'Youth Unemployment Rate (%)'},
                               orientation='h',
                               color='YouthUnemployment',
                               color_continuous_scale='Reds')

            fig_highest.update_layout(template='plotly_white', height=500)
            st.plotly_chart(fig_highest, use_container_width=True)

    elif analysis_type == "Time Series Comparison":
        st.markdown('<h2 class="sub-header">📈 Time Series Comparison</h2>', unsafe_allow_html=True)

        if countries:
            fig = create_time_series_plot(df, countries)
            st.plotly_chart(fig, use_container_width=True)

            # Statistics table
            st.markdown("### Selected Countries Statistics")
            country_stats = []
            for country in countries:
                country_data = df[df['Country'] == country]
                if not country_data.empty:
                    latest_rate = country_data[country_data['Year'] == selected_year]['YouthUnemployment']
                    if not latest_rate.empty:
                        country_stats.append({
                            'Country': country,
                            'Latest Rate': latest_rate.iloc[0],
                            'Average': country_data['YouthUnemployment'].mean(),
                            'Min': country_data['YouthUnemployment'].min(),
                            'Max': country_data['YouthUnemployment'].max()
                        })

            if country_stats:
                stats_df = pd.DataFrame(country_stats).round(2)
                st.dataframe(stats_df)
        else:
            st.warning("Please select at least one country to compare.")

    elif analysis_type == "Data Explorer":
        st.markdown('<h2 class="sub-header">🔍 Data Explorer</h2>', unsafe_allow_html=True)

        # Raw data viewer
        st.markdown("### Raw Data Preview")
        st.dataframe(df.head(100))

        # Data summary
        st.markdown("### Dataset Summary")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Basic Statistics:**")
            st.write(f"- Total observations: {len(df):,}")
            st.write(f"- Total countries: {df['Country'].nunique()}")
            st.write(f"- Year range: {df['Year'].min()} - {df['Year'].max()}")
            st.write(f"- Missing values: {df['YouthUnemployment'].isnull().sum():,}")

        with col2:
            st.markdown("**Unemployment Statistics:**")
            st.write(f"- Mean: {df['YouthUnemployment'].mean():.2f}%")
            st.write(f"- Median: {df['YouthUnemployment'].median():.2f}%")
            st.write(f"- Min: {df['YouthUnemployment'].min():.2f}%")
            st.write(f"- Max: {df['YouthUnemployment'].max():.2f}%")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p><strong>Global Youth Unemployment Analysis Dashboard</strong></p>
        <p>Data Source: World Bank World Development Indicators | Created with Streamlit</p>
        <p>© 2024 Data Analysis Team</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
