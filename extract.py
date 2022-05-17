#!/bin/env python

import sys
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="source_file", help="path to file containing cracked hashes with usernames")
    parser.add_argument("-o", "--output", dest="dest_file", help="output file to store results")
    options = parser.parse_args()
    if not options.source_file:
        parser.error("[-] Please specify path to source file.")
    if not options.dest_file:
        parser.error("[-] Please specify path to destination file.")
    return options

def show_banner():
    print("Rival's tool.")

def show_arguments(options):
    print("filepath: " + options.source_file)
    print("file to save: " + options.dest_file)

def clear_file(file):
    f = open(file, "w")
    f.write("")
    f.close()

def get_info(options):
    print("")
    print("[+] clearing file to save")
    clear_file(options.dest_file)
    print("[+] extracting usernames from file... \n")
    with open(options.source_file, "r") as f:
        for line in f:
            info = line.split(":")
            username = info[0].split("\\")[1]
            pass_length = str(len(info[2].strip()))
            print("[+] username: " + username)
            print("[+] password length:" + pass_length)
            print("")
            o = open(options.dest_file, "a")
            o.write(username + "," + pass_length + "\n")
            o.close()

def main():
    show_banner()
    options = get_arguments()
    show_arguments(options)
    get_info(options)
    sys.exit()

if __name__ == "__main__":
    main()
