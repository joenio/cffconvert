import json
from abc import abstractmethod


class SchemaorgObjectShared:

    supported_cff_versions = None

    def __init__(self, cffobj):
        self.cffobj = cffobj
        self.context = None
        self.author = None
        self.code_repository = None
        self.contributor = None
        self.date_published = None
        self.description = None
        self.identifier = None
        self.keywords = None
        self.license = None
        self.name = None
        self.type = None
        self.url = None
        self.version = None

    def __str__(self, sort_keys=True, indent=2):
        data = {
            "@context": self.context,
            "@type": self.type,
            "author": self.author,
            "codeRepository": self.code_repository,
            "contributor": self.contributor,
            "datePublished": self.date_published,
            "description": self.description,
            "identifier": self.identifier,
            "keywords": self.keywords,
            "license": self.license,
            "name": self.name,
            "url": self.url,
            "version": self.version
        }
        filtered = [item for item in data.items() if item[1] is not None]
        return json.dumps(dict(filtered), sort_keys=sort_keys, indent=indent, ensure_ascii=False) + "\n"

    def add_all(self):
        self.add_author()           \
            .add_contributor()      \
            .add_date_published()   \
            .add_description()      \
            .add_identifier()       \
            .add_keywords()         \
            .add_license()          \
            .add_name()             \
            .add_type()             \
            .add_urls()             \
            .add_version()
        return self

    @abstractmethod
    def add_author(self):
        pass

    @abstractmethod
    def add_contributor(self):
        pass

    @abstractmethod
    def add_date_published(self):
        pass

    def add_description(self):
        if "abstract" in self.cffobj.keys():
            self.description = self.cffobj["abstract"]
        return self

    @abstractmethod
    def add_identifier(self):
        pass

    def add_keywords(self):
        if "keywords" in self.cffobj.keys():
            self.keywords = self.cffobj["keywords"]
        return self

    def add_license(self):
        if "license" in self.cffobj.keys():
            self.license = f"https://spdx.org/licenses/{self.cffobj['license']}"
        return self

    def add_name(self):
        if "title" in self.cffobj.keys():
            self.name = self.cffobj["title"]
        return self

    @abstractmethod
    def add_type(self):
        pass

    @abstractmethod
    def add_urls(self):
        pass

    def add_version(self):
        if "version" in self.cffobj.keys():
            self.version = self.cffobj["version"]
        return self

    def as_string(self):
        return str(self)

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if "cff-version" not in self.cffobj.keys():
            raise ValueError("Missing key 'cff-version' in CITATION.cff file.")
        if self.cffobj["cff-version"] not in self.supported_cff_versions:
            raise ValueError(f"'cff-version': '{self.cffobj['cff-version']}' isn't a supported version.")
