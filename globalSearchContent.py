from pathlib import Path
import json
import traceback
from datetime import datetime, timezone
from argparse import ArgumentParser

BASE_DIR = Path(__file__).parent
JSON_PATH = BASE_DIR / r"project.json"
SEARCH_PATH = BASE_DIR / r"search.txt"
LOG_PATH = BASE_DIR / r"logs.txt"

SEARCH_SUFFIXES = [".py", ".txt", ".md", ".c", ".html", ".css", ".js", ".kt", ".ts", ".java", ".mjs", ".cpp", ".rs", "json"]


def make_json(store, dir_path):
    for sub_ofile in dir_path.iterdir():
        if(sub_ofile.name.startswith(".")):
            continue
        if(sub_ofile.is_file()):
            store.append(sub_ofile.name)
        elif(sub_ofile.is_dir()):
            odir = {}
            odir_store = []
            odir[sub_ofile.name] = odir_store
            store.append(odir)
            #recurse
            make_json(odir_store, sub_ofile)

if(__name__ == "__main__"):
    parser = ArgumentParser(
        usage=r"""
            -i --index     get project index,
            -s --search     search file
        """
    )
    parser.add_argument("-i", "--index", action="store_true")
    parser.add_argument("-s", "--search", action="store_true")
    args = parser.parse_args()


    if(args.index):
        #Initialize some variables used for build directories.
        project = {}
        store = []
        project[BASE_DIR.name] = store
        make_json(store, BASE_DIR)
        with JSON_PATH.open("w", encoding="utf-8") as f:
            f.write(json.dumps(project, indent=2, ensure_ascii=False))
            f.flush()

    if(args.search):
        close_before = 0
        text = ""

        while(True):
            ipt = input()
            if (ipt == r"}" and close_before):
                break
            elif(ipt == r"{"):
                close_before = 1
                continue
            elif(not close_before):
                continue
            text += ipt + "\n"

        lst = text.split(",")
        print(lst)

        logs = []
        searches = {}

        for search_item in lst:
            if not search_item.strip():
                continue
            try:
                results = BASE_DIR.glob(search_item.strip())
            except Exception as e:
                error_reason = {}
                error_reason["type"] = type(e).__name__
                error_reason["repr"] = repr(e)
                error_reason["traceback"] = traceback.format_exc()
                logs.append(error_reason)
            else:
                for result in results:
                    if result.suffix in SEARCH_SUFFIXES:
                        with result.open("r", encoding="utf-8") as f:
                            searches[result.as_posix()] = f.read()

        logs_json = json.dumps(logs, indent=2, ensure_ascii=False)
        now = datetime.now(timezone.utc).timestamp() * 1000
        with LOG_PATH.open("a", encoding="utf-8") as f:
            f.write(str(now) + "\n")
            f.write(logs_json + "\n"*10)

        now = datetime.now(timezone.utc).timestamp() * 1000
        with SEARCH_PATH.open("w", encoding="utf-8") as f:
            f.write(str(now) + "\n")
            searches_text = ""
            for key, val in searches.items():
                searches_text += key + "\n\n" + val + "\n"*5
            f.write(searches_text)
