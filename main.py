import sys
from scanner.port_scanner import PortScanner
import argparse

def main(target_ports, verbose, host_name, output_closed=False, start_port=0, end_port=65535):

  scanner = PortScanner(target_ports=target_ports, verbose=verbose, output_closed=output_closed, start_port=start_port, end_port=end_port)
  res = scanner.scan(host_name)

  return res

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="Port scanner")

  # Host name is first argument and not require flag just ./main.py <host_name>
  parser.add_argument("hostname")

  parser.add_argument("-tp", "--target-ports", type=int, help="Number of target ports to scan", default=100)

  parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity", default=True)

  parser.add_argument("-oc", "--output-closed", action="store_true", help="Output closed ports", default=False)

  parser.add_argument("-sp", "--start-port", type=int, help="Start port to scan", default=0)
  parser.add_argument("-ep", "--end-port", type=int, help="End port to scan", default=65535)

  args = parser.parse_args()

  result = main(target_ports=args.target_ports, verbose=args.verbose, host_name=args.hostname, output_closed=args.output_closed, start_port=args.start_port, end_port=args.end_port)

  print(result)

