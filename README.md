# make project json
This project is a command-line tool that allows you to search for files in the current working directory and export the project's JSON structure.

## Project features

Supports exporting the project's file structure as a JSON directory tree to `project.json`, as well as performing a recursive search and saving the results to `search.txt`.

## Usage


### use directly without pip install

```console
$ python ./make_project_json.py
```

```console
$ python globalSearchContent.py
```

search all python, html, css files.\
search results in search.txt.\
the object path glob method parses the entry (e.g. **/*.py stuff) in Unix style.

```
{
**/*.py,
**/*.html,
**/*.css
}

```



### after pip install (as a cli tool)

```console
$ gsearch -i
$ gsearch -s
```

## Build by pip to install cli tool

```console
$ cd ./project
$ pip install -e .
```

after this, u can run this cli tool