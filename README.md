 # sphinxcontrib-quizdown

[![demo](https://github.com/bonartm/sphinxcontrib-quizdown/actions/workflows/build_deploy.yml/badge.svg)](https://github.com/bonartm/sphinxcontrib-quizdown/actions/workflows/build_deploy.yml)

> A sphinx extension for writing quizzes with a markdown-like syntax, called [quizdown](https://github.com/bonartm/quizdown-js). 

### 🚀 See the [demo](https://bonartm.github.io/sphinxcontrib-quizdown/) or try the interactive [quizdown live editor](https://bonartm.github.io/quizdown-live-editor/).

- supports markdown text formatting, images and syntax highlighting.
- different [quiz-types](https://github.com/bonartm/quizdown-js/blob/main/docs/syntax.md): single-choice, multiple-choice, sequence.
- support for hints and explanations.
- [options](https://github.com/bonartm/quizdown-js/blob/main/docs/options.md) for color theme, question shuffling, localization.
- mobile friendly with touch support for all question types.


## Installation

First, install the library with:

```bash
pip install git+git://github.com/bonartm/sphinxcontrib-quizdown
```

Then change the `conf.py` of your Sphinx project:

```python
extensions = [
    ...,
    'sphinxcontrib.quizdown',
    ...
]
```

## Usage

A new directive is added that let's you write markdown-like quizdown inside your `.rst` documents:

```rst
.. quizdown::

    ---
    primary_color: orange
    secondary_color: lightgray
    text_color: black
    shuffle_questions: false
    ---

   ## What is the capital of Germany?

   > It's the largest city in Germany.  

   - [x] Berlin
   - [ ] Cologne
   - [ ] Frankfurt
   - [ ] Munich

   ## Put the [days](https://en.wikipedia.org/wiki/Day) in order!

    > Monday is the *first* day of the week.

    1. Monday
    2. Tuesday
    3. Wednesday
    4. Friday
    5. Saturday  
```

You can also write you quiz in an external markdown file and reference it like so:

```rst
.. quizdown:: quiz.md
```

The HTML builder will wrap a `<div class="quizdown"></div>` around the text and includes the `quizdown.js` library in the build.

To use another version of quizdown or to set global options you can place a dictionary `quizdown_config` in your project's `conf.py` and change some of the values (quizdown uses the default option of not specified):

```python
# global options passed to the quizdown library
quizdown_config = {
    'quizdown_js': 'https://cdn.jsdelivr.net/gh/bonartm/quizdown-js@latest/public/build/quizdown.js' # quizdown javascript
    'start_on_load': True,			# detect and convert all divs with class quizdown
    'shuffle_answers': True,		# shuffle answers for each question
    'shuffle_questions': False,     # shuffle questsions for each quiz
    'primary_color': '#FF851B',     # primary CSS color
    'secondary_color': '#DDDDDD',   # secondary CSS color
    'text_color': 'black',          # text color of interactive elements
    'locale': 'en'                  # language of text in user interface
}
```


## 📚 Documentation

> The quizzes are for fun and not for serious assessment. Since everything is rendered on the client side, the hints and solutions to the questions become visible once javascript is disabled in the browser.

Check out the [documentation](https://github.com/bonartm/quizdown-js/blob/main/docs/) on the main project page. You might be interested in:

- different [quiz-types](https://github.com/bonartm/quizdown-js/blob/main/docs/syntax.md): single-choice, multiple-choice, sequence.
- support for [hints and explanations](https://github.com/bonartm/quizdown-js/blob/main/docs/syntax.md#hints-and-comments).
- [options](https://github.com/bonartm/quizdown-js/blob/main/docs/options.md) for color theme, question shuffling, localization.



## Credits

[sphinxcontrib-mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid) and the [sphinx-contrib template](https://github.com/sphinx-contrib/cookiecutter) served as a reference for this project. Thank you for the inspiration!
