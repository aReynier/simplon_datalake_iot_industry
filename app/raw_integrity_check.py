from raw.data_verification import verify_data_integrity


def check_raw_integrity():
    verify_data_integrity('data_input/LineA_Stable_10K.csv','production_lines/lineA/LineA_Stable_10K.csv')
    verify_data_integrity('data_input/LineB_Flux.csv','production_lines/lineB/LineB_Flux.csv')
    verify_data_integrity('data_input/LineC_Turbulent.csv','production_lines/lineC/LineC_Turbulent.csv')
    verify_data_integrity('data_input/LineD_SpikeControl.csv','production_lines/lineD/LineD_SpikeControl.csv')
    verify_data_integrity('data_input/LineE_SmoothRun.csv','production_lines/lineE/LineE_SmoothRun.csv')


if __name__ == "__main__":
    check_raw_integrity()