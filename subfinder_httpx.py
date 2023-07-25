import argparse
import os
import uuid

# Create the parser
parser = argparse.ArgumentParser()

# Sample add argument
# parser.add_argument('-sample', help = 'help sample', type = str, required = False)

parser.add_argument('-d', help = 'Domain name, example: google.com', type = str, required = False)
parser.add_argument('-o', help = 'Output file, default: output.txt', type = str, required = False)
parser.add_argument('-df', help = 'Domain file path, example: ./domain_file.txt', type = str, required = False)

# Parse the argument
args = parser.parse_args()

# Set output file name
if args.o == None:
    args.o = 'output.txt'

# Subfinder and httpx
def subfinder_httpx_run(domain, output):
    subfinder_output = str(uuid.uuid4())
    print('[+] Finding subdomain...')
    os.system('subfinder -d %s -o %s' % (domain, subfinder_output))
    print('[+] Checking alive subdomain...')
    os.system('cat %s | httpx | tee -a %s' % (subfinder_output, output))
    os.system('rm %s' % (subfinder_output))

# Processing
def process_single_domain(domain, output):
    subfinder_httpx_run(domain, output)
    print('[+] Done! The output saved in %s' % (output))

def process_domain_file(domain_file, output):
    domains = open(domain_file, 'r').readlines()
    for domain in domains:
        # print(domain.strip())
        subfinder_httpx_run(domain.strip(), output)

if args.d:
    process_single_domain(args.d, args.o)
elif args.df:
    process_domain_file(args.df, args.o)
        
