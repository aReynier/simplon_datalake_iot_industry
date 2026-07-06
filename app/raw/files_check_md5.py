from check_md5 import check_md5

def files_check_md5():
    check_md5('data_input/LineA_Stable_10K.csv','production_lines/lineA/LineA_Stable_10K.csv')
    check_md5('data_input/LineB_Flux.csv','production_lines/lineB/LineB_Flux.csv')
    check_md5('data_input/LineC_Turbulent.csv','production_lines/lineC/LineC_Turbulent.csv')
    check_md5('data_input/LineD_SpikeControl.csv','production_lines/lineD/LineD_SpikeControl.csv')
    check_md5('data_input/LineE_SmoothRun.csv','production_lines/lineE/LineE_SmoothRun.csv')
if __name__ == "__main__":
    files_check_md5()