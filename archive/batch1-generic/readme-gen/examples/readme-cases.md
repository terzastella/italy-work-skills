# readme-gen cases

## Script with clear entrypoint

Input repo: `main.py` with `argparse --input/--output`, 2-line `requirements.txt`.

Output: README with Install from `requirements.txt`, Usage with `python main.py --input x --output y`
(verified by reading `argparse`), rest `[TODO]`.

## Empty repo

Output: skeleton + `Missing: description, entrypoint, dependencies, license.`
No fantasy-filled sections.
