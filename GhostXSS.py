import argparse
import threading
import requests

def scan_single_domain(domain, active_only, output_file, threads):
    # Placeholder for scanning logic on a single domain
    print(f"Scanning single domain: {domain}")
    if active_only:
        print("Filtering for active subdomains only.")
    # Insert XSS scanning logic here
    if output_file:
        with open(output_file, 'a') as f:
            f.write(f"Results for {domain}\n")  # Add results to output file

def scan_multiple_domains(file_path, active_only, output_file, threads):
    print(f"Scanning multiple domains from file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            domains = file.read().splitlines()
            threads_list = []
            for domain in domains:
                thread = threading.Thread(target=scan_single_domain, args=(domain, active_only, output_file, threads))
                thread.start()
                threads_list.append(thread)
            for thread in threads_list:
                thread.join()
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")

def main():
    parser = argparse.ArgumentParser(
        description="Ghost XSS - Advanced XSS & Vulnerability Attack Tool\n"
                    "Version 1.0 - Unleash the power of Cross-Site Scripting!",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Examples:\n"
               "  python ghost_xss.py -u example.com\n"
               "      Scan a single domain (example.com) for vulnerabilities.\n\n"
               "  python ghost_xss.py -l domains.txt\n"
               "      Scan all domains listed in \"domains.txt\".\n\n"
               "  python ghost_xss.py -u example.com -a\n"
               "      Scan only active subdomains of example.com.\n\n"
               "  python ghost_xss.py -l domains.txt -o results.txt\n"
               "      Scan domains in \"domains.txt\" and save results to \"results.txt\".\n\n"
               "  python ghost_xss.py -u example.com --threads 50\n"
               "      Scan example.com with 50 threads for faster processing.\n\n"
               "Notes:\n"
               "  - Use `-u` or `-l` to specify your target(s).\n"
               "  - `-a` filters for active subdomains only.\n"
               "  - Adjust scan speed with `--threads`, useful for larger targets.\n\n"
               "Happy Scanning with Ghost XSS!"
    )

    # Defining command-line arguments without --help/-h to avoid conflict
    parser.add_argument('-u', '--url', help="Target a single domain for scanning.")
    parser.add_argument('-l', '--list', help="Scan multiple domains from a specified file (one domain per line).")
    parser.add_argument('-a', '--active', action='store_true', help="Only scan active subdomains.")
    parser.add_argument('-o', '--output', help="Save scan results to a specified file.")
    parser.add_argument('--threads', type=int, default=10, help="Set number of threads for faster scanning (default: 10, max: 100).")

    args = parser.parse_args()

    # Determine number of threads (limit to 100 max for safety)
    threads = min(args.threads, 100)

    if args.url:
        scan_single_domain(args.url, args.active, args.output, threads)
    elif args.list:
        scan_multiple_domains(args.list, args.active, args.output, threads)
    else:
        print("Error: Please specify a target domain with -u or a list of domains with -l.")
        parser.print_help()

if __name__ == "__main__":
    main()
