import speedtest
import json
def run_speedtest():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1000000  # Convert bps to Mbps
    upload_speed = st.upload() / 1000000  # Convert bps to Mbps
    servernames = []
    st.get_servers(servernames)
    ping_latency = st.results.ping

    data = {
        "download_speed": download_speed,
        "upload_speed": upload_speed,
        "ping_latency": ping_latency
    }
    print("data send")
    return data