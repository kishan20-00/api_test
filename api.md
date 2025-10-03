# APITest

Methods:

- <code title="get /">client.<a href="./src/api_test/_client.py">get_status</a>() -> object</code>

# Auth

Types:

```python
from api_test.types import TokenResponse
```

Methods:

- <code title="post /auth/logout">client.auth.<a href="./src/api_test/resources/auth/auth.py">logout</a>() -> object</code>
- <code title="post /auth/request-magic-link">client.auth.<a href="./src/api_test/resources/auth/auth.py">request_magic_link</a>(\*\*<a href="src/api_test/types/auth_request_magic_link_params.py">params</a>) -> object</code>
- <code title="post /auth/verify-magic-link-token">client.auth.<a href="./src/api_test/resources/auth/auth.py">verify_magic_link_token</a>(\*\*<a href="src/api_test/types/auth_verify_magic_link_token_params.py">params</a>) -> <a href="./src/api_test/types/token_response.py">TokenResponse</a></code>

## Login

Methods:

- <code title="get /auth/login/github">client.auth.login.<a href="./src/api_test/resources/auth/login.py">github</a>() -> object</code>
- <code title="get /auth/login/google">client.auth.login.<a href="./src/api_test/resources/auth/login.py">google</a>() -> object</code>

## GitHub

Methods:

- <code title="get /auth/github/callback">client.auth.github.<a href="./src/api_test/resources/auth/github.py">callback</a>() -> object</code>

## Google

Methods:

- <code title="get /auth/google/callback">client.auth.google.<a href="./src/api_test/resources/auth/google.py">callback</a>() -> object</code>

## Token

Methods:

- <code title="post /auth/token/exchange">client.auth.token.<a href="./src/api_test/resources/auth/token.py">exchange</a>(\*\*<a href="src/api_test/types/auth/token_exchange_params.py">params</a>) -> <a href="./src/api_test/types/token_response.py">TokenResponse</a></code>
- <code title="post /auth/token/refresh">client.auth.token.<a href="./src/api_test/resources/auth/token.py">refresh</a>() -> <a href="./src/api_test/types/token_response.py">TokenResponse</a></code>

# API

## V1

Types:

```python
from api_test.types.api import V1AudioInferenceResponse
```

Methods:

- <code title="post /api/v1/audio-inference">client.api.v1.<a href="./src/api_test/resources/api/v1/v1.py">audio_inference</a>(\*\*<a href="src/api_test/types/api/v1_audio_inference_params.py">params</a>) -> <a href="./src/api_test/types/api/v1_audio_inference_response.py">V1AudioInferenceResponse</a></code>
- <code title="post /api/v1/generate">client.api.v1.<a href="./src/api_test/resources/api/v1/v1.py">generate</a>(\*\*<a href="src/api_test/types/api/v1_generate_params.py">params</a>) -> object</code>
- <code title="post /api/v1/generate-image">client.api.v1.<a href="./src/api_test/resources/api/v1/v1.py">generate_image</a>(\*\*<a href="src/api_test/types/api/v1_generate_image_params.py">params</a>) -> object</code>
- <code title="get /api/v1/api-key-logs">client.api.v1.<a href="./src/api_test/resources/api/v1/v1.py">retrieve_api_key_logs</a>(\*\*<a href="src/api_test/types/api/v1_retrieve_api_key_logs_params.py">params</a>) -> object</code>
- <code title="get /api/v1/health">client.api.v1.<a href="./src/api_test/resources/api/v1/v1.py">retrieve_health</a>() -> object</code>
- <code title="get /api/v1/token-count">client.api.v1.<a href="./src/api_test/resources/api/v1/v1.py">retrieve_token_count</a>() -> object</code>
- <code title="post /api/v1/save-message">client.api.v1.<a href="./src/api_test/resources/api/v1/v1.py">save_message</a>(\*\*<a href="src/api_test/types/api/v1_save_message_params.py">params</a>) -> object</code>

