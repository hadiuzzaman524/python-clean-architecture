# COVID-19 ETL Pipeline

A production-grade ETL pipeline for processing COVID-19 data from BigQuery public datasets, featuring robust data transformation and storage capabilities.

---

## 🏗️ Architecture

This project follows **Clean Architecture** principles for maintainability and scalability:

- **Domain Layer**: Business logic, use cases, value objects
- **Infrastructure Layer**: External integrations (BigQuery, Database)
- **Data Layer**: Models, repositories, data sources
- **Application Layer**: Dependency injection and orchestration

---

## 📊 Data Source

- **BigQuery Public Dataset**:  
  `bigquery-public-data.covid19_open_data.covid19_open_data`

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL database (local or Docker)
- Google Cloud credentials (for BigQuery access)

### 1. Environment Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Database Setup

Run PostgreSQL using Docker:

```bash
docker run -d \
  --name my-postgres \
  -p 5432:5432 \
  -e POSTGRES_PASSWORD=your_db_password \
  postgres
```

### 3. Configuration

Edit your config in [config/app_config.toml](config/app_config.toml):

```toml
[postgres]
HOST = "192.168.0.236"  # Your IP
USERNAME = "db_user_name"
PASSWORD = "db_password"
PORT = "5432"
DB_NAME = "your_db_name"

[bigquery]
PROJECT_ID = "carbon-zone-466205-r5"
SERVICE_ACCOUNT_FILEPATH = "config/carbon-zone-466205-r5-baaa1a665c04.json"
```

### 4. Create Database Table

```sql
CREATE TABLE covid_daily_records (
    date DATE NOT NULL,
    country_code VARCHAR(10) NOT NULL,
    country_name TEXT,
    new_confirmed INTEGER,
    new_deceased INTEGER,
    cumulative_deceased INTEGER,
    cumulative_tested INTEGER,
    population_male INTEGER,
    population_female INTEGER,
    smoking_prevalence NUMERIC,
    diabetes_prevalence NUMERIC,
    PRIMARY KEY (country_code, date)
);
```

### 5. Run ETL Pipeline

```bash
python main.py --cron-name covid_data_orchestrator --start-date 2020-08-01 --end-date 2020-08-02
```

#### Example Commands

```bash
# Process single day
python main.py --cron-name covid_data_orchestrator --start-date 2020-08-01 --end-date 2020-08-01

# Process date range
python main.py --cron-name covid_data_orchestrator --start-date 2020-08-01 --end-date 2020-08-31
```

---

## 🧪 Testing

Run all tests and check coverage:

```bash
PYTHONPATH=$(pwd) pytest --cov=etl_covid_19 --cov-report=term-missing test/
```

---

## 📁 Project Structure

```
etl_covid_19/
├── container.py
├── data/
│   ├── data_source/
│   ├── model/
│   └── repository/
├── domain/
│   ├── services/
│   ├── use_cases/
│   └── value_objects/
└── infrastructure/
    ├── bigquery/
    └── database/
test/
├── unit/
├── integration/
├── contracts/
└── conftest.py
```

---

## 📞 Support

- 📧 Email: hadiuzzaman908@gmail.com
- 🐛 Issues: [GitHub Issues](https://github.com/hadiuzzaman524/python-clean-architecture/issues)
- 📖 Documentation: [Wiki](https://github.com/hadiuzzaman524/python-clean-architecture/wiki)
- 💬 Discussions: [GitHub Discussions](https://github.com/hadiuzzaman524/python-clean-architecture/discussions)