CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    national_id VARCHAR(20) UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    name VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



CREATE TABLE insurance_embeddings (
    id TEXT PRIMARY KEY,
    text TEXT,
    context_text TEXT,
    policy_name TEXT,
    metadata_file TEXT,
    type TEXT,
    embedding vector(768)
);