# APITest

Methods:

- <code title="get /">client.<a href="./src/api_test/_client.py">get_status</a>() -> object</code>

# Auth

Types:

```python
from api_test.types import TokenResponse
```

# API

## V1

### Debug

Types:

```python
from api_test.types.api.v1 import User
```

### Conversations

Types:

```python
from api_test.types.api.v1 import Conversation
```

### Messages

Types:

```python
from api_test.types.api.v1 import Message
```

### Logs

Types:

```python
from api_test.types.api.v1 import Log
```

### Benchmark

#### External

Types:

```python
from api_test.types.api.v1.benchmark import ExternalBenchmarkRecord
```

### Files

Types:

```python
from api_test.types.api.v1 import File, FileListResponse
```

Methods:

- <code title="post /api/v1/files">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">create</a>(\*\*<a href="src/api_test/types/api/v1/file_create_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/file.py">File</a></code>
- <code title="get /api/v1/files/s3/{key}">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">retrieve</a>(key) -> object</code>
- <code title="patch /api/v1/files/{fileId}">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">update</a>(file_id, \*\*<a href="src/api_test/types/api/v1/file_update_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/file.py">File</a></code>
- <code title="get /api/v1/files">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">list</a>(\*\*<a href="src/api_test/types/api/v1/file_list_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/file_list_response.py">FileListResponse</a></code>
- <code title="delete /api/v1/files/{fileId}">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">delete</a>(file_id) -> object</code>
- <code title="delete /api/v1/files/{fileId}/purge">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">delete_purge</a>(file_id) -> object</code>
- <code title="post /api/v1/files/presigned-post">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">presigned_post</a>(\*\*<a href="src/api_test/types/api/v1/file_presigned_post_params.py">params</a>) -> object</code>
- <code title="get /api/v1/files/{file_id}/download">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">retrieve_download</a>(file_id, \*\*<a href="src/api_test/types/api/v1/file_retrieve_download_params.py">params</a>) -> object</code>

#### Multipart

Methods:

- <code title="post /api/v1/files/multipart/abort">client.api.v1.files.multipart.<a href="./src/api_test/resources/api/v1/files/multipart.py">abort</a>(\*\*<a href="src/api_test/types/api/v1/files/multipart_abort_params.py">params</a>) -> object</code>
- <code title="post /api/v1/files/multipart/complete">client.api.v1.files.multipart.<a href="./src/api_test/resources/api/v1/files/multipart.py">complete</a>(\*\*<a href="src/api_test/types/api/v1/files/multipart_complete_params.py">params</a>) -> object</code>
- <code title="post /api/v1/files/multipart/init">client.api.v1.files.multipart.<a href="./src/api_test/resources/api/v1/files/multipart.py">init</a>(\*\*<a href="src/api_test/types/api/v1/files/multipart_init_params.py">params</a>) -> object</code>

# Health

Methods:

- <code title="get /health">client.health.<a href="./src/api_test/resources/health.py">check</a>() -> object</code>
