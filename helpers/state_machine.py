import enum


class ProjectStates(enum.Enum):
    NAME = 'project_name'
    AUTHOR = 'project_description'
    TEXT = 'text'
    GET_NAME = 'get_name'
    GET_AUTHOR = 'get_author'
    ADD_USER = 'add_user'
