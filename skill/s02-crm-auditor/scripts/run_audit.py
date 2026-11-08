"""CLI adapter for the S02 Variant 1 deterministic audit engine."""
import argparse
import json
from pathlib import Path
from audit import audit, write_results


def main():
    parser = argparse.ArgumentParser(description="Audit synthetic CRM CSV exports")
    parser.add_argument("--contacts", required=True)
    parser.add_argument("--deals", required=True)
    parser.add_argument("--associations")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    summary, issues = audit(args.contacts, args.deals, args.associations)
    write_results(summary, issues, args.output)
    print(json.dumps({"summary": summary, "issues": issues, "output_directory": str(Path(args.output))}, sort_keys=True))


if __name__ == "__main__":
    main()
