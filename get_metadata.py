import argparse
import glob
import json
import os
import subprocess
from ffmpy import FFprobe

parser = argparse.ArgumentParser("Extract metadata from mp3 files to JSON files")
parser.add_argument("path", help="Path to recursively extract metadata from files", type=str)

def extract_metadata(file_name):
    probe = FFprobe(
        global_options='-v quiet -print_format json -show_format -show_streams',
        inputs={file_name: None}
    )

    stdout, stderr = probe.run(stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output_json = json.loads(stdout.decode('utf-8'))

    with open(f'{file_name}.json', 'w') as f:
        json.dump(output_json.get('format', {}).get('tags', {}), f, indent=4)


def main():
    args = parser.parse_args()
    absolute_path = os.path.abspath(args.path)
    search_pattern = os.path.join(absolute_path, '**', '*.mp3')

    for file_name in glob.iglob(search_pattern, recursive=True):
        extract_metadata(file_name)




if __name__ == "__main__":
    main()
