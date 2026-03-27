import asyncio
import argparse
import logging
from pathlib import Path
import shutil

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


async def copy_file(file_path: Path, output_folder: Path):
    try:
        ext = file_path.suffix.lower().replace(".", "")
        if not ext:
            ext = "no_extension"

        target_folder = output_folder / ext
        target_folder.mkdir(parents=True, exist_ok=True)

        target_file = target_folder / file_path.name

        await asyncio.to_thread(shutil.copy2, file_path, target_file)

    except Exception as e:
        logging.error(f"Error copying {file_path}: {e}")


async def read_folder(source_folder: Path, output_folder: Path):
    tasks = []

    try:
        for item in source_folder.iterdir():
            if item.is_dir():
                tasks.append(read_folder(item, output_folder))
            else:
                tasks.append(copy_file(item, output_folder))

        await asyncio.gather(*tasks)

    except Exception as e:
        logging.error(f"Error reading folder {source_folder}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Async file sorter")
    parser.add_argument("source", help="Source folder path")
    parser.add_argument("output", help="Output folder path")

    args = parser.parse_args()

    source = Path(args.source)
    output = Path(args.output)

    # Перевірки
    if not source.exists() or not source.is_dir():
        print("❌ Source folder does not exist")
        return

    output.mkdir(parents=True, exist_ok=True)

    asyncio.run(read_folder(source, output))


if __name__ == "__main__":
    main()