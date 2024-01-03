"""The metadata for the website"""
from typing import List, Literal, Union
from pydantic import (
    AnyUrl,
    BaseModel,
    Field,
    FileUrl,
    FilePath,
    model_validator,
)


def is_allowed_type(v: FileUrl | FilePath) -> bool:
    """Check if the image is a valid type"""
    ALLOWED_FILE_TYPES = (".jpg", ".jpeg", ".png")
    if isinstance(v, FileUrl):
        if v.path is not None and v.path.endswith(ALLOWED_FILE_TYPES):
            return True
        raise ValueError("The image must be a .jpg, .jpeg, or .png file")
    else:
        if not v.is_file():
            raise ValueError("The image must be a file")
        if v.suffix not in ALLOWED_FILE_TYPES:
            raise ValueError("The image must be a .jpg, .jpeg, or .png file")
        if not v.exists():
            raise ValueError("The image must exist")
        return True


class TwitterMetadata(BaseModel):
    """The Twitter metadata for the website"""

    twitter_card: Literal["summary", "summary_large_image", None] = Field(
        description="The type of the website",
        default=None,
    )
    twitter_title: Union[str, None] = Field(
        description="The title of the website",
        min_length=0,
        max_length=50,
        default=None,
    )
    twitter_description: Union[str, None] = Field(
        description="The description of the website",
        min_length=0,
        max_length=150,
        default=None,
    )
    twitter_image: FileUrl | FilePath = Field(
        description="The image of the website",
    )
    twitter_creator: Union[str, None] = Field(
        description="The Twitter username of the website creator",
        min_length=0,
        max_length=50,
        default=None,
    )
    twitter_site: Union[str, None] = Field(
        description="The Twitter username of the website",
        min_length=0,
        max_length=50,
        default=None,
    )

    @model_validator(mode="after")
    def check_image_type(self):
        """Validate the data after the model is created"""

        # check if the twitter creator is a valid username
        if str(self.twitter_creator)[0] != "@" and self.twitter_creator is not None:
            raise ValueError("The Twitter username must start with @")
        # check is the twitter site is a valid username
        if self.twitter_site is not None and str(self.twitter_site)[0] != "@":
            raise ValueError("The Twitter username must start with @")
        # check if the image is a valid type
        is_allowed_type(self.twitter_image)
        return self


class OpenGraphMetadata(BaseModel):
    """The Open Graph metadata for the website"""

    og_title: str = Field(
        description="The title of the website",
        min_length=0,
        max_length=50,
    )
    og_url: AnyUrl = Field(description="The url of the website")
    og_image: FileUrl | FilePath = Field("The image of the website")
    og_type: Literal["website", "article", None] = Field(
        description="The type of the website",
        default=None,
    )
    og_description: Union[str, None] = Field(
        description="The description of the website",
        min_length=0,
        max_length=150,
        default=None,
    )
    og_locale: Union[str, None] = Field(
        description="The locale of the website", default=None
    )

    @model_validator(mode="after")
    def check_image_type(self):
        """Validate the data after the model is created"""

        # check if the image is a valid type
        is_allowed_type(self.og_image)
        return self


class Metadata(BaseModel):
    """The metadata for the website"""

    name: str = Field(
        description="The name of the website",
        min_length=0,
        max_length=50,
    )
    description: Union[str, None] = Field(
        description="The description of the website",
        min_length=0,
        max_length=150,
        default=None,
    )
    keywords: Union[List[str], None] = Field(
        description="The keywords for the website",
        min_length=0,
        max_length=10,
    )
    author: Union[str, None] = Field(
        description="The author of the website",
        min_length=0,
        max_length=50,
        default=None,
    )
    favicon: Union[FileUrl, FilePath, None] = Field(
        description="The favicon of the website",
        default=None,
    )

    twitter: Union[TwitterMetadata, None] = None
    open_graph: Union[OpenGraphMetadata, None] = None


def add_metadata(metadata: Metadata):
    """Add the metadata to the website"""
    pass
