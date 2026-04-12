erDiagram
    users {
        UUID id PK
        String kakao_user_id UK "Unique"
        String notion_token "Nullable"
        String current_status
        Timestamp created_at
    }
    
    knowledge_metadata {
        UUID id PK "Pinecone Vector ID 매핑"
        UUID user_id FK
        String source_type
        String source_url "Nullable"
        Boolean is_processed "Default: False"
    }
    
    tasks {
        UUID id PK
        UUID user_id FK
        String status
        JSON result_summary "Nullable"
    }

    %% Relationships (관계)
    users ||--o{ knowledge_metadata : "owns (1:N)"
    users ||--o{ tasks : "triggers (1:N)"