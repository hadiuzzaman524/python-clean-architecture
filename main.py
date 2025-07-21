import argparse
import importlib
from datetime import datetime


class CronExecutor:
    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(description="Run COVID-19 ETL Cron")
        parser.add_argument(
            "--cron-name", required=True, type=str, help="Set the orchestrator name"
        )
        parser.add_argument(
            "--start-date",
            type=lambda d: datetime.strptime(d, "%Y-%m-%d").date(),
            required=False,
            help="Start date in YYYY-MM-DD (optional)",
        )
        parser.add_argument(
            "--end-date",
            type=lambda d: datetime.strptime(d, "%Y-%m-%d").date(),
            required=False,
            help="End date in YYYY-MM-DD (optional)",
        )

        return parser.parse_args()

    def get_job_instance(self):
        args = self.parse_arguments()
        try:
            module = importlib.import_module(f"etl_covid_19.presentation.{args.cron_name}")
        except ModuleNotFoundError as e:
            print(f"Module not found: {e}")
            exit(1)

        class_name = args.cron_name.replace("_", " ").title().replace(" ", "")
        parsed_args = {
            "start_date": args.start_date,
            "end_date": args.end_date,
        }

        if hasattr(module, class_name):
            job_class = getattr(module, class_name)
            return job_class(**parsed_args)
        else:
            print(f"Class `{class_name}` not found in module `{args.cron_name}`.")
            exit(1)


if __name__ == "__main__":
    handler = CronExecutor()
    job = handler.get_job_instance()
    job.trigger()
