 # sphinxcontrib-quizdown

[![demo](https://github.com/bonartm/sphinxcontrib-quizdown/actions/workflows/build_deploy.yml/badge.svg)](https://github.com/bonartm/sphinxcontrib-quizdown/actions/workflows/build_deploy.yml)

Sphinx extension for [`quizdown.js`](https://github.com/bonartm/quizdown-js). Write quizzes directly in your content or 
include external `.md` files.

### Try quizdown in the [**live editor**](https://bonartm.github.io/quizdown-live-editor/).


## Installation

First, install the library with:

```bash
pip install git+git://github.com/bonartm/sphinxcontrib-quizdown
```

Then change the `conf.py` of your Sphinx project:

```python
extensions = [
    ...,
    'sphinxcontrib.quizdown'.
    ...
]
```

## Usage

A new directive is added that let's you write markdown-like quizdown inside your `.rst` documents:

```rst
.. quizdown::

   ## What is the capital of Germany?

   > It's the largest city in Germany.  

   - [x] Berlin
   - [ ] Cologne
   - [ ] Frankfurt
   - [ ] Munich
```

You can also write you quiz in an external markdown file and reference it like so:

```rst
.. quizdown:: quiz.md
```

The HTML builder will wrap a `<div class="quizdown"></div>` around the text and 
includes the `quizdown.js` library in the build.

To set global options, use another version of quizdown or change the syntax highlighting you can set 
the following options in your project's `conf.py`:

```python
# quizdown javascript
quizdown_js='https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@latest/public/build/quizdown.js'
# quizdown css
quizdown_css='https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@latest/public/build/quizdown.css'
# stylesheet for syntax highlighting
quizdown_highlight_css='https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@10.6.0/build/styles/github.min.css'
# global options passed to the quizdown library
quizdown_config = {
    'start_on_load': True,			# detect and convert all divs with class quizdown
    'shuffle_answers': True,		# shuffle answers for each question
    'shuffle_questions': False,     # shuffle questsions for each quiz
    'primary_color': '#FF851B',     # primary CSS color
    'secondary_color': '#DDDDDD',   # secondary CSS color
    'title_color': 'black'          # text color of the title
}
```


## Acknowledge

[sphinxcontrib-mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid) and the [sphinx-contrib template](https://github.com/sphinx-contrib/cookiecutter) served as a reference for this project. Thank you for the inspiration!