import os
import pytest
from test.contracts.CodemetaObject import Contract
from cffconvert.behavior_1_0_x.codemeta import CodemetaObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def codemeta_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "r", encoding="utf8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return CodemetaObject(citation.cffobj, initialize_empty=True)


class TestCodemetaObject(Contract):

    def test_check_cffobj(self, codemeta_object):
        codemeta_object.check_cffobj()
        # doesn't need an assert

    def test_author(self, codemeta_object):
        codemeta_object.add_author()
        expected_author = [{
            "@type": "Person",
            "givenName": "Gonzalo",
            "familyName": "Fernández de Córdoba Jr.",
        }]
        assert codemeta_object.author == expected_author

    def test_code_repository(self, codemeta_object):
        codemeta_object.add_code_repository()
        assert codemeta_object.code_repository is None

    def test_date_published(self, codemeta_object):
        codemeta_object.add_date_published()
        assert codemeta_object.date_published == "1999-12-31"

    def test_description(self, codemeta_object):
        codemeta_object.add_description()
        assert codemeta_object.description is None

    def test_identifier(self, codemeta_object):
        codemeta_object.add_identifier()
        assert codemeta_object.identifier is None

    def test_keywords(self, codemeta_object):
        codemeta_object.add_keywords()
        assert codemeta_object.keywords is None

    def test_license(self, codemeta_object):
        codemeta_object.add_license()
        assert codemeta_object.license is None

    def test_name(self, codemeta_object):
        codemeta_object.add_name()
        assert codemeta_object.name == 'example title'

    def test_version(self, codemeta_object):
        codemeta_object.add_version()
        assert codemeta_object.version == '1.0.0'

    def test_print(self, codemeta_object):
        actual_codemeta = codemeta_object.add_all().print()
        fixture = os.path.join(os.path.dirname(__file__), "codemeta.json")
        with open(fixture, "r", encoding="utf8") as f:
            expected_codemeta = f.read()
        assert actual_codemeta == expected_codemeta