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

    # NOTE: add TC range set
    range_set = " ".join(f"tc-{index}" for index, _ in ranges)

    # NOTE: add origin supported range set
    range_set += " " + " ".join("latin, latin-ext, cyrillic, cyrillic-ext, greek, greek-ext, vietnamese, sinhala, hebrew, oriya, malayalam, gurmukhi, kannada, arabic, tamil, khmer, telugu, bengali, thai, devanagari, myanmar, gujarati".split(","))

    font_name = basename(ipath).rsplit(".")[0]

    os.system(
        f'npx font-ranger -f {ipath} -o fonts -u {range_set} -p "/fonts/" -m {font_name} -b 400 -s normal -i swap -l {font_name}'
    )


if __name__ == "__main__":
    fire.Fire(get_range_settings)
