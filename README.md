## Project Overview
This project analyzes transactional retail data using RFM (Recency, Frequency, Monetary) analysis to identify high-value customers, quantify revenue concentration, and uncover purchasing patterns. The goal is to generate actionable insights that support data-driven marketing strategies and customer prioritization.

## Data Overview 
This project uses a publicly available dataset from the UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/352/online+retail

The dataset contains all transactions from a UK-based online retail company between December 1, 2010 and December 9, 2011 and includes the following information:

| Field | Description |
|-------|-------------|
| Customer ID | Unique customer identifier |
| Invoice Number | Transaction identifier |
| Product Code & Description | Item details |
| Quantity | Units purchased per item |
| Invoice Date | Transaction date |
| Unit Price | Price per unit |
| Customer Country | Geographic location |

Each row represents a single product within a transaction, meaning multiple rows may 
correspond to a single purchase. The dataset notes that a portion of customers are 
wholesalers, however no explicit labels are provided. Customer types are therefore 
inferred from purchasing behavior rather than predefined categories.

## Project Goals
- Segment customers using RFM analysis  
- Identify high-value customer groups and revenue concentration patterns  
- Analyze purchasing behavior across segments to inform targeted marketing strategies  
- Generate actionable insights to support customer retention and business decision-making  

## Methodology
1. Data cleaning and preprocessing (handling missing Customer IDs, negative quantities, 
   and zero-price entries). 
2. Loading cleaned data into SQLite for aggregation of transaction-level data into 
   customer-level RFM metrics.
3. Exploratory data analysis to identify distributional skew and justify segmentation approach.
4. RFM scoring using quintile-based ranking across Recency, Frequency, and Monetary 
   dimensions.
5. Customer segmentation using composite RFM score thresholds.
6. Visualization and interpretation of segment-level behavioral differences.

## Key Insights
- High-value customers represent 29% of the customer base but generate 76% of total revenue, contributing over 10× more revenue than low-value customers.
- Low-value customers (39% of the base) account for just 7% of revenue and exhibit low engagement, averaging 170 days since their last purchase and only 1.2 orders, suggesting many are one-time buyers.
- Mid-value customers demonstrate moderate engagement (avg. 64 days since last purchase, 2.85 orders) and represent the strongest opportunity for conversion into high-value customers.
- Revenue and purchase frequency are heavily right-skewed, consistent with the presence of high-frequency or wholesale buyers driving a disproportionate share of total revenue.

## Business Implications
- Revenue is highly concentrated among a relatively small group of high-value customers, suggesting that retention and targeted engagement of this segment should be prioritized.
- Given the nature of the business (occasion-based purchases), low-value customer behavior may reflect one-time buying patterns, limiting the effectiveness of traditional retention strategies.
- Mid-value customers present the strongest opportunity for growth, where targeted incentives or personalized marketing could increase purchase frequency and customer lifetime value.

## Tools Used
- Python (Pandas, NumPy)
- SQLite
- Data Visualization (Matplotlib / Seaborn)
- Jupyter Notebook

## Author
Farishtay Fahim
[LinkedIn] (www.linkedin.com/in/farishtayfahim)