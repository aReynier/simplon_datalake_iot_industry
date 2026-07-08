from raw.data_ingestion import ingest_data
from raw_integrity_check import check_raw_integrity


production_lines = [
    {"id": "A", "name": "LineA_Stable_10K"},
    {"id": "B", "name": "LineB_Flux"},
    {"id": "C", "name": "LineC_Turbulent"},
    {"id": "D", "name": "LineD_SpikeControl"},
    {"id": "E", "name": "LineE_SmoothRun"}
]

def main():
    ingest_data("LineA_Stable_10K", "A")
    ingest_data("LineB_Flux", "B")
    ingest_data("LineC_Turbulent", "C")
    ingest_data("LineD_SpikeControl", "D")
    ingest_data("LineE_SmoothRun", "E")

    check_raw_integrity()


if __name__ == "__main__":
    main()