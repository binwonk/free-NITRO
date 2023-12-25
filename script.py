import uuid
import requests
import time


def free_nitro():
  url = "https://api.discord.gx.games/v1/direct-fulfillment"
  headers = {
      "Content-Type":
      "application/json",
      "Sec-Ch-Ua":
      '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
      "User-Agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
  }
  data = {"partnerUserId": str(uuid.uuid4())}

  r = requests.post(url, json=data, headers=headers)

  if r.status_code == 200:
    freenitro = r.json().get("token")
    print(
        f"\n here is ur FREE nitro:\nhttps://discord.com/billing/partner-promotions/1180231712274387115/{freenitro}"
    )
    time.sleep(3)
    free_nitro()
  elif r.status_code == 429:
    print("ratelimited lil bro")


free_nitro()