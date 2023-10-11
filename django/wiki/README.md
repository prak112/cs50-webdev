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
    - Step 2: Configure URL in `encyclopedia/urls.py` as :
        ```python
            # renders all listed titles and not found pages
            path("<str:title>", views.renderhtml, name="renderhtml")  # --> renders as default view for all sidebar links
            path("renderhtml/<str:title>", views.renderhtml, name="renderhtml")  # --> renders only when called for
        ```
    - Step 3: Define view to render multiple views with a selection block (`if-else`) in `encyclopedia/views.py`
    - Step 3: Include view in `encyclopedia/urls.py`
- [X] **Index Page** - hyperlink all the entries listed in the Wiki homepage
    - Step 1: Check `Django Template Engine` syntax for hyperlink using `<a>` tag
    - Step 2: Use the `route name` for `<a href="">` inside the `li` tag in `index.html` as follows :
        ```html
        <!--django template engine, loop entries-->
            <li><a href="{% url 'renderhtml' entry %}">{{ entry }}</a></li>
            <!--'renderhtml' - 'route name' for the view -->
            <!--'entry' - input parameter for 'renderhtml'--->
        <!--end for loop-->    
        ```
- [ ] **Search Entries** - enable search box in sidebar to search for Wiki entries
    - Step 1: Set up URL config in `encyclopedia/urls.py`
    - Step 2: Create view with following logic :
        - Get a list of all entries through `util.get_entries()`
        - Compare the `search_term` with the list of entries
        - Collect the result set
        - Pass and render it on the template as follows:
        ```html
        {% for match in results %}
            <li><a href="{% url 'renderhtml' entry %}">{{ match }}</a></li>
        {% endfor %}
        ```
- [X] **New Page** - enable '*Create New Page*' link in sidebar to create a new entry
    - Step 1: Set up URL config in `encyclopedia/urls.py`
    - Step 2: In `encyclopedia/views.py`, import `django.forms` to create form fields for title, content area and submit button
    - Step 3: Create and render basic view `new_entry` with form fields
    - Step 4: Process form data submission by adding `if-else` blocks to check for validity of `request` and data 
    - Step 5: Use `util.save_entry(title, content)` function with required parameters to save the user entry to `entries`
    - Step 6: Convert the saved entry from `.md` to `.html` using `subprocess` module as follows:
        ```python
            # convert Markdown to HTML
            markdown_file = f"entries/{title}.md"   
            html_file = f"encyclopedia/templates/encyclopedia/{title}.html"
            cli_command = f"python -m markdown2 {markdown_file} > {html_file}"
            subprocess.run(cli_command, shell=True, check=True)
        ```
    - Step 7: User is redirected to the new entry through `renderhtml` view
    - Step 8: If entry exists already, render `page_exists.html` with reference to existing page in sidebar
    - Step 9: If form data invalid, render form data with *Client-side validation* error messages
- [ ] **Edit Page** - enable '*Edit Page*' option in each entry page to edit, save and redirect to an updated entry
    - Step 1: Identify the task as specific to each individual HTML file, since the content must be repopulated
    - Step 2: URL config in `encyclopedia/urls.py` (URLs are global to all HTML files)
    - Step 3: Start with one HTML, by adding `{% url 'name' arg=value %}` inside `{% block nav %}` dynamice content for navigation links
        - Step 3.1: `arg` would be `title` and `value` would be name of the topic, hence `topic`
        - Step 3.2: Go to `renderhtml` view, pass `title` as `topic` in `return` statement 
    - Step 4: Create template `edit_entry` with form elements from `Class NewForm()`
    - 
- [X] **Random Page** - enable '*Random Page*' link in sidebar to open a random entry
    - Step 1: Add `<a>` tag to '*Random Page*' with url name
    - Step 2: Add url name to `encyclopedia/urls.py` (URL config)
    - Step 3: Define view, `random_page`
- [X] **Markdown to HTML Conversion** - convert the Markdown files in '*entries*' to HTML
    - [X] Easy Way
        ```python 
        >>> pip3 install markdown2      # install markdown to HTML converter

        >>> python -m markdown2 markdown.md > file.html     # convert markdown to HTML in CLI
        ```
    - [ ] Hard Way - using regular expressions (`re`) in Python without external libraries at all!

<br>
<hr>

# Key Takeaways 
( *in 1-line* )
- Understand and represent path directories and routes correctly in the code.
- Parameters passed *TO* HTML template and passed *BETWEEN* HTML templates are different. Refer this- [from HTML](/django/wiki/encyclopedia/templates/encyclopedia/css.html) and [to HTML](/django/wiki/encyclopedia/templates/encyclopedia/edit_entry.html)