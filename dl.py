#!/usr/bin/env python3
from pytube import YouTube
import os
import argparse

def download_video(url, output):
  pass

def download_audio(url, output):
  pass

def main():
  parser = argparse.ArgumentParser(description="download youtube audio/video from the terminal")
  parser.add_argument("--a", action="store_true", help="download audio")
  parser.add_argument("--v", action="store_true", help="download video")
  parser.add_argument("urls", type=str, help="a txt file with links to the youtube videos")
  parser.add_argument("output", type=str, help="folder where the downloaded files will be saved")

  args = parser.parse_args()


  if not os.path.exists(args.output):
    os.makedirs(args.output)
    print(f"{args.output} created!")

  with open(args.urls, "r") as f:
    urls = f.readlines()

  print(urls)

  for url in urls:
    if args.a:
      download_audio(url, args.output)
    else:
      download_video(url, args.output)


  
if __name__ == "__main__":
  main()
