# Overview
- Assignment is to build an Encyclopedia webapge of web development tools
- Every encyclopedia provides the possibility for a human-friendly entry format to contribute easily, such as in this case, it is Markdown entries
- Every entry should be converted to HTML before rendering which will be done using [`markdown2`](https://github.com/trentm/python-markdown2) library

- Assignment is provided with a zipped file of distribution code consisting of 
    - pre-built `wiki` project with `encyclopedia` application
    - preset `wiki/settings.py`, `wiki/urls.py` and `encyclopedia/urls.py`
    - `util.py` for handy functions such as, `list_entries`, `get_entry`, `save_entry`, which are self-explanatory and useful for completing the assignment,
    - `entries` folder with Markdown entries which are to be rendered as a HTML file before rendering the view,
    - `encyclopedia/templates` is provided with `layout.html` and `index.html` to render dynamic content


# Tasks - Solutions
- [X] **Entry Page** - render by visiting url `wiki/TITLE`, where `TITLE` is the name of the entry
    - Step 1: Convert Markdown entries in `entries` to HTML files in `encyclopedia/templates`
    - Step 2: Create single function to render multiple views with a selection block (`if-else`) in `encyclopedia/views.py`
    - Step 3: Include view in `encyclopedia/urls.py`
- [X] **Index Page** - hyperlink all the entries listed in the Wiki homepage
    - Step 1: Check `Django Template Engine` syntax for hyperlink using `</a>` tag
    - Step 2: Use the `route name` for `<a href="">` inside the `li` tag in `index.html` as follows :
        ```html
        <!--django template engine, for loop-->
            <li><a href="{% url 'renderhtml' entry %}">{{ entry }}</a></li>
            <!--'renderhtml' - 'route name' for the view -->
            <!--'entry' - input parameter for 'renderhtml'--->
        <!--end for loop-->    
        ```
- [ ] **Search Entries** - 
- [ ] **New Page** - 
- [ ] **Edit Page** -
- [ ] **Random Page** -
- [X] **Markdown to HTML Conversion** - 
    - Could be done easy way, (*Took the easy way for now* &ensp;:-P )
        ```python 
        >>> pip3 install markdown2      # install markdown to HTML converter

        >>> python -m markdown2 markdown.md > file.html     # convert markdown to HTML in CLI
        ```
    - Or the hard way by using regular expressions (`re`) in Python without external libraries at all!


