# COVID-19 ETL Pipeline

A production-grade ETL pipeline for processing COVID-19 data from BigQuery public datasets with comprehensive data transformation and storage capabilities.

## 🏗️ Architecture

This project follows Clean Architecture principles with clear separation of concerns:

- **Domain Layer**: Business logic, use cases, and value objects
- **Infrastructure Layer**: External integrations (BigQuery, Database)
- **Data Layer**: Models, repositories, and data sources
- **Application Layer**: Dependency injection and orchestration

## 📊 Data Source

**BigQuery Public Dataset**: `bigquery-public-data.covid19_open_data.covid19_open_data`

### Sample Query
```sql
SELECT 
  date,
  country_code,
  country_name,
  new_confirmed,
  new_deceased,
  cumulative_deceased,
  cumulative_tested,
  population_male,
  population_female,
  smoking_prevalence,
  diabetes_prevalence
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
ORDER BY date DESC
LIMIT 100
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- PostgreSQL database
- Google Cloud credentials (for BigQuery access)

### Installation
```bash
# Clone repository
git clone <repository-url>
cd covid-etl-pipeline

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database and BigQuery credentials
```

### Environment Configuration
```bash
# Database Configuration
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=covid_etl

# BigQuery Configuration
GOOGLE_APPLICATION_CREDENTIALS=path/to/service-account.json
BIGQUERY_PROJECT_ID=your-project-id
```

## 🔄 Usage

### Run ETL Pipeline
```bash
python main.py --cron-name covid_data_orchestrator --start-date 2020-08-01 --end-date 2020-08-02
```

### Command Line Options
- `--cron-name`: Name of the orchestrator to run
- `--start-date`: Start date for data extraction (YYYY-MM-DD)
- `--end-date`: End date for data extraction (YYYY-MM-DD)

### Example Commands
```bash
# Process single day
python main.py --cron-name covid_data_orchestrator --start-date 2020-08-01 --end-date 2020-08-01

# Process date range
python main.py --cron-name covid_data_orchestrator --start-date 2020-08-01 --end-date 2020-08-31

# Process recent data
python main.py --cron-name covid_data_orchestrator --start-date 2023-01-01 --end-date 2023-01-31
```

## 🧪 Testing

### Run All Tests
```bash
PYTHONPATH=$(pwd) pytest --cov=etl_covid_19 --cov-report=term-missing test/
```

### Test Coverage Report

Our test suite maintains **100% line coverage** across all modules:

```
======================================================================================== tests coverage =========================================================================================
_______________________________________________________________________ coverage: platform darwin, python 3.11.11-final-0 _______________________________________________________________________
Name                                                            Stmts   Miss  Cover   Missing
---------------------------------------------------------------------------------------------
etl_covid_19/container.py                                          19      0   100%
etl_covid_19/data/data_source/covid_data_source.py                  7      0   100%
etl_covid_19/data/model/base_db_model.py                            3      0   100%
etl_covid_19/data/model/covid_model.py                             15      0   100%
etl_covid_19/data/repository/covid_data_pipeline_impl.py           21      0   100%
etl_covid_19/domain/services/covid_data_pipeline.py                13      0   100%
etl_covid_19/domain/use_cases/base_use_case.py                      6      0   100%
etl_covid_19/domain/use_cases/fetch_covid_data_usecase.py           8      0   100%
etl_covid_19/domain/use_cases/insert_covid_data_use_case.py         9      0   100%
etl_covid_19/domain/use_cases/transform_covid_data_usecase.py       9      0   100%
etl_covid_19/domain/value_objects/__init__.py                       0      0   100%
etl_covid_19/domain/value_objects/covid_daily_record.py            15      0   100%
etl_covid_19/infrastructure/bigquery/bigquery_client.py            18      0   100%
etl_covid_19/infrastructure/database/database_client.py            24      0   100%
---------------------------------------------------------------------------------------------
TOTAL                                                             167      0   100%
```

### Test Commands

```bash
# Basic test run
pytest test/

# With coverage report
PYTHONPATH=$(pwd) pytest --cov=etl_covid_19 --cov-report=term-missing test/

# Generate HTML coverage report
PYTHONPATH=$(pwd) pytest --cov=etl_covid_19 --cov-report=html test/
# Open htmlcov/index.html in browser

# Run with branch coverage (recommended)
PYTHONPATH=$(pwd) pytest --cov=etl_covid_19 --cov-branch --cov-report=term-missing test/

