# Project features

Supports exporting the project's file structure as a JSON directory tree to `project.json`, as well as performing a recursive search and saving the results to `search.txt`.

# Usage

```python
python ./make_project_json.py
```

```python
python globalSearchContent.py

>>>{
>>>**/*.py,
>>>**/*.html,
>>>**/*.css
>>>}

#search all python, html, css files
#search results in search.txt
#the object path glob method parses the entry (e.g. **/*.py stuff) in Unix style
```