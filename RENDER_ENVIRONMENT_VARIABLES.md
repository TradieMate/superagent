# Complete Environment Variables Guide for Render Deployment

This document provides a comprehensive list of ALL environment variables needed for deploying Superagent on Render.

## 🚨 **CRITICAL - DO NOT SET MANUALLY**
- `PORT` - **Automatically set by Render** (usually 10000). Do NOT override this.

## 📋 **MANDATORY VARIABLES**

### Backend API Service

#### Core Application
```bash
# Database (Required)
DATABASE_URL=postgresql://username:password@host:port/database
DATABASE_MIGRATION_URL=postgresql://username:password@host:port/database
DATABASE_SHADOW_URL=postgresql://username:password@host:port/database_shadow

# Authentication (Required)
JWT_SECRET=your-super-secret-jwt-key-here

# AI Provider (Required - at least one)
OPENAI_API_KEY=sk-your-openai-api-key
OPENROUTER_API_KEY=sk-your-openrouter-api-key  # For open source LLMs

# API Configuration (Required)
SUPERAGENT_API_URL=https://your-backend-service.onrender.com

# Memory Provider (Required)
MEMORY=motorhead
MEMORY_API_URL=https://memory.superagent.sh

# Vector Store (Required - choose one)
VECTORSTORE=pinecone  # Options: pinecone, qdrant, weaviate, astra, supabase
```

#### Vector Store Configuration (Choose One)

**Pinecone:**
```bash
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENVIRONMENT=your-pinecone-environment
PINECONE_INDEX=your-pinecone-index-name
```

**Qdrant:**
```bash
QDRANT_API_KEY=your-qdrant-api-key
QDRANT_HOST=your-qdrant-host
QDRANT_INDEX=superagent
```

**Weaviate:**
```bash
WEAVIATE_API_KEY=your-weaviate-api-key
WEAVIATE_URL=your-weaviate-url
WEAVIATE_INDEX=superagent
```

**Astra DB:**
```bash
ASTRA_DB_ID=your-astra-db-id
ASTRA_DB_REGION=your-astra-region
ASTRA_DB_APPLICATION_TOKEN=your-astra-token
ASTRA_DB_COLLECTION_NAME=your-collection-name
ASTRA_DB_KEYSPACE_NAME=your-keyspace-name
```

**Supabase Vector Store:**
```bash
SUPABASE_DB_URL=postgresql://username:password@host:port/database
SUPABASE_TABLE_NAME=superagent
```

### Frontend UI Service

#### Core Frontend
```bash
# Backend Connection (Required)
NEXT_PUBLIC_SUPERAGENT_API_URL=https://your-backend-service.onrender.com

# Supabase Authentication (Required)
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICEROLE_KEY=your-supabase-service-role-key

# Environment
NODE_ENV=production
```

## 🔧 **OPTIONAL BUT RECOMMENDED**

### Backend Optional Features

#### Memory with Redis
```bash
REDIS_MEMORY_URL=redis://username:password@host:port/0
REDIS_MEMORY_WINDOW=10
```

#### Azure OpenAI (Alternative to OpenAI)
```bash
AZURE_OPENAI_API_KEY=your-azure-openai-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=2023-12-01-preview
AZURE_OPENAI_EMBEDDINGS_API_KEY=your-azure-embeddings-key
AZURE_OPENAI_EMBEDDINGS_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_EMBEDDINGS_API_VERSION=2023-12-01-preview
AZURE_OPENAI_EMBEDDINGS_DEPLOYMENT=text-embedding-3-small
```

#### Code Execution Tools
```bash
E2B_API_KEY=your-e2b-api-key
CODE_EXECUTOR_TOKEN=your-code-executor-token
CODE_EXECUTOR_URL=your-code-executor-url
```

#### Search Tools
```bash
TAVILY_API_KEY=your-tavily-api-key
```

#### Fine-tuning
```bash
LAMINI_API_KEY=your-lamini-api-key
REPLICATE_API_TOKEN=your-replicate-token
```

