from raw.data_ingestion import ingest_data
from raw.check_md5 import check_md5


def main():
    ingest_data("LineA_Stable_10K", "A")
    ingest_data("LineB_Flux", "B")
    ingest_data("LineC_Turbulent", "C")
    ingest_data("LineD_SpikeControl", "D")
    ingest_data("LineE_SmoothRun", "E")

check_md5()

if __name__ == "__main__":
    main()