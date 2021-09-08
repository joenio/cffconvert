from cffconvert.behavior_shared.bibtex_author import BibtexAuthorShared as Shared


class BibtexAuthor(Shared):

    def __init__(self, author_cff):
        super().__init__(author_cff)

    def as_string(self):
        state = [
            ('G', self._exists_nonempty('given-names')),
            ('F', self._exists_nonempty('family-names')),
            ('A', self._exists_nonempty('alias')),
            ('N', self._exists_nonempty('name'))
        ]
        key = ''.join([item[0] if item[1] is True else '.' for item in state])
        return self._behaviors[key]()