FROM apache/airflow:3.0.3

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH="/opt/airflow:/opt/airflow/dags:/opt/airflow/etl_covid_19"

# Set Airflow version
ARG AIRFLOW_VERSION=3.0.3

# Copy and install Python dependencies first
COPY requirements.txt /opt/airflow/requirements.txt
RUN pip install apache-airflow==${AIRFLOW_VERSION} -r /opt/airflow/requirements.txt

# Copy project files - do this as airflow user (default)
COPY setup.py /opt/airflow/setup.py
COPY etl_covid_19/ /opt/airflow/etl_covid_19/
COPY config/ /opt/airflow/config/
COPY dags/ /opt/airflow/dags/

# Install the custom package
RUN pip install -e /opt/airflow/

# Verify installation
RUN python -c "import etl_covid_19; print('✓ etl_covid_19 module accessible')" && \
    python -c "from config.app_config import config; print('✓ Config loadable')" && \
    echo "✓ Docker build completed successfully"