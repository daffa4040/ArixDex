#  JOIN TELEGRAM : https://t.me/apsstudiotech
#  JOIN DISCORD : https://discord.gg/N9caefVJ7F

import requests
import random
import sys
import time
from colorama import init, Fore, Style

init(autoreset=True)

APSSTUDIO_art = """
 █████╗ ██████╗ ███████╗    ███████╗████████╗██╗   ██╗██████╗ ██╗ ██████╗ 
██╔══██╗██╔══██╗██╔════╝    ██╔════╝╚══██╔══╝██║   ██║██╔══██╗██║██╔═══██╗
███████║██████╔╝███████╗    ███████╗   ██║   ██║   ██║██║  ██║██║██║   ██║
██╔══██║██╔═══╝ ╚════██║    ╚════██║   ██║   ██║   ██║██║  ██║██║██║   ██║
██║  ██║██║     ███████║    ███████║   ██║   ╚██████╔╝██████╔╝██║╚██████╔╝
╚═╝  ╚═╝╚═╝     ╚══════╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚═╝ ╚═════╝ 
JOIN TELEGRAM : https://t.me/apsstudiotech
JOIN DISCORD  : https://discord.gg/N9caefVJ7F                                            
"""

def random_color():
    colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    return random.choice(colors)

def spinning_delay(seconds):
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + seconds
    while time.time() < end_time:
        for symbol in spinner:
            sys.stdout.write(f"\r{random_color()}Waiting {int(end_time - time.time())} seconds {symbol}{Style.RESET_ALL}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\r" + " " * 40 + "\r")  

def post_task(account_id, task):
    url = f"https://miner-webapp-fz9k.vercel.app/api/task?id={account_id}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Origin': 'https://miner-webapp-fz9k.vercel.app',
        'Referer': 'https://miner-webapp-fz9k.vercel.app/task',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    
    try:
        response = requests.post(url, headers=headers, json={"task": task})
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"{Fore.RED}Task request error: {e}{Style.RESET_ALL}")
        return None


def post_boost(account_id, command):
    url = f"https://miner-webapp-fz9k.vercel.app/api/boost?id={account_id}&command={command}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://miner-webapp-fz9k.vercel.app',
        'Referer': 'https://miner-webapp-fz9k.vercel.app/boost',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    }
    
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"{Fore.RED}Boost request error: {e}{Style.RESET_ALL}")
        return None

def read_ids():
    try:
        with open('token.txt', 'r') as file:
            return [line.strip() for line in file.readlines()]
    except IOError as e:
        print(f"{Fore.RED}Error reading token.txt: {e}{Style.RESET_ALL}")
        return []

tasks = [
    "join_telegram",
    "follow_twitter",
    "visit_website",
    "subscribe_youtube",
    "follow_instagram"
]

boost_commands = [
    "upgrade_miner_10",
    "upgrade_miner_20"
]

initial_url_template = "https://miner-webapp-fz9k.vercel.app/api/claim?id={}"
initial_headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://miner-webapp-fz9k.vercel.app',
    'Pragma': 'no-cache',
    'Referer': 'https://miner-webapp-fz9k.vercel.app/?id={}', 
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
}

def main():
    while True:
        try:
            print(APSSTUDIO_art)

            ids = read_ids()
            if not ids:
                print(f"{Fore.YELLOW}No IDs found in token.txt.{Style.RESET_ALL}")
                return

            for account_id in ids:
                initial_url = initial_url_template.format(account_id)
                initial_headers['Referer'] = initial_headers['Referer'].format(account_id)

                try:
                    initial_response = requests.post(initial_url, headers=initial_headers)
                    initial_response.raise_for_status()
                    data = initial_response.json()

                    print(f"Raw response: {initial_response.text}")

                    username = data.get('username', 'N/A')
                    balance = data.get('balance', 'N/A')
                    claimable_coins = data.get('claimable_coins', 'N/A')

                    print(f"{random_color()}username: {username}{Style.RESET_ALL}")
                    print(f"{random_color()}balance: {balance}{Style.RESET_ALL}")
                    print(f"{random_color()}claimable coins: {claimable_coins}{Style.RESET_ALL}")

                    for task in tasks:
                        task_response = post_task(account_id, task)
                        if task_response:
                            print(f"{random_color()}Task '{task}' response: {task_response.text}{Style.RESET_ALL}")
                        time.sleep(0.2)  

                    for command in boost_commands:
                        boost_response = post_boost(account_id, command)
                        if boost_response:
                            print(f"{random_color()}Boost command '{command}' response: {boost_response.text}{Style.RESET_ALL}")
                        time.sleep(0.2) 

                    print()
                    
                except requests.RequestException as e:
                    print(f"{Fore.RED}Initial request error: {e}{Style.RESET_ALL}")

 
            print("Sleeping for 10 minutes...")
            spinning_delay(600)  

        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
            print("Restarting...")
            time.sleep(5)  

if __name__ == "__main__":
    main()
