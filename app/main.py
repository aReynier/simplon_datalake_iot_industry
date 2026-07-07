from raw.data_ingestion import ingest_data
from raw_integrity_check import check_raw_integrity


def main():
    ingest_data("LineA_Stable_10K", "A")
    ingest_data("LineB_Flux", "B")
    ingest_data("LineC_Turbulent", "C")
    ingest_data("LineD_SpikeControl", "D")
    ingest_data("LineE_SmoothRun", "E")

    check_raw_integrity()


if __name__ == "__main__":
    main()