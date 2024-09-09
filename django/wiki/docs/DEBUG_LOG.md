# Key Takeaways 
( *in 1-line* )

- [Entry Page](#entry-page) and [New Page](#new-page) : 
    - Understand and represent path directories and routes correctly in the code.
- [Edit Page](#edit-page) : 
    - Parameters passed *TO* HTML template and passed *BETWEEN* HTML templates are different. Refer this- [from HTML](/django/wiki/encyclopedia/templates/encyclopedia/entry_template.html) and [to HTML](/django/wiki/encyclopedia/templates/encyclopedia/edit_entry.html)
- [Edit Page](#edit-page) : 
    - When submitting data through `django.forms` and `POST` request, **NEVER** refresh the browser! Causes *Double Submitting Form* error, which cause browser to interpret the `POST` request as a `GET` request
- [Search Entries](#search-entries) : 
    - Know the request type for each `request`
- [Search Entries](#search-entries) : 
    - Very fundamental, but a good reminder. Always check and convert data type of varaibles being handled in string operations. See example:
        ```python
            def search(request):
                ...

                if entry.lower() == str(query).lower():
                    return HttpResponseRedirect(reverse('renderhtml', args=[entry]))
                elif entry.lower().__contains__(str(query).lower()):
                    results.append(entry)

            ...
        ```
- [Edit Page](#edit-page) :
    - Skip non-essential verifications for `request` Types. See example : 
        ```python
            def edit_entry(request, title):
                ...

                if form.has_changed() and request.method == 'POST': # this is impossible to pass, since we are updating the form with a POST request !
                    updated_form = forms.NewForm(request.POST)

                ...
        ```
- [Edit Page](#edit-page) :  
    - Sometimes the answer is right in your code, but you don't see it. Like, windows path notation with `"\"`. See example :
        ```python
            def edit_entry(request, title):
                ...

                markdown_file = os.path.join(settings.BASE_DIR, f"entries\\{title}.md")   
                html_file = os.path.join(settings.BASE_DIR, f"encyclopedia\\templates/encyclopedia\\{title}.html")
                
                ...
        ```
- [Entry Page](#entry-page) :
    - Automate every possible repeating event / if event needs manual interference 
    - For example : To render updated or newly created Markdown entries as HTML with `layout.html` template.

<hr>
<br>