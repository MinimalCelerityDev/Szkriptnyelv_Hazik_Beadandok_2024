import requests

def get_ip_jsonip():
    response = requests.get("https://jsonip.com/")
    data = response.json()
    return data["ip"]

def get_ip_ipinfo():
    response = requests.get("http://ipinfo.io/")
    data = response.json()
    return data["ip"]

def get_ip_ipify():
    response = requests.get("https://api.ipify.org/?format=json")
    data = response.json()
    return data["ip"]

def get_ip_geo():
    response = requests.get("https://reallyfreegeoip.org/json/")
    data = response.json()
    return data["ip"], data

def main():
    print("Válassza ki, melyik szolgáltatást használja az IP-címe lekérésére:")

    print("1 - jsonip.com")
    print("2 - ipinfo.io")
    print("3 - ipify.org")

    print("4 - reallyfreegeoip.org (részletes információkkal)")

    choice = input("Adja meg a választott opció számát (1-4): ")

    if choice == "1":
        print("Az Ön IP címe:", get_ip_jsonip())
    elif choice == "2":
        print("Az Ön IP címe:", get_ip_ipinfo())
    elif choice == "3":
        print("Az Ön IP címe:", get_ip_ipify())
    elif choice == "4":
        ip, details = get_ip_geo()
        print("Az Ön IP címe:", ip)
        print("További információk:", details)
    else:
        print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
