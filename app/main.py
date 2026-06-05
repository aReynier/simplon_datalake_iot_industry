from raw.data_ingestion import ingest_data


def main():
    ingest_data("LineA_Stable_10K", "A")
    ingest_data("LineB_Flux", "B")
    ingest_data("LineC_Turbulent", "C")
    ingest_data("LineD_SpikeControl", "D")
    ingest_data("LineE_SmoothRun", "E")


if __name__ == "__main__":
    main()