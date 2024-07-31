class Song:
    def __init__(self, id, title, artist):
        self.id = id
        self.title = title
        self.artist = artist


class SongSerializer:

    def _serialize_json(self, song):
        print(f"(id:{song.id}, song: {song.title})")

    def _serialize_xml(self, song):
        print(f"<id>{song.id}</id> <song>{song.title}</song>")
    
    def _get_serializer(self, format):
        if format == "JSON":
            return self._serialize_json
        elif format == "XML":
            return self._serialize_xml
        else:
            raise ValueError("format not supported")
    
    def serialize(self, song, format):
        serialized = self._get_serializer(format)
        return serialized(song)


song1 = Song(1, "Yellow", "Coldplay")
serializer = SongSerializer()

serializer.serialize(song1, "JSON")