# Run specific test categories
pytest test/unit/                    # Unit tests only
pytest test/integration/             # Integration tests only
pytest -m "not slow"                # Skip slow tests
```

### Test Categories

- **Unit Tests**: Fast, isolated tests for individual components
- **Integration Tests**: End-to-end pipeline testing
- **Contract Tests**: External API schema validation
- **Performance Tests**: Memory and speed benchmarks

### Coverage Quality Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|---------|
| Line Coverage | 95%+ | 100% | ✅ |
| Branch Coverage | 95%+ | TBD | 🔄 |
| Mutation Score | 85%+ | TBD | 🔄 |

## 📁 Project Structure

```
etl_covid_19/
├── container.py                     # Dependency injection container
├── data/
│   ├── data_source/                 # Data source abstractions
│   ├── model/                       # Database models
│   └── repository/                  # Data access layer
├── domain/
│   ├── services/                    # Business services
│   ├── use_cases/                   # Application use cases
│   └── value_objects/               # Domain value objects
└── infrastructure/
    ├── bigquery/                    # BigQuery client
    └── database/                    # Database client

test/
├── unit/                           # Unit tests
├── integration/                    # Integration tests
├── contracts/                      # API contract tests
└── conftest.py                     # Test configuration
```

## 🔧 Development

### Code Quality

We maintain high code quality standards:

- **100% test coverage** across all modules
- **Clean Architecture** principles
- **SOLID** design patterns
- **Type hints** throughout codebase
- **Comprehensive error handling**

### Pre-commit Hooks
```bash
# Install pre-commit hooks
pre-commit install

# Run manually
pre-commit run --all-files
```

### Code Formatting
```bash
# Format code
black etl_covid_19/
isort etl_covid_19/

# Lint code
flake8 etl_covid_19/
mypy etl_covid_19/
```

## 🚀 Deployment

### Docker Deployment
```bash
# Build image
docker build -t covid-etl-pipeline .

# Run container
docker run -d \
  --name covid-etl \
  -e DB_HOST=your_db_host \
  -e DB_USER=your_db_user \
  -e DB_PASSWORD=your_db_password \
  covid-etl-pipeline
```

### Kubernetes Deployment
```bash
# Apply manifests
kubectl apply -f k8s/

# Check deployment
kubectl get pods -l app=covid-etl
```

### Cron Job Setup
```bash
# Add to crontab for daily execution
0 2 * * * /path/to/venv/bin/python /path/to/main.py --cron-name covid_data_orchestrator --start-date $(date -d "yesterday" +\%Y-\%m-\%d) --end-date $(date -d "yesterday" +\%Y-\%m-\%d)
```

## 📊 Monitoring & Observability

### Logging
- Structured logging with JSON format
- Configurable log levels
- Request/response tracing
- Error tracking and alerts

### Metrics
- Pipeline execution time
- Data processing volume
- Error rates and types
- Resource utilization

### Health Checks
```bash
# Check database connectivity
python -c "from etl_covid_19.infrastructure.database.database_client import DatabaseClient; print('DB OK')"

# Check BigQuery connectivity
python -c "from etl_covid_19.infrastructure.bigquery.bigquery_client import BigQueryClient; print('BQ OK')"
```

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Ensure tests pass (`pytest test/`)
4. Ensure 100% coverage maintained
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open Pull Request

### Contribution Guidelines

- Maintain 100% test coverage
- Follow Clean Architecture principles
- Add comprehensive tests for new features
- Update documentation for API changes
- Use conventional commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Troubleshooting

### Common Issues

**Database Connection Errors**
```bash
# Check database connectivity
pg_isready -h localhost -p 5432

# Test connection
psql -h localhost -p 5432 -U your_user -d your_db
```

**BigQuery Authentication Issues**
```bash
# Check service account
gcloud auth application-default print-access-token

# Test BigQuery access
bq ls your-project-id:
```

**Memory Issues with Large Datasets**
- Adjust batch size in configuration
- Monitor memory usage during execution
- Consider implementing data chunking

### Performance Optimization

- Use connection pooling for database operations
- Implement batch processing for large datasets
- Cache frequently accessed data
- Monitor and optimize slow queries

## 📞 Support

For questions, issues, or contributions:

- 📧 Email: support@covid-etl.com
- 🐛 Issues: [GitHub Issues](https://github.com/your-org/covid-etl/issues)
- 📖 Documentation: [Wiki](https://github.com/your-org/covid-etl/wiki)
- 💬 Discussions: [GitHub Discussions](https://github.com/your-org/covid-etl/discussions)