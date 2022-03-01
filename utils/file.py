def human_readable_size(size):
    if size < 1024:
        return f"{size} B"
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 * 1024 * 1024:
        return f"{size / 1024 / 1024:.2f} MB"
    else:
        return f"{size / 1024 / 1024 / 1024:.2f} GB"

class File:
    def __init__(self, extension: str, path: str, delete_path: str, rename_path:str, name: str, date: str, size: str) -> None:
        self.extension = extension
        self.path = path
        self.delete_path = delete_path
        self.rename_path = rename_path
        self.name = name
        self.date = date
        self.size = size

        self.image = self.is_image()
        self.audio = self.is_audio()
        self.video = self.is_video()
        self.document = self.is_document()
        self.archive = self.is_archive()
        self.application = self.is_application()

    def __str__(self) -> str:
        return f"{self.type} {self.name}"

    def is_image(self) -> bool:
        return self.extension in ['.jpg', '.jpeg', '.png', '.gif']

    def is_audio(self) -> bool:
        return self.extension in ['.mp3', '.wav', '.ogg']
    
    def is_video(self) -> bool:
        return self.extension in ['.mp4', '.avi', '.mkv']

    def is_document(self) -> bool:
        return self.extension in ['.doc', '.docx', '.pdf', '.txt']

    def is_archive(self) -> bool:
        return self.extension in ['.zip', '.rar', '.7z']

    def is_application(self) -> bool:
        return self.extension in ['.exe', '.msi']

    @property
    def type(self) -> str:
        if self.is_image(): return 'Image'
        if self.is_audio(): return 'Audio'
        if self.is_video(): return 'Video'
        if self.is_document(): return 'Document'
        if self.is_archive(): return 'Archive'
        if self.is_application(): return 'Application'
        return 'File'