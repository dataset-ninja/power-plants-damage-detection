from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Damage Detection of Power Plants"
PROJECT_NAME_FULL: str = "Replication Data for Remote Damage Detection of Power Plants Using Deep Learning Based Drone Image Analysis"
HIDE_DATASET = False  # set False when 100% sure about repo quality

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.CC0_1_0()
APPLICATIONS: List[Union[Industry, Domain, Research]] = [
    Industry.Energy(is_used=False),
    Domain.DroneInspection(),
    Domain.DamageDetection(),
    Research.Engineering(),
]
CATEGORY: Category = Category.EnergyAndUtilities(extra=Category.Drones())

CV_TASKS: List[CVTask] = [CVTask.ObjectDetection()]
ANNOTATION_TYPES: List[AnnotationType] = [CVTask.ObjectDetection()]

RELEASE_DATE: Optional[str] = "2020-10-24"  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = None

HOMEPAGE_URL: str = (
    "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW"
)
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1763947
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/power-plants-damage-detection"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[Union[str, dict]] = {
    "Solar_large.rar": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#",
    "Solar_small.rar": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#",
    "Solar_small_IR.rar": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#",
    "Wind.rar": "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW#",
}
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[str] = "https://www.sciencedirect.com/science/article/pii/S2352484721005102"
CITATION_URL: Optional[
    str
] = "https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/GFYPQW"
AUTHORS: Optional[List[str]] = [
    "Shihavuddin, ASM",
    "Mohammad Rifat Ahmmad Rashid",
    "Xiao Chen",
    "Md Hasan Maruf",
    "Mohammad Asif UL Haq",
    "Muhammad Abul Hasan",
    "Ahmed Al Mansur",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = [
    "Green University of Bangladesh",
    "University of Liberal Arts Bangladesh",
]
ORGANIZATION_URL: Optional[Union[str, List[str]]] = [
    "https://green.edu.bd/",
    "https://ulab.edu.bd/",
]

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = {
    "image-sets": [
        "Solar_large",
        "Solar_small",
        "Solar_small_IR",
        "Wind",
    ]
}
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "hide_dataset": HIDE_DATASET,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