#### Tracing & Analytics
```bash
# Langfuse
LANGFUSE_PUBLIC_KEY=your-langfuse-public-key
LANGFUSE_SECRET_KEY=your-langfuse-secret-key
LANGFUSE_HOST=https://cloud.langfuse.com

# LangSmith
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT_ID=your-project-id

# AgentOps
AGENTOPS_API_KEY=your-agentops-api-key
AGENTOPS_ORG_KEY=your-agentops-org-key

# Segment Analytics
SEGMENT_WRITE_KEY=your-segment-write-key
```

#### Billing (Stripe)
```bash
STRIPE_SECRET_KEY=your-stripe-secret-key
```

### Frontend Optional Features

#### GitHub OAuth
```bash
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-client-secret
```

#### External Datasources
```bash
NEXT_PUBLIC_APIDECK_API_KEY=your-apideck-api-key
NEXT_PUBLIC_APIDECK_API_ID=your-apideck-api-id
```

#### Billing Frontend
```bash
STRIPE_SECRET_KEY=your-stripe-secret-key
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
STRIPE_WEBHOOK_SECRET=your-stripe-webhook-secret
NEXT_PUBLIC_STRIPE_HOBBY_PLAN=price_hobby_plan_id
NEXT_PUBLIC_STRIPE_PRO_PLAN=price_pro_plan_id
```

#### Frontend Analytics
```bash
NEXT_PUBLIC_SEGMENT_WRITE_KEY=your-segment-write-key
NEXT_PUBLIC_LANGFUSE_PUBLIC_KEY=your-langfuse-public-key
NEXT_PUBLIC_LANGFUSE_BASE_URL=https://cloud.langfuse.com
```

#### Storage
```bash
NEXT_PUBLIC_SUPABASE_STORAGE_NAME=superagent
```

## 📝 **RENDER SERVICE CONFIGURATION**

### Backend Service Settings
- **Service Type:** Web Service
- **Environment:** Docker
- **Root Directory:** `./libs/superagent`
- **Dockerfile Path:** `Dockerfile`
- **Health Check Path:** `/health`

### Frontend Service Settings
- **Service Type:** Web Service
- **Environment:** Docker
- **Root Directory:** `./libs/ui`
- **Dockerfile Path:** `Dockerfile`

## 🔍 **MINIMAL WORKING CONFIGURATION**

For a basic deployment, you need AT MINIMUM:

### Backend (Minimum)
```bash
DATABASE_URL=postgresql://...
DATABASE_MIGRATION_URL=postgresql://...
JWT_SECRET=your-secret
OPENAI_API_KEY=sk-...
SUPERAGENT_API_URL=https://your-backend.onrender.com
MEMORY=motorhead
MEMORY_API_URL=https://memory.superagent.sh
VECTORSTORE=pinecone
PINECONE_API_KEY=...
PINECONE_ENVIRONMENT=...
PINECONE_INDEX=...
```

### Frontend (Minimum)
```bash
NEXT_PUBLIC_SUPERAGENT_API_URL=https://your-backend.onrender.com
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=...
SUPABASE_SERVICEROLE_KEY=...
NODE_ENV=production
```

## ⚠️ **IMPORTANT NOTES**

1. **Database URLs:** All three database URLs can be the same for simple deployments
2. **SUPERAGENT_API_URL:** Must match your actual Render backend service URL
3. **Vector Store:** Choose only ONE vector store and configure its variables
4. **Memory Provider:** Default is motorhead, but you can use Redis for better performance
5. **PORT Variable:** Never set this manually - Render handles it automatically
6. **Secrets:** Use Render's environment variable encryption for sensitive values
7. **Service Dependencies:** Deploy backend first, then use its URL in frontend configuration

## 🚀 **DEPLOYMENT ORDER**

1. **Deploy Backend Service** with all backend environment variables
2. **Note the backend URL** (e.g., `https://your-backend.onrender.com`)
3. **Deploy Frontend Service** using the backend URL in `NEXT_PUBLIC_SUPERAGENT_API_URL`
4. **Test both services** using the health endpoints

## 🔗 **USEFUL LINKS**

- [Render Environment Variables Documentation](https://render.com/docs/environment-variables)
- [Supabase Setup Guide](https://supabase.com/docs)
- [Pinecone Setup Guide](https://docs.pinecone.io/)
- [OpenAI API Keys](https://platform.openai.com/api-keys)