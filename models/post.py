from orator.orm import has_many

from db import Model


class Post(Model):

    @has_many
    def comments(self):
        from .comment impoert Comments

        return Comments
