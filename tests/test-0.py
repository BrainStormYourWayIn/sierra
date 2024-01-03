from sierra import (
    Table,
    autoPrettify,
    cTags,
    div,
    head,
    image,
    openBody,
    p,
    section,
    title,
)

title("The title goes here")
head("Sierra!", type="h2", color="#0388fc")
openBody()

with div("newTag") as t:  # Opening a tag 'newTag'

    with div("someClass") as d:  # Creating a div within  'newTag'
        p("Some text")  # Adding a paragraph
        d.css(background_color="rgb(211, 111, 121)")  # Adding CSS to the div

        with section(
            "anotherClass", "id='some_id'"
        ):  # Creating section within the div within 'newTag'
            with Table() as st:
                st.getTable(
                    "/path/to/file.csv", attr="id='table_id'"
                )  # Displaying a table from a CSV and giving it an id

                with cTags("#table_id") as t:  # Adding CSS from the table id
                    t.css(
                        font_family="Arial, Helvetica, sans-serif",
                        border="1px solid #d1d5e8",
                        padding="8px",
                        width="20%",
                    )

            p(
                "This is a paragraph within a section, which is within a div tag and comes after the table."
            )

    with image(src="sierra.jpg") as i:
        i.show()  # Displaying an image
        i.css(opacity=1.2)  # Adding CSS to it

autoPrettify()
