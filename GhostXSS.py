import argparse
import os
import threading
import requests

# Tool logo and information
def show_logo():
    print("""
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░▒▓████████▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓███████▓▒░▒▓███████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░     ░▒▓█▓▒░
░▒▓█▓▒▒▓███▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░   ░▒▓█▓▒░           ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓██████▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░  ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░     ░▒▓█▓▒░
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓███████▓▒░   ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓███████▓▒░

Ghost Fring - XSS Attack Tool, Version 1.0 - Unleash the power of Cross-Site Scripting!
""")
    print("Type Your command here:")

# XSS attack function (placeholder for actual scanning logic)
def xss_attack(domain):
    print(f"Scanning {domain} for XSS vulnerabilities...")
    # Insert XSS attack logic here

# Main function
def main():
    show_logo()
    parser = argparse.ArgumentParser(
        description="Ghost XSS - Advanced XSS & Vulnerability Attack Tool",
        add_help=False,
        formatter_class=argparse.RawTextHelpFormatter
    )

    # Define arguments
    parser.add_argument('-u', '--url', help="Target a single domain for scanning.")
    parser.add_argument('-l', '--list', help="Scan multiple domains from a specified file (one domain per line).")
    parser.add_argument('-a', '--active', action='store_true', help="Only scan active subdomains.")
    parser.add_argument('-o', '--output', help="Save scan results to a specified file.")
    parser.add_argument('--threads', type=int, default=10, help="Set number of threads for faster scanning (default: 10, max: 100).")
    parser.add_argument('-h', '--help', action='help', help="Show this help message with command details and examples.")

    # Parse arguments
    args, unknown = parser.parse_known_args()

    # Check if any target domain or list is provided
    if not any([args.url, args.list]):
        parser.print_help()
        print("\nError: Please specify a target domain with -u or a list of domains with -l.")
        return

    # Process single domain scan
    if args.url:
        xss_attack(args.url)

    # Process multiple domain scan from list file
    elif args.list:
        if os.path.exists(args.list):
            with open(args.list, 'r') as file:
                domains = file.read().splitlines()
                for domain in domains:
                    xss_attack(domain)
        else:
            print(f"Error: File '{args.list}' not found.")
            return

    # Output results if specified
    if args.output:
        print(f"Results will be saved to {args.output}")

if __name__ == "__main__":
    main()