### Debug

Types:

```python
from api_test.types.api.v1 import User
```

Methods:

- <code title="get /api/v1/debug/current-user">client.api.v1.debug.<a href="./src/api_test/resources/api/v1/debug.py">retrieve_current_user</a>() -> <a href="./src/api_test/types/api/v1/user.py">User</a></code>

### Users

Types:

```python
from api_test.types.api.v1 import UserRetrieveResponse
```

Methods:

- <code title="get /api/v1/users/by-github/{oauth_id}">client.api.v1.users.<a href="./src/api_test/resources/api/v1/users.py">retrieve</a>(oauth_id) -> <a href="./src/api_test/types/api/v1/user.py">User</a></code>
- <code title="patch /api/v1/users/{user_id}">client.api.v1.users.<a href="./src/api_test/resources/api/v1/users.py">update</a>(user_id, \*\*<a href="src/api_test/types/api/v1/user_update_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/user.py">User</a></code>
- <code title="get /api/v1/users/">client.api.v1.users.<a href="./src/api_test/resources/api/v1/users.py">retrieve</a>() -> <a href="./src/api_test/types/api/v1/user_retrieve_response.py">UserRetrieveResponse</a></code>

### Conversations

Types:

```python
from api_test.types.api.v1 import Conversation
```

Methods:

- <code title="get /api/v1/conversations/get-or-create/{user_id}">client.api.v1.conversations.<a href="./src/api_test/resources/api/v1/conversations.py">retrieve</a>(user_id) -> <a href="./src/api_test/types/api/v1/conversation.py">Conversation</a></code>
- <code title="patch /api/v1/conversations/{conv_id}">client.api.v1.conversations.<a href="./src/api_test/resources/api/v1/conversations.py">update</a>(conv_id, \*\*<a href="src/api_test/types/api/v1/conversation_update_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/conversation.py">Conversation</a></code>
- <code title="delete /api/v1/conversations/{conv_id}">client.api.v1.conversations.<a href="./src/api_test/resources/api/v1/conversations.py">delete</a>(conv_id) -> None</code>

### Messages

Types:

```python
from api_test.types.api.v1 import Message
```

Methods:

- <code title="get /api/v1/messages/{msg_id}">client.api.v1.messages.<a href="./src/api_test/resources/api/v1/messages.py">retrieve</a>(msg_id) -> <a href="./src/api_test/types/api/v1/message.py">Message</a></code>
- <code title="patch /api/v1/messages/{msg_id}">client.api.v1.messages.<a href="./src/api_test/resources/api/v1/messages.py">update</a>(msg_id, \*\*<a href="src/api_test/types/api/v1/message_update_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/message.py">Message</a></code>
- <code title="delete /api/v1/messages/{msg_id}">client.api.v1.messages.<a href="./src/api_test/resources/api/v1/messages.py">delete</a>(msg_id) -> None</code>

### Logs

Types:

```python
from api_test.types.api.v1 import Log, LogRetrieveResponse, LogRetrieveResponse
```

Methods:

- <code title="get /api/v1/logs/endpoint/{endpoint}">client.api.v1.logs.<a href="./src/api_test/resources/api/v1/logs.py">retrieve</a>(endpoint, \*\*<a href="src/api_test/types/api/v1/log_retrieve_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/log_retrieve_response.py">LogRetrieveResponse</a></code>
- <code title="post /api/v1/logs/">client.api.v1.logs.<a href="./src/api_test/resources/api/v1/logs.py">update</a>(\*\*<a href="src/api_test/types/api/v1/log_update_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/log.py">Log</a></code>
- <code title="get /api/v1/logs/">client.api.v1.logs.<a href="./src/api_test/resources/api/v1/logs.py">retrieve</a>(\*\*<a href="src/api_test/types/api/v1/log_retrieve_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/log_retrieve_response.py">LogRetrieveResponse</a></code>

### Benchmark

Types:

```python
from api_test.types.api.v1 import BenchmarkRetrieveVllmMetricsResponse
```

Methods:

- <code title="get /api/v1/benchmark/vllm-metrics">client.api.v1.benchmark.<a href="./src/api_test/resources/api/v1/benchmark/benchmark.py">retrieve_vllm_metrics</a>() -> <a href="./src/api_test/types/api/v1/benchmark_retrieve_vllm_metrics_response.py">BenchmarkRetrieveVllmMetricsResponse</a></code>

#### External

Types:

```python
from api_test.types.api.v1.benchmark import ExternalBenchmarkRecord, ExternalListResponse
```

Methods:

- <code title="post /api/v1/benchmark/external">client.api.v1.benchmark.external.<a href="./src/api_test/resources/api/v1/benchmark/external.py">create</a>(\*\*<a href="src/api_test/types/api/v1/benchmark/external_create_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/benchmark/external_benchmark_record.py">ExternalBenchmarkRecord</a></code>
- <code title="get /api/v1/benchmark/external">client.api.v1.benchmark.external.<a href="./src/api_test/resources/api/v1/benchmark/external.py">list</a>() -> <a href="./src/api_test/types/api/v1/benchmark/external_list_response.py">ExternalListResponse</a></code>

### Keys

Types:

```python
from api_test.types.api.v1 import KeyUpdateResponse, KeyRetrieveResponse
```

Methods:

- <code title="post /api/v1/keys/">client.api.v1.keys.<a href="./src/api_test/resources/api/v1/keys.py">update</a>(\*\*<a href="src/api_test/types/api/v1/key_update_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/key_update_response.py">KeyUpdateResponse</a></code>
- <code title="delete /api/v1/keys/{key_id}">client.api.v1.keys.<a href="./src/api_test/resources/api/v1/keys.py">delete</a>(key_id) -> None</code>
- <code title="get /api/v1/keys/">client.api.v1.keys.<a href="./src/api_test/resources/api/v1/keys.py">retrieve</a>(\*\*<a href="src/api_test/types/api/v1/key_retrieve_params.py">params</a>) -> <a href="./src/api_test/types/api/v1/key_retrieve_response.py">KeyRetrieveResponse</a></code>

### Storage

Methods:

- <code title="get /api/v1/storage/info">client.api.v1.storage.<a href="./src/api_test/resources/api/v1/storage.py">retrieve_info</a>() -> object</code>

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
- <code title="post /api/v1/files/ingest">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">ingest</a>(\*\*<a href="src/api_test/types/api/v1/file_ingest_params.py">params</a>) -> object</code>
- <code title="post /api/v1/files/presigned-post">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">presigned_post</a>(\*\*<a href="src/api_test/types/api/v1/file_presigned_post_params.py">params</a>) -> object</code>
- <code title="get /api/v1/files/{file_id}/download">client.api.v1.files.<a href="./src/api_test/resources/api/v1/files/files.py">retrieve_download</a>(file_id, \*\*<a href="src/api_test/types/api/v1/file_retrieve_download_params.py">params</a>) -> object</code>

#### Multipart

Methods:

- <code title="post /api/v1/files/multipart/abort">client.api.v1.files.multipart.<a href="./src/api_test/resources/api/v1/files/multipart.py">abort</a>(\*\*<a href="src/api_test/types/api/v1/files/multipart_abort_params.py">params</a>) -> object</code>
- <code title="post /api/v1/files/multipart/complete">client.api.v1.files.multipart.<a href="./src/api_test/resources/api/v1/files/multipart.py">complete</a>(\*\*<a href="src/api_test/types/api/v1/files/multipart_complete_params.py">params</a>) -> object</code>
- <code title="post /api/v1/files/multipart/init">client.api.v1.files.multipart.<a href="./src/api_test/resources/api/v1/files/multipart.py">init</a>(\*\*<a href="src/api_test/types/api/v1/files/multipart_init_params.py">params</a>) -> object</code>

# OpenAI

## V1

### Chat

Methods:

- <code title="post /openai/v1/chat/completions">client.openai.v1.chat.<a href="./src/api_test/resources/openai/v1/chat.py">create_completion</a>(\*\*<a href="src/api_test/types/openai/v1/chat_create_completion_params.py">params</a>) -> object</code>

### Audio

Methods:

- <code title="post /openai/v1/audio/transcriptions">client.openai.v1.audio.<a href="./src/api_test/resources/openai/v1/audio.py">create_transcription</a>(\*\*<a href="src/api_test/types/openai/v1/audio_create_transcription_params.py">params</a>) -> object</code>

### Images

Methods:

- <code title="post /openai/v1/images/generations">client.openai.v1.images.<a href="./src/api_test/resources/openai/v1/images.py">create_generation</a>(\*\*<a href="src/api_test/types/openai/v1/image_create_generation_params.py">params</a>) -> object</code>

### Models

Methods:

- <code title="get /openai/v1/models/{model_id}">client.openai.v1.models.<a href="./src/api_test/resources/openai/v1/models.py">retrieve</a>(model_id) -> object</code>
- <code title="get /openai/v1/models">client.openai.v1.models.<a href="./src/api_test/resources/openai/v1/models.py">list</a>() -> object</code>

### Files

Methods:

- <code title="get /openai/v1/files/{file_id}">client.openai.v1.files.<a href="./src/api_test/resources/openai/v1/files.py">retrieve</a>(file_id) -> object</code>
- <code title="get /openai/v1/files">client.openai.v1.files.<a href="./src/api_test/resources/openai/v1/files.py">list</a>(\*\*<a href="src/api_test/types/openai/v1/file_list_params.py">params</a>) -> object</code>
- <code title="delete /openai/v1/files/{file_id}">client.openai.v1.files.<a href="./src/api_test/resources/openai/v1/files.py">delete</a>(file_id) -> object</code>
- <code title="get /openai/v1/files/{file_id}/content">client.openai.v1.files.<a href="./src/api_test/resources/openai/v1/files.py">download_content</a>(file_id) -> object</code>
- <code title="post /openai/v1/files">client.openai.v1.files.<a href="./src/api_test/resources/openai/v1/files.py">upload</a>(\*\*<a href="src/api_test/types/openai/v1/file_upload_params.py">params</a>) -> object</code>

### Batches

Types:

```python
from api_test.types.openai.v1 import BatchCreateResponse, BatchCancelResponse
```

Methods:

- <code title="post /openai/v1/batches">client.openai.v1.batches.<a href="./src/api_test/resources/openai/v1/batches.py">create</a>(\*\*<a href="src/api_test/types/openai/v1/batch_create_params.py">params</a>) -> <a href="./src/api_test/types/openai/v1/batch_create_response.py">BatchCreateResponse</a></code>
- <code title="get /openai/v1/batches/{batch_id}">client.openai.v1.batches.<a href="./src/api_test/resources/openai/v1/batches.py">retrieve</a>(batch_id) -> object</code>
- <code title="get /openai/v1/batches">client.openai.v1.batches.<a href="./src/api_test/resources/openai/v1/batches.py">list</a>(\*\*<a href="src/api_test/types/openai/v1/batch_list_params.py">params</a>) -> object</code>
- <code title="post /openai/v1/batches/{batch_id}/cancel">client.openai.v1.batches.<a href="./src/api_test/resources/openai/v1/batches.py">cancel</a>(batch_id) -> <a href="./src/api_test/types/openai/v1/batch_cancel_response.py">BatchCancelResponse</a></code>

# Health

Methods:

- <code title="get /health">client.health.<a href="./src/api_test/resources/health.py">check</a>() -> object</code>
