from servee import frontendadmin
from chunks.models import Chunk

class ChunkAdmin(frontendadmin.ServeeModelAdmin):
    exclude = ["key"]

frontendadmin.site.register(Chunk, ChunkAdmin)
