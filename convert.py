import os
import re
from os.path import basename, splitext
import fire


def get_range_settings(ipath):
    with open("noto-sans-tc.css") as ifile:
        text = ifile.read()

    ranges = re.findall(r"\[(\d+)\].*?unicode\-range:(.*?);", text, re.DOTALL)

    for index, _range in ranges:
        print(f"'tc-{index}': '{_range.strip()}',")

    range_set = " ".join(f"tc-{index}" for index, _ in ranges)

    font_name = basename(ipath).rsplit(".")[0]

    os.system(
        f'npx font-ranger -f {ipath} -o fonts -u {range_set} -p "/fonts/" -m {font_name} -b 400 -s normal -i swap -l {font_name}'
    )


if __name__ == "__main__":
    fire.Fire(get_range_settings)
