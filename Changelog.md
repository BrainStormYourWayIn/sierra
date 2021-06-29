# Changelog

__________________________________________________________________

## 15 June 2021 - v1.0.1

- Initial Release.

__________________________________________________________________

## 20 June 2021 - v1.1.0

- added syntax.

__________________________________________________________________

## 21 June 2021 - v1.1.1

- improved autocomplete.

__________________________________________________________________

## 21 June 2021 - v1.1.5

- bullet lists issue rectified.
- README updated.

__________________________________________________________________

## 23 June 2021 - v1.2.0

- global and event attributes enabled out of the box on div and section.
- tTags(p=False) changed to tTags(p=True).
- Added definition lists.
- global attributes enabled out of the box on table.
- removed compulsory `class` args for div and section.
- table `cols` renamed to `heads` for easier identification.
- removed 'All rights reserved' on table.py (copyright Pandas).
- enabled multiple dts in def_list.

__________________________________________________________________

## 24 June 2021 - v1.2.3

- solved issue with table `{col}`.
- solved issue with table attributes.
- `autoPrettify()` updated.

__________________________________________________________________

## 29 June 2021 - v2.0.0

- openTags to open_tags context-manager
- open_tags added css, attributes
- removed closeTags, closeTagBefore
- added tag attributes to img
- added tag attributes to table
- added tag attributes to bullets
- addBullets to bullets(), changed to context-manager
- css default display from 'block' to False
- cTags() default color from 'black' to False to provide for img css
- removed tTags()
- div(), section() added as context-manager
- p() added as func, attributes added
- def_lists renamed to des_lists
- arg def_list renamed to arg des_list
- added write_to_template()
- addImg() changed to image(), context manager
- image() tag attributes added
