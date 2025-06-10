# Render Environment Variables for Superagent

## 🚨 **CRITICAL - DO NOT SET MANUALLY**
- `PORT` - **Automatically set by Render** (usually 10000). Do NOT override this.

## 📋 **BACKEND SERVICE VARIABLES**

```bash
# Core Application
OPENAI_API_KEY=
DATABASE_URL=
DATABASE_MIGRATION_URL=
JWT_SECRET=
OPENROUTER_API_KEY=
DATABASE_SHADOW_URL=

# Memory
MEMORY=motorhead
REDIS_MEMORY_URL=
REDIS_MEMORY_WINDOW=
MEMORY_API_URL=

# Vector Store (Weaviate)
VECTORSTORE=weaviate
WEAVIATE_API_KEY=
WEAVIATE_INDEX=
WEAVIATE_URL=

# Supabase
SUPABASE_DB_URL=
SUPABASE_TABLE_NAME=

# Tools
E2B_API_KEY=
REPLICATE_API_TOKEN=
TAVILY_API_KEY=

# API Configuration
SUPERAGENT_API_URL=
```

## 📋 **FRONTEND SERVICE VARIABLES**

```bash
# Backend Connection
NEXT_PUBLIC_SUPERAGENT_API_URL=

# Supabase Authentication
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICEROLE_KEY=

# Environment
NODE_ENV=production
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

## 🚀 **DEPLOYMENT ORDER**

1. **Deploy Backend Service** with backend environment variables
2. **Note the backend URL** (e.g., `https://your-backend.onrender.com`)
3. **Deploy Frontend Service** using the backend URL in `NEXT_PUBLIC_SUPERAGENT_API_URL`