import traceback
import warnings

from bs4 import BeautifulSoup


def title(Title, icon=False):
    """Adds a title to the webpage, an icon (if entered)

    \nThis must be the first function called after `from sierr import *`
    \nCalling it initiates the HTML and CSS (already linked) file that is created in the working directory upon running of the code

    Args:
        Title(str, compulsory)   : Title of the HTML file.
        icon(str, optional)      : Icon to be displayed. Should be a .ico file. Defaults to no icon.
    """

    with open("index.html", "w") as f:
        f.write(
            f"""<!doctype html>
<html lang="en">
<meta charset="utf-8">
<head>
<title>{Title}</title>
<link rel="stylesheet" href="style.css">"""
        )

        if type(icon) == str and icon.split(".")[-1] == "ico":
            f.write(f'\n<link rel="shortcut icon" href={icon}>')
    open("style.css", "w").write("")


def addFont(font_link):
    """Give the font link to add different fonts to your webpage.

    \nAdd only the `href` attribute to `font_link`

    Args:
        font_link (str, compulsory): The font link.
    """

    with open("index.html", "a") as f:
        f.write(f'\n<link href="{font_link}" rel="stylesheet">')


def head(Head, type="header", **kwargs):
    """Adds a header

    \n`kwargs` is used to add CSS styling attributes to the `type` mentioned
    \nUse underscores instead of hyphens when adding arguments
    \nFor example, the styling attribute `font-size` must be entered in as `font_size`

    \nArgs:
        Head (str, compulsory)   : Caption header.
        type (str, optional)     : Header type. Anything from 'h1' to 'h6'
        **kwargs (optional)      : CSS styling arguments
    """

    # Use underscores for hyphens in **kwags for styling args

    with open(f"index.html", "a") as f:
        f.write(
            f"""
<{type}>{Head}</{type}>"""
        )

    if kwargs:

        with open("style.css", "a+") as s:
            s.write(f"\n\n{type} {{")
            for key, value in kwargs.items():
                s.write(f"\n\t{key.replace('_', '-')}: {value};")
            s.write("\n}")


def join_attr(tup):
    string = ""
    for item in tup:
        string = string + item
        string = string.replace("  ", " ")
    return string


class image:
    def __init__(self, src: str, **kwargs):
        """Adds an image to the webpage. Use `kwargs` to add tag attributes

        \nUse `.show()` to display the image and `.css()` to style it

        \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
        \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name.
        \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`

        \nArgs:
        \nsrc (str, compulsory) : The location of the image file
        \nkwargs (optional)     : Add tag attributes to `<img>`
        """
        self.src = src
        self.kwargs = kwargs

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if exc_type is not None:
            traceback.print_exception(exc_type, exc_value, tb)

    def show(self):
        """
        Display the image
        \nUse `kwargs` to add tag attributes. Python-conflicting attribute names like `class` and `for` to be prefixed by a double underscore, that is, to be entered in as `__class` and `__for`
        \nUse a single underscore in place of a hyphen in the `key` of `kwargs`, which is the tag atrribute name.
        \neg. Tag attribute `initial-scale` must be `initial_scale` as the `key`
        """

        with open("index.html", "a+") as f:
            if self.kwargs:

                all_attr = (
                    f'<img src="{self.src}"  ',
                    *(
                        f'  {key.replace("__", "").replace("_", "-")}="{value}"'
                        for key, value in self.kwargs.items()
                    ),
                    ">",
                )
                f.write(f"\n{join_attr(all_attr)}")

            else:
                f.write(f'\n<img src="{self.src}">')

            return self.kwargs

    def css(self, **kwargs):
        """Writes the given parameters to the CSS file.

        \nUse underscores instead of hyphens
        \nFor example, styling attribute `font-size` must be entered in as `font_size`

        \nUsing this adds CSS directly to `<img>` irrespective of an image `class` or `id` mentioned
        \nUse `writeCSS()` to add CSS to a specific `class` or `id`

        \nArgs:
            **kwargs (optional) : CSS parameters.
        """

        with open("style.css", "a+") as s:
            s.write("\n\nimg {")
            for key, value in kwargs.items():
                s.write(f"\n\t{key.replace('_', '-')}: {value};")
            s.write("\n}")


def autoPrettify():
    """Improve overall look of code and close all tags automatically (if not already done)."""

    warnings.showwarning(
        r"""Auto prettifying also involves auto closing unclosed HTML tags which may not be accurate if not used after development is complete.
Use after all development for best results. See "bs4 auto closing tags" for more info.""",
        UserWarning,
        "main_htm.py",
        None,
    )
    # check_unclosed()
    with open("index.html", "r") as f:
        soup = BeautifulSoup(f, "html.parser")
        auto_close_all_tags = soup.prettify()
        with open("index.html", "w") as f:
            f.write(auto_close_all_tags)
