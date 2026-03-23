import requests
import time


class NetLaconis

  def download_speed(url):
      start = time.time()
      r = requests.get(url, stream=True)
      size = 0
      for chunk in r.iter_content(1024 * 1024):
          size += len(chunk)
      duration = time.time() - start
      return size / duration / 1_000_000  # Mbps

print(download_speed("https://speed.hetzner.de/100MB.bin"))
