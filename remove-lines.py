import logging
import os
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def remove_lines_from_file(file_path, strings_to_remove):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            if not any(s in line for s in strings_to_remove):
                file.write(line)

    logging.info(f'Processed {file_path}')


def remove_extra_blank_line(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == "## Description":
            if i >= 2 and lines[i-1].strip() == "" and lines[i-2].strip() == "":
                new_lines.pop()  # Remove one of the blank lines
        new_lines.append(lines[i])
        i += 1

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

    logging.info(f'Processed {file_path}')


def find_and_process_files(directory, strings_to_remove):
    for root, _, files in os.walk(directory):
        for file in files:
            if file == 'README.md':
                file_path = os.path.join(root, file)
                # remove_lines_from_file(file_path, strings_to_remove)
                remove_extra_blank_line(file_path)


if __name__ == "__main__":
    directory = 'solutions/'
    strings_to_remove = ['edit_url:', '[中文文档]']
    find_and_process_files(directory, strings_to_remove)
