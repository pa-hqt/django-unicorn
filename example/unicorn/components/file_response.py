import io

from django_unicorn.components import UnicornView
from django.http import FileResponse


class FileResponseView(UnicornView):
    data = ["Line 1", "Line 2", "Line 3"]

    def _dynamically_created_file(self):
        # Imagine that the returned file is dynamically created with data that are only available within the unicorn component
        in_memory_buffer = io.BytesIO()
        for line in self.data:
            in_memory_buffer.write(f"{line}\n".encode("UTF-8"))
        in_memory_buffer.seek(0)  # seek to start before it can be read by FileResponse
        return in_memory_buffer

    def download_file(self):
        file = self._dynamically_created_file()
        return FileResponse(file, as_attachment=True, filename="Dynamically created file.txt")
