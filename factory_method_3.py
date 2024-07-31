class Song:
    def __init__(self, id, title, artist):
        self.id = id
        self.title = title
        self.artist = artist

    def serialize(self):
        serializer.start_object(self.id)
        serializer.add_property(self.title)
        serializer.add_property(self.artist)

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

class JsonSerializer:
    def __init__(self):
        self.obj = None
    
    def start_object(self, object_name, object_id):

    


song1 = Song(1, "Yellow", "Coldplay")
serializer = SongSerializer()

serializer.serialize(song1, "JSON